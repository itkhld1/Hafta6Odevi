import math
def fn_x(a, b, c):
    d = b**2 - 4*a*c
    if d < 0: return None
    return ((-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a))
