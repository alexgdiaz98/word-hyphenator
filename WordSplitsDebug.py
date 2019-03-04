import re
with open('WordSplits.txt', 'r') as doc:
    with open('Debug.txt', 'r') as doc2:
        counts = [0,0,0,0,0,0,0,0,0,0]
        patterns = doc.readlines()
        words = doc2.readlines()
        strip = ".0123456789 \n "
        counter = 0
        for word in words:
            word = word.replace("\n", "")
            #print("Word = " + word)
            patternTable = []
            hyphenTable = []
            for i in range(len(word)-1):
                hyphenTable.append(0)
            for pattern in patterns:
                pattern = pattern.replace("\n", "")
                alpha = pattern
                for char in strip:
                    alpha = alpha.replace(char,"")
                if pattern.startswith("."):
                    if word.startswith(alpha):
                        #print(word + " matched with " + pattern + " at the start")
                        patternTable.append([pattern, alpha]) # row in detailed example table
                        counter += 1
                elif pattern.endswith("."):
                    if word.endswith(alpha):
                        #print(word + " matched with " + pattern + " at the end")
                        patternTable.append([pattern, alpha])
                        counter += 1
                else:
                    if alpha in word:
                        #print(word + " matched with " + pattern + " in the middle")
                        patternTable.append([pattern, alpha])
                        counter += 1
            '''
            print(word + ": ", end=" ")
            for pair in patternTable:
                print(pair[0], end=" ")
            print()
            '''
            for pair in patternTable:
                pair[0] = pair[0].replace('.', "")
                indeces = [m.start() for m in re.finditer(pair[1], word)]
                #print(", ".join(str(x) for x in indeces))
                comp = 0
                for ind in range(len(pair[0])): #for each character in the pattern
                    if pair[0][ind] in "123456789":
    
                        #print("ind = " + str(ind))
                        #print("hyphenTable length = " + str(len(hyphenTable)))
                        for i in indeces:
                            if not (i + ind == 0 or i + ind - comp >= len(word)):
                                #print("i = " + str(i) + " pair[0][ind] = " + pair[0][ind])
                                if hyphenTable[i + ind - 1 - comp] < int(pair[0][ind]):
                                    hyphenTable[i + ind - 1 - comp] = int(pair[0][ind])
                        comp += 1
            hyphenCount = 0
            for i in range(len(hyphenTable)):
                if hyphenTable[i] % 2 == 1:
                    word = word[:i+hyphenCount+1] + '-' + word[i+hyphenCount+1:]
                    hyphenCount += 1
            '''
            print(word + " " + ", ".join(str(x) for x in hyphenTable))
            print(
            '''
            counts[hyphenCount] += 1
            '''
            if counter % 1000 == 0:
                print(str(counter))
            '''
            print(word + "\t\t\t" + str(hyphenCount) + " total is now " + str(counts[hyphenCount]))
            
            
        for i in range(len(counts)):
            print(str(i) + " hyphens: " + str(counts[i]))
'''
Detailed Example:

m i s t r a n s l a t e
| | | | | |2| | | | | | a2n
| | |1| | | | | | | | | .mis1
|2| | | | | | | | | | | m2is
| | | | | |2|1|2| | | | 2n1s2
| | | | | | |2| | | | | n2sl
| | | | | | | |1|2| | | s1l2
| | | | | | | |3| | | | s3lat
| | | |4| | | | | | | | st4r
| | | | | | | | | |4| | 4te.
| | |1| | | | | | | | | 1tra
m2i s1t4r a2n2s3l2a4t e
| | | | | | | | | | | |
m i s-t r a n s-l a t e

'''
