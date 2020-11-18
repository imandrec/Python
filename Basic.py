t=lambda var: var**4
print(t(7))

planet = "Earth"
diameter = 12742
print('the diameter of {} is {} kilometers'.format(planet,diameter))

#Given this nested list, use indexing to grab the word "hello"
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

#Given this nested dictionary grab the word "hello"
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])

#Create a function that grabs the email website domain from a string in the form: user@domain.com 
var = 'user@domain.com'
print(var.split('@')[1])

#Create a basic function that returns True if the word 'dog' is contained in the input string
findDog = ('Is there a dog here?')
print('dog' in (findDog))

#Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. 
seq = ['blackberries','apple','apples','blueberries','kiwi']
print(list(filter(lambda word: word[0]=='b',seq)))

#You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases
def caught_speeding(speed, is_birthday):

    if is_birthday:
        speeding = speed - 5;
    else:
        speeding = speed;
    if speeding > 80:
        return 'Big Ticket';
    elif speeding > 60:
        return 'Small Ticket';
    else:
        return 'No Ticket';
print(caught_speeding(81,True));

#Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases
def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1;
    return count
x=countDog('This dog runs faster than the other dog dude!');
print (x);
