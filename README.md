# word_frequencies
count words and frequencies inside a file.

This little script is used to check bachelor and master thesis against often used words 

First approach was to read latex/lyx files, but this didn't work very well, because it's neccassary to implement a lot of stuff around to avoid words hits, which are latex stuff.

Current approach is to read a normal text file and an ignore_words file and analyse the text.

# History
| date | version | information |
|---|:-:|---|
| 2023-07-23 | 0.1 | solution only for text files |


# ignore_words
every row should be a word or an regulare expresseion. If a word inside the text file hits agains an ignore_word or a regex, this word will be ignored.

## Building a RegEx object list
if regex is used, before starting analysis of a text file, all ignore_words and regexe are read and compiled. During analyze this compiled object list is used to get a better performance
# PrettyTable output
Output is set by PrettyTable and as Markdown, so it's easy to use in web presentations. Default is set to the top 100 words (via parameter this can be changed)

