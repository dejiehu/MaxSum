
def MaxSum(m,n,a_list):
    if (n < m |m < 1):
        return 0
    b = []
    c = []
    for i in range(0,n+1):
        b.append(0)
        c.append(0)
    for i in range(1,m+1):
        b[i] = b[i-1] + a_list[i]
        c[i-1] = b[i]
        max = b[i]
        for j in range(i + 1,i + n - m + 1):
            if b[j-1] > c[j-1]:
                b[j] = b[j-1] + a_list[j]
            else:
                b[j] = c[j - 1] + a_list[j]
            c[j - 1] = max
            if max <b[j]:
                max = b[j]
        c[i + n - m] = max
    sum = 0
    for i in range(m,n+1):
        if sum < b[i]:
            sum = b[i]
    print(sum,b,c,a_list)

# def search(b, n, m, max, a):
#     index = 0
#     search_num = []
#     for i in range(1, n + 1):
#         if max == b[m][n + 1 - i]:
#             index = n + 1 - i
#             break
#     row = m
#     i = 0
#     index_num = 2
#     search_num.append([index])
#     while 1:
#         if b[row][index] - a[index] == b[row][index - 1]:
#             search_num[i].append(index - 1)
#             index -= 1
#         else:
#             index_num = index - 1
#             while index_num > 0:
#                 if row - 1 > 0 and b[row - 1][index_num] == b[row][index] - a[index]:
#                     search_num.append([index_num])
#                     i += 1
#                     index = index_num
#                     row = row - 1
#                     break
#                 else:
#                     index_num -= 1
#         if index == 1 or index_num == 0:
#             break
#     print("%d 子段每一段的下标" % m, search_num)

if __name__ == '__main__':
    # a_list = [0,2,-1,-2,3]
    a_list = [0, -2, 11, -4, 13, -5, 6, -2]
    MaxSum(3, len(a_list)-1,a_list)
    # max, b = MaxSum(2, len(a_list) - 1, a_list)
    # search(b, len(a_list) - 1, 2, max, a_list)
