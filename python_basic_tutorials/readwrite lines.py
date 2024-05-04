with open('txt files/readwrite lines.txt', 'r') as f:
    # print(line, type(line))
    while 1:
        line = f.readline()
        if not line:
            break

        print(line)
    # print(line[1])

with open('txt files/readwrite lines 1.txt', 'w') as w:
    lines = ['line 1\n', 'line 2\n', 'line 3\n']
    w.writelines(lines)
