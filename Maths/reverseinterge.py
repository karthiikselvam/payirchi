def revint(x):
    strofx = str(x)
    if x > 0:
        revstr = strofx[::-1]
        return revstr
    else:
        revstr = strofx[:0:-1]
        return "-"+ revstr


result = revint(-123)
print(result)

