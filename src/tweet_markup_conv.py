#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NOTE: Use python3 because it uses unicode by default.
"""

import os
import json
import sys

md_file = "MarkdownTweets.md"

def tweetdir_to_markdown(dirname):
    """
    Function that takes a directory containing the users tweet archive and 
    converts them into markdown. Dirname must be composed of tweets organized 
    in json format. Only want to archive original tweets, so any tweets 
    containing @ are ignored.
    """
    # Blank file
    holder = open(md_file, 'w')
    holder.write("Tweet Archive")
    holder.write("\n\n")
    holder.write("<hr>")
    holder.write("\n\n")
    holder.close() 
    
    if(os.path.isdir(dirname)):
        for tweetfile in reversed(os.listdir(dirname)):
            abspath = os.path.abspath(dirname + "/" + tweetfile)
            tmp = 'tmp'    
            # Delete the first line.  
            with open(abspath, 'r') as fin:
                data = fin.read().splitlines(True)
            with open(tmp, 'w') as fout:
                fout.writelines(data[1:]) 
           
            tweetfile_to_markdown(tmp)
        os.remove(tmp)
    else:
        print("Error: Directory does not exist")

def tweetfile_to_markdown(filename):
    holder = open(md_file, 'a')

    with open(filename) as data_file:
        data = json.load(data_file)
        
        for tweet in data:
            message = tweet["text"]
            date = tweet["created_at"]
            
            if '@' not in message and 'RT' not in message:
                holder.write("**" + date + "**\n")
                holder.write(message + "\n\n")

    holder.close()

if __name__ == '__main__':
    if(len(sys.argv) == 2):
        dirname = sys.argv[1]
        tweetdir_to_markdown(dirname)
    else:
        print("Error: Directory not specified")
