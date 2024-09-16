from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, static_folder='static')
app.config['TEMPLATES_AUTO_RELOAD'] = True


# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Breakfast Page
@app.route('/breakfast')
def breakfast():
    return render_template('breakfast.html')

# Mains Page
@app.route('/mains')
def mains():
    return render_template('mains.html')

# Dessert Page
@app.route('/dessert')
def dessert():
    return render_template('dessert.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Signup Page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Account Page (only after login/signup)
@app.route('/account')
def account():
    # Normally you'd have logic here to check if a user is logged in
    return render_template('account.html')


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
