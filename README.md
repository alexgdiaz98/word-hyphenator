# Word Hyphenator
Python project that uses Liang's Algorithm to hyphenate words lfor use in a dictionary. These hyphens occur to denote where one would hyphenate a word to separate it between two lines.

## Logic

Each line in WordSplits.txt is a pattern of alphabetical characters and integers between 1-9. If the characters in that pattern exist in the word being considered, then we record between which characters that number lies. After considering all patterns relevant to the word, we record the highest number for each space between characters. If the highest number in each space is odd, then a hyphen is placed in that space.

Consider the word "mistranslate" and its relevant patterns.

```
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
```
## Usage
To debug:

```python3 WordSplitsDebug.py``` or ```./WordSplitsDebug.py```

To use (all english language words):

```python3 WordSplits.py``` or ```./WordSplits.py```
