#include <stdio.h>

int hitung(int value1, int value2) {
    return value1 - value2;
}

int mutlak(int number) {
    if (number < 0) {
        return -number;
    } else {
        return number;
    }
}

int main() {
    int a, b, c, d;

    scanf("%d %d %d %d", &a, &c, &b, &d);

    int hasil = mutlak(hitung(a, b)) + mutlak(hitung(c, d));
    printf("%d", hasil);

    return 0;
}