from flask import Flask, render_template, redirect, jsonify, url_for, request, session
import os
from recipes import recipes, get_recipe_by_id


app = Flask(__name__, static_folder='static')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'secret_key'


user_datastore = {
    'admin': {'password': 'adminpass', 'is_admin': True},
    'user': {'password': 'userpassword', 'is_admin': False}
}


# Photo upload configuration
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Make sure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# Home Page
@app.route('/')
def home():
    """Home page for the app."""
    latest_recipe = get_latest_recipe()
    is_logged_in = 'username' in session  # Check if the user is logged in
    return render_template("index.html", latest_recipe=latest_recipe, is_logged_in=is_logged_in)





@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = user_datastore.get(username)
       
        # Check if the user exists and the password matches
        if user and user['password'] == password:
            session['username'] = username
            session['is_admin'] = user.get('is_admin', False)
           
            # Redirect admin to the admin account page
            if session['is_admin']:
                return redirect(url_for('admin_account'))
           
            # Redirect regular users to the home page
            return redirect(url_for('home'))
        else:
            return "Invalid username or password", 401
       
    return render_template('login.html')


# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
       
        # Prevent the use of reserved admin credentials
        if username == 'admin' or password == 'adminpassword':
            return "Username or password not allowed", 403
       
        # Check if the username is already taken
        if username in user_datastore:
            return "Username already exists", 409
       
        # Add the new user to the datastore
        user_datastore[username] = {'password': password, 'is_admin': False}  # Set new user as non-admin
        session['username'] = username
        session['is_admin'] = False  # Regular user
       
        return redirect(url_for('home'))
   
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
        recipe_servings = request.form['servings']
        recipe_vegan = request.form.get('vegan', 'No')
        recipe_ingredients = request.form['ingredients']  # Capture the ingredients


        # Create the new recipe dictionary
        new_id = max([r['id'] for cat in recipes.values() for r in cat], default=0) + 1
        new_recipe = {
            'id': new_id,
            'title': recipe_title,
            'category': recipe_category,
            'servings': recipe_servings,
            'vegan': recipe_vegan,
            'ingredients': recipe_ingredients.split("\n"),  # Store ingredients as a list
            'instructions': recipe_instructions.split("\n"),  # Store instructions as a list
        }


        # Add the new recipe to the corresponding category
        if recipe_category not in recipes:
            recipes[recipe_category] = []  # Create the category if it doesn't exist


        recipes[recipe_category].append(new_recipe)


        return redirect(url_for('admin_account'))  # Redirect after successful upload


    return render_template('admin_account.html')




#  Latest Recipe Section
def get_latest_recipe():
    all_recipes = [r for cat in recipes.values() for r in cat]  # Flatten the recipe lists
    if not all_recipes:
        return None  # No recipes available
    latest_recipe = max(all_recipes, key=lambda x: x['id'])  # Get the recipe with the highest ID
    return latest_recipe






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


    # Render the recipe page and pass the recipe
    return render_template('recipes.html', recipe=recipe)


@app.route('/upload_recipe', methods=['POST'])
def upload_recipe():
    return jsonify({'success': False, 'message': 'Use the admin_account route to upload recipes.'})




@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()  # Get the search query and convert to lowercase for case-insensitive search


    if not query:
        return redirect(url_for('home'))  # If no query, redirect to home


    search_results = []


    # Search through all the recipes in all categories
    for category, recipe_list in recipes.items():
        for recipe in recipe_list:
            # Check if the query matches the recipe title, category, or vegan status
            if (query in recipe['title'].lower() or
                query in recipe['category'].lower() or
                (query == 'vegan' and recipe['vegan'].lower() == 'yes')):
                search_results.append(recipe)


    # If no results found, you can add a message or handle it in the template
    if not search_results:
        return render_template('search_results.html', message="No recipes found.", recipes=search_results)


    # Render the results on a separate template
    return render_template('search_results.html', recipes=search_results)




if __name__ == '__main__':
    app.run(debug=True)
