t=lambda var: var**4
print(t(7))

planet = "Earth"
diameter = 12742
print('the diameter of {} is {} kilometers'.format(planet,diameter))


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])

var = 'user@domain.com'
print(var.split('@')[1])

findDog = ('Is there a dog here?')
print('dog' in (findDog))

seq = ['blackberries','apple','apples','blueberries','kiwi']
print(list(filter(lambda word: word[0]=='b',seq)))
#e of 3 possible icketIf your speed is 60 ss, the ret is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases
def caught_speeding(speed, is_birthday):

    if is_birthday:
        speeding = speed - 5;
    else:
        speeding = speed; l
    if speeding > 80:
        return 'Big Ticket';
    elif speeding > 60:
        return 'Small Ticket';
    else:
        return 'No Ticket';
print(caught_speeding(81,True));

def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1;
    return count
x=countDog('This dog runs faster than the other dog dude!');
print (x);

#Guess number

import random

def numberGuess():
  randNum = random.randrange(1,11) # this line generates a random number
  guess = int(input("Try to guess the number:")) # ask user for a number
  print (randNum)
  while True:
    if (guess == randNum):
        print ("You got it!")
        break
    if (guess > randNum):
        print ("Wrong! You guessed too high")
        guess = int(input("Try to guess the number:"))  # ask user for a number
    if (guess < randNum):
        print ("Wrong! You guessed too low")
        guess = int(input("Try to guess the number:"))  # ask user for a number

numberGuess()
