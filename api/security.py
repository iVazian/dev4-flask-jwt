
def login():
    pass
    # Get data from request

    # Get user from database

    # Check if user exists and password is correct
    if not user or not check_password_hash(user['password'], password) :
        return {'message': 'invalid credentials'}, 401
    # Delete password from user (should not be sent back!)

    # Create JWT
    del user['password']