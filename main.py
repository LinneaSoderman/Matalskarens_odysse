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
    database="matalskarens_odysee"
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






































































