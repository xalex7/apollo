# Welcome messaage:
print("Hi .. This is Apollo - Your Personal Assistant")

# Collecting user information:
name = input("What is your name? ")
age = int(input("How old are you? "))

# Custom message based on age:
if age < 18:
    print(f"Hi {name}, you're young!")
elif 18 <= age < 60:
    print(f"Hi {name}, you're an adult!")
else:
    print(f"Hi {name}, You're at your golden age!")

# Check if a number is even or odd:
print("\nLet's analyze a number!")
number = int(input("Enter a number: "))

# Analyzing a number:
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

# Ask for favorite activities:
print("Tell me your favorite activities. Type 'Done' when you're finished.")

# Initialize an empty activities list:
activities = []

# Loop asking to collect favorite activities input:
while True:
    activity = input("Enter an activity: ")
    if activity.lower() == 'done':
        break
    elif activity == '':
        continue
    activities.append(activity)

# Display the list of activities:
print("\nYour favorite activities are:")
for activity in activities:
    print(f"- {activity}")

# Option to remove an activity:
wantToRemove = input("\nWould you like to remove any of the activites? ")
if wantToRemove.lower() == "yes":
    removeActivity = input("Which activity would you like to remove? ")
    if removeActivity in activities:
        activities.remove(removeActivity)
        print(f"{removeActivity} was removed.")
    else:
        print(f"{removeActivity} is not in your activities list.")
    
    print("Updated list of activities:")
    for activity in activities:
        print(f"- {activity}")
else:
    print("\nThank You!\n")