alphabet = "abcdefghijklmnopqrstuvwxyz"
Rotor1 = "uvwxyzabcdefghijklmnopqrst"
Rotor2 = "nopqrstuvwxyzabcdefghijklm"
Rotor3 = "ijklmnopqrstuvwxyzabcdefgh"

beginwoord = input("Hier je woord typen:")
print("Het beginwoord is:" + beginwoord)

print(alphabet.index("0"))
print(Rotor1.index("0"))

def encrypt(letter) :
  ind = alphabet.index(letter)
  newletter = Rotor1[ind]
  print(newletter)

  for letter in "woord"
  encrypt letter