from math import floor

def extended_gcd(a, b):
    # i just modified the example on wikipedia for this because I am small brain and dont want to think about what the extended_gcd does in math and convert to code
    (old_r, r) = (a, b)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)
    while not (r == 0):
        quotient = floor(old_r / r)
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)

    # the equation is as + bt = gcd(a, b)
    return (old_s, old_t)

print(extended_gcd(26513, 32321))
