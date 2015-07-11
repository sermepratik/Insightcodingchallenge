#!/bin/bash

python ./src/wordsintweets.py ./tweet_input/tweets.txt ./tweet_output/unique_words.txt

python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/running_median.txt
