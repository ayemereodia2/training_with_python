try:
    fp = open(r"test.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("Please check the path")