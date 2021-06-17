# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
tempList = list()
counts = dict()
for line in handle:
   if line.startswith("From "):
        words = line.split()
        hour = words[5]
        time = hour.split(":") 
        temp = time[0]
        tempList.append(temp)
for list in tempList:
    if list not in counts:
        counts[list] = 1
    else:
    	counts[list] = counts[list] + 1
for k,v in sorted(counts.items()) :
    print(k,v)
