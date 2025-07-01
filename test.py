l = ['ali', 'mohamed', 'saad','4','5',6,7,8,9]

groups = [l[i: i+2] for i in range(0, len(l), 2)]

for i in range(0, 9, 3):
    print(i)