def hitung(value1, value2):
    return value1 - value2

def mutlak(number):
    if number < 0:
        return -number
    else:
        return number

a, c, b, d = map(int, input().split())

hasil = mutlak(hitung(a, b)) + mutlak(hitung(c, d))
print(hasil)