import Cypher as cph
text = input('type text to cypher: ')
newTxt = ""
totalCycles = int(input("total cycles: "))

for i in range(totalCycles):
    for character in text:
        newTxt = newTxt + cph.cycle(character)
    text = newTxt
    newTxt = ""

print(f"cyphered Text: {text}")