import secrets

random_number = secrets.randbelow(100) + 1
score = 0
first_time = True
actual_number = random_number

while True:
    print(f"Actual number: {actual_number}")
    user_choice = input("The next number will be bigger or smaller? ")
    random_number = secrets.randbelow(100) + 1
    print(f"New number: {random_number}")
    if user_choice.lower() == "bigger":
        if random_number > actual_number:
            score += 1
            print(f"Nice! Score: {score}\n")
        else:
            print(f"Wrong! Score: {score}\n")
    elif user_choice.lower() == "smaller":
        if random_number < actual_number:
            score += 1
            print(f"Nice! Score: {score}\n")
        else:
            print(f"Wrong! Score: {score}\n")
    elif user_choice.lower() == "exit":
        print(f"You left the game with {score} points")
        break
    else:
        print("Invalid choice! Try again\n")
    actual_number = random_number
