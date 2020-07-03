
file2 = open('C:\\Users\\87408\\Desktop\\test\\abc.txt', 'w', encoding='utf-8')
file2.write('张无忌\n')
file2.write('宋青书\n')
file3 = open('C:\\Users\\87408\\Desktop\\test\\abc.txt', 'a', encoding='utf-8')
file3.write('金毛狮王\n')
file3.write('张三丰\n')
file3.close()
f = open('C:\\Users\\87408\\Desktop\\test\\1.txt', 'a', encoding='utf-8')
f.write('难念的经')
f.close()
f1 = open('C:\\Users\\87408\\Desktop\\test\\1.txt', 'r', encoding='utf-8') # 打开文件
content = f1.read()
print(content)
f1.close()
with open('abc.txt', 'a') as file1:
    file1.write('人')