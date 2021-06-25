import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

randomCharacter1=chr(random.randint(96,122))
randomCharacter2=chr(random.randint(46,63))

uppercaseLetter=chr(random.randint(65,90)) 

randomNumber=chr(random.randint(48,57)) 


password = uppercaseLetter + uppercaseLetter + uppercaseLetter +randomCharacter1 + randomCharacter1 + randomCharacter1 + randomCharacter2 +randomCharacter2 + randomCharacter2 + randomNumber + randomNumber +randomNumber

password = shuffle(password)	

print(password)