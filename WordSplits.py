import re
import sys

if (len(sys.argv) == 2):
    text_file = sys.argv[1]
else:
    text_file = "Enable1.txt"

with open('WordSplits.txt', 'r') as pattern_doc:
    with open(text_file, 'r') as word_doc:
        counts = [0,0,0,0,0,0,0,0,0,0]
        patterns = pattern_doc.readlines()
        words = word_doc.readlines()
        strip = ".0123456789 \n " # Characters removed from a pattern to make alphabetical string
        counter = 0 # Number of patterns for a given word
        for word in words:
            word = word.replace("\n", "")
            #print("Word = " + word)
            patternTable = [] # Array of patterns found for given word -> patternTable[i] = [pattern, alpha]
            hyphenTable = [] # Array of highest number found for each space between characters in word
            for i in range(len(word)-1):
                hyphenTable.append(0)
            for pattern in patterns:
                pattern = pattern.replace("\n", "")
                alpha = pattern # Pattern = '.eq5ui5t' -> Alpha = 'equit'
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
                #print("considering", pair[0])
                if (pair[0][0] == '.'): # If pattern begins with '.'
                    pair[0] = pair[0].replace('.', "")
                    char_index = 0
                    for i in range(len(pair[0])):
                        if (pair[0][i] in "123456789"):
                            if (i == 0):
                                #print("Error: Hyphen Number occured before word begins")
                                pass
                            elif (char_index == len(word)):
                                #print("Hyphen Number at end of '.*' word", word, pair[0])
                                pass
                            elif (int(pair[0][i]) > hyphenTable[char_index-1]):
                                hyphenTable[char_index-1] = int(pair[0][i])
                        else:
                            char_index += 1
                elif (pair[0][-1] == '.'): # If pattern ends with '.'
                    pair[0] = pair[0].replace('.', "")
                    char_index = 0
                    for i in range(len(pair[0])):
                        if (pair[0][i] in "123456789"):
                            if (i == len(pair[0])-1):
                                #print("Error: Hyphen Number occured after word ends")
                                pass
                            elif (len(pair[1]) == len(word) and char_index == 0 and i == 0):
                                #print("Hyphen Number at beginning of '*.' word", word, pair[0])
                                pass
                            elif (int(pair[0][i]) > hyphenTable[len(hyphenTable)-len(pair[1])+char_index]):
                                hyphenTable[len(hyphenTable)-len(pair[1])+char_index] = int(pair[0][i])
                        else:
                            char_index += 1
                else: # If pattern has no '.'
                    indeces = [m.start() for m in re.finditer(pair[1], word)]
                    #print(pair[0], "found at indeces: ", end="")
                    #print(", ".join(str(x) for x in indeces))
                    for ind in indeces:
                        char_index = 0
                        for i in range(len(pair[0])): # For each character in the pattern
                            if (pair[0][i] in "123456789"):
                                if ((i != 0 or ind != 0) and (i != len(pair[0])-1 or ind != len(hyphenTable)-len(pair[1])+1)):
                                    if (int(pair[0][i]) > hyphenTable[ind+char_index-1]):
                                        hyphenTable[ind+char_index-1] = int(pair[0][i])
                                #else:
                                #	print("Detected Hyphen Number at the beginning or end of a word", pair[0], word)
                            else:
                                char_index += 1
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
            
            if counter % 1000 == 0:
                print(str(counter),"word:", word)
            
            #print(word, "has", str(hyphenCount), "hyphens. Hyphen Table:", str(hyphenTable), '\n')
            
            
        for i in range(len(counts)):
            print("Number of words with", str(i), "hyphens:", str(counts[i]))