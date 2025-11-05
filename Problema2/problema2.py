import subprocess
import time
from math import comb
from pathlib import Path

def pascal_coeffs(n):
    return [comb(n, k) for k in range(n + 1)]

def evaluar_polinomio(coeffs, x):
    return sum(c * (x ** i) for i, c in enumerate(coeffs))

def ejecutar_prueba_dos(n=100, x=2):
    carpeta = Path(__file__).parent  
    salida = []

    # Ejecución en Python
    t0 = time.perf_counter()
    coeffs = pascal_coeffs(n)
    t1 = time.perf_counter()
    gen_py = (t1 - t0) * 1000

    t2 = time.perf_counter()
    valor_py = evaluar_polinomio(coeffs, x)
    t3 = time.perf_counter()
    eval_py = (t3 - t2) * 1000

    salida.append("=== RESULTADOS EN PYTHON ===\n")
    salida.append(f"n = {n}, x = {x}\n")
    salida.append(f"Resultado f(x) = {valor_py}\n")
    salida.append(f"Tiempo generación coeficientes: {gen_py:.3f} ms\n")
    salida.append(f"Tiempo evaluación polinomio: {eval_py:.3f} ms\n\n")

    # Crear código en C 
    codigo_c = f"""
    #include <stdio.h>
    #include <time.h>
    #include <math.h>

    double comb(int n, int k) {{
        if (k == 0 || k == n) return 1;
        if (k > n) return 0;
        double res = 1;
        for (int i = 1; i <= k; i++)
            res = res * (n - i + 1) / i;
        return res;
    }}

    int main() {{
        int n = {n};
        double x = {x};
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

        printf("=== RESULTADOS EN C ===\\n");
        printf("n = %d, x = %.2f\\n", n, x);
        printf("Resultado f(x) = %.0f\\n", valor);
        printf("Tiempo generación coeficientes: %.3f ms\\n", tiempo_gen);
        printf("Tiempo evaluación polinomio: %.3f ms\\n", tiempo_eval);
        return 0;
    }}
    """

    archivo_c = carpeta / "problema2.c"
    archivo_c.write_text(codigo_c, encoding="utf-8")

    ejecutable = carpeta / "problema2_exec"
    subprocess.run(["gcc", str(archivo_c), "-lm", "-o", str(ejecutable)], check=True)
    resultado_c = subprocess.run([str(ejecutable)], capture_output=True, text=True)

    salida.append(resultado_c.stdout)

    archivo_salida = carpeta / "problem2_comparacion.txt"
    archivo_salida.write_text("".join(salida), encoding="utf-8")

    print("✅ Ejecución completada.")
    print(f"📄 Archivo de comparación: {archivo_salida}")
    print(f"💻 Código C generado: {archivo_c}")
    print(f"⚙️ Ejecutable: {ejecutable}")
    print("\nResumen:\n")
    print("".join(salida))

if __name__ == "__main__":
    ejecutar_prueba_dos(100, 2)
