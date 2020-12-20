def MaxSum(m,n,a_list):
    if (n < m or m < 1):
        return 0
    b = []
    for i in range(m + 1):
        b.append([])
        for j in range(n + 1):
            b[i].append(0)
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

def search_index_addr(m,a_list,b,max):
    index_list = []
    for i in range(len(b[m])-1,-1,-1):
        if max == b[m][i]:
            index = i
            break
    i = 0
    index_num = 2
    index_list.append([index])
    while 1:
        if b[m][index] - a_list[index] == b[m][index - 1]:
            index_list[i].append(index - 1)
            index -= 1
        else:
            index_num = index - 1
            while index_num > 0:
                if m - 1 > 0 and b[m - 1][index_num] == b[m][index] - a_list[index]:
                    index_list.append([index_num])
                    i += 1
                    index = index_num
                    m = m - 1
                    break
                else:
                    index_num -= 1
        if index == 1 or index_num == 0:
            break
    print(len(index_list),"子段各的下标为" ,index_list)

if __name__ == '__main__':
    a_list = [0, -2, 11, -4, 13, -5, 6, -2]
    max,b = MaxSum(6, len(a_list) - 1, a_list)
    search_index_addr(6, a_list, b,max)