sentence, sub = input().lower(), input().lower()
occurrences = 0
index = 0

while index!=-1:
    index = sentence.find(sub, index)
    if index is not -1:
        occurrences+=1
        index+=1



print(occurrences)
