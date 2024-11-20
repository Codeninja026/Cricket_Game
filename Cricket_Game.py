
import random as rd
import time
your_score =0
computer_score = 0
innings =1

def load():
    for _ in range(5):
        time.sleep(0.4)
        print("..", end="", flush=True)
    print()


def toss():
    global innings
    print("Coined Tossed...",end="")
    load()
    choice = ['Heads', 'Tails']
    pred_choice = rd.choice(choice)
    print("1.Heads")
    print("2.Tails")
    print("Your call(1 or 2): ")
    time.sleep(1.5)
    toss = int(input())
    if (toss == 1 and "Heads" == pred_choice) or (toss == 2 and "Tails" == pred_choice):
        print("you win the toss")
        print("1.bowl first")
        print("2.bat first")
        bat_or_bowl = int(input())
        if bat_or_bowl==1:
            print("You elected to bowl")
            bowl()
            innings=2
            print("Get ready for bat..")
            load()
            time.sleep(3)
            bat()
            if your_score > computer_score:
                return
        else:
            print("You elected to bat")
            bat()
            innings=2
            print("Get ready for bowl..")
            load()
            time.sleep(1.5)
            bowl()
            if your_score > computer_score:
                return

    else:
        print("You Lose the toss")
        comp_bat_bowl = rd.choice(['bat','bowl'])
        if comp_bat_bowl == 'bat':
            print("Computer elected to bat")
            load()
            print("Your bowling...",end="")
            bowl()
            innings =2
            print("Your batting is ready to start.....",end="")
            load()
            bat()
            if your_score > computer_score:
                return
        else:
            print("Computer elected to bowl")
            print("You have to bowl first")
            bowl()
            innings=2
            print("Your batting....is ready to start",end="")
            load()
            bat()
            if your_score > computer_score:
                return

def bowl():
    global your_score, computer_score,innings
    while True:
        print("Select bowler..")
        load()
        time.sleep(1)
        print("1.speed bowler")
        print("2.spinner")
        print("Enter your choice: ")
        computer_choice_score = rd.choice([1,2,3,4,6])
        choice_bowler = int(input())
        if choice_bowler==1:
            for i in range(6):
                print("Bowl->",(i+1))
                print("1.Yorker")
                print("2.Bouncer")
                print("3.Cutter")
                print("4.Slower ball")
                print("5.In swing")
                print("6.Out swing")
                print("Enter choice type: ")
                choice_type = int(input())
                print("Bowling...",end="")
                load()
                computer_predicted_choice = rd.randrange(1,6)

                if choice_type == computer_predicted_choice:
                    print("Computer out")
                    print(f"computer score is {computer_score}")
                    return
                else:
                    print(f"Computer hitted {computer_choice_score}")
                    computer_score += computer_choice_score
                    if innings == 2:
                        if your_score < computer_score:
                            return
                    print(f"Computer score: {computer_score}")
        else:
            for i in range(6):
                print("Bowl->",(i+1))
                print("1.Googly")
                print("2.Carrom ball")
                print("3.Off spin")
                print("Enter your choice: ")
                choice_type = int(input())
                print("Bowling...",end="")
                load()
                computer_predicted_choice = rd.randrange(1, 3)
                if choice_type == computer_predicted_choice:
                    print("Computer Out")
                    print(f"computer score is {computer_score}")
                    return
                else:
                    print(f"Computer hitted {computer_choice_score}")
                    computer_score += computer_choice_score
                    if innings == 2:
                        if your_score > computer_score:
                            return
                    print(f"computer score {computer_score}")



def bat():
    global your_score, computer_score, innings
    range = [1,2,3,4,6]
    score =0

    while True:
        print("Enter your run: (1,2,3,4,6): ")
        x = int(input())
        if x<1 or x>6 or x==5 :
            print("Invalid,run enter again")
        else:
            computer_predict =rd.choice(range)
            if computer_predict == x :
                print("Your Out")
                print(f"Your score is: {your_score}")
                break
            else:
                your_score += x
                if innings == 2:
                    if your_score > computer_score:
                        return
                print(f"Your score is: {your_score}")


if __name__=="__main__":
    while True:
        print("1.start\n2.exit\n")
        v= int(input())
        if v<1 or v>2:
            print("Invalid choice try again")
        else:
            if v==1:
                print("Game started")
                toss()
                if your_score>computer_score:
                    print("You win the game..")
                    print("Ooooo....")
                else:
                    print("You lose the game")
                    print("better luck next time")

            else:
                exit(0)