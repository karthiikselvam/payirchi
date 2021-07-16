# 3^3
# base, exponent
# pow(n) = result 
# pow(3,4) = pow(3,4-1) * 3
# pow(base,exponent) = pow(base,exponent-1) * base
# if exponent = 1 return base

def pow(base,exponent):
    if exponent == 1:
        return base
    else:
        return pow(base,exponent-1) * base

result = pow(3,4)
print(result)

