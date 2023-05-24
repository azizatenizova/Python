# years = int(input("Enter number of years: "))

# unit = int(input("""Pick which unit to convert to: 
#                  1-Days 
#                  2-Weeks 
#                  3-Months
#                  Input: """)) 

# if unit == 1:
#     print(f"{365 * years} days")
# elif unit == 2:
#     print(f"{52 * years} weeks")
# elif unit == 3:
#     print(f"{12 * years} months")
# else: 
#     print("Pick the right choice")

age = int(input("Enter your age: "))
if age <= 13:
    print("child")
elif age >= 13 and age <= 18:
    print("teenager")
elif age >= 18 and age <= 65:
    print("adult")
elif age > 65: 
    print("Elder")
