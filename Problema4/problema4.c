#include <stdio.h>

int main() {
    int x = 10;
    float y = 3.14;
    
    for (int i = 0; i < x; i++) {
        if (i % 2 == 0) {
            printf("Par: %d\\n", i);
        } else {
            printf("Impar: %d\\n", i);
        }
    }
    
    while (x > 0) {
        x--;
        if (x == 5) {
            continue; // Saltar el 5
        }
        if (x == 2) {
            break; // Salir en 2
        }
    }
    
    return 0;
}