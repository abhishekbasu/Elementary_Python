import csv
from random import * #The element of spice

class Humans:
	def __init__ (self,name,health):
		self.name = name
		self.health = health
		self.attacks=[]
	def DisplayName (self):
		print("My name is " + self.name)
	def LearnAttack (self, attack):
		self.attacks.append(attack)

class Swordsman(Humans):
	def __init__ (self, name, health):
		self.name = name
		self.health = health
		self.attacks=[]
		self.LearnAttack("sword-fight")

def DATAINPUT(filename):
    inputFile = open(filename,"r")
    dictmain = {}
    i=0
    for line in inputFile:
        d=str.strip(line)
        k=d.split(",")
        reqlength= int(k[1])
        dictmain[str(k[0])]=(int(k[1]))
    inputFile.close()
    return dictmain

def ATTACK(swman1, swman2):
	swman1.health+=randrange(10,20)
	swman2.health-=randrange(20,40)
	if swman1.health>100:
		swman1.health=100
	if swman2.health<0:
		swman2.health=0

def SELECTOR(named, playerList):
	for i in range(1, len(playerList)):
		if(named== playerList[i].name):
			return i

def SIMULATION(n, index):
	for i in range(0,n):
			
			###
			if(i%5==0): #Bonus every fifth round
				z= (randrange(1, len(A))) #The guy who gets bonus health
			if(A[z].health+40<100):
				A[z].health+=40
			else:
				A[z].health=100
			###

			###
			x= (randrange(1, len(A))) #The guy who attacks
			y= (randrange(1, len(A))) #The guy who gets attacked
			###

			if (x==index):
				for i in range(1, len(A)):
					print(A[i].name+str(A[i].health))
				hit=str(raw_input("\nThis is your moment ! , select the player you wish to hit = "))
				y=SELECTOR(hit, A)
			if (x==y):
				i-=1
			if (x is not y):
				if(A[y].health==0):
					print("   Hey! don't attack him, he's already dead")
				ATTACK(A[x],A[y])
				print(str(i+1)+" "+A[x].name + "  attacks  " + A[y].name)

#Initialisation
allPlayers= DATAINPUT("players.csv")
A=[0]

for keys in allPlayers:
	A.append(Swordsman(keys, allPlayers[keys]))

#Select Player
player=str(raw_input("Enter your character name = "))
index=SELECTOR(player, A)

#Game On!
SIMULATION(50, index) #Number of rounds of battle!

#Game Ends!
print("_"*50)
print("\n" + "  "*10+ "FINAL SCORES \n")
print("_"*50)
for i in range(1, len(A)):
	print(A[i].name+" "*45+str(A[i].health))