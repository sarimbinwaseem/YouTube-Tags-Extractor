#!/bin/bash
echo "Enter YouTube video link: "
read link
python3 tagsExtractor.py $link
