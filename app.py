from flask import Flask, render_template, redirect, jsonify, url_for, request, session
import os
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
        # recipe_author = session.get('username', 'Admin')
        recipe_servings = request.form['servings']
        recipe_vegan = request.form.get('vegan', 'No') 

        # Loops over all the lists of recipes in each category. Then, loops over each recipe r in the current category list cat.
        new_id = max([r['id'] for cat in recipes.values() for r in cat]) + 1

        # Create the new recipe dictionary
        new_recipe = {
            'id': new_id,
            'title': recipe_title,
            'category': recipe_category,
            # 'author': recipe_author,
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


# Photo upload
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Make sure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload_recipe', methods=['POST'])
def upload_recipe():
    # Get form data
    title = request.form.get('title')
    # author = request.form.get('author')
    category = request.form.get('category')
    servings = request.form.get('servings')
    vegan = request.form.get('vegan', 'No')  # Default to 'No' if unchecked
    ingredients = request.form.get('ingredients')
    instructions = request.form.get('instructions')

    # Handle file upload
    if 'photo' not in request.files:
        return jsonify({'success': False, 'message': 'No photo part'})

    photo = request.files['photo']

    if photo.filename == '':
        return jsonify({'success': False, 'message': 'No selected photo'})

    if photo:
        # Save the photo file in the 'static/uploads/' directory
        photo_filename = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
        photo.save(photo_filename)  # Save the file

        # Store the relative file path (so it can be used in the HTML)
        photo_url = f'/static/uploads/{photo.filename}'

        # Create a new recipe object
        new_recipe = {
            'title': title,
            # 'author': author,
            'photo': photo_url,  # Store the relative URL of the uploaded photo
            'category': category,
            'servings': servings,
            'vegan': vegan,
            'ingredients': ingredients.split("\n"),  # Assuming ingredients are entered line by line
            'instructions': instructions.split("\n")  # Assuming instructions are entered line by line
        }

        # Save `new_recipe` to the recipes dictionary under the appropriate category
        if category not in recipes:
            recipes[category] = []  # Create the category if it doesn't exist
        
        # Assign a new unique ID for the recipe
        new_id = max([r['id'] for cat in recipes.values() for r in cat], default=0) + 1
        new_recipe['id'] = new_id  # Add a unique ID to the recipe

        # Append the new recipe to the correct category
        recipes[category].append(new_recipe)

        return jsonify({'success': True, 'message': 'Recipe uploaded successfully!'})

    return jsonify({'success': False, 'message': 'Failed to upload recipe'})




if __name__ == '__main__':
    app.run(debug=True)
