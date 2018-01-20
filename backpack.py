# backpack game
# getting information about players
# storing the information about players

player = []

for i in range(2):
    player.append({             # run loop for correct number of player
        'name':'',              # add dictionary name, score, backpack to 'player'
        'score':i+1,            # score start from i+1
        'backpack':[]           # list of iteam of each player's backpack
     })
    a = input("enter the integer'")
    
    player[i]['name']= input("enter the name" +str(i+1)+":")
    print("enter 4 iteam of each backpack.  ")

    
    for j in range(4):
        backback_iteam = input(" enter iteam name" +str(j+1) + ":  " )
        player[i]["backpack"].append(backback_iteam)
    print("\n")
     
for p in range(2):
    print(player[p])
    print(player[p]["backpack"])
    print("\n")
    

game_on = True
while 1:
    for i in range(2):
        player_choice = input(player[i]['name'] + ', guess iteam from other backpack: ')
        other_player = player[(i+1)%2]
        if player_choice in other_player["backpack"]:
            print("you guessed an ieam from backpack! ")
            player[i]['score'] +=1
            print(player[i]['score'],+1)
        else:
            print("you didn't guessed an iteam from backpack")
        print("\n")
        
    play_again = str(input(" Do you want to play agian? type yes or no"))
    if(play_again == "no"):
        break
    print("\n")

print("\n")
for t in range(2):
    print(player[t]["name"] +"score: " +str(player[t]["score"]))
    
