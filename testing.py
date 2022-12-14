# import requests
#
# def recipe_search(ingredient):
#     app_id = 'laurahill207@hotmail.com'
#     app_key = 'Hector2021'
#     result = requests.get(
#     'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,app_key)
#     )
#
#     url= 'https://api.edamam.com/search?q={INGREDIENT}&app_id={YOUR_APP_KEY}&app_key={YOUR_APP_KEY}'
#
#     response = requests.get(url)
#     recipe_search = response.json()
#     return response['recipes']
#
# def run():
#     ingredient = input('Please enter an ingredient: ')
#     requests = recipe_search(ingredient)
#     for result in requests:
#         recipe = result['recipe']
#
#         print("Here are some recipes including {}." .format(ingredient))
#         print(recipe['label'])
#         print(recipe['uri'])
#         print()
#
#     if None:
#         print("There are no recipes with this ingredient. Please try another.")
#
#
# run()
#

import requests

# method to get access to the api and return results from 0 - 15
def basic_search(ingredient):
    id = 'bc7182eb'
    key = 'ae53400b50540675de6131d635744446'
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&from=0&to=5&health=keto-friendly'.format(ingredient, id,
    key)
    print(url)
    response = requests.get(url)
    return response.json()

# method to get list of recipes containing ingredient entered
def results(ingredient, hits):
    recipe_number = 0
    data = hits

    while len(data['hits']) < 1:
        print('there are no recipes containing that ingredient try again,')
        ingredient = input('Enter an ingredient ')
        data = hits

    for recipe in data['hits']:
        label = (recipe['recipe']['label'] )
        url = (recipe['recipe']['url'] )
        recipe_number = recipe_number +1
        print('Recipe {}, is {}, and the url is {}'.format(recipe_number,label,url))

# method to filter list by calories
def calories(calorie_input,hits):
    data = hits
    newData = []
    recipe_number= 0
    for recipe in data:
        calories = (recipe['recipe'] ['calories'])
        label = (recipe ['recipe'] ['label'])
        url = (recipe['recipe'] ['url'])
        if calories < calorie_input:
            newData.append(recipe)
            # print(' {} is {} calories, the link for the recipe is: {}' .format(label, int(calories), url))
    return newData

# method to filter list by cooking time in minutes#
def cook_time(time_input, hits):
    data = hits
    newData = []
    for recipe in data:
        time = (recipe['recipe'] ['totalTime'])
        if int(time) > 0 and int(time) < int(time_input):
            # print(' Recipe {}: {} takes {} minutes to prepare, the link for the recipe is: {}'.format(recipe_number,label, int(time), url))
            newData.append(recipe)
    return newData


# method to filter the recipes
def filter(hits):
        hits = hits['hits']
        calorie_input = int(input("how many calories would you like to have for your recipe? "))
        hits = calories(calorie_input,hits)
        meal_input = input('how many minutes have you got ?')
        hits = cook_time(meal_input, hits)
        printResults(hits)

def printResults(hits):
    for recipe in hits:
        calories = (recipe['recipe']['calories'])
        label = (recipe['recipe']['label'])
        url = (recipe['recipe']['url'])
        time = (recipe['recipe'] ['totalTime'])
        print(' {} is {} calories, it take {} minutes the link for the recipe is: {}' .format(label, int(calories), time, url))


def healthLabels():
    recipe_number = 0
    data = basic_search(ingredient)
    for recipe in data['hits']:
        # alergy = 'Sugar'
        label = (recipe ['recipe'] ['label'])
        healthLabel = (recipe['recipe']['healthLabels'] )
        recipe_number = recipe_number +1
        if 'Keto-Friendly' in healthLabel:
            print('true')
        else:
            print('not true')
        print('Recipe {}, is {}'.format(recipe_number,healthLabel))


# Main program #
ingredient = input('Enter an ingredient ')
hits = basic_search(ingredient)
results(ingredient,hits)
# healthLabels()
# input_filter = input("you can filter your results by choosing \n c = calories  \n t = time taken  \nplease enter a choice c or t  ")
filter(hits)

