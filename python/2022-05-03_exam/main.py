import os

def read_first_line(_filename):
    with open(_filename, "r") as rf:
        return rf.read()

def main():
    # read values
    A = read_first_line(f"{os.path.dirname(os.path.realpath(__file__))}\\A.txt")
    B = read_first_line(f"{os.path.dirname(os.path.realpath(__file__))}\\B.txt")

    # calculate and store to file
    res = int(A) + int(B)
    if res > 1_000_000:
        with open(f"{os.path.dirname(os.path.realpath(__file__))}\\miljon2r.txt", "w") as wf:
            wf.write(str(res))
    else:
        with open(f"{os.path.dirname(os.path.realpath(__file__))}\\tulemus.txt", "w") as wf:
            wf.write(str(res))

    # print in loop if res less than 20
    if(res < 20):
        for i in range(res):
            print("Tere!")

if __name__ == "__main__":
    main()