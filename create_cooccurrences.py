import csv
from collections import Counter
from itertools import combinations
from pickle import dump
from sys import maxsize

from config import path_to_counter, path_to_genesis

csv.field_size_limit(maxsize)

counter = Counter()

with open(path_to_genesis) as f:
    
    line_count = 0
    
    for page_id, titles in csv.reader(f, delimiter="\t"):
    
        line_count += 1
    
        counter.update(list(combinations(sorted(titles.split(";")), 2)))

        if line_count % 1e2 == 0:
            print("pruning counter")
            counter = Counter(dict(counter.most_common(5000000)))
            print("pruned")
            break

with open(path_to_counter, "wb") as f:
    dump(counter, f)

print("saved cooccurrences")
