# Experiment programmed for practice by: Fernando Dilland Mireles Cisneros

# Python3 program for explaining
# use of list, tuple, set and
# dictonary

# Lists <<<<<<<<<<<
l = []

# Adding element into list using append
print("<<<<< List >>>>>")
l.append(5)
l.append(10)
print("Adding 5 and 10 in list using append:", l)

# Adding element in the middle into set using insert
l.insert(1, 20)
l.insert(2, 23)
print("Adding 20 and 23 (in the middle) in list using insert:", l)

# Adding list into list using extend
l.extend([31, 46])
print("Adding list with 31 and 46 in list using extend:", l)

# Adding tuple into list using extend
l.extend((65, 66))
print("Adding tuple with 65 and 66 in list using extend:", l)

# Adding string into list using extend
l.extend("FER")
print("Adding string elementos with FER in list using extend:", l)

# Popping last element from list
l.pop()
print("> Popped the last element from list:", l)

# Popping specific element from list
l.pop(2)
print("> Popped number 3 (the second one starting from 0) element from list:", l)

print()

# Set <<<<<<<<<<<
print("<<<<< Set >>>>>")
s = set()

# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set:", s)

# Adding set into set
s2={31,72}
s.update(s2)
print("Adding a set (unordered object) with 31 and 72 in set:", s)

# Adding set into set
s3=[452,926]
s.update(s3)
print("Adding contents of another Iterable (unordered) with 452 and 926 in set:", s)

# Removing element from set with remove (if element  does not exist, it raises a KeyError)
s.remove(5)
print("Removing 5 from set with remove:", s)

# Removing element from set with discard (if element  does not exist, it does not raise a KeyError)
s.discard(72)
print("Removing 72 from set with discard:", s)

# Removing element from set with pop
s.pop()
print("Removing an arbitrary element from set:", s)
print()

# Tuple <<<<<<<<<<<
print("<<<<< Tuple >>>>>")
t = tuple(l)

# Tuples are immutable
print("Tuple immutable:", t)
print()

# Dictonary <<<<<<<<<<<
print("<<<<< Dictonary >>>>>")
d = {}

# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictonary:", d)

# Removing key-value pair
del d[10]
print("Dictonary:", d)