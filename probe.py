t = dict()
with open('wp.txt', 'r', encoding='iso-8859-1') as f:
    a = f.read(100)
    for i in a:
        t[i] = 1
        pass