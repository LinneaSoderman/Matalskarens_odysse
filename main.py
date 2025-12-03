from flask import Flask, jsonify, request, session
from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker
from functools import wraps

url = URL.create(
    drivername="postgresql+psycopg2",
    host="localhost",
    port=5432,
    username="postgres",
    password="Linnea10",
    database="matälskarens_odysse(den)"
)
engine = create_engine(url)

app = Flask(__name__)
app.config["SECRET_KEY"] = "byt-ut-den-här-i-produktion"  # behövs för sessions
Session = sessionmaker(bind=engine)


# --- Hjälp-funktion

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"message": "Authentication required."}), 401
        return f(*args, **kwargs)
    return wrapper


# --- Users ---

@app.get('/user')
@login_required
def get_user():
    with Session() as db:
        result = db.execute(text("SELECT * FROM user")).fetchall()
        user_list = [
            {
                "id": row.id,
                "first_name": row.first_name,
                "last_name": row.last_name,
                "email": row.email
            } for row in result
        ]

    return jsonify(user_list), 200

@app.post('/user')
def create_use():
    data = request.get_json() or {}
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    password = data.get("password")

    if not first_name or not last_name or not email or not password:
        return jsonify({"message": "Please provide first_name, last_name, email and password."}), 400

    with Session() as db:
        # Kolla om e-post redan finns
        existing = db.execute(
            text("SELECT id FROM user WHERE email = :email"),
            {"email": email}
        ).fetchone()

        if existing:
            return jsonify({"message": "Email already registered."}), 409

        # Skapa användare (plaintext password – byt till hashing senare!)
        db.execute(
            text("""
                INSERT INTO user (first_name, last_name, email, password)
                VALUES (:first_name, :last_name, :email, :password)
            """),
            {"first_name": first_name, "last_name": last_name, "email": email, "password": password}
        )
        db.commit()

        # Hämta nya användaren
        new_user = db.execute(
            text("SELECT id, first_name, last_name, email FROM users WHERE email = :email"),
            {"email": email}
        ).fetchone()

    return jsonify({
        "message": "User created successfully.",
        "user": {
            "id": new_user.id,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "email": new_user.email
        }
    }), 201
