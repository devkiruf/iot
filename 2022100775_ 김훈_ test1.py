for i in range(1,6):
    for j in range(1,6):
        if j > 6 - (i+1):
            print(j - (6 - (i+1)), end="")
        else:
            print(" ", end="")
    print()
