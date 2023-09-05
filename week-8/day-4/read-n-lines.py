def readLastNLines(filename: str, n: int) -> None:
    with open(filename, "r") as f:
        lines = f.readlines()
        if n > len(lines):
            print("Not enough lines")
        else:
            # print("".join(line for line in lines[len(lines) - 3 :]))
            for line in lines[len(lines) - 3 :]:
                print(line.strip())


readLastNLines("sentence.txt", 3)