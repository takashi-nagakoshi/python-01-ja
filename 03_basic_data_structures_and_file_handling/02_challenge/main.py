import math
import random

rock = 0
scissors = 1
paper = 2

while True:
    # ユーザー
    user_choice = int(input("Select your hand by 0/1/2 (0-rock, 1-scissors, 2=paper) :"))

    # コンピューター
    # 0 1 2
    # 0.3 * 3 = 0.9 => 0
    # 0.4 * 3 = 1.2 => 1
    # 0.7 * 3 = 2.1 => 2
    computer_choice = math.floor(random.random() * 3)

    if (
        (user_choice == rock and computer_choice == scissors)
        or (user_choice == scissors and computer_choice == paper)
        or (user_choice == paper and computer_choice == rock)
    ):
        print("You win!")
    elif user_choice == computer_choice:
        print("It is a draw!")
    elif (
        (user_choice == rock and computer_choice == paper)
        or (user_choice == scissors and computer_choice == rock)
        or (user_choice == paper and computer_choice == scissors)
    ):
        print("Computer wins!")