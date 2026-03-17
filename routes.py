```python
# Import necessary libraries
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User, Laptop, Order, Payment

# Initialize the blueprint
laptop_store = Blueprint('laptop_store', __name__)

# Define the user registration route
@laptop_store.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Please provide all required fields'}), 400

    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'Username already exists'}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

# Define the user login route
@laptop_store.route('/login', methods=['POST'])
def login():
    """Login a user"""
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Please provide all required fields'}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'Invalid username or password'}), 401

    if not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401

    # Generate a JWT token
    from flask_jwt_extended import create_access_token
    access_token = create_access_token(identity=username)

    return jsonify({'access_token': access_token}), 200

# Define the laptop creation route
@laptop_store.route('/laptops', methods=['POST'])
@jwt_required()
def create_laptop():
    """Create a new laptop"""
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    stock = data.get('stock')

    if not name or not description or not price or not stock:
        return jsonify({'message': 'Please provide all required fields'}), 400

    new_laptop = Laptop(name=name, description=description, price=price, stock=stock)
    db.session.add(new_laptop)
    db.session.commit()

    return jsonify({'message': 'Laptop created successfully'}), 201

# Define the order creation route
@laptop_store.route('/orders', methods=['POST'])
@jwt_required()
def create_order():
    """Create a new order"""
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    laptop_id = data.get('laptop_id')
    quantity = data.get('quantity')

    if not laptop_id or not quantity:
        return jsonify({'message': 'Please provide all required fields'}), 400

    laptop = Laptop.query.get(laptop_id)
    if not laptop:
        return jsonify({'message': 'Laptop not found'}), 404

    if laptop.stock < quantity:
        return jsonify({'message': 'Insufficient stock'}), 400

    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    new_order = Order(user_id=user_id, laptop_id=laptop_id, quantity=quantity, total_price=laptop.price * quantity)
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Order created successfully'}), 201

# Define the payment creation route
@laptop_store.route('/payments', methods=['POST'])
@jwt_required()
def create_payment():
    """Create a new payment"""
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    order_id = data.get('order_id')
    payment_method = data.get('payment_method')

    if not order_id or not payment_method:
        return jsonify({'message': 'Please provide all required fields'}), 400

    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    new_payment = Payment(order_id=order_id, payment_method=payment_method)
    db.session.add(new_payment)
    db.session.commit()

    return jsonify({'message': 'Payment created successfully'}), 201
```

###