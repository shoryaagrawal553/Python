name=  "Tony Stark"
  
# methods:- does no change to the original string/ value
print(name.upper())  # converts to uppercase
print(name.lower())  # converts to lowercase
print(name)  # original string remains unchanged

# .find()  to find index of a substring or character
print(name.find('S'))   # returns the index of first occurrence of 'S' in name
print(name.find("Stark"))  # returns the index of first occurrence of 'Stark' in name
print(name.find('s'))   # returns -1 if the substring is not found

# .replace()  to replace a substring with another substring
print(name.replace("Tony Stark", "Ironman"))  # replaces "Tony Stark" with "Ironman" (replaces whole string)
print(name.replace("Stark", "Rogers"))     # replaces a part of the string
print(name.replace("T", "H"))  # replaces 'T' with 'H' (replaces first occurrence only)
print(name.replace("k", " man"))  # replaces 'k' with "man"
print(name)  #no change in original

#in keyword -> returns True or Flase depending on whether the substring is present in the string
print("S" in name)  # returns True
print("s" in name)  # returns False (case-sensitive)
print("Stark" in name)  # returns True
print("Ironman" in name)  # returns False (not present in name)





















