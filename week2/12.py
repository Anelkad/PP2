thistuple = ("apple", "banana", "cherry")

print(thistuple[1])                 # banana
print(thistuple[-1])                # cherry

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 


fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)



fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits1
print(green)
print(yellow)
print(red)



fruits2 = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits2
print(green)
print(tropic)
print(red)