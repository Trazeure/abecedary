#Library to get charachters from the abecedary and symbols fast

#lower letters
def get_lower():
    return ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#upper letters
def get_upper():
    return['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#numbers

def get_numbers():
    return[str(i) for i in range(10)]

#symbols
def get_symbols():
    return['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~']
