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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Runtime : O(n)
#  Authors note : I realize this could be also written as O(3n), 
#  but in the efficiency lectures, it mentions dropping the constants
def identifyTelemarketers(calls: list, texts: list) -> set:
    outgoingCallsOnly = set()
    incomingCallsOnly = set()
    for call in calls:
        dialer = call[0]
        number = call[1]
        outgoingCallsOnly.add(dialer)
        incomingCallsOnly.add(number)
    for text in texts:
        dialer = text[0]
        number = text[1]
        outgoingCallsOnly.discard(dialer)
        outgoingCallsOnly.discard(number)
    for incomingCall in incomingCallsOnly:
        outgoingCallsOnly.discard(incomingCall)
    sortedTelemarkteres = sorted(outgoingCallsOnly)
    return sortedTelemarkteres

print("These numbers could be telemarketers:\n{0}".format(identifyTelemarketers(calls, texts)))