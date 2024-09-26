from flask import Flask, render_template, redirect, url_for, request, session
from recipes import recipes, get_recipe_by_id

app = Flask(__name__, static_folder='static')
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.secret_key = 'secret_key'

user_datastore = {
    'admin': {'password': 'adminpassword', 'is_admin': True},
    'user1': {'password': 'userpassword', 'is_admin': False}
}


# Home Page
@app.route('/')
def home():
    """Home page for the app."""
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = user_datastore.get(username)

        if user and user['password'] == password:
            session['username'] = username
            session['is_admin'] = user.get('is_admin', False)

            if user['is_admin']:
                return redirect(url_for('admin_account'))

            # Redirect regular users to the home page
            return redirect(url_for('home'))
        else:
            # Handle invalid login
            return "Invalid username or password", 401
        
    return render_template('login.html')


# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in user_datastore:
            user_datastore[username] = {'password': password, 'is_admin': False}
            session['username'] = username
            return redirect(url_for('home'))
    
    # Render the signup page for GET request
    return render_template('sign-up.html')

@app.route('/admin/account', methods=['GET', 'POST'])
def admin_account():
    if not session.get('is_admin'):
        return "Unauthorized", 403  # Restrict access to non-admin users

    if request.method == 'POST':
        # Get the data from the form
        recipe_title = request.form['title']
        recipe_instructions = request.form['instructions']
        recipe_category = request.form['category']
        recipe_author = session.get('username', 'Admin')
        recipe_servings = request.form['servings']
        recipe_vegan = request.form.get('vegan', 'No') 

        # Loops over all the lists of recipes in each category. Then, loops over each recipe r in the current category list cat.
        new_id = max([r['id'] for cat in recipes.values() for r in cat]) + 1

        # Create the new recipe dictionary
        new_recipe = {
            'id': new_id,
            'title': recipe_title,
            'category': recipe_category,
            'author': recipe_author,
            'servings': recipe_servings,
            'vegan': recipe_vegan,
            'ingredients': [],
            'instructions': recipe_instructions.split("\n")
        }

        # Add the new recipe to the corresponding category
        recipes[recipe_category].append(new_recipe)

    return render_template('admin_account.html')


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


@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def recipe_page(recipe_id):
    # Fetch the recipe by ID
    recipe = get_recipe_by_id(recipe_id)
    
    # If recipe is not found, return a 404 error
    if not recipe:
        return "Recipe not found", 404

    # Render the recipe page and pass the recipe, no need for comments
    return render_template('recipes.html', recipe=recipe)


if __name__ == '__main__':
    app.run(debug=True)
