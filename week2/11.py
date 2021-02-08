thistuple = ("apple", "banana", "cherry")
print(thistuple)              # ('apple', 'banana', 'cherry')
print(len(thistuple))         # 3

thistuple1 = ("apple",)      
print(type(thistuple1))       # <class 'tuple'>

thistuple2 = ("apple")
print(type(thistuple2))       # <class 'str'>

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)      # ('apple', 'banana', 'cherry')
print(tuple2)      # (1, 5, 7, 9, 3)
print(tuple3)      # (True, False, False)

thistuple = ("apple", "banana", "cherry")

print(thistuple[1])                 # banana
print(thistuple[-1])                # cherry

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 