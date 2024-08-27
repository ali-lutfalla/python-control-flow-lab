# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.



def check_letter(letter):
  # Check for the type of the input
  if not isinstance(letter, str):
      raise Exception("Sorry, please enter a string")

  # Check if the input is a single letter
  if len(letter) != 1:
      raise Exception("Sorry, please enter only one letter")

  vowels = ['a', 'e', 'i', 'o', 'u']

  if letter in vowels:
      print(f"The letter {letter} is a vowel")
  else:
      print(f"The letter {letter} is a consonant")

# Call the function
try:
  check_letter(letter = input("Enter a letter: ").lower())
except Exception as e:
  print(e)

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility(age):
#     # Your control flow logic goes here
  if not isinstance(age, int):
    raise Exception("Sorry, please enter a valid number")
  if age < 0:
    raise Exception("Sorry, please enter a valid age")
  age_to_vote = 18
  if age >= age_to_vote:
    print("You are eligible to vote")
  else:
    print("You are not eligible to vote")

# Call the function
try:
  check_voting_eligibility(age = int(input("Enter your age: ")))
except Exception as e:
  print(e)


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years(dog_age):
    # Your control flow logic goes here
  if not isinstance(dog_age, int):
    raise Exception("Sorry, please enter a valid number")
  if dog_age < 0:
    raise Exception("Sorry, please enter a valid age")
  count_for_age = 1
  total_dog_years = 0
  while count_for_age <= dog_age:
    if count_for_age <= 2:
      total_dog_years += 10
    else:
      total_dog_years += 7
    count_for_age += 1
  print(f"The dog's age in dog years is {total_dog_years}")

# Call the function
try:
  calculate_dog_years(dog_age = int(input("Input a dog's age: ")))
except Exception as e:
  print(e)


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice(is_cold, is_raining):
#     # Your control flow logic goes here
  if not isinstance(is_cold, bool):
    raise Exception("Sorry, please enter a valid boolean")
  if not isinstance(is_raining, bool):
    raise Exception("Sorry, please enter a valid boolean")
  if is_cold and is_raining:
        print("Wear a waterproof coat.")
  elif is_cold and not is_raining:
        print("Wear a warm coat.")
  elif not is_cold and is_raining:
        print("Carry an umbrella.")
  elif not is_cold and not is_raining:
        print("Wear light clothing.")
  

# Call the function
try:
  weather_advice(is_cold=eval(input("Is it cold? (True/False): ")), is_raining=eval(input("Is it raining? (True/False): ")))
except Exception as e:
  print(e)


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season(month, day):
    # Your control flow logic goes here
    if not isinstance(month, str):
        raise Exception("Please enter a valid month entry!")
    if not isinstance(day, int):
        raise Exception("Please enter a valid day!")
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    if month not in months:
        raise Exception("Please enter a month in the range of MMM format")
    if day > 31 or day < 1:
        raise Exception("Please enter a valid number in the range of the days of the month")
    season_dates = {
        "Winter": [("Dec", 21, 31), ("Jan", 1, 31), ("Feb", 1, 28), ("Mar", 1, 19)],
        "Spring": [("Mar", 20, 31), ("Apr", 1, 30), ("May", 1, 31), ("Jun", 1, 20)],
        "Summer": [("Jun", 21, 30), ("Jul", 1, 31), ("Aug", 1, 31), ("Sep", 1, 21)],
        "Fall": [("Sep", 22, 30), ("Oct", 1, 31), ("Nov", 1, 30), ("Dec", 1, 20)],
    }
    for season, dates in season_dates.items():
        for m, start, end in dates:
            if month == m and start <= day <= end:
                print(f"{month} {day} is in {season}.")
                return
    print("You probably Entered out of bound day value for the month!")
    
        
# Call the function
try:
    determine_season(month=input("Please enter the month in MMM format like Jan: "), day=int(input("please enter the day of the month: ")))
except Exception as e:
    print(e)