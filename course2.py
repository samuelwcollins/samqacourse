import sys

friend = sys.stdin.readline()
friend = friend[ :-1]

greeting = "Hello dogfriend"

if friend == "Pants" or friend == "Joel" or friend == "Sarah":
    greeting = "It's the homegirl Pants! Where's the ball?"

elif friend == "Lola" or friend == "Frances":
    greeting = "Hello Lola, sorry I can't feed you, please don't bark."

print greeting
