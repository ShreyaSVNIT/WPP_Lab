string = input("Enter a word: ")
newstr = ''
for i in range(len(string)) :
    if i %2 != 0 : 
        newstr+= string[i].upper()
    else :
        newstr+=string[i].lower()
print(newstr)