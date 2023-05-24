foods = ("apple", "banana", "orange", "mango", "straberry", "grape", "mandarin", "strawberry")

calories = (52, 96, 62, 60, 33, 68, 50, 33)

print(foods)
print(calories)


foods_list = list(foods)
calories_list = list(calories)

print(f"{foods_list[4]} caloric value is {calories_list[4]}")

print(f"{foods_list[-2]} caloric value is {calories_list[-2]}")

print(set(foods_list))

fruits = {"apple": 52, "banana": 96, "orange": 62, "mango": 60, "strawberry": 33, "grape": 68, "mandarin": 50, "strawberry": 33}

fruits["tomato"] = 60
fruits["grape"] = 50

print(fruits)