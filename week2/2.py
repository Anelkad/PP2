thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()
print(x)            # dict_keys(['brand', 'model', 'year'])   show all keys

car["color"] = "white"
print(x)            # add key:value

y = thisdict.values()
print(y)            # dict_values(['Ford', 'Mustang', 1964])   show all value

car["year"] = 2020
print(x)            # change value of key

x1 = thisdict.items()
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018
print(thisdict) 