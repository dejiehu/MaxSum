def readfileTolist(filename):
    file = open(filename,"r",encoding='utf-16')
    list_row = file.readlines()
    list_data = []
    for i in range(len(list_row)):
        list_line = list_row[i].strip().split('\t')
        list_data.append(list_line)
    file.close()
    return list_data

def writefile(list_data):
    with open('data_AfterPro.txt', 'w',encoding='utf-16') as f:
        for i in range(len(list_data)):
            for j in range(len(list_data[i])):
                if j != len(list_data[0]) - 1:
                    f.write(list_data[i][j]+"\t")
                else:
                    f.write(list_data[i][j])
            if i != len(list_data)-1:
                f.write("\n")
    f.close()

if __name__ == '__main__':
    old_data = readfileTolist("Old_data.txt")
    new_data = readfileTolist("New_data.txt")
    print(old_data)
    print(new_data)
    for i in range(len(new_data)-1,-1,-1):
        for j in range(len(old_data)-1,-1,-1):
            if old_data[j][0] == new_data[i][0]:
                del new_data[i]
                del old_data[j]
                break
            if int(old_data[j][0]) < int(new_data[i][0]):
                break
            del old_data[j]
    print(old_data)
    print(new_data)
    writefile(new_data)

