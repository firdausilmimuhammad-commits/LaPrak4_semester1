def maksimal(a, b):
    if a > b:
        return a
    else:
        return b

def minimal(a, b):
    if a < b:
        return a
    else:
        return b

batas = 0
maks = -100000
minim = 100000

bilangan = int(input())

nilai_list = []
while len(nilai_list) < bilangan:
    nilai_list.extend(map(int, input().split()))

while batas < bilangan:
    nilai = nilai_list[batas]
    maks = maksimal(maks, nilai)
    minim = minimal(minim, nilai)
    batas += 1

print(f"{maks} {minim}")