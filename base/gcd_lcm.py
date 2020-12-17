import math

#최대 공약수
a = 21
b = 14
print(math.gcd(a, b))

#최소 공배수
def lcm(a, b):
    return a*b // math.gcd(a,b)
print(lcm(a,b))