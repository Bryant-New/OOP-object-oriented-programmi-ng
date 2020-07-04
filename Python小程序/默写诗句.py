list_test = ['一弦一柱思华年。\n','只是当时已惘然。\n']
with open('poem2.txt', 'r', encoding='gbk') as f:
    lines =f.readlines()
print(lines)
with open('poem2.txt', 'w') as new:
    for line in lines:
        if line in list_test:
            new.write('____________。\n')  # write函数暴力清除掉原来的内容，写上新的内容
        else:
            new.write(line)
