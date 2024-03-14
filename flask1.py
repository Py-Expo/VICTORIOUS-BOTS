from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

# Dummy user data for demonstration purposes
users = {}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST','GET'])
def login():
    mobile_number = request.form.get('mobile_number')
    password = request.form.get('password')

    if mobile_number in users:
        stored_password_hash = users[mobile_number]['password_hash']
        if check_password_hash(stored_password_hash, password):
            # Successful login, redirect to the desired page
            return redirect(url_for('sos'))
    
    # If login fails, redirect back to login page with error message
    return redirect(url_for('index', error=True))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        mobile_number = request.form.get('mobile_number')
        password = request.form.get('password')

        # Check if the mobile number is already registered
        if mobile_number in users:
            return redirect(url_for('index', error=True))
        
        # Hash the password before storing it
        password_hash = generate_password_hash(password)

        # Store the user data (mobile number and hashed password)
        users[mobile_number] = {'password_hash': password_hash}

        # Redirect to login page after successful signup
        return redirect(url_for('index'))

    return render_template('signup.html')

@app.route('/sos')
def sos():
    # Your SOS logic goes here
    return render_template('sos.html')
@app.route('/user_location_map',methods=["GET","POST"])
def user_location_map():
    # Your SOS logic goes here
    return render_template('user_location_map.html')

@app.route('/redirect', methods=['POST'])
def redirect_to_page():
    redirect_url = request.form.get('redirect_url')
    # Assuming the user_location_map.html is in the "Templates" folder
    return redirect(redirect_url)

if __name__ == '__main__':
    app.run(debug=True)
