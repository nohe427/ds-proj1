"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Runtime : O(n)
def uniqueNumberCount(calls: list) -> int:
    uniqueNumbers = set()
    for call in calls:
        uniqueNumbers.add(call[0])
        uniqueNumbers.add(call[1])
    return len(uniqueNumbers)

print("There are {0} different telephone numbers in the records.".format(uniqueNumberCount(calls)))
