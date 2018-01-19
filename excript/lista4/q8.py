def func_variadica(**kwargs):
    print(kwargs)
    print(type(kwargs))

func_variadica(a=1, b=2, c=3, d=4)
func_variadica(um=True, dois=False, tres=True, quatro=True)
