while True:
    try:
        n = int(input())
    except:
        break
    res = 0 
    prev = 0

    while True:
        res += 1
        prev = ((prev % n) * 10 + 1) % n
        if prev == 0:
            print(res)
            break