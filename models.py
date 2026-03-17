```python
# Import necessary libraries
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the database
db = SQLAlchemy()

# Define the User model
class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        """Set the user password"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check the user password"""
        return check_password_hash(self.password, password)

# Define the Laptop model
class Laptop(db.Model):
    """Laptop model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

# Define the Order model
class Order(db.Model):
    """Order model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    laptop_id = db.Column(db.Integer, db.ForeignKey('laptop.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(80), nullable=False, default='pending')

# Define the Payment model
class Payment(db.Model):
    """Payment model"""
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    payment_method = db.Column(db.String(80), nullable=False)
    payment_status = db.Column(db.String(80), nullable=False, default='pending')
```

###