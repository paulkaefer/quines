def foo():
    print("import inspect")
    print("lines = inspect.getsource(foo)")
    print("print(lines)")
    
    print("\nfoo()")

import inspect
lines = inspect.getsource(foo)
print(lines)

foo()
