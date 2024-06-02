for i in range(1, 8):
    for j in range(1, 8-i):
        print(" ", end="")
    for j in range(1, i+1):
        print("T", end="")
    print()

