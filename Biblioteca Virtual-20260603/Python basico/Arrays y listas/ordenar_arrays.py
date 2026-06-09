desorden = [10, 8, 25, 12, 79, 1, 4, 62]

          # Vuelta 1  [8, 10, 12, 25, 1, 4, 62, 79]

          # Vuelta 2  [8, 10, 12, 1, 4, 25, 62, 79]

          # Vuelta 3  [8, 10, 1, 4, 12, 25, 62, 79]

          # Vuelta 4  [8, 1, 4, 10, 12, 25, 62, 79]

          # Vuelta 5  [1, 4, 8, 10, 12, 25, 62, 79]

          # Vuelta 6  [1, 4, 8, 10, 12, 25, 62, 79]
          
print(desorden)

ordenado = desorden

orden = False
while (orden == False):
    orden = True
    indice = 0
    while (indice < len(ordenado)-1):

        if (ordenado[indice] < ordenado[indice+1]):
            apoyo =  ordenado[indice]
            ordenado[indice] = ordenado[indice+1]
            ordenado[indice+1] = apoyo
            orden = False
        
        indice = indice + 1

print(ordenado)






