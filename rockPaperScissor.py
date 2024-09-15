import random

# This will return the choice of the computer
def comp_choice():
    choices=["rock","paper","scissor"]
    return random.choice(choices)

def find_winner(uc, cc):
    if uc==cc:
        return "draw"
    
    elif ((uc=="rock" and cc== "scissor")
          or(uc == "scissor" and cc == "paper")
          or(uc == "paper" and cc == "rock")):
        return "Player"
    
    else:
        return "Computer"
    
def play_game():
    cs=0
    ps=0
    while True:
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
            print("="*80)

        else:
            print("It's a draw")
        print(f"Score \n Computer : {cs} \n Player : {ps}\n\n")
        print("="*80)

    print("Final Score: ")
    print("Computeer Score : ",cs)
    print("Player Score : ",ps)
    print("Thanks for playing")

if __name__ == "__main__":
    play_game()
