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
    # elif set(x).difference(ascii_letters + digits):
        # print(x, end=" ")
# HackerRank.com presents "Pythonist 2"
