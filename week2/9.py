list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)              # ['a', 'b', 'c', 1, 2, 3]

for x in list2:
  list1.append(x)
print(list1)              # ['a', 'b', 'c', 1, 2, 3]


list3 = ["a", "b", "c"]
list4 = [1, 2, 3]
list3.extend(list4)
print(list3)              # ['a', 'b', 'c', 1, 2, 3]


thislist1 = ["apple", "banana", "cherry"]
mylist = thislist1.copy()
print(mylist)                 # ['apple', 'banana', 'cherry']

thislist2 = ["apple", "banana", "cherry"]
mylist = list(thislist2)
print(mylist)                 # ['apple', 'banana', 'cherry']