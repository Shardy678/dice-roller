import random

def roll(num_dice, num_sides):
    total = 0
    rolls = []
    for i in range(num_dice):
        roll_result = random.randint(1, num_sides)
        rolls.append(roll_result)
        total += roll_result
    return total, rolls

def main():
    while True:
        choice = input("Enter the dice notation (e.g., 2d6): ")
        dice_parts = choice.split('d')
        num_dice = int(dice_parts[0])
        num_sides = int(dice_parts[1])
        total, rolls = roll(num_dice, num_sides)
        print(f'Rolls: {rolls}')
        print(f'Total: {total}')

if __name__ == "__main__":
    main()
    
main()