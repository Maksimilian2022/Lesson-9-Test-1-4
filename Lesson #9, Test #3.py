number_lines = {}
with open('3.txt', 'r', encoding='utf-8') as txt3:
    txt3_list = []
    for line in txt3:
        txt3_list.append(line.strip())
    txt3_list.append('3.txt')


with open('2.txt', 'r', encoding='utf-8') as txt2:
    txt2_list = []
    for line in txt2:
        txt2_list.append(line.strip())
    txt2_list.append('2.txt')


with open('1.txt', 'r', encoding='utf-8') as txt1:
    txt1_list = []
    for line in txt1:
        txt1_list.append(line.strip())
    txt1_list.append('1.txt')



for lines in sorted([txt2_list, txt1_list, txt3_list], reverse = True):
    print(lines[-1])
    print(len(lines) - 1)
    for line in lines[:-1]:
        print(line)
    print()


