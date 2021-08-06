def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a

    if b > a:
        return gcd(a, b % a)
    if a > b:
        return gcd(a % b, b)
   

print(gcd(66528, 52920))
