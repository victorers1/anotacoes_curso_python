def func1():
    def func2():
        return True

    return func2()

if(func1()):
    print("Acabou")
