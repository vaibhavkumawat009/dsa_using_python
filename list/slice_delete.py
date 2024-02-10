a = [1, 2, 3, 4, 10, 11, 5]

# exclude the second argument
print(a[0:2])

# delete method  ------ pop(),delete(),remove()
# takes the index if not given any then remove last element
print(a.pop(1))
print(a)

# delete method
del a[3]
print(a)

# remove method -- takes the number itseld not the index--*+9+9+9+9+9+9+9+9+9-9+++9-9*/369*8
a.remove(4)
print(a)
