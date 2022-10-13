print("Hallo jij, ik ben computer BEEP BOOP")
print("wie ben jij")
username = input()
print("Hallo " + username + " BEEP")
print("ik welke jaar ben je geboren")
jaar = int(input())
print("het jaar is 2022")
print("dus jij bent")
x = 2022
print(x - jaar)
score = 0
# question 1
vraag1 = input("welke opleiding doe ik \na. media voorgeving \nb. software development \nc. audio visueel \nantwoord ALLEEN DE LETTER ")
if vraag1 == "b":
    score = score + 1 
    print("goed 😉")
    print("score", + score)
    print("\n")
else:
    print("FOUT L bozo")
    print("score", + score)
    print("\n")

# question 2
vraag1 = input("op welke school zat ik hiervoor? \na. tabor college dampte \nb. newton SG \nc. copernicus SG \nantwoord ")
if vraag1 == "c":
    score = score + 1 
    print("goed 😉")
    print("score", + score)
    print("\n")
else:
    print("FOUT L bozo")
    print("score", + score)
    print("\n")

    # question 2
vraag1 = input("hoelang duurd de reis naar deze school voor mij \na. 30 min \nb. 1 uur \nc. 1,5 uur \nantwoord ")
if vraag1 == "c":
    score = score + 1 
    print("goed 😉")
    print("score", + score)
    print("\n")
else:
    print("FOUT L bozo")
    print("score", + score)
    print("\n")
