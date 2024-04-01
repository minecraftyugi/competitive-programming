f=lambda y:__import__("math").factorial(y)%2**32
exec"x=input();print f(x)if x<64else 0;"*input()
