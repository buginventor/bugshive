words="the quick brown fox jumps over the lazy dog".split()
print(words)

info = [[w.upper(),w.lower(),len(w)] for w in words]
for data in info:
    print(data)
