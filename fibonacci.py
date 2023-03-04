n = int(input("Informe um numero: "))
ultimo=1
penultimo=0


if (n<3):
    print(f"{n} pertence a sequencia")
else:
    termo=0
    while termo < n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
    
    if(termo==n):
        print(f"{n} pertence a sequencia")
    else:
        print(f"{n} nao pertence a sequencia")
