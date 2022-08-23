def cycle(caracter):
    upperCase = caracter.isupper()
    caracter = caracter.lower()
    receivedChar = ord(caracter)+1
    if (receivedChar - ord('z') > 0):
        if (receivedChar - 1 == ord('z')):
            return 'A' if upperCase else 'a'
        else:
            if(receivedChar > ord('~')):
                return '{'
            return chr(receivedChar)
    if (receivedChar-1 < ord('0')):
        if (receivedChar == ord('0')):
            return ' '
        else:
            return chr(receivedChar)
    try:
        charToInt = int(caracter)
        if (charToInt + 1 > 9):
            return '0'
        return str(charToInt+1)
    except ValueError:
        if (receivedChar == ord('A')):
            return ':'
        elif (receivedChar == ord('a')):
            return '['
        else:
            return chr(receivedChar).upper() if upperCase else chr(receivedChar)