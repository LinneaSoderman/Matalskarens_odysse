from flask import Flask, jsonify, request, session
from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker
from functools import wraps

import os
from dotenv import load_dotenv
load_dotenv()

url = URL.create(
    drivername="postgresql+psycopg2",
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)
engine = create_engine(url)

app = Flask(__name__)
app.config["SECRET_KEY"] = "byt-ut-den-här-i-produktion"  # behövs för sessions
Session = sessionmaker(bind=engine)


# --- Hjälp-funktion

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "users_id" not in session: ## user_id blev users_id eftersom vi ändrade i databasen
            return jsonify({"message": "Authentication required."}), 401
        return f(*args, **kwargs)
    return wrapper



@app.post('/login')
def login():
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Please provide email and password."}), 400

    with Session() as db:
        users = db.execute(
            text("SELECT id, first_name, last_name, email, password FROM users WHERE email = :email"),
            {"email": email}
        ).mappings().fetchone()


        if not users or users["password"] != password:
            return jsonify({"message": "Invalid email or password."}), 401


        session["users_id"] = users["id"]
        session["users_email"] = users["email"]

    return jsonify({
        "message": "Login successful.",
        "users": {
            "id": users["id"],
            "email": users["email"]
        }
    }), 200



@app.delete('/login')
def logout():
    session.clear()
    return jsonify({"message": "Logged out."}), 200




@app.post("/book-rooms")
@login_required
def book_room():
    data = request.get_json() or {}
    room_ids = data.get("room")
    user_id = session.get("users_id")

    if not room_ids or not isinstance(room_ids, list) or len(room_ids) == 0:
        return jsonify({"message": "Please provide a non-empty list of room IDs."}), 400

    with Session() as db:

        result = db.execute(
            text("INSERT INTO booking (user_id) VALUES (:user_id) RETURNING id"),
            {"user_id": user_id}
        )
        booking_id = result.fetchone()[0]


        for room_id in room_ids:
            room_exists = db.execute(
                text("SELECT id FROM room WHERE id=:room_id"),
                {"room_id": room_id}
            ).fetchone()
            if not room_exists:
                return jsonify({"message": f"Room {room_id} not found."}), 404

            db.execute(
                text("INSERT INTO booking_x_room (booking_id, room_id) VALUES (:booking_id, :room_id)"),
                {"booking_id": booking_id, "room_id": room_id}
            )

        db.commit()

    return jsonify({
        "booking_id": booking_id,
        "user_id": user_id,
        "rooms": room_ids,
        "status": "created"
    }), 201


if __name__ == "__main__":
    app.run(debug=True)


























































