# WordCount MapReduce en Python

Este proyecto simula el modelo de programación MapReduce usando Python para realizar un conteo de palabras (WordCount). Hecho en google colab

## Archivos principales
- `wordcount-mapreduce.py`: Código en Python separado por funciones 

## Flujo implementado

1. **Mapper**: emite (palabra, 1)
2. **Shuffle**: agrupa las palabras iguales
3. **Reducer**: suma las repeticiones de cada palabra

## Resultado de ejemplo

hadoop: 2
es: 3
poderoso: 1
útil: 1
big: 1
data: 1
el: 1
futuro: 1
