text = input("Enter text: ")
shifted = ''.join(chr(ord(c) + 1) for c in text)
print("Result:", shifted)
