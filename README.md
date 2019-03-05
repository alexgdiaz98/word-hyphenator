# Word Hyphenator
Python project that uses Liang's Algorithm to hyphenate words lfor use in a dictionary. These hyphens occur to denote where one would hyphenate a word to separate it between two lines.

## Logic

Each line in WordSplits.txt is a pattern of alphabetical characters and integers between 1-9. If the characters in that pattern exist in the word being considered, then we record between which characters that number lies. After considering all patterns relevant to the word, we record the highest number for each space between characters. If the highest number in each space is odd, then a hyphen is placed in that space.

A '.' character in a pattern denotes the required beginning or end of the word for that pattern to apply.

Consider the words "mistranslate" and "lexicographically" and their relevant patterns.

```
m i s t r a n s l a t e           l e x i c o g r a p h i c a l l y
| | | | | |2| | | | | | a2n       | |2| | | | | | | | | | | | | | | .le2
| | |1| | | | | | | | | .mis1     | | | | | | | |4| | | | | | | | | 4aphi
|2| | | | | | | | | | | m2is      | | | | | | | | | | | |1| | | | | 1ca
| | | | | |2|1|2| | | | 2n1s2     | | | |1| | | | | | | | | | | | | 1co
| | | | | | |2| | | | | n2sl      | | | |2| | | | | | | | | | | | | 2cog
| | | | | | | |1|2| | | s1l2      | | | | | |4| | | | | | | | | | | co4gr
| | | | | | | |3| | | | s3lat     | | | | | |1| | | | | | | | | | | 1gr
| | | |4| | | | | | | | st4r      | | | | | |5| | | | | | | | | | | 5graphic
| | | | | | | | | |4| | 4te.      | | | | | | | | | | | | | | |1| | l1l
| | |1| | | | | | | | | 1tra      | | | | | | | | | | | | | | |1| | 1ly
m2i s1t4r a2n2s3l2a4t e           | | | | | | | | | | |1| | | | | | ph1ic
| | | | | | | | | | | |           | | |3| | | | | | | | | | | | | | x3i
m i s-t r a n s-l a t e           | | | |5| | | | | | | | | | | | | xi5c
                                  l e2x3i5c o5g r4a p h1i1c a l1l y
                                  | | | | | | | | | | | | | | | | |
                                  l e x-i-c o-g r a p h-i-c a l-l y
```
## Usage

To use (all english language words):

```python3 WordSplits.py``` or ```./WordSplits.py```

To use with custom .txt file:

```python3 WordSplits.py [file_name]```
