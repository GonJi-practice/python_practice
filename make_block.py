def block(a):

    for i in range(0, a, 1):
        for j in range(a, -1, -1):
            if j > i:
                print(" ", end = " ")
            else:
                print("x", end = " ")
        print("")

