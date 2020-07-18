# fspell
Simple spell checker for Fongbe using Python.

This spell checker uses a simple Python dictionary (`dict`) to store the valid
words and a BK-Tree to get suggestions for unknown words. Suggestions are
sorted using bigrams. The first suggestion is the word with the more bigrams
in common with the unknown word.

## How to Use
- Open a terminal and change working directory to the project directory.
- Simply run `python3 fspell.py`

## How Does It Work?
The program used a predefined set of files.
- The file `words` contains the list of valid words. It is the base dictionary. 
- The file `misspells` contains the words you want suggestions for.
- A third file `words.sample` contains a sample of words from the file `words`.
  It was used when testing the program.

## About Performance
The program takes 1.5s on our computer to load the words from the dictionary
and create the BK-Tree. It takes 1.482s to find suggestions for the words in
our default `misspells` file. Our computer was running under Ubuntu 16.04 with an
Intel Core I5 processor and 8 Gio of memory.

## Useful Links
We have used functions and data structures presented in the following pages.
- Damerau-Levenshtein distance,
  https://web.archive.org/web/20150909134357/http://mwh.geek.nz:80/2009/04/26/python-damerau-levenshtein-distance/
- [BK-Tree](https://www.geeksforgeeks.org/bk-tree-introduction-implementation/)

## License
This work is under the MIT licence. A copy of the licence is available in the `licence` file.
