def readLongestWord(filname:str):
    with open(filname,"r") as f:
        data=f.readlines()
        long=0
        length=0
        for lines in data:
            words=lines.split()
            for item in words:
               if len(item)>long:
                long=len(item)
                word=item
    print(long,word)



readLongestWord("sentence.txt")