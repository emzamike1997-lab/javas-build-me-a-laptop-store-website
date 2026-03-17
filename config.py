```python
# Import necessary libraries
import os

# Define the configuration
class Config:
    """Configuration class"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///laptop_store.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'super-secret'
```

### Running the Application
To run the application, navigate to the project directory and execute the following command:
```bash
python app.py
```
This will start the Flask development server, and you can access the API endpoints using a tool like Postman or cURL.

### API Endpoints
The following API endpoints are available:

* `POST /register`: Register a new user
* `POST /login`: Login a user
* `POST /laptops`: Create a new laptop (requires authentication)
* `POST /orders`: Create a new order (requires authentication)
* `POST /payments`: Create a new payment (requires authentication)

Note: This is a basic implementation, and you may want to add additional features, error handling, and security measures depending on your specific requirements.