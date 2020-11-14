print('Countries and capitals quiz!')
print('Do your best :)')

totalQuestions = 5
score = 0

ans = input('Do you want to start?')

if ans.lower() == 'yes':
    print('Lets start!')
    score += 1
else:
    print('Have a good day').exit()

ans = input('BELGIUM')

if ans.lower() == 'BRUSSELS':
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('BOLIVIA')

if ans == "SUCRE":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('CHILE')

if ans.lower() == "SANTIAGO":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('EGYPT')

if ans.lower() == "CAIRO":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('IRAQ')

if ans.lower() == "BAGHDAD":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('LIBERIA')

if ans.lower() == "MONROVIA":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('NEW ZEALAND')

if ans.lower() == "WELLINGTON":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('PHILIPPINES')

if ans.lower() == "MANILA":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('SOUTH KOREA')

if ans.lower() == "SEOUL":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('SPAIN')

if ans.lower() == "	MADRID":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


print("Thank you for playing, you got " + str(score) + ' questions correct!' )
percent = (score/totalQuestions) * 100
print("Mark: " + str(int(percent)) + '%')

if percent >= 50:
    print('Nice! You passed!')
else:
    print('You need to practice more!')
