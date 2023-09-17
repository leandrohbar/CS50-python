# 1. Create a dictionary of fruits and their calories
def main():
    fruit = str(input("Item: ")).strip().title()
    calorie(fruit)


# 2. Create a function that takes a fruit as an argument and returns the calories for that fruit
def calorie(fruits):
    calories = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80,
    }
    if fruits in calories:
        print(f"Calories: {calories[fruits]}")


main()
