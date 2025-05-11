#include <stdio.h>
#include <stdint.h>

int main() {
    int x = 42;  // Normal (stack üzerinde) değişken

    printf("Hex adresi: %p\n", (void*)&x);
    printf("Decimal adresi: %llu\n", (unsigned long long)(uintptr_t)&x);

    return 0;
}
