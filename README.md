<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Lexer para Dockerfile - Analizador Léxico con Expresiones Regulares

[ [

## 📋 Descripción

**Lexer implementado para la asignatura *Lenguaje y Compiladores* (UNEG)** que analiza archivos **Dockerfile** y los convierte en una secuencia de **tokens** usando expresiones regulares. Detecta instrucciones Docker (`FROM`, `RUN`, `COPY`, etc.), rutas, nombres de imagen, identificadores y reporta **errores léxicos**.

### 🎯 Objetivo Académico

Respuesta a la **Pregunta 2** del Tema 4: "Construya un lexer para la verificación de archivos Docker mediante expresiones regulares".

## 🚀 Características

- ✅ **Tokenización completa** de Dockerfile
- ✅ **Detección de errores léxicos** (`MISMATCH`)
- ✅ **Ignora comentarios** (`#...`) y espacios
- ✅ **Reporta línea y columna** de cada token
- ✅ **Ejemplos de prueba** incluidos


## 🛠️ Requisitos

```bash
Python 3.8 o superior (incluye `re` por defecto)
```

**¡NO requiere instalación adicional!**

## 📦 Instalación

1. **Clona el repositorio:**
```bash
git clone https://github.com/tuusuario/dockerfile-lexer.git
cd dockerfile-lexer
```

2. **¡Ya está listo!** No necesita `pip install`

## ▶️ Uso

### Ejecución básica:

```bash
python3 docker_lexer.py
```


### Analizar otro archivo:

```bash
# Edita docker_lexer.py y cambia la línea:
nombre_archivo = "mi_dockerfile.txt"
python3 docker_lexer.py
```


## 📊 Ejemplo de Salida

**Dockerfile de prueba:**

```dockerfile
FROM ubuntu:20.04
RUN apt-get update
WORKDIR /app
# Comentario ignorado
COPY . /app
```

**Salida del lexer:**

```
(FROM, 'FROM', línea 1, col 0)
(IMAGE_NAME, 'ubuntu:20.04', línea 1, col 5)
(RUN, 'RUN', línea 2, col 0)
(IDENT, 'apt-get', línea 2, col 4)
(IDENT, 'update', línea 2, col 12)
(WORKDIR, 'WORKDIR', línea 3, col 0)
(PATH, '/app', línea 3, col 8)
(COPY, 'COPY', línea 5, col 0)
(PATH, '.', línea 5, col 5)
(PATH, '/app', línea 5, col 8)
```


## 🧪 Pruebas de Error Léxico

**Dockerfile con error:**

```dockerfile
FORM ubuntu:20.04  # ERROR: FORM no es instrucción válida
RUN apt-get update
```

**Detecta correctamente:**

```
❌ ERROR LÉXICO: Carácter inesperado en línea 1
```


## 🏗️ Estructura del Proyecto

```
dockerfile-lexer/
├── docker_lexer.py     # Lexer principal
├── Dockerfile          # Ejemplo de prueba (VÁLIDO)
├── Dockerfile_error    # Ejemplo con error léxico
├── README.md          # 👈 Este archivo
└── tests/             # Archivos adicionales de prueba
```


## 🔍 Cómo Funciona (Teoría → Práctica)

### 1. **Definición de Tokens**

Lista de 15 tokens con expresiones regulares específicas:

```
('FROM', r'\bFROM\b')           # Instrucción Docker
('PATH', r'^[/][a-zA-Z0-9._/-]+') # Rutas absolutas
('IDENT', r'[a-zA-Z_][a-zA-Z0-9_]*') # Comandos shell
```


### 2. **Expresión Regular Global**

```python
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in tokens)
```


### 3. **Algoritmo de Tokenización**

- Recorre carácter por carácter con `re.finditer()`
- Ignora `SKIP` (espacios) y `COMMENT` (\#...)
- Reporta **línea y columna** exacta
- `MISMATCH` → **Error léxico**


## 🎓 Tokens Reconocidos

| Token | Ejemplo | Regex |
| :-- | :-- | :-- |
| `FROM` | `FROM` | `\bFROM\b` |
| `PATH` | `/app` | `^[/][a-zA-Z0-9._/-]+` |
| `IMAGE_NAME` | `ubuntu:20.04` | `[a-zA-Z0-9][a-zA-Z0-9._]*(:[a-zA-Z0-9._-]*)?` |
| `IDENT` | `apt-get` | `[a-zA-Z_][a-zA-Z0-9_]*` |
| `STRING` | `["bash"]` | `"[^"]*"|\[.*\]` |

## 📝 Para la Defensa

**Diapositiva recomendada:**

```
Lexer Dockerfile → 3 Ejemplos ejecutados ✅
1. FROM ubuntu:20.04 → (FROM, IMAGE_NAME)
2. WORKDIR /app → (WORKDIR, PATH)
3. FORM ubuntu → ERROR LÉXICO detectado
```


## 🤝 Contribuidores

- **César** - Implementación principal
- **UNEG** - Asignatura Lenguaje y Compiladores


## 📄 Licencia

Proyecto académico - Uso educativo

## 🙏 Agradecimientos

- **Msc. Félix Márquez** - Docente UNEG
- **Tema 4** - Material teórico de autómatas y regex

***

**¡Ejecuta `python3 docker_lexer.py` y listo!** 🚀

<p align="center">
  <img src="https://img.shields.io/badge/UNEG-Lenguajes%20y%20Compiladores-orange" alt="UNEG">
</p>
