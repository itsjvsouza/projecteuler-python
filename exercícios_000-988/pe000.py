#Dentre os primeiros 945 mil números quadrados, qual é a soma de todos os quadrados ímpares?

vezes = 1
resultado = 1
total = 1

while vezes < 472500:
    
    resultado = resultado + (8 * vezes)
    total =  total + resultado
    vezes += 1

print(total)
