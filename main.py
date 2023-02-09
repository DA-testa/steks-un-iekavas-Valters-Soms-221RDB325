# Valters Soms 17.gr. 221rdb325
# python3
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

# funkcija atgriež true ja iekavas sakrīt, false ja nesakrīt
def are_matching(left, right):
  return (left + right) in ["()", "[]", "{}"]

# funkcija kas paņem tekstu
def find_mismatch(text):
  opening_brackets_stack = []
  for i, next in enumerate(text):
    if next in "([{":
      # ja simbols ir (, [, { tad pievinojam to mūsu stekam kā Bracket klases instanci
      opening_brackets_stack.append(Bracket(next, i + 1))

    # ja simbols ir ), ], } tad veic 2 pārbaudes [lai izvadītu pirmo neaizvērto iekavu]
    if next in ")]}":
      # 1) Ja steks ir tukšs, vai (pēdējais pievienotais) elements nav vienāds ar (pašreizējo simbolu 'next'):
      if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
        print(i + 1)
        exit(0)
      # 2) Ja (pēdējais pievienotais) elemants ir vienāds ar (pašreizējo simbolu 'next'), tas tiek izņemts
      opening_brackets_stack.pop()

def main():
  text = input()
  mismatch = find_mismatch(text)
  # Printing answer, write your code here
  if not mismatch:
    print("Success")
    exit(0)
  else:
    print(mismatch)

if __name__ == "__main__":
  main()
