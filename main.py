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
        if "users_id" not in session:
            return jsonify({"message": "Authentication required."}), 401
        return f(*args, **kwargs)
    return wrapper

@app.get('/feature-sort-search-result')
def get_hotels():
    with Session() as session:

        result = session.execute(text("SELECT * FROM sortera_sökresultat_efter_pris_betyg_eller_popularitet")).fetchall()

        hotels_list = [
            {
                "hotel_name": row.hotel_name,
                "city": row.city,
                "reigon": row.reigon,
                "stars": row.stars,
                "price": row.price
            }
            for row in result
        ]

        return jsonify(hotels_list), 200

@app.get('/detailed-description-of-each-trip')
def get_trip_details():
    with Session() as session:
        result = session.execute(text("""
            SELECT * FROM detaljerad_beskrivning_om_varje_resa
        """)).fetchall()



@app.get('/show-departures-arivals')
def get_departures_arivals():
    with Session() as session:
        result = session.execute(text("SELECT * FROM som_resenär_vill_jag_se_avgångs_och_ankomsttider")).fetchall()

    product_list = [dict(row._mapping) for row in result]

    return jsonify(product_list), 200


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

@app.get('/hotel/search')
def search_hotel():
    city = request.args.get("city")
    country = request.args.get("country")
    guests = request.args.get("guests")

    query = """
        SELECT *
        FROM "söka_efter_lediga_boenden_i_en_viss_region_och_tidsperiod"
        WHERE 1=1
    """
    params = {}

    if city:
        query += " AND city = :city"
        params["city"] = city

    if country:
        query += " AND country = :country"
        params["country"] = country

    if guests:
        query += " AND guest_limit >= :guests"
        params["guests"] = int(guests)

    with Session() as db:
        result = db.execute(text(query), params).fetchall()

        accommodations_list = [
            {
                "hotel_id": row.hotel_id,
                "hotel_name": row.hotel_name,
                "city": row.city,
                "country": row.country,
                "guest_limit": row.guest_limit
            }
            for row in result
        ]
        
    return jsonify(accommodations_list), 200
      
      
@app.get('/feature/enter-amount-of-adults-and-children')
def get_enter_adults_children():
    with Session() as session:
        result = session.execute(text("SELECT * FROM visar_hotell_där_man_kan_se_om_boendet_har_tillräcklig_kapaci")).fetchall()
        adults_children_list = [
            {
                "hotel_name": row.hotel_name,
                "room_type": row.room_type,
                "total_beds": row.total_beds,
                "adults": row.adults,
                "kids": row.kids

            } for row in result
        ]

    return jsonify(adults_children_list), 200

    
@app.get('/show-if-accommodation-is-fully-booked')
def get_se_om_ett_boende_är_fullbokat():
    with Session() as session:
        result = session.execute(text("""
            SELECT * FROM se_om_ett_boende_är_fullbokat
        """)).fetchall()

    # Om du vill returnera JSON måste du konvertera Row-objekten
    product_list = [dict(row._mapping) for row in result]

    return jsonify(product_list), 200

















































