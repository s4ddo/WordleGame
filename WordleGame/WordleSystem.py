from ast import Return
from re import I

class The_Hidden_Word:
    Word = ""
    def getWord(self):
        return self.Word
    def setWord(self, theWord):
         self.Word = theWord
    def getLetters(self):
        for x in self.Word: 
            return x


Guess = " " 
Attempts = 0

def AddWord(Word):
    global Word1
    Word1 = The_Hidden_Word()
    Word1.setWord(Word)
    


def CheckGuess(Goon, AttemptsLeft, index):
  Goos = Goon.upper()
  if AttemptsLeft < 1:
    pass
  else:
      Hidden_Word = Word1.getWord()
      if Goos[index] in Hidden_Word:
        occurances = Hidden_Word.count(Goos[index])
        count = 0
        for y in range(5):
               if Goos[y] == Hidden_Word[y] and Goos[y] == Goos[index]:
                   count = count + 1
               if Goos[index] == Hidden_Word[y]:
                 if index == y:
                    return "True"
        for x in range(index+1):
               if Goos[x] == Goos[index]:
                  count = count + 1
        if count <= occurances:
            return "Exists"
        else:
            return "False"
      else:
       return "False"

def getLetter(Word, index):
    return Word[index].upper()
    
   



