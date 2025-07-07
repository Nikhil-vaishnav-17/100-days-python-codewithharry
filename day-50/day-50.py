#Methods in file I/O

with open('my_file.txt', 'r') as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            break

with open('marks.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break

        m1 , m2, m3 = line.split(',')
        print(f'Marks 1: {m1}\nMarks 2: {m2}\nMarks 3: {m3}')
        print(line)

with open('Counting.txt', 'w') as f:
    for i in range(100):
        f.write(str(i) + '\n')