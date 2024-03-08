def main():
  with open("books/frankenstein.txt") as f:
    print("--- Begin report of books/frankenstein.txt ---")
    file_contents = f.read()
    print(f"{numberOfWords(file_contents)} words found in the document")
    list_of_letters = toList(countLetters(file_contents))
    list_of_letters.sort(reverse=True, key=sort_on)
    printListOfLetters(list_of_letters)
    print("--- End report ---")

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

def toList(dict):
  l = []
  for letter in dict:    
    td = {"letter":letter, "num": dict[letter]}
    l.append(td)
  return l

def printListOfLetters(listOfLetters):
  for letter in listOfLetters:
    if letter['letter'].isalpha():
      print(f"The '{letter['letter']}' character was found {letter['num']} times")

def sort_on(dict):
  return dict["num"]

main()