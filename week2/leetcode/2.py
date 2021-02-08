def interpret(command: str):
    f = command.replace("()", "o")
    s = f.replace("(", "")
    t = s.replace(")", "")
    return t
print(interpret("G()()()()(al)"))