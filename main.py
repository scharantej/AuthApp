 
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create the database tables
db.create_all()

# Define the home page route
@app.route('/')
def index():
    return render_template('index.html')

# Define the login page route
@app.route('/login')
def login():
    return render_template('login.html')

# Define the login handler route
@app.route('/login_handler', methods=['POST'])
def login_handler():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('profile'))

    return render_template('login.html', error="Invalid credentials")

# Define the register page route
@app.route('/register')
def register():
    return render_template('register.html')

# Define the register handler route
@app.route('/register_handler', methods=['POST'])
def register_handler():
    username = request.form['username']
    password = request.form['password']

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('login'))

# Define the profile page route
@app.route('/profile')
def profile():
    if 'logged_in' in session:
        return render_template('profile.html')

    return redirect(url_for('login'))

# Define the logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
