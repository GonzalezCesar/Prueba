import subprocess
import os
import sys

# 1. Código C a ejecutar (el mismo del punto 1)
CODIGO_C = """
#include <stdio.h>
#include <string.h>

typedef struct {
    const char *palabra_c;
    const char *traduccion_es;
} PalabraReservada;

PalabraReservada lista_palabras[] = {
    {"auto", "automático"},
    {"break", "romper / salir"},
    {"case", "caso"},
    {"char", "carácter"},
    {"const", "constante"},
    {"continue", "continuar"},
    {"default", "predeterminado"},
    {"do", "hacer"},
    {"double", "doble (precisión)"},
    {"else", "sino / de lo contrario"},
    {"enum", "enumeración"},
    {"extern", "externo"},
    {"float", "flotante (real)"},
    {"for", "para (bucle)"},
    {"goto", "ir a"},
    {"if", "si (condicional)"},
    {"int", "entero"},
    {"long", "largo"},
    {"register", "registro"},
    {"return", "retornar / devolver"},
    {"short", "corto"},
    {"signed", "con signo"},
    {"sizeof", "tamaño de"},
    {"static", "estático"},
    {"struct", "estructura"},
    {"switch", "selector / interruptor"},
    {"typedef", "definición de tipo"},
    {"union", "unión"},
    {"unsigned", "sin signo"},
    {"void", "vacío / nulo"},
    {"volatile", "volátil"},
    {"while", "mientras (bucle)"}
};

int main() {
    int total_palabras = sizeof(lista_palabras) / sizeof(lista_palabras[0]);
    int i;

    printf("\\n--- Verificación de Palabras Reservadas de C y Traducción ---\\n");
    printf("Palabras encontradas: %d\\n", total_palabras);
    printf("------------------------------------------------------------\\n");
    printf("| %-15s | %-30s |\\n", "Palabra C", "Traducción al Español");
    printf("------------------------------------------------------------\\n");

    for (i = 0; i < total_palabras; i++) {
        printf("| %-15s | %-30s |\\n", 
               lista_palabras[i].palabra_c, 
               lista_palabras[i].traduccion_es);
    }
    
    printf("------------------------------------------------------------\\n");

    return 0;
}
"""

# Nombres de archivos
NOMBRE_C = "palabras.c"
NOMBRE_EJECUTABLE = "palabras_c"
# El nombre del ejecutable en Windows es palabras_c.exe, en otros es palabras_c
if sys.platform == "win32":
    NOMBRE_EJECUTABLE += ".exe"

def ejecutar_programa_c():
    """Guarda, compila y ejecuta el código C, luego limpia."""
    
    # 2. Guardar el código C en un archivo
    try:
        with open(NOMBRE_C, "w") as f:
            f.write(CODIGO_C)
        print(f"✅ Archivo C '{NOMBRE_C}' creado con éxito.")
    except IOError as e:
        print(f"❌ Error al escribir el archivo C: {e}")
        return

    # 3. Compilar el código C (usando GCC)
    print(f"\n⚙️ Compilando el código C con GCC...")
    try:
        # Comando de compilación: gcc palabras.c -o palabras_c
        comando_compilacion = ["gcc", NOMBRE_C, "-o", NOMBRE_EJECUTABLE]
        resultado_compilacion = subprocess.run(
            comando_compilacion, 
            capture_output=True, 
            text=True,
            check=True
        )
        print("✅ Compilación exitosa.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error de compilación. Asegúrate de tener GCC instalado.")
        print(f"Error de salida:\n{e.stderr}")
        return
    except FileNotFoundError:
        print("❌ Error: Compilador 'gcc' no encontrado. Por favor, instálalo o verifica tu PATH.")
        return

    # 4. Ejecutar el programa C compilado
    print(f"\n🚀 Ejecutando el programa C compilado...\n")
    try:
        # Comando de ejecución: ./palabras_c
        comando_ejecucion = [f"./{NOMBRE_EJECUTABLE}"]
        # En Windows, a veces la ejecución requiere el nombre del ejecutable directamente
        if sys.platform == "win32":
             comando_ejecucion = [NOMBRE_EJECUTABLE]
        
        resultado_ejecucion = subprocess.run(
            comando_ejecucion, 
            capture_output=True, 
            text=True,
            check=True
        )
        print(resultado_ejecucion.stdout)
        print(f"✅ Ejecución del programa C finalizada.")

    except subprocess.CalledProcessError as e:
        print(f"❌ El programa C terminó con un error (código de salida {e.returncode}).")
        print(f"Error de salida:\n{e.stderr}")
    except FileNotFoundError:
        # Esto no debería pasar si la compilación fue exitosa
        print(f"❌ Error al ejecutar '{NOMBRE_EJECUTABLE}'. Archivo no encontrado.")

    # 5. Limpiar los archivos generados
    print("\n🧹 Limpiando archivos generados...")
    try:
        os.remove(NOMBRE_C)
        os.remove(NOMBRE_EJECUTABLE)
        print("✅ Archivos temporales eliminados.")
    except OSError as e:
        print(f"⚠️ Advertencia: No se pudieron eliminar los archivos '{e.filename}': {e.strerror}")

if __name__ == "__main__":
    ejecutar_programa_c()