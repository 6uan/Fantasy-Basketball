import os
from flask import Flask, render_template, request, redirect, url_for, flash, session as flask_session, g
from config.supabase_client import supabase
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

# runs before every request to get user info
@app.before_request
def load_user_info():
    g.user_info = flask_session.get('user_info', None)

# make user info globally available in all templates
@app.context_processor
def inject_user_info():
    return dict(user_info=g.user_info)

# default route for landing page
@app.route('/')
def home():
    return render_template('index.html')

# route for playerstats page
@app.route('/playerstats')
def playerstats():
    response = supabase.table('players').select('*').execute()
    player_data = response.data if response.data else []
    return render_template('pages/playerstats.html', players=player_data)

# route for leaderboards page
@app.route('/leaderboards')
def leaderboards():
    return render_template('pages/leaderboards.html')

# route for gameschedule page
@app.route('/gameschedule')
def gameschedule():
    return render_template('pages/gameschedule.html')

# route for gameschedule page
@app.route('/myteam')
def myteam():
    return render_template('pages/myteam.html')

# route for playershop page
@app.route('/playershop')
def playershop():
    return render_template('pages/playershop.html')

# register and login pages
@app.route('/register')
def register():
    return render_template('pages/register.html')

@app.route('/login')
def login():
    return render_template('pages/login.html')

# login endpoints
@app.route('/postregister', methods=['POST'])
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
        flask_session['user_info'] = {
            'email': email,
            'username': username
        }
        return redirect(url_for('home'))
    else:
        return "Sign-up failed", 401

@app.route('/postlogin', methods=['POST'])
def postlogin():
    email = request.form.get('email')
    password = request.form.get('password')
    session_response = None # Initialize session
    # Attempt to sign in with email and password
    try: 
        session_response = supabase.auth.sign_in_with_password({ 'email': email, 'password': password })
    # If the login fails, print the error message
    except Exception as e:
        print(e) # "Invalid login credentials"
        flash("Invalid email or password. Please try again.", "font-semibold text-red-500")
        return redirect(url_for('login')) # Redirect to login page
    
    # If the login is successful, redirect to the home page
    if session_response:
        user = session_response.user
        user_info = {
            'email': user.email,
            'username': user.user_metadata.get('username', user.email)
        }
        flask_session['user_info'] = user_info
        return redirect(url_for('home'))
    else:
        flash("Login Failed", "error")
        return "Login Failed", 401


if __name__ == '__main__':
    app.run(debug=True)