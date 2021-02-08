thisset = {"apple", "banana", "cherry"}
print(thisset)                  # {'banana', 'apple', 'cherry'}  the set list is unordered

thisset1 = {"apple", "banana", "cherry", "apple"}
print(thisset1)                 # {'banana', 'apple', 'cherry'}  cannot have two items with the same value

print(len(thisset))             # 3

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)   # {'cherry', 'apple', 'banana'}
print(set2)   # {1, 3, 5, 7, 9}
print(set3)   # {False, True}

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)      