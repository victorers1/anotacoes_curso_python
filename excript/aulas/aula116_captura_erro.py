def erro(x):
    try:
        eval(x)
    except(TypeError, NameError) as e:
        print("NameError ou TypeError ocorreu")
        print(e.args)
        print(e)
    except ValueError as e:  # pode ter memsmo nome
        print("ValueError")
        print(type(e))
        print(e.args)
        print(e)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    else:
        print("Nada ocorreu")

# TypeError
erro("int+int")
print(40*'-')

# NameError
erro("a")
print(40*'-')

# ValueError
erro("float('d')")
print(40*'-')

# ZeroDivisionError
erro("1/0")
print(40*'-')

# Else
erro("10+10")
print(40*'-')