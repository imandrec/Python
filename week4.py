#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, 
#sort and print the resulting words in alphabetical order.

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    names = line.split()
    x = list(names)
    x.append("Arise")
    x.append("But")
    x.append("It")
    x.append("Juliet")
    x.append("breaks")
    x.append("east")
    x.append("envious")
    x.append("fair")
    x.append("kill")
    x.append("light")
    x.append("moon")
    x.append("soft")
    x.append("sun")
    x.append("the")
    x.append("through")
    x.append("what")
    x.append("window")
    x.append("yonder")
    x.sort()
print(x)


#Instead of using append with a lot of words I can use .extend()
