#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 17:31:12 2019

@author: zub
"""

import re
from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter


def prep_text():
    with open('ep6.txt', 'r', encoding = 'utf-8') as input, open('ep6_out.txt', 'w', encoding = 'utf-8') as output:
        for line in input:
            line = re.sub(r'^"\d+"', '', line).casefold()
            output.write(line)    
    
    path = 'ep6_out.txt'
      
    with open(path, 'r') as source:
        lines = source.readlines()
        
        vader = re.compile(r'"vader".+')
        vader_lines = list()
        
        for line in lines:
            match = vader.search(line)
            if match:
                vader_lines.append(match.group())
                
        global vader_lines_str
        vader_lines_str = str()
        
        for line in vader_lines:
            vader_lines_str += line
            vader_lines_str = vader_lines_str.replace('"vader"', '')
            vader_lines_str = vader_lines_str.replace('"', '')
            vader_lines_str = vader_lines_str.replace(',', '')
    
        luke = re.compile(r'"luke".+')
        luke_lines = list()

        for line in lines:
            match = luke.search(line)
            if match:
                luke_lines.append(match.group())
        
        global luke_lines_str
        luke_lines_str = str()
        
        for line in luke_lines:
            luke_lines_str += line
            luke_lines_str = luke_lines_str.replace('"luke"', '')
            luke_lines_str = luke_lines_str.replace('"', '')
            luke_lines_str = luke_lines_str.replace(',', '')
            
            
    print(f'Lord Vader says: \n {vader_lines_str}')
    print()
    print(f'Luke Skywalker says: \n {luke_lines_str}')


prep_text()

vader = vader_lines_str
luke = luke_lines_str

def process_vader():
    vader_tokenized = word_sentence_tokenize(vader)
    
    single_sentence_tokenized = vader_tokenized[27]
    print()
    print(f"Vader's single tokenized sentence: {single_sentence_tokenized}")
    
    pos_tagged_vader = list()
    
    for sentence in vader_tokenized:
        pos_tagged_vader.append(pos_tag(sentence))
        
    pos_tagged_sentence = pos_tagged_vader[27]
    print()
    print(f"Vader's single part-of-speech tagged sentence: {pos_tagged_sentence}")
    
    np_chunk_grammar = 'NP: {<DT>?<JJ.?>*<NN>}'
    np_chunk_parser = RegexpParser(np_chunk_grammar)
    
    vp_chunk_grammar = 'VP: {<DT>?<JJ.?>*<NN><VB.?>((<RB.?>)|(<DT>?<JJ.?>*<NN>)|(<IN><DT>?<JJ.?>*<NN>))*}'
    vp_chunk_parser = RegexpParser(vp_chunk_grammar)
    
    np_chunked_vader = list()
    vp_chunked_vader = list()
    
    for sentence in pos_tagged_vader:
        np_chunked_vader.append(np_chunk_parser.parse(sentence))
        vp_chunked_vader.append(vp_chunk_parser.parse(sentence))
    
    top_np_chunks = np_chunk_counter(np_chunked_vader)
    top_vp_chunks = vp_chunk_counter(vp_chunked_vader)
    
    print()
    print("Vader's most-commonly used noun-phrases:")
    print(*top_np_chunks, sep = '\n')
    print()
    print(f"Vader's most-commonly used verb-phrases:")
    print(*top_vp_chunks, sep = '\n')
    
process_vader()

def process_luke():
    luke_tokenized = word_sentence_tokenize(luke)
    
    single_sentence_tokenized = luke_tokenized[72]
    print()
    print(f"Luke's single tokenized sentence: {single_sentence_tokenized}")
    
    pos_tagged_luke = list()
    
    for sentence in luke_tokenized:
        pos_tagged_luke.append(pos_tag(sentence))
        
    pos_tagged_sentence = pos_tagged_luke[72]
    print()
    print(f"Luke's single part-of-speech tagged sentence: {pos_tagged_sentence}")
    
    np_chunk_grammar = 'NP: {<DT>?<JJ.?>*<NN>}'
    np_chunk_parser = RegexpParser(np_chunk_grammar)
    
    vp_chunk_grammar = 'VP: {<DT>?<JJ.?>*<NN><VB.?>((<RB.?>)|(<DT>?<JJ.?>*<NN>)|(<IN><DT>?<JJ.?>*<NN>))*}'
    vp_chunk_parser = RegexpParser(vp_chunk_grammar)
    
    np_chunked_luke = list()
    vp_chunked_luke = list()
    
    for sentence in pos_tagged_luke:
        np_chunked_luke.append(np_chunk_parser.parse(sentence))
        vp_chunked_luke.append(vp_chunk_parser.parse(sentence))
    
    top_np_chunks = np_chunk_counter(np_chunked_luke)
    top_vp_chunks = vp_chunk_counter(vp_chunked_luke)
    
    print()
    print("Luke's most-commonly used noun-phrases:")
    print(*top_np_chunks, sep = '\n')
    print()
    print(f"Luke's most-commonly used verb-phrases:")
    print(*top_vp_chunks, sep = '\n')
    
process_luke()