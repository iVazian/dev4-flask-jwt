from flask import Flask
from flask_cors import CORS
from db import DB
from resources.user import create_user

# Create a new Flask application
app = Flask(__name__)
app.debug = True

# Enable cors on the server
CORS(app)

# Register the JWT manager
app.config['JWT_SECRET_KEY'] = 'super-secret' #Change this!
jwt = JWTManager(app)
# ============================ Routes ============================

# JWT routes
app.add_url_rule('/users', None, create_user, methods=['POST'])

# Start app
if __name__ == '__main__':
    DB.create()
    app.run()