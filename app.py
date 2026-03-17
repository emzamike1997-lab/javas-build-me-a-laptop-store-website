```python
# Import necessary libraries
from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from routes import laptop_store

# Initialize the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///laptop_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'

# Initialize the database
db.init_app(app)

# Initialize the JWT manager
jwt = JWTManager(app)

# Register the blueprint
app.register_blueprint(laptop_store)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

###