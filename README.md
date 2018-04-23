# cooccurrences
Counts of pairs of places appearing in same Wikipedia article

# Tab-Separated Values Files
You can download the counts as a zipped tsv from [here](https://s3.amazonaws.com/firstdraftgis/cooccurrences.tsv.zip).  The tsv looks like this:

| a             | b                        | count |
| ------------- | ------------------------ | ----- |
| New York City | United States of America | 500   |
| Russia        | Soviet Union             | 300   |

# Pickled Counter
You can also download the counts as a zipped pickled Python Counter from [here](https://s3.amazonaws.com/firstdraftgis/cooccurrences.pickle.zip).  Here's how you can use it:
```
import pickle

with open("/tmp/cooccurrences.pickle", "rb") as f:
    cooccurrences = pickle.load(f)

count = cooccurrences[("New York City", "United States of America")]
print("New York City and United States of America appear together " + str(count) + " times.")
```

# Sorted
The keys are sorted using Python's `sorted` method.  You must sort your keys before looking up the results.  For example:
```

two_random_keys.sort()
a, b = two_random_keys
count = cooccurrences[two_random_keys]
print(a + " and " + b + " appear together " + str(count) + " times.")
```
