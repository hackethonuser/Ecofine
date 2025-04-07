from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to users table
    name = db.Column(db.String(255), nullable=False)  # Item name
    description = db.Column(db.Text)  # Item description
    quantity = db.Column(db.Integer, nullable=False)  # Quantity of items available
    image = db.Column(db.String(255))  # URL or path to image of the item

    def __repr__(self):
        return f'<Item {self.name}>'
