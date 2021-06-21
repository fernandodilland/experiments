# Python3 program for explaining
# use of list, tuple, set and
# dictonary

# Lists <<<<<<<<<<<
l = []

# Adding Element into list
print("<<<<< List >>>>>")
l.append(5)
l.append(10)
print("Adding 5 and 10 on list using append:", l)
l.insert(2, 20)
l.insert(3, 23)
print("Adding 20 and 23 on list using insert:", l)
l.extend([31, 46])
print("Adding list with 31 and 46 on list using extend:", l)
l.extend((65, 66))
print("Adding tuple with 65 and 66 on list using extend:", l)
l.extend("FER")
print("Adding string elementos with FER on list using extend:", l)

# Popping Elements from list
l.pop()
print("> Popped the last element from list:", l)

# Force overlapping
l.insert(2, 85)
l.insert(3, 73)
print(">> Overlapping 85 and 73 in list using insert (Pos 2(3) and 3(4) ):", l)

l.extend([999999, 4])
l.extend([888888888, 5])
print(">> Adding 93 and 37 in list using extend (Pos 4(5) and 5(6) ):", l)

print()

# Set <<<<<<<<<<<
print("<<<<< Set >>>>>")
s = set()

# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set:", s)

# Removing element from set
s.remove(5)
print("Removing 5 from set:", s)
print()

# Tuple <<<<<<<<<<<
print("<<<<< Tuple >>>>>")
t = tuple(l)

# Tuples are immutable
print("Tuple:", t)
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