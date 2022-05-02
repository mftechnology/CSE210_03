

from ListDice import ListDice




def main():
    tryagain = "yes"
    score_total = 0
    
    while tryagain == "yes" or tryagain == "y":
        score = 50
        Round = ListDice() 
        listdice = Round.listDice
        result = verifyscore(listdice,score)
        score_total += result 
        display(listdice,result,score_total)
        
        tryagain = input("Roll dice? You must enter 'y' or 'n' ").lower()

def display(msg,score, score_total):
    print("============================")
    print ("Rolling the dices...")
    print(f"The numbers are: {msg}")
    print()
    print(f"Score round: {score}")
    print(f"Score total: {score_total}")
    print()
    print("============================") 

def verifyscore(list,score):
    for i in range(5):
        if list[i] == 1:
            score += 100
        elif list[i] == 5:
            score += 50
    return score    

main()