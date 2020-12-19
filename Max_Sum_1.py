
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
                b[j] =c[j - 1] + a_list[j]
            c[j - 1] = max
            if max <b[j]:
                max = b[j]
        c[i + n - m] = max
    sum = 0
    for i in range(m,n+1):
        if sum < b[i]:
            sum = b[i]
    print(sum,b,c,a_list)
if __name__ == '__main__':
    # a_list = [0,10,-1,-2]
    a_list = [0, -2, 11, -4, 13, -5, 6, -2]
    MaxSum(4, len(a_list)-1,a_list)
