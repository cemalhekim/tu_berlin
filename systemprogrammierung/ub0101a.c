#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>  // <-- gerekli olan bu

int main() {
    int *ptr = malloc(sizeof(int));
    if (ptr == NULL) {
        perror("malloc");
        return 1;
    }
    
    printf("Hex adresi: %p\n", (void*)ptr);
    printf("Decimal adresi: %llu\n", (unsigned long long)(uintptr_t)ptr);

    free(ptr);
    return 0;
}
