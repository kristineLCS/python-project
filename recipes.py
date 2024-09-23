recipes = {
    'breakfast': [
        {'id': 1,
        'title': 'Buttermilk Fluffy Pancakes',
        'category': 'Breakfast',
        'author': 'Jane',
        'servings': '12',
        'vegan': 'No',
        'ingredients': ['3 cups plain flour', '3 tbsp white sugar', '3 tsp baking powder', '1 1/2 tsp baking soda', '3/4 tsp salt', '3 cups buttermilk', '1/2 cup milk', '3 eggs', '1/3 cup melted butter'],
        'instructions': ['Combine all the dry ingredients in a bowl.', 'In a seperate bowl, mix together the buttermilk, milk, eggs, and melted butter.', "Add the wet mixture into the dry mixture. Don't over mix the batter or you will end up with a tough pancake",
                         'Get your pan or griddle hot and greased with butter', 'Pour or scoop your batter into the pre-heated pan and wait until bubbles appear on your pancake, and then flip it with your spatula.', 'Continue with the rest of your batter.', 
                         'Decorate with toppings of your choice and enjoy!.']
         }
    ],
    'mains': [
        {'id': 2,
        'title': 'Beef and Broccoli',
        'category': 'Mains',
        'author': 'Nara',
        'servings': '4 people',
        'vegan': 'No',
        'ingredients': ['1 lb / 455g flank steak, thinly sliced', '2 tbsp olive oil, divided', '1 lb / 455g broccoli', '2 tsp sesame seed, optional for garnish', 'Sauce ingredients','1 tsp fresh grated ginger', 
                        '2 tsp grated garlic', '1/2 cup / 120ml hot water', '6 tbsp low sodium soy sauce', '3 tbsp light brown sugar', '1 1/2 tbsp corn starch', '1/4 tsp black pepper', '2 tbsp sesame oil'],
        'instructions': ['Optional but this dish is best paired with white rice, so start cooking your rice first before making this!', 'Freeze your steak for half an hour for easy slicing', 
                         'Combine all your sauce ingredients until everything is dissolved and well combined', 'Over a medium heat, add 1 tbsp of your olive oil and saute your broccoli florets for 4 - 5 mins until broccoli is bright green and crisp-tender. Transfer to a plate.', 
                         'Increase heat to high and add 1 tbsp of oilive oil to pan. Add beef and saute 2 minutes per side or just until cooked through.', 'Add sauce mixture and reduce heat to midium/low. Allow it to simmer for 3 - 4 minutes. Add broccoli and stir to combine. If sauce is too thick, carefully add 1 tbsp at a time until your deisred thickness/thiness is achieved.', 
                         'Serve with rice and enjoy!']
        }
    ],
    'dessert': [
        {'id': 3,
        'title': 'Red Velvet Cake',
        'category': 'Dessert',
        'author': 'Danny',
        'servings': '6',
        'vegan': 'No',
        'ingredients': ['2 1/2 cups / 300g plain flour', '1 tsp salt', '1 tsp baking soda', '1/2 cup / 113g unsalted room temp. butter', '1 1/2 cups / 300g granualated sugar', '2 large room temp. eggs', '2 tsp vanilla extract', '2 tbsp cocoa powder', '1 cup / 240ml room temp. buttermilk', '1 tbsp white vinegar', '1 - 2 tbsp liquid red food colouring',
                        'Cream Cheese Frosting', '454g room temp. cream cheese', '1 1/2 cups / 340g room temp. unsalted butter', '1 tsp vanilla extract', 'A pinch of salt', '675g confectioners sugar'],
        'instructions': ['Preheat oven to 177 degrees C. Butter and flour, or alternatively line your cake pans with baking paper.', 'In a medium bowl, sift flour salt, and baking powder' ]
        }
    ]
}

# Helper function to find a recipe by ID
def get_recipe_by_id(recipe_id):
    for category in recipes.values():
        for recipe in category:
            if recipe['id'] == recipe_id:
                return recipe
    return None
