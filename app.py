from flask import Flask, render_template, redirect, url_for, request, session
from recipes import recipes, get_recipe_by_id

app = Flask(__name__, static_folder='static')
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.secret_key = 'Replace me with a real secret key for production use'

user_datastore = {}


# Home Page
@app.route('/')
def home():
    """Home page for the app."""
    return render_template("index.html")

@app.route('/login', methods=['GET'])
def login():
    if 'username' in session:
        return redirect(url_for("account"))

    # Otherwise, display the login form.
    return render_template('login.html')
 
@app.route('/login', methods=['POST'])
def login_action():
    # Get the username from the form field.
    session["username"] = request.form["username"]
    session["password"] = request.form["password"]

    return redirect(url_for("account"))


# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle the signup action
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]
        return redirect(url_for("account"))
    
    # If the user is already logged in, redirect to account page
    if 'username' in session:
        return redirect(url_for("account"))
    
    # Render the signup page for GET request
    return render_template('sign-up.html')

# Account Page (only after login/signup)
@app.route('/account')
def account():
    # Normally you'd have logic here to check if a user is logged in
    return render_template('account.html')

@app.route('/logout')
def logout():
    session.pop("username", None)

    return redirect(url_for("home"))

@app.route('/breakfast')
def show_breakfast_recipes():
    return render_template('breakfast.html', recipes=recipes['breakfast'])

@app.route('/mains')
def show_mains_recipes():
    return render_template('mains.html', recipes=recipes['mains'])

@app.route('/dessert')
def show_dessert_recipes():
    return render_template('dessert.html', recipes=recipes['dessert'])

@app.route('/recipe/<int:recipe_id>')
def recipe_page(recipe_id):
    recipe = get_recipe_by_id(recipe_id)
    if recipe:
        return render_template('recipes.html', recipe=recipe)
    else:
        return "Recipe not found", 404
    

if __name__ == '__main__':
    app.run(debug=True)
