# fspell
Simple spell checker for Fongbe using Python.

This spell checker uses a simple Python set (`set`) to store the valid
words and a BK-Tree to get suggestions for unknown words. Suggestions are
ranked using Sorenson-Dice coefficient.

## How to Use
- Open a terminal and change working directory to the project directory.
- Simply run `python3 fspell.py`

## How Does It Work?
The program uses a predefined set of files.
- The file `words` contains the list of valid words. It is the base dictionary. 
- The file `misspells` contains the words you want suggestions for,
  one per line (you can change its content at will).

## About Performance
With CPython, the program takes 1.5s on our computer to load the words from the dictionary
and create the BK-Tree. It takes 1.482s to find suggestions for the words in
our default `misspells` file. Our computer was running under Ubuntu 16.04 with an
Intel Core I5 processor and 8 Gio of memory.

If you want the program to run faster, you can use PyPy.

## Useful Links
We have used functions and data structures presented in the following pages.
- Damerau-Levenshtein distance,
  https://web.archive.org/web/20150909134357/http://mwh.geek.nz:80/2009/04/26/python-damerau-levenshtein-distance/
- [BK-Tree](https://www.geeksforgeeks.org/bk-tree-introduction-implementation/)
- Sorenson-Dice coefficient, http://www.catalysoft.com/articles/StrikeAMatch.html and
  https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient

## License
This work is under the MIT licence. A copy of the licence is available in the `licence` file.
