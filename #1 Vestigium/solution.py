def isduplicates(array):
    for i in range(0, len(array)):
        for j in range(1, len(array)):
            if j != i:
                if array[i] == array[j]:
                    return True
    return False


def islatinsquare(dimension, matrix):
    global r
    global c
    c = 0
    r = 0

    for a in range(dimension):

        if isduplicates([row[a] for row in matrix]):
            c += 1
    for array in matrix:
        if isduplicates(array):
            r += 1


def output(T, dimension, matrix):
    k = 0
    for i in range(dimension):
        k += matrix[i][i]
    x = casenum
    islatinsquare(dimension, matrix)
    print("Case #"+str(x)+": "+str(k)+" "+str(r)+" "+str(c))


T = int(input().strip())

for i in range(T):
    casenum = i+1
    matrix = []
    dimension = int(input().strip())
    for i in range(dimension):
        a = []
        input1 = input().split(" ")
        for j in range(dimension):
            a.append(int(input1[j]))
        matrix.append(a)
    output(T, dimension, matrix)
