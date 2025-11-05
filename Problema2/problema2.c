
    #include <stdio.h>
    #include <time.h>
    #include <math.h>

    double comb(int n, int k) {
        if (k == 0 || k == n) return 1;
        if (k > n) return 0;
        double res = 1;
        for (int i = 1; i <= k; i++)
            res = res * (n - i + 1) / i;
        return res;
    }

    int main() {
        int n = 100;
        double x = 2;
        double valor = 0;
        clock_t start, end;

        start = clock();
        double coef[n+1];
        for (int i = 0; i <= n; i++)
            coef[i] = comb(n, i);
        end = clock();
        double tiempo_gen = ((double)(end - start)) / CLOCKS_PER_SEC * 1000;

        start = clock();
        for (int i = 0; i <= n; i++)
            valor += coef[i] * pow(x, i);
        end = clock();
        double tiempo_eval = ((double)(end - start)) / CLOCKS_PER_SEC * 1000;

        printf("=== RESULTADOS EN C ===\n");
        printf("n = %d, x = %.2f\n", n, x);
        printf("Resultado f(x) = %.0f\n", valor);
        printf("Tiempo generación coeficientes: %.3f ms\n", tiempo_gen);
        printf("Tiempo evaluación polinomio: %.3f ms\n", tiempo_eval);
        return 0;
    }
    