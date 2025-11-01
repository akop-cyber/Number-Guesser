
import random
playgame = "yes"
while playgame == "yes":
    print("There will be three levels in the game")
    print("Level 1: range of number: 1 - 100 with 10 attempts")
    print("Level 2: range of number: 1 - 200 with 8 attempts")
    print("Level 3: range of number: 1 - 300 with 6 attempts")
    print("Level 4: customizable range and attempts")
    level = int(input("Enter the level(1/2/3/4): "))
    if level == 1:
        a = 100
        b = 10
        print("You chose level 1. You will get",b,"attempts and you have to guess between 1 -",a)
    elif level == 2:
        a = 200
        b = 8
        print("You chose level 2. You will get",b,"attempts and you have to guess between 1 -",a)
    elif level == 3:
        a = 300
        b = 6
        print("You chose level 3. You will get",b,"attempts and you have to guess between 1 -",a)
    elif level == 4:
        a = int(input("Enter the maximum number you want: "))
        b = int(input("Enter number of attempts you want: "))
    secret_num = random.randint(1,a)
    c = b + 1
    i = 0
    while i < c:
        guess = int(input("Enter your guess: "))
        if guess > secret_num:
            print("Too High")   
        elif guess < secret_num:
            print("Too Low")
        elif guess == secret_num:
            print("You Won. You guessed the number",secret_num,"in",i,"attempts")
            play_again = input("Do you want to play again(yes/no): ")
            play_again = play_again.lower()
            if play_again == "yes":
                playgame = "yes"
            elif play_again == "no":
                playgame = "no"
                print("Thank you for playing my game.")
                print("A game by Ak Studios")
            break
        i += 1
        if i == b:
            print("Sorry you are out of attempts")
            play_again = input("Do you want to play again(yes/no): ")
            play_again = play_again.lower()
            if play_again == "yes":
               playgame = "yes"
            elif play_again == "no":
               playgame = "no"
               print("Thank you for playing my game.")
               print("A game by Akop Studios")
            break




















    
    

