# this program will pull random meal plans for the keto diet

import random

proteins = [
    'chicken',
    'steak',
    'fish',
    'sausage link',
    'ham',
    'pastrami',
    'pork',
    'ground beef',
    'turkey',
    'seafood',
    'hot dogs',
    'eggs'
]

veggies = [
    'cauliflower',
    'artichokes',
    'cabbage',
    'celery',
    'mushrooms',
    'okra',
    'sauerkraut',
    'spinach',
    'tomatoes',
    'brocolli',
    'squash',
    'zuchinni',
    'brussel sprouts',
    'green salad',
    'radish',
    'turnip',
    'Jicama',
    'green beans',
    'cucumber',
    'onion',
    'bell peppers'
]

fats = [
    'butter',
    'cooking oil',
    'cheese',
    'bacon',
    'avocado',
    'dressing',
    'nuts',
    'pork rinds'
]

meal = {
    'protein': random.choice(proteins),
    'veggie': random.choice(veggies),
    'fat': random.choice(fats)
}

# sometimes we want one more veggie
if random.randint(0,100) < 50:
    meal['veggie'] = meal['veggie']  + ' and ' + random.choice(veggies)     



meal_str = "Tonight's meal is {protein} with a side of {veggie}, topped with {fat}."
print(meal_str.format(**meal))