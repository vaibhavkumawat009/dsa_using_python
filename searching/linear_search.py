def linearsearch(clist, target):
    for i in range(len(clist)):
        if (clist[i] == target):
            return i
    return -1


print(linearsearch([1, 2, 3, 5, 10], 100))
