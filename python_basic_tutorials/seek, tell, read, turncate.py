
with open('txt files/readwrite lines.txt', 'r') as f:
    f.seek(5)  # skip to index 5
    print(f.tell())  # tells the index
    print(f.read(6))

with open('txt files/seek, tell, read, turncate.txt', 'w') as w:
    w.write('hello world')
    w.truncate(7)  # reduces the length of file to 7 characters

with open('txt files/seek, tell, read, turncate.txt', 'r') as f:
    print(f.read())
