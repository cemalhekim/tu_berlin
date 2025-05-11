#include <stdio.h>
#include <stdlib.h>
int main() {
    int my_array[] = {3, 17, 42, 4, -9};
    int zahl1 = my_array[1];
    int zahl2 = *my_array;
    int zahl3 = *(my_array + 2);
    int zahl4 = *my_array + 2;
    printf("Zahl 1: %d\n Zahl 2: %d\n Zahl 3: %d\n Zahl 4: %d\n",
        zahl1, zahl2, zahl3, zahl4);
}