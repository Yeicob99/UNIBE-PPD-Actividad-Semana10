texto = """
hadoop es poderoso hadoop es útil
big data es el futuro
"""

# --- Mapper ---
def mapper(texto):
    resultado = []
    for linea in texto.strip().split('\n'):
        for palabra in linea.strip().split():
            resultado.append((palabra, 1))
    return resultado

# --- Shuffle (agrupación) ---
from collections import defaultdict
def shuffle(mapped_data):
    shuf = defaultdict(list)
    for palabra, count in mapped_data:
        shuf[palabra].append(count)
    return shuf

# --- Reducer ---
def reducer(shuffled_data):
    output = {}
    for palabra, counts in shuffled_data.items():
        output[palabra] = sum(counts)
    return output

# --- Ejecutar ---
mapped = mapper(texto)
shuffled = shuffle(mapped)
reduced = reducer(shuffled)

for palabra, total in reduced.items():
    print(f"{palabra}: {total}")
