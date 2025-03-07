import random

def roll_dice(sides=6):
    """Simulate rolling a single die with a given number of sides."""
    return random.randint(1, sides)

def roll_multiple_dice(num_dice, sides=6):
    """Roll multiple dice and return the results as a list."""
    return [roll_dice(sides) for _ in range(num_dice)]

def main():
    print("Welcome to the Dice Roller Simulator!")
    
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            sides = int(input("Enter the number of sides on each die (default is 6): ") or 6)
        except ValueError:
            print("Please enter valid integers.")
            continue
        
        # Roll the dice
        results = roll_multiple_dice(num_dice, sides)
        
        print(f"You rolled: {results}")
        print(f"Total: {sum(results)}")
        
        # Ask user if they want to roll again
        roll_again = input("Do you want to roll again? (y/n): ").lower()
        if roll_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
