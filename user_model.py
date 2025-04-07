from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.Enum('lister', 'collector', name='user_role'), nullable=False)
    items = db.relationship('Item', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'
