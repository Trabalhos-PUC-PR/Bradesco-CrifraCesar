def cycle(caracter):
    upperCase = caracter.isupper()
    caracter = caracter.lower()
    receivedChar = ord(caracter)+1
    if(receivedChar - ord('z') > 0):
        return 'A' if upperCase else 'a'
    if(receivedChar-1 < ord('0')):
        if(receivedChar == ord('0')):
            return ' '
        else:
            return chr(receivedChar)
    try:
        charToInt = int(caracter)
        if(charToInt + 1 > 9):
            return '0'
        return str(charToInt+1)
    except ValueError:
        return chr(receivedChar).upper() if upperCase else chr(receivedChar)
