def defangIPaddr(address: str):
    l = address.split(".")
    new_add = "[.]".join(l)
    return new_add
print(defangIPaddr("1.1.1.1"))