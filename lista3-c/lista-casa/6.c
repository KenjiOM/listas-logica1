#include <stdio.h>

int main () {
    int a;
    for (a = 0; a <= 20; a += 1) {
        if (a % 2 == 0) {
            printf("%d é par \n", a);
        } else {
            printf("%d é ímpar \n", a);
        }
    }
}