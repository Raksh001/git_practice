from decimal import *

## Print default precision
print("Default Precision: " + str(getcontext().prec))
## Test 1. As intended by the excercise using string types for values.
print("Test 1")
test01 = Decimal('0.2345') + Decimal('0.12')
## This will result in a four decimal place number: 0.3545.
print(len(str(test01))-2)
print(test01)
## Test 2
print("Test 2")
test02 = Decimal(0.2345) + Decimal(0.12)
## This will result in a float with a precision of 28 decimal places.
print(len(str(test02))-2)
print(test02)
## Test 3
print("Test 3")
test03 = Decimal(0.2345 + 0.12)
## This will result in a float of 54 decimal places.
## It seems the Decimal precision didn't even affect this.
print(len(str(test03))-2)
print(test03)
## Test
## Test 4
print("Test 4")
test04 = Decimal(str(0.2345 + 0.12))
## Converting the sum to a string, and then we see something interesting.
print(len(str(test04))-2)
print(test04)
## Test 5
print("Test 5")
print("Current Precision: " + str(getcontext().prec))
test05 = Decimal(0.2345) + Decimal(0.12)
## Following, precision is set after Decimal is invoked.  No change.
getcontext().prec = 4
print("Current Precision: " + str(getcontext().prec))
print(len(str(test05))-2)
print(test05)
## Reset Precision to default value.
getcontext().prec = 28
print("Current Precision: " + str(getcontext().prec))
## Test 6
print("Test 6")
## Precision is set before Decimal is used.
## This results in the decimal places being set to 4 and rounding occurs.
getcontext().prec = 4
print("Current Precision: " + str(getcontext().prec))
test06 = Decimal(0.2345) + Decimal(0.12)
## Now we see why placement of precision is key.
print(len(str(test06))-2)
print(test06)
getcontext().prec = 28