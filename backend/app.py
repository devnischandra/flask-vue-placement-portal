import os
from dotenv import load_dotenv
from flask import Flask, send_from_directory
from flask_cors import CORS

from extensions import db, bcrypt, jwt, mail, cache
from models import User

from api import api_bp

load_dotenv()

app = Flask(__name__)
CORS(app,supports_credentials=True)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///placement_portal_app_db")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_USERNAME")
app.config["CACHE_TYPE"] = "RedisCache"
app.config["CACHE_REDIS_URL"] = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")
app.config["CACHE_DEFAULT_TIMEOUT"] = 300


db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)
mail.init_app(app)
cache.init_app(app)

with app.app_context():
    db.create_all()

    admin_email = os.getenv("ADMIN_EMAIL")
    admin_password = os.getenv("ADMIN_PASSWORD")

    admin = User.query.filter_by(email=admin_email).first()

    if not admin:
        password_hash = bcrypt.generate_password_hash(admin_password).decode("utf-8")

        admin = User(
            role="admin",
            name="admin",
            email=admin_email,
            password_hash=password_hash
        )

        db.session.add(admin)
    db.session.commit()

@app.errorhandler(400)
def error_handler_400(e):
    return {"msg":e.name}, 400

@app.errorhandler(403)
def error_handler_403(e):
    return {"msg":e.name}, 403

@app.route("/<filename>")
def download_file(filename):
    return send_from_directory(".", filename, as_attachment=True)

app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True)


