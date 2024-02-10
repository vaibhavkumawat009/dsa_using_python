# we can update the list
a = [1, 23, 4, 5, 7]
# a[1] = 40
"""inserting in the list """
a.insert(0, 11)
print(a)

a.append(10)
print(a)

# adding another list in our list
b = [101, 102, 103]
a.extend(b)
print(a)
