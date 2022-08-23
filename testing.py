import requests

def recipe_search(ingredient):
    app_id = 'laurahill207@hotmail.com'
    app_key = 'Hector2021'
    result = requests.get(
    'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,app_key)
    )

    url= 'https://api.edamam.com/search?q={INGREDIENT}&app_id={YOUR_APP_KEY}&app_key={YOUR_APP_KEY}'

    response = requests.get(url)
    recipe_search = response.json()
    return response['recipes']

#
def run():
    ingredient = input('Please enter an ingredient: ')
    requests = recipe_search(ingredient)
    for result in requests:
        recipe = result['recipe']

        print("Here are some recipes including {}." .format(ingredient))
        print(recipe['label'])
        print(recipe['uri'])
        print()

    if none:
        print("There are no recipes with this ingredient. Please try another.")


run()

