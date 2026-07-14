import os
from dotenv import load_dotenv
from flask import Flask

from extensions import db, bcrypt
from models import User

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///placement_portal_app_db"

db.init_app(app)
bcrypt.init_app(app)

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

if __name__ == "__main__":
    app.run(debug=True)


