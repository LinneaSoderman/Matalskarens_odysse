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
        if "user_id" not in session:
            return jsonify({"message": "Authentication required."}), 401
        return f(*args, **kwargs)
    return wrapper


@app.get('/detailed-description-of-each-trip')
def get_trip_details():
    with Session() as session:
        result = session.execute(text("""
            SELECT * FROM detaljerad_beskrivning_om_varje_resa
        """)).fetchall()

    # Om du vill returnera JSON måste du konvertera Row-objekten
    product_list = [dict(row._mapping) for row in result]

    return jsonify(product_list), 200

@app.get('/show-if-accommodation-is-fully-booked')
def get_se_om_ett_boende_är_fullbokat():
    with Session() as session:
        result = session.execute(text("""
            SELECT * FROM se_om_ett_boende_är_fullbokat
        """)).fetchall()

    # Om du vill returnera JSON måste du konvertera Row-objekten
    product_list = [dict(row._mapping) for row in result]

    return jsonify(product_list), 200































































