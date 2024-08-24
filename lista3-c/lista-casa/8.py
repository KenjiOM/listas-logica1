#include <stdio.h>

int main () {
    int a;
    do {
        printf("%d \n", a);
        a = a + 2;
    } while (a <= 20);
}