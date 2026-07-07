import random
matchplayed=0
wins=0
losses=0
draws=0

def playagain():
    print("Enter the number of games you wanna play: ")
    choice=int(input(""))
    your_score=0
    computer_score=0
    dictionary= {"snake" : 1, "water": -1,"gun": 0}
    reversedict ={1:"snake🐍",-1:"water💧",0:"gun🔫"}
    global matchplayed, wins,losses,draws

    for i in range(choice):
                yourstr=input(f"Game {i+1}: Enter your choice (snake, water, or gun): ").lower()

                if(yourstr not in dictionary):
                      print("Invalid input! Please enter a valid choice: snake, water, or gun")
                      continue
                computer=random.choice([1,0,-1])
            
                you=dictionary[yourstr]

                print(f"you chose {reversedict[you]} \n Computer chose {reversedict[computer]}")


                if(computer==dictionary[yourstr]):
                    print("Its a draw!🤝")
                    draws+=1
                    matchplayed+=1
                   
                elif((computer-you)==-2 or (computer-you)==1):
                        print(" YOU WON!🏆 ")
                        your_score+=1
                        wins+=1
                        matchplayed+=1
                       
                            
                elif((computer-you)==-1 or (computer-you)==2):
                        print(" YOU LOST!😔 ")
                        computer_score+=1
                        losses+=1
                        matchplayed+=1
                         
                else:
                      print("Error")                           
    if(your_score==computer_score):
            print("HaHA!\tyou think like a computer")
    elif(your_score>computer_score):
            print("CONGRATS!\tYou are smarter than the computer")
    else:
            print("OOPS!\tBetter luck next time")
   
    print("Do you want to see the scoreboard?{y/n}")
    score=input("")
    if(score=='y'):
           print(f"{'='*20}\n📊 Scoreboard \n{'='*20}\n Matches played: {matchplayed}\n Wins: {wins}\n Losses: {losses}\n Draws: {draws}\n Win percent: {wins/matchplayed*100 if matchplayed > 0 else 0:.2f}%\n{'='*20}")
      

print(f"{'='*23}\n🐍 Snake water gun game🔫 \n{'='*23}")
print("Type 'start' to start the game")
start=input("")
if(start=="start"):
 while True:
     playagain()

     play = input("Play again? (y/n): ").lower()

     if play != "y":
        break  
else:
      print("error")     