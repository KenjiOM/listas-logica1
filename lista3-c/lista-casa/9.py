#include <stdio.h>

int main () {
    int a;
    a = 0;
    do {
        if (a % 2 == 0) {
            printf("%d é par \n", a);
            a++;
        } else {
            printf("%d é ímpar \n", a);
            a++;            
        }
    } while (a <= 20);
}