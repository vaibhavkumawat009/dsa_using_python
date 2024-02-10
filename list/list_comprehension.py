a = [1, 2, 3, 4, 5, 6]
b = [i * 2 for i in a]
print(b)

# we can use list comprehension for list,range,string,tuple

# condition list comprehension
c = [a[i] for i in range(len(a)) if a[i] > 3]
print(c)
