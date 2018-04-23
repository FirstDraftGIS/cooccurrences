import csv
from collections import Counter
from itertools import combinations
from pickle import dump
from sys import maxsize

from config import max_key_count, path_to_counter, path_to_genesis, path_to_tsv

csv.field_size_limit(maxsize)

counter = Counter()

def prune(counter, max_key_count):
    return Counter(dict(counter.most_common(max_key_count)))

with open(path_to_genesis) as f:
    
    line_count = 0
    
    for page_id, titles in csv.reader(f, delimiter="\t"):
    
        line_count += 1
    
        counter.update(list(combinations(sorted(titles.split(";")), 2)))

        if line_count % 1e6 == 0:
            print("pruning counter")
            counter = prune(counter, max_key_count)
            print("pruned")

counter = prune(counter, max_key_count)

with open(path_to_counter, "wb") as f:
    dump(counter, f)
print("pickled")

with open(path_to_tsv, "w") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["a", "b", "count"])
    for (a, b), count in counter.most_common():
        writer.writerow([a, b, count])
print("wrote tsv")
