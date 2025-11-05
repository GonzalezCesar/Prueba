# 🧩 Prueba Diagnóstica — Lenguajes y Compiladores

**Universidad Nacional Experimental de Guayana**  
**Vicerrectorado Académico — Ingeniería en Informática**  
**Profesor:** Msc. Félix Márquez  
**Periodo:** 2025-II  

---

## 📘 Descripción General

Este repositorio contiene la solución completa a la **Prueba Diagnóstica** del curso **Lenguajes y Compiladores**.  
Cada ejercicio fue implementado en **Python**, siguiendo las instrucciones del enunciado original.  
Se incluyen scripts funcionales, salidas de ejemplo y medición de tiempos cuando aplica.

---

## 📁 Estructura del Repositorio

```
.
├── Problema1/
│   ├── problema1.py
│   ├── ejemplo.txt
│   └── salida.txt
│
├── Problema2/
│   ├── problema2.py
│   ├── problem2_output_n100.txt
│   └── README.md
│
├── Problema3/
│   ├── problema3.py
│   ├── problema3_resultado.txt
│   └── ejemplos.txt
│
├── Problema4/
│   ├── problema4.py
│   ├── problema4_resultado.txt
│   └── ejemplo_codigo.c
│
└── README.md   ← (este archivo)
```

---

## 🚀 Instrucciones de Ejecución

Cada script puede ejecutarse directamente desde terminal o entorno Python 3.

### 🔹 Requisitos previos

- Python **3.9 o superior**
- Librerías estándar (`re`, `math`, `time`, `pathlib`, `PyPDF2` solo si se analiza el PDF original)

Instalación recomendada:
```bash
sudo apt install python3
```

---

## 🧠 Descripción de los Problemas

### 🟩 **Problema 1 – Validación de notación FEN**

**Enunciado:**  
Dada una cadena `C`, validar si se encuentra en notación **FEN (Forsyth–Edwards Notation)** utilizada en ajedrez.

**Solución:**  
Se implementó un validador con expresiones regulares que verifica:
- 8 filas separadas por `/`
- Turno (`w` o `b`)
- Enroques (`KQkq` o `-`)
- Posición al paso (`a3`, `h6`, o `-`)
- Contadores de jugada

**Ejecución:**
```bash
python3 problema1.py
```

**Ejemplo de salida:**
```
"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" → VÁLIDA
"hola mundo" → INVÁLIDA
```

---

### 🟨 **Problema 2 – Generación y evaluación del polinomio (x+1)^n**

**Enunciado:**  
Dado un número entero no negativo `n`, generar los coeficientes del polinomio `(x+1)^n` usando el **triángulo de Pascal**, evaluar `f(x)` y medir tiempos.

**Solución:**
- Se usan listas dinámicas (`list`) para los coeficientes.
- Se mide el tiempo de generación y evaluación con `time.perf_counter()`.
- Se guarda todo en un archivo `.txt`.

**Ejecución:**
```bash
python3 problema2.py
```

**Ejemplo de salida:**
```
n = 100, x = 2
Resultado: f(2) = 515377520732011331036461129765621272702107522001
Tiempos -> generación: 0.043 ms, evaluación: 0.069 ms
Archivo guardado: problem2_output_n100.txt
```

---

### 🟦 **Problema 3 – Reconocimiento de cadenas y patrones**

**Enunciado:**  
Implementar reconocimiento de:
- Cadenas
- Números en notación científica
- Direcciones IP
- Correos electrónicos

**Solución:**
Uso de expresiones regulares (`re.findall`) para cada tipo de patrón, guardando los resultados en un archivo de texto.

**Ejecución:**
```bash
python3 problema3.py
```

**Ejemplo de salida:**
```
Cadenas: ['servidor', 'principal', 'Contacto', 'Valores']
Científicos: ['3.4e-5', '-2E10']
IPs: ['192.168.1.10', '10.0.0.5']
Emails: ['soporte@example.com', 'admin@miweb.org']
```

---

### 🟥 **Problema 4 – Traducción de palabras reservadas en C**

**Enunciado:**  
Analizar un código fuente en C y traducir sus **palabras reservadas** al **español**.

**Solución:**
- Se lee el texto del código.
- Se buscan tokens con `re.findall(r'\b[a-zA-Z_]+\b')`.
- Se compara con un diccionario de 32 palabras reservadas de C.
- Se genera un archivo con las traducciones encontradas.

**Ejecución:**
```bash
python3 problema4.py
```

**Ejemplo de salida:**
```
int → entero
if → si
else → si no
return → retornar / devolver
Archivo guardado: problema4_resultado.txt
```

---

## 🧾 Créditos

**Autor:** *Cesar Alejandro Abache González*  
**Materia:** Lenguajes y Compiladores  
**Profesor:** Msc. Félix Márquez  
**Año:** 2025-II  

---

## 🧩 Licencia
Proyecto académico libre de uso educativo.  
Puedes modificar o reutilizar los scripts citando la fuente.

---
