from app import create_app
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     "mssql+pyodbc://DESKTOP-QP7N91R/plotflixdb?driver=ODBC+Driver+17+for+SQL+Server"
# )
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), nullable=False, unique=True)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False)
#     date_created = db.Column(db.DateTime, server_default=db.func.now())

#     def __repr__(self):
#         return f"<User {self.username}>"

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

