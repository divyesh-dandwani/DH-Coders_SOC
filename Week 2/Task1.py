def getUniqueUsingSet(arr):
    s = set()

    for i in arr:
        s.add(i)

    return list(s)


def getUniqueUsingDict(arr):
    d = {}

    for i in arr:
        d[i] = 1

    return list(d.keys())


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input()))

unique_set = getUniqueUsingSet(arr)
unique_dict = getUniqueUsingDict(arr)

print("\nUnique elements using Set:")
for i in unique_set:
    print(i)

print("\nUnique elements using Dictionary:")
for i in unique_dict:
    print(i)