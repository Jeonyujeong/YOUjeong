#number_baseball_game
from random import randint

rn = []

for x in range(3):
    rn.append(randint(0,9))

if rn[0]==rn[1]:
    while rn[0]==rn[1]:
        rn[1] = randint(0,9)
elif rn[0]==rn[2] or rn[1]==rn[2]:
    while rn[0]==rn[2] or rn[1]==rn[2]:
        rn[2] = randint(0,9)

#print (rn)
print ("Start number baseball game!")
print ("---------------------------")

strike =0
#ball = 0

while strike!=3:
    
    strike = 0
    ball = 0

    gn = []
    for n in range(3):
        gn.append(int(input("Guess number:")))
        
    print (gn)

    #strike
    for st in range(3):
        if rn[st]==gn[st]:
            strike += 1
    
    #ball
    for st in range(3):
        for i in range(3):
            if rn[st] == gn[i]:
                if st!=i:
                    ball +=1

    print ("{} strike {} ball".format(strike, ball))
    print ("\n")
    print ("retry")
else :
    print ("Congratulations!")
