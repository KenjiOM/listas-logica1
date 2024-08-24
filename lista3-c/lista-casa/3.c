#include <stdio.h>

int main () {
    int a;
    a = 0;
    while (a <= 20) {
        if (a % 2 == 0) {
            printf("%d é par\n", a);
            a++;
        } else {
            printf("%d é impar\n", a);
            a++;
        }
    }
}