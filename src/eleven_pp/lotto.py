
def lotto():
    import random
    a = []
    n = 0

    while n < 6:
        b = random.randint(1, 45)
        a.append(b)
        n = n + 1
    print(a)

