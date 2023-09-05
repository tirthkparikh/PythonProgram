def vowelWords(file):
    with open(file,"r") as f:
        data=f.readlines()
       
    with open("sentence1.txt","w") as f:
        newValue=""
        for i in data:
            flag=False
            value=i.split()
            for i in value:
                count=0
                for j in i:
                    if j.lower() in "aeiou":
                        count+=1
                    if count>2:
                        newValue+=f"{i} "
                        flag=True
                        break
            if flag:
                newValue+="\n"
        f.write(newValue)
               
                   

vowelWords("sentence.txt")