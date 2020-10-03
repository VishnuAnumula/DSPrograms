# # write a program to accept a sentence and toggle its case

avv = input("Enter the sentence: ")
words = avv.split()
for i in range(len(words)):
    if words[i].isupper()==True:
        words[i] = words[i].lower()
    else:
        words[i] = words[i].upper()
print("The toggled sentence is")
for i in range(len(words)):
    print(words[i],end=' ')