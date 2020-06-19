alphabet = "abcdefghijklmnopqrstuvwxyz"
Rotor1 = "uvwxyzabcdefghijklmnopqrst"
Rotor2 = "nopqrstuvwxyzabcdefghijklm"
Rotor3 = "ijklmnopqrstuvwxyzabcdefgh"


print(alphabet.index("0"))
print(Rotor1.index("0"))

def encrypt(letter) :
  ind = alphabet.index(letter)
  newLetter = Rotor1[ind]
  print(newLetter)

  for letter in "woord":
    encrypt letter