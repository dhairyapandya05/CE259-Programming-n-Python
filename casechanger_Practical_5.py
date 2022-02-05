word = input("Enter your string : \n")
l = list(word)

for x in l:
    if(x.islower()):
        print(x.upper(), end="")
    elif(x.isupper()):
        print(x.lower(), end="")
    elif(x.isnumeric):
        print(x, end="")
    elif(not (x.isalnum())):
        print(x, end="")
# input: HackerRank.com presents "Pythonist 2"
# output:hACKERrANK.COM PRESENTS "pYTHONIST 2"
