from flask import request, redirect, url_for, session as flask_session, flash
from config.supabase_client import supabase
from config.usertables import get_user_team, insert_user_table


# Function to register a user
def postregister():
    email = request.form.get('email')
    password = request.form.get('password')
    username = request.form.get('username')
    session_response = supabase.auth.sign_up({ 
        'email': email, 
        'password': password, 
        'options': {'data': {'username': username}}  # Store the username in the user's metadata
    })
    if session_response:
        uid = session_response.user.id
        insert_user_table(uid)
        user_team= get_user_team(uid)
        flask_session['user_info'] = {
            'email': email,
            'email_prefix': email.split('@')[0],
            'username': username,
            'uid': uid,
            'user_team': user_team
        }
        return redirect(url_for('home'))
    else:
        return "Sign-up failed", 401
    
# Function to login a user
def postlogin():
    email = request.form.get('email')
    password = request.form.get('password')
    session_response = None # Initialize session
    
    try: 
        session_response = supabase.auth.sign_in_with_password({ 'email': email, 'password': password })
    except Exception as e: # catches if login fails -> "Invalid login credentials"
        flash("Invalid email or password. Please try again.", "font-semibold text-red-500")
        return redirect(url_for('login')) # Redirect to login.html
    
    if session_response:
        # print(session_response)
        user = session_response.user
        uid = user.id
        user_team= get_user_team(uid)
        user_info = {
            'email': user.email,
            'email_prefix': email.split('@')[0],
            'username': user.user_metadata.get('username', user.email),
            'uid': user.id,
            'user_team': user_team
        }
        flask_session['user_info'] = user_info
        return redirect(url_for('home'))
    else:
        flash("Login Failed", "error")
        return "Login Failed", 401
