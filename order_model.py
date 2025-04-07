from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)  # Foreign key to items table
    collector_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to users table (collector)
    quantity = db.Column(db.Integer, nullable=False)  # Quantity of items ordered
    order_date = db.Column(db.DateTime, default=db.func.current_timestamp())  # Order timestamp
    status = db.Column(db.Enum('pending', 'completed', name='order_status'), default='pending')  # Order status

    def __repr__(self):
        return f'<Order {self.id}>'
