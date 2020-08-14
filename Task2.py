"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Runtime : O(1)
def updateCallLog(callers: dict, caller: str, timeOnCall: str) -> int:
    if caller not in callers.keys():
        callers[caller] = int(timeOnCall)
    else:
        callers[caller] += int(timeOnCall)
    # Returns the most time spent this caller has spent on calls
    return callers[caller]

from typing import Tuple

# Runtime : O(n)
def longestCaller(calls: list) -> Tuple[str, int]:
    callers = dict()
    topNumber = ""
    topNumberTime = 0
    for call in calls:
        timeSpent = updateCallLog(callers, call[0], call[3])
        if timeSpent > topNumberTime:
            topNumberTime = timeSpent
            topNumber = call[0]
        timeSpent = updateCallLog(callers, call[1], call[3])
        if timeSpent > topNumberTime:
            topNumberTime = timeSpent
            topNumber = call[1]
    return topNumber, topNumberTime

topCaller, topCallerTime = longestCaller(calls)
print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(topCaller, topCallerTime))