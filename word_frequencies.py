#!/usr/bin/python
from prettytable import PrettyTable
import argparse
import os
import re

start_word = "begin_layout"
stop_word = "end_layout"
ignore_lines = "\\"
word_sep = " "


table = PrettyTable()
table.junction_char = '|'


table.field_names = ["normalized Word", "Count", "Word(s)"]


parser = argparse.ArgumentParser(
        prog="word_frequencies",
        description="count words and frequencies from words inside a text. Exclude stopwords",
        epilog="Please use parameters"
        )
parser.add_argument("--file", required=True, dest="file", help="select file to analyze")
parser.add_argument("--exclude", dest="stopwords", help="use this file to exclude words")
parser.add_argument("--lyx", action='store_true', help="if set, only text inside /begin_layout and /end_layout is scanned")
parser.add_argument("--limit", type=int, dest='limit', default=100, help="set limit for table output, default=100")
parser.add_argument("-v", action='count', default=0, dest="verbose", help="Verbose output; -v default, -vv more output, -vvv maximum output")

args = parser.parse_args()

exclude_regex=[]
exclude_words=[]
lines = []
word_list = []
all_words_list = {}
word_frequencies = {}
pair_exclude = []

def build_word_frequency(wlist):
    print(f"Build word frequencies...")
    for w in wlist:
        #word_frequencies.append(wlist.count(w))
        count = word_frequencies.get(w,0)
        word_frequencies[w] = count + 1

def isValidWord(word):
    for r in exclude_regex:
        if r.match(word):
            if args.verbose > 0:
                print(f"Excluded word ('{word}') found with regex ('{r}')")
            return False
    return True

def buildCompiledRegex(word_list, regex_list):
    compiled_re = []
    print(f"Compile exluding regexe...")
    for w in word_list:
        regex = re.compile(w)
        regex_list.append(regex)
    return compiled_re

def build_word_list(lines, sep=" "):
    print (f"Scann ({len(lines)}) lines and split them to words...")
    for l in lines:
        wl = l.split(sep)
        for w in wl:
            if len(w) > 0 \
                and w.isnumeric() == False \
                and w[0] != "\\" :
                if isValidWord(w):
                    normalized_word = w.lower()
                    word_list.append(normalized_word)
                    if normalized_word in all_words_list:
                        v = all_words_list[normalized_word]
                        if w not in v:
                            all_words = f"{all_words_list.get(normalized_word)},{w}"
                            all_words_list[normalized_word] = all_words
                    else:
                        all_words_list[normalized_word] = str(w)
                    # pair_exclude.append(False)
               

    print (f"Number of words ({len(word_list):>8d})")



def file_load(file_path, wlist):
    #check if file is present
    if os.path.isfile(file_path):
        lines = []
        idx = 1
        try:
            with open(file_path, "r") as infile:
                copy = False
                for line in infile:
                    line = line.replace("\n","")
                    if args.verbose > 1:
                        print(f"LINE({idx:04d}) : [{line}]")
                    if len(line) == 0:
                        idx += 1
                        continue
                    if args.lyx:
                        if re.search(start_word, line.strip()):
                            copy=True
                            if args.verbose > 1:
                                print(f"START_WORD found")                           
                                continue 
                        elif re.search(stop_word, line.strip()):
                            copy=False
                            if args.verbose > 1:
                                print(f"STOP_WORD found")                           
                            continue
                        elif copy:
                            wlist.append(line.replace("\n",""))
                    else:
                        if len(line) > 2 and line != None:
                            wlist.append(line.strip())
                    idx += 1
                # close file
                infile.close()     
        except Exception as err:
            print(err)
            print(f"{file_path} is not a regular file or file not found")

def word_count(file):
    pass



if __name__ == "__main__":
    print(f"Input file loading...")
    file_load(args.file, lines)
    file_load(args.stopwords, exclude_words)
    buildCompiledRegex(word_list=exclude_words, regex_list=exclude_regex)
    build_word_list(lines)
    build_word_frequency(word_list)
    if args.verbose > 0:
        print(word_list)
        print(word_frequencies)
    
    #results = list(zip(word_list, word_frequencies, pair_exclude))
    for r in word_frequencies:
        table.add_row([r, word_frequencies[r], all_words_list[r]])
    #print(f"Pairs: {results}")
    #print(f"Number of pairs {len(results)}")
    print(f"\n## List of word frequencies")
    print(table.get_string(start=2, end=args.limit, sortby="Count", reversesort=True))
