def fac_number(number):
    result = 1
    for i in range(number):
        result = (i + 1) * result
    return result

print(fac_number(5))
