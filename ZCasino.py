import random
playerMoney = 100
def roulette(playerMoney):
   while playerMoney > 0:
        print("tu possède : ", playerMoney)
        nb = input("Choisi un nombre entre 0 et 49: ")
        money = input("Tu parries Combien ?: ")
        
        try:
                money = int(money)
                if money <= playerMoney:
                    playerMoney = playerMoney - money
                    nb = int(nb)
                    if nb >= 0 and nb <= 49:
                        print("lancement de la roulette, lenombre choisi est :", nb)
                        randomNumber = random.randrange(50)
                        if nb % 2 == 0 and randomNumber % 2 == 0 and nb != randomNumber:
                            sameColor = True
                            playerMoney = playerMoney + money / 2
                            print("tu récupères : ", money)
                            
                        elif nb % 2 != 0 and randomNumber % 2 != 0 and nb != randomNumber:
                            sameColor = True
                            print(sameColor)
                            playerMoney = playerMoney + money / 2
                            print("tu récupères : ", money)
                            
                        elif nb == randomNumber:
                            print("Tu as gagné")
                            playerMoney = playerMoney + money + money * 3
                            print("tu récupères : ", money)
                                   
                        else:
                            sameColor = False
                            print(sameColor)
                            playerMoney
                            print("tu as tout perdu")
                              
                else:
                    print("Tu n'as pas assez d'argent, tu as :", playerMoney, "€")           

        except: 
                print("error")

roulette(playerMoney)
