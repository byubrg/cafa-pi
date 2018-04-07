GOLookup.py
This script will retrieve the GO term data for an id you submit. You can
submit a list of space separated terms, or a file containing a list of newline
separated terms, or just a single term.

To run the GO_term retrieval script, you need to load the following:

module load python/3/6
pip3 install --user requests

GOParent.py
This script takes child terms of either biofilm formation or motility and
converts them to the parent term we are search for. 
