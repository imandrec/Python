# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}

# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             

# Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", 
                    "progressive rock", "soft rock", "R&B", "disco"])

# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])

# Add element to set

A.add("NSYNC")

# Try to add duplicate element to the set

A.add("NSYNC")

# Remove the element from set

A.remove("NSYNC")

# Verify if the element is in the set

"AC/DC" in A

# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets

album_set1, album_set2

# Find the intersections

intersection = album_set1 & album_set2
intersection

# Find the difference in set1 but not set2

album_set1.difference(album_set2) 

# Use intersection method to find the intersection of album_list1 and album_list2

album_set1.intersection(album_set2)  

# Find the union of two sets

album_set1.union(album_set2)

# Check if superset

set(album_set1).issuperset(album_set2)   

# Check if subset

set(album_set2).issubset(album_set1)    

# Check if subset

set({"Back in Black", "AC/DC"}).issubset(album_set1) 

# Check if superset

album_set1.issuperset({"Back in Black", "AC/DC"})  

# Write your code below and press Shift+Enter to execute
set(['rap','house','electronic music', 'rap'])

# Write your code below and press Shift+Enter to execute
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print(sum(A))
print(sum(B))

# Write your code below and press Shift+Enter to execute

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
album_set3

# Write your code below and press Shift+Enter to execute
album_set1.issubset(album_set2)
#Answer is False



