from flask import Flask, render_template, request, redirect, url_for
from config.supabase_client import supabase

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# default route for landing page
@app.route('/')
def home():
    return render_template('index.html')


# route for playerstats page
@app.route('/playerstats')
def playerstats():
    response = supabase.table('playerdata').select('*').execute()
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

# attempt to create login
# Gets email and password, if user logs in redirect to /home else return 401
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = supabase.auth.sign_in_with_password({ 'email': email, 'password': password })
    if user:
        return redirect(url_for('home'))
    else:
        return "Login Failed", 401

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    user = supabase.auth.sign_up({ 'email': email, 'password': password })
    if user:
        return redirect(url_for('home'))
    else:
        return "Sign-up failed", 401

if __name__ == '__main__':
    app.run(debug=True)