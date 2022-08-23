import Cypher as cph
text = input('type text to cypher: ')
newTxt = ""

for character in text:
    newTxt = newTxt + cph.cycle(character)

print(f"cyphered Text: {newTxt}")