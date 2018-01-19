def func_variadica(*args):
    print(args)
    print(type(args))

l = [False, True]
func_variadica(*l)
func_variadica('0', '1', "dois")
func_variadica(False, 1, "dois", 3.0)
