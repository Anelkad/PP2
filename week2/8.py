list1 = ["apple", "banana", "cherry"]
list2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(list1[1])         # banana
print(list1[-1])        # cherry

print(list2[2:5])       # ['cherry', 'orange', 'kiwi']
print(list2[:4])        # ['apple', 'banana', 'cherry', 'orange']
print(list2[2:])        # ['cherry', 'orange', 'kiwi', 'melon', 'mango']

if "apple" in list1:
  print("Yes, 'apple' is in the fruits list")


list1 = ["apple", "banana", "cherry"]
list1.append("orange")
print(list1)                 # ['apple', 'banana', 'cherry', 'orange']


list2 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
list2.extend(tropical)
print(thislist)   