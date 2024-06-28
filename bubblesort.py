array = [1, 3, 2, 4, 6, 7, 0, 99, 71]

for i in range(len(array)):
    for j in range(0, len(array) - 1 - i):
        if (array[j] > array[j + 1]):
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
    print("/n/n")
print(array)
