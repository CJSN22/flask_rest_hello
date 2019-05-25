from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.String(12), unique=False, nullable=False)


    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone
        }


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.String(80), db.ForeignKey('Person.id'), unique=False, nullable=False)
    create_date = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return '<Cart %r>' % self.id

    def serialize(self):
        return {
            "person_id": self.person_id,
            "create_date": self.create_date

        }