def MaxSum(m,n,a_list):
    if (n < m or m < 1):
        return 0
    b = []
    for i in range(m + 1):
        b.append([])
        for j in range(n + 1):
            b[i].append(0)
    # print(b)
    for i in range(1, m + 1):
        for j in range(i, n - m + i + 1):
            if j > i:
                b[i][j] = b[i][j - 1] + a_list[j]
                for k in range(i - 1, j):
                    if b[i][j] < b[i-1][k] + a_list[j]:
                        b[i][j] = b[i - 1][k] + a_list[j]
            else:
                b[i][j] = b[i - 1][j - 1] + a_list[j]
    sum = 0
    for i in range(m, n + 1):
        if sum < b[m][i]:
            sum = b[m][i]
    print(sum,b)
    return sum, b


def search(b,n,m,max,a):
    index = 0
    search_num = []
    for i in range(1, n + 1):
        if max == b[m][n + 1 - i]:
            index = n + 1 - i
            break
    row = m
    i = 0
    index_num = 2
    search_num.append([index])
    while 1:
        if b[row][index] - a[index] == b[row][index - 1]:
            search_num[i].append(index - 1)
            index -= 1
        else:
            index_num = index - 1
            while index_num > 0:
                if row - 1 > 0 and b[row - 1][index_num] == b[row][index] - a[index]:
                    search_num.append([index_num])
                    i += 1
                    index = index_num
                    row = row - 1
                    break
                else:
                    index_num-=1
        if index == 1 or index_num == 0:
            break
    print("%d 子段每一段的下标"%m,search_num)

if __name__ == '__main__':
    a_list = [0, -2, 11, -4, 13, -5, 6, -2]
    max,b = MaxSum(1, len(a_list) - 1, a_list)
    search(b,  len(a_list) - 1, 1, max, a_list)