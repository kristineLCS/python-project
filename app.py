from flask import Flask, render_template, redirect, url_for, request, session

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

# @app.route('/status', methods=['post'])
# def set_status():
#     """Set the status of the current user.
#     """
#     # If the user is not logged in, redirect to the login page.
#     if 'username' not in session:
#         return redirect(url_for('login'))

#     # Get the status from the form field.
#     status = request.form['status']

#     # Get the username from the session.
#     # Note this also means a user can only set their own status.
#     username = session['username']

#     # Update the status in the user datastore.
#     user_datastore[username] = status

#     # Redirect to the home page.
#     return redirect(url_for('home'))

# Breakfast Page
@app.route('/breakfast')
def breakfast():
    return render_template('breakfast.html')

# Mains Page
@app.route('/mains')
def mains():
    return render_template('main.html')

# Dessert Page
@app.route('/dessert')
def dessert():
    return render_template('dessert.html')





# Route for breakfast category with recipe id
# @app.route('/breakfast/<int:id>')
# def breakfast(id):
#     # Fetch recipe by id from breakfast recipes
#     recipe = get_breakfast_recipe_by_id(id)
#     return render_template('breakfast.html', recipe=recipe)

# # Route for mains category with recipe id
# @app.route('/mains/<int:id>')
# def mains(id):
#     # Fetch recipe by id from mains recipes
#     recipe = get_main_recipe_by_id(id)
#     return render_template('mains.html', recipe=recipe)

# # Route for dessert category with recipe id
# @app.route('/dessert/<int:id>')
# def dessert(id):
#     # Fetch recipe by id from dessert recipes
#     recipe = get_dessert_recipe_by_id(id)
#     return render_template('dessert.html', recipe=recipe)

# def get_breakfast_recipe_by_id(id):
#     # Placeholder function to get a recipe by id for breakfast
#     # You should replace this with actual data fetching logic
#     recipes = {
#         1: 'Pancakes',
#         2: 'French Toast'
#     }
#     return recipes.get(id, 'Recipe not found')

# def get_main_recipe_by_id(id):
#     # Placeholder function to get a recipe by id for mains
#     # You should replace this with actual data fetching logic
#     recipes = {
#         1: 'Spaghetti Bolognese',
#         2: 'Chicken Curry'
#     }
#     return recipes.get(id, 'Recipe not found')

# def get_dessert_recipe_by_id(id):
#     # Placeholder function to get a recipe by id for dessert
#     # You should replace this with actual data fetching logic
#     recipes = {
#         1: 'Chocolate Cake',
#         2: 'Apple Pie'
#     }
#     return recipes.get(id, 'Recipe not found')

if __name__ == '__main__':
    app.run(debug=True)
