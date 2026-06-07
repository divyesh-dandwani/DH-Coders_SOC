def print_transpose(a, row, col):
    for i in range(col):
        for j in range(row):
            print(a[j][i], end=" ")
        print()


def diagonal_sum(a, row, col):
    if row != col:
        print("ERR : For Diagonal Row and Column must be same")
        return

    pr_sum = 0
    sec_sum = 0

    for i in range(row):
        for j in range(col):
            if i == j:
                pr_sum += a[i][j]

            if i + j == row - 1:
                sec_sum += a[i][j]

    print("Primary Diagonal Sum =", pr_sum)
    print("Secondary Diagonal Sum =", sec_sum)


print("Enter No. of Rows :")
row = int(input())

a = []

for i in range(row):
    lst = list(map(int, input().split()))
    a.append(lst)

col = len(a[0])

print("\nEnter Your Choice :")
print("1. Transpose")
print("2. Diagonal Sum")

ch = int(input())

match ch:
    case 1:
        print_transpose(a, row, col)

    case 2:
        diagonal_sum(a, row, col)

    case _:
        print("Invalid Choice")