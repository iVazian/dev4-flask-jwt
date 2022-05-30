
def login():
    pass
    # Get data from request
    email = request.json.get('email', None)
    password = request.json.get('password', None)
   
    # Get user from database
    qry = 'SELECT * FROM `users` WHERE `email` = :email'
    user = DB.one(qry, {'email': email})

    # Check if user exists and password is correct
    if not user or not check_password_hash(user['password'], password) :
        return {'message': 'invalid credentials'}, 401
    
    # Delete password from user (should not be sent back!)
    del user['password']
    
    # Create JWT
    access_token = create_access_token(user)
    return jsonify(access_token = access_token, message = 'success'), 200
