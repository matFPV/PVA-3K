X = input("Input: ")

if len(X) < 2 or len(X) > 2000:
    print("incorrect length")
else:
    addup = []
    for i in range(len(X)):
        for j in range(i + 2, len(X) + 1):
            addup.append(sum(X[i:j]))
    sumset = tuple(set(addup))
    multiples = [[num]*addup.count(num) for addup in sumset if addup.count(num) > 1]
    res = 0
    for i in multiples:
        res += len(i)* (len(i) - 1) // 2
    print(res)
