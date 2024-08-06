import os
from flask import Flask, render_template, request, redirect, url_for, flash, session as flask_session, g
from config.supabase_client import supabase
from dotenv import load_dotenv
from config.usertables import get_user_team, update_coins, update_points, remove_player, add_player, insert_user_table
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
    print(flask_session)
    # 518295b1-b9c0-41b0-9748-b2d876d3655f
    return render_template('index.html')

# route for playerstats 
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

# Route for myteam page
@app.route('/myteam')
def myteam():
    app.logger.debug('Session: %s', flask_session)
    if 'user_info' not in flask_session:
        return redirect(url_for('login'))

    uid = flask_session['user_info'].get('uid')
    return redirect(url_for('show_team', user_id=uid))

# Route that appends uid to the end of the URL
@app.route('/myteam/<user_id>')
def show_team(user_id):
    user_team = get_user_team(user_id)

    if not user_team:
        return redirect(url_for('home'))

    if isinstance(user_team, list) and len(user_team) > 0:
        team = user_team[0]  # Get team record

        return render_template(
            'pages/myteam.html',
            points=team.get('total_points'),
            coins=team.get('coins'),
            center=team.get('center'),
            point_guard=team.get('point_guard'),
            shooting_guard=team.get('shooting_guard'),
            power_forward=team.get('power_forward'),
            small_forward=team.get('small_forward')
        )
    else:
        return redirect(url_for('home'))

# Function to retrieve corresponding user team
def get_user_team(uid):
    try:
        response = supabase.from_('user_teams').select('*').eq('uid', uid).execute()
    except Exception as e:
        flash("Access token expired. Please login again.", "font-semibold text-red-500")
        return redirect(url_for('login')) # Redirect to login.html
    
    if response and response.data:
        return response.data
    else:
        return None

# route for playershop page
@app.route('/playershop')
def playershopteams():
    response = supabase.table('teamdata').select('*').execute()
    team_data = response.data if response.data else []
    print(team_data)
    return render_template('pages/playershopteams.html', teams=team_data)


# route for players of a specific team
@app.route('/playershop/<team_id>')
def playershop_team(team_id):
    # Fetch team data
    team_response = supabase.table('teamdata').select('*').eq('team_id', team_id).execute()
    team_data = team_response.data[0] if team_response.data else None

    # Fetch players for the specific team
    players_response = supabase.table('playervalues').select('*').eq('team_id', team_id).execute()
    players_data = players_response.data if players_response.data else []

    return render_template('pages/playershopteam.html', team=team_data, players=players_data)


# register and login pages
@app.route('/register')
def register():
    return render_template('pages/register.html')

@app.route('/login')
def login():
    return render_template('pages/login.html')

# login endpoints

# triggered on form submit in pages/register.html
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
            'email_prefix': email.split('@')[0],
            'username': username
        }
        return redirect(url_for('home'))
    else:
        return "Sign-up failed", 401

# triggered on form submit in pages/login.html
@app.route('/postlogin', methods=['POST'])
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
        print(session_response)
        user = session_response.user
        user_info = {
            'email': user.email,
            'email_prefix': email.split('@')[0],
            'username': user.user_metadata.get('username', user.email),
            'uid': user.id,
        }
        flask_session['user_info'] = user_info
        return redirect(url_for('home'))
    else:
        flash("Login Failed", "error")
        return "Login Failed", 401

# logout route
@app.route('/logout')
def logout():
    flask_session.pop('user_info', None)
    return redirect(url_for('home'))    

if __name__ == '__main__':
    app.run(debug=True)