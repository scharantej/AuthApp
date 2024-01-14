 
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app
app = Flask(__name__)

# Define the login route
@app.route('/login', methods=['POST'])
def login():
    # Get the form data
    server_name = request.form['server_name']
    username = request.form['username']
    password = request.form['password']

    # Validate the credentials
    if server_name == 'my_server' and username == 'my_username' and password == 'my_password':
        # Redirect to the dashboard
        return redirect(url_for('dashboard'))
    else:
        # Display an error message
        return render_template('login.html', error='Invalid credentials')

# Define the dashboard route
@app.route('/dashboard')
def dashboard():
    # Render the dashboard page
    return render_template('dashboard.html')

# Run the app
if __name__ == '__main__':
    app.run()
