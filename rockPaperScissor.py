import random

# This will return the choice of the computer.
def comp_choice():
    choices=["rock","paper","scissor"]
    return random.choice(choices)

# This will return the winner.
def find_winner(uc, cc):
    if uc==cc:
        return "draw"
    
    elif ((uc=="rock" and cc== "scissor")          # uc-User Choice, cc-Computer Choice
          or(uc == "scissor" and cc == "paper")
          or(uc == "paper" and cc == "rock")):
        return "Player"
    
    else:
        return "Computer"
    
# Game starts from here
def play_game():
    cs=0             # initialize score with 0        cs-Computer Score, ps-Player Score
    ps=0
    while True:              #the loop will circulate until you don't quit the game
        print("Rock, Paper, Scissor - Choose your move:")
        uc=input("Enter 'Rock', 'Paper', 'Scissor' (or 'quit' to stop playing): ").lower()      
        if (uc=='quit'):
            break

        if uc not in ["rock", "paper","scissor"]:
            print("Incorrect choice please try again.\n\n")
            continue

        cc=comp_choice()
        print("Computer Choose : ",cc)

        result=find_winner(uc, cc)
        if (result == "Player"):
            print("You win this match!")
            ps+=1
        elif (result == "Computer"):
            print("Computer win this match!")
            cs+=1
        else:
            print("It's a draw")
        print(f"Score \n Computer : {cs} \n Player : {ps}\n\n")
        print("="*80)

    print("Final Score: ")
    print("Computeer Score : ",cs)
    print("Player Score : ",ps)
    print("Thanks for playing")

# Program starts from here.
if __name__ == "__main__":
    play_game()
