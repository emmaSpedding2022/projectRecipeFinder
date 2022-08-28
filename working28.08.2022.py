import requests
from colorama import Fore
#******
#Method to run main program
#******
def main():
     while True:
         ingredient = input(Fore.GREEN + 'Enter an ingredient ')
         data = basic_search(ingredient)
         #check if there are any recipes for the ingredient input
         if len(data['hits']) > 0 :
             results(ingredient, data)
             #Filter the results
             filterResult = filter(data['hits'])
             #if the filter returns no results, filter again until you get a result
             while filterResult ==[]:
                 filterResult = filter(data['hits'])
         #if there are no recipes for the ingredient rerun
         else:
             print(Fore.RED + 'there are no recipes containing that ingredient try again,')

#******
# method to get access to the api and return results from 0 - 15
# this can be added at the end of the search to only get recipes that are Keto friendly (&health=keto-friendly)
#******
def basic_search(ingredient):
    id = 'bc7182eb'
    key = 'ae53400b50540675de6131d635744446'
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&from=0&to=15'.format(ingredient, id,
    key)
    response = requests.get(url)
    return response.json()

#******
# method to get list of recipes containing ingredient entered by the user
#******
def results(ingredient, data):
    recipe_number = 0
    # data = hits
    for recipe in data['hits']:
        label = (recipe['recipe']['label'] )
        url = (recipe['recipe']['url'] )
        recipe_number = recipe_number +1
        print(Fore.BLUE +'Recipe {}, is {}, and the url is {}'.format(recipe_number,label,url))

#******
# method to filter list by calories
#******
def calories(calorie_input,hits):
    data = hits
    newData = []
    #For each recipe check if the calories are less than the calories input by the user
    for recipe in data:
        calories = (recipe['recipe'] ['calories'])
        #if the calories are less than user input add to a new list and return that list
        if calories < calorie_input:
            newData.append(recipe)
    return newData

#******
# method to filter list by cooking time in minutes
#******
def cook_time(time_input, hits):
    data = hits
    newData = []
    #For each recipe filtered already by calories: check if the cooking time is less than the time input by the user
    for recipe in data:
        time = (recipe['recipe'] ['totalTime'])
        #if the time to cook is less than user input add to a new list and return that list
        if int(time) > 0 and int(time) < int(time_input):
            newData.append(recipe)
    return newData

#******
# method to filter the recipes
#******
def filter(hits):
        #takes informtion from the user on the amount of calories they want in the recipe
        calorie_input = int(input(Fore.GREEN + "how many calories would you like to have for your recipe? "))
        hits = calories(calorie_input,hits)
        #takes informtion from the user on the amount of time in minutes they have to cook the recipe
        meal_input = input('how many minutes have you got ?')
        hits = cook_time(meal_input, hits)
        printResults(hits)
        if len(hits) == 0:
            print(Fore.RED + 'There are no recipes that are under {} calories and take less than {} minutes to prepare'.format(calorie_input, meal_input))
            print(Fore.RED + 'Increase calories and/or time to filter the list again ')

        return hits

#******
#Method to print the results of the search
#******
def printResults(hits):
    for recipe in hits:
        calories = (recipe['recipe']['calories'])
        label = (recipe['recipe']['label'])
        url = (recipe['recipe']['url'])
        time = (recipe['recipe'] ['totalTime'])
        print(Fore.BLUE + '#{} is {} calories, it take {} minutes the link for the recipe is:'.format(label, int(calories), time) + ' {}' .format(url))


main()

#******
#Method to filter on a health label - not complete
#******
# def healthLabels():
#     recipe_number = 0
#     data = basic_search(ingredient)
#     for recipe in data['hits']:
#         # alergy = 'Sugar'
#         label = (recipe ['recipe'] ['label'])
#         healthLabel = (recipe['recipe']['healthLabels'] )
#         recipe_number = recipe_number +1
#         if 'Keto-Friendly' in healthLabel:
#             print('true')
#         else:
#             print('not true')
#         print('Recipe {}, is {}'.format(recipe_number,healthLabel))
