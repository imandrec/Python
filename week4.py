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

#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
#Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

#option 1 

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = 0
for line in handle:
   if line.startswith("From: "):
        words = line.split()        
        print(words[1])  
        count = count + 1
print("There were", count,"lines in the file with From as the first word")

#option 2

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != "From":
        continue
    print(words[2])



