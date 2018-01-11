a = 0


def func1():
    b = 0
    print("Valor inicial de b: {}".format(b))

    def func2():
        # nonlocal b  #como b não está no escopo local nem no global, a priori não poderiamos chamá-la
        b = 5
        print("Mudei valor de b para {} numa função interna". format(b))

    func2()
    print("Valor final de b: {}".format(b))


func1()

print(40*'-')


def func3():
    b = 0
    print("Valor inicial de b: {}".format(b))

    def func4():
        nonlocal b  # como b não está no escopo local nem no global, a priori não poderiamos chamá-la
        b = 5
        print("Mudei valor de b para {} numa função interna". format(b))

    func4()
    print("Valor final de b: {}".format(b))


func3()

print(40*'-')

x = 0
print("Valor inicial de x: {}".format(x))


def func5():
    global x  # A diferença está aqui
    x = 3
    print("Mudei valor de x para {}".format(x))


func5()
print("Valor final de x: {}".format(x))
