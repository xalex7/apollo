# Main program:
def main():
    print("Hi .. This is Apollo - Your Personal Assistant")
    # Collecting user information:
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    greet_user(name, age)
    years_until_100(age)
    check_even_or_odd()
    favorite_activities = collect_favorite_activites()
    save_activities(favorite_activities)

# Custom message based on age:
def greet_user(name, age):
    if age < 18:
        print(f"\nHi {name}, you're young!")
    elif 18 <= age < 60:
        print(f"\nHi {name}, you're an adult!")
    else:
        print(f"\nHi {name}, You're at your golden age!")

# Years until 100:
def years_until_100(age):
    years_left = 100 - age
    print(f"You'll be 100 in {years_left} years")

# Check if a number is even or odd:
def check_even_or_odd():
    print("\nLet's analyze a number!")
    number = int(input("Enter a number: "))

    # Analyzing a number:
    if number % 2 == 0:
        print(f"The number {number} is even.\n")
    else:
        print(f"The number {number} is odd.\n")

# Collect favorite activities:
def collect_favorite_activites():
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
    wantToRemove = input("\nWould you like to remove any of the activites? <Yes/No> ")
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
    
    return activities
    
def save_activities(activities):
    with open("activities.txt", "w") as file:
        for activity in activities:
            file.write(activity + "\n")

def load_activities():
    try:
        with open ("activities.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
if __name__ == "__main__":
    main()