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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
# Assumption
# - We are checking for the numbers called call[1], not the numbers that are being called from call[0].
# - call[0] should always be a bangalore area code
# - Area code numbers are what we are interested in here.
# - Mobile numbers do have an area code called a prefix.

# Runtime : O(1)
def isLandline(number: str) -> bool:
  if number[0] == '(':
    return True

# Runtime : O(1)
def getLandlineAreaCode(number: str) -> str:
  number = number [1:]
  areaCode = ''
  while number[0] != ')':
    areaCode += number[0]
    number = number[1:]
  return areaCode

# Runtime : O(1)
def isBangaloreAreaCode(number: str) -> bool:
  if number[0:5] == '(080)':
    return True

# Runtime : O(1)
def isTelemarketer(number: str) -> bool:
  if number[0] == '1' and number[1] == '4' and number[2] == '0':
    return True

# Runtime : O(1)
def getTelemarketerAreaCode() -> str:
  return '140'

# Runtime : O(1)
def isMobileNumber(number: str) -> bool:
  if ' ' in number:
    return True
  return False

# Runtime : O(1)
def getMobileNumberAreaCode(number: str) -> str:
  return number.split(' ')[0][:4]

# Runtime : O(n log(n))
def getAreaCodes(calls: list) -> set:
  areaCodes = set()
  for call in calls:
    dialer = call[0]
    number = call[1]
    # If the number is not a bangalore area code, restart the loop with the next number
    if not isBangaloreAreaCode(dialer):
      continue
    # Determine what number was used and carry on
    if isLandline(number):
      areaCodes.add(getLandlineAreaCode(number))
      continue
    if isMobileNumber(number):
      areaCodes.add(getMobileNumberAreaCode(number))
      continue
    if isTelemarketer(number):
      areaCodes.add(getTelemarketerAreaCode())
      continue
  sortedAreaCodes = sorted(areaCodes)
  return sortedAreaCodes

calledCodes = getAreaCodes(calls)
print("The numbers called by people in Bangalore have codes:\n{0}".format('\n'.join(calledCodes)))

## Part B

# Runtime : O(n)
def calculateB2BCalls(calls: list) -> float:
  totalB2B = 0
  totalCallsInB = 0 
  for call in calls:
    dialer = call[0]
    number = call[1]
    if isBangaloreAreaCode(dialer):
      totalCallsInB += 1
      if isBangaloreAreaCode(number):
        totalB2B += 1
      continue
  return round(100*(totalB2B/totalCallsInB), 2)

print("{0} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(calculateB2BCalls(calls)))