def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(numberOfWords(file_contents))
    print(countLetters(file_contents))

def numberOfWords(txt):
  words = txt.split()
  return len(words)

def countLetters(textFromBook):
  letterCounts = {}
  toLower = textFromBook.lower()
  for letter in toLower:
    if letter not in letterCounts:
      letterCounts[letter] = 1
    else:
      letterCounts[letter] += 1
  return letterCounts

main()