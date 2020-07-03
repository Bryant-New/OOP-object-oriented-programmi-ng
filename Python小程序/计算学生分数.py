file1 = open('C:\\Users\\87408\\Desktop\\test\\scores.txt', 'r', encoding='utf-8')
file_lines = file1.readlines()  # readlines()会从txt文件取得一个列表，列表中的每个字符串就是scores.txt中的每一行。而且每个字符串后面还有换行的\n符号。
file1.close()
print(file_lines)

final_scores = []  # 新建一个空列表,把成绩写入一个空的列表
for i in file_lines:  # 用for循环来遍历这个列表，然后处理列表中的数据
    data = i.split()  # 使用split()来把字符串分开，它会按空格把字符串里面的内容分开。
    sum = 0
    for score in data[1:]:  # 遍历列表中第1个数据和之后的数据
        sum = sum + int(score)  # 然后依次加起来，但分数写在.txt文件中是字符串，所以要转换
    result = data[0]+str(sum)+'\n'  # 后面加上换行符，写入的时候更清晰
    print(result)
    final_scores.append(result)  # 每统计一个学生的总分，就把姓名和总分写入空列表

winner = open('C:\\Users\\87408\\Desktop\\test\\winner.txt', 'w', encoding='utf-8')   # 以open函数新建一个winner.txt文件写入总成绩
winner.writelines(final_scores)  # 17行的代码是以writelines()的方式写进去，为什么不能用write()？因为final_scores是一个列表，而write()的参数必须是一个字符串，而writelines()可以是序列，所以我们使用writelines()。
winner.close()