def registro_lados():
    lados = []
    for i in range(4):
        lado = float(input(f"Ingresar el tamaño del lado {i+1}: "))
        lados.append(lado)
    return lados

def identificar_tipo(lados):
    l1, l2, l3, l4 = lados
    
    if l1 == l2== l3 == l4:
        return "cuadrado"
    elif (l1 == l2 and l3 == l4) or (l1 == l3 and l2 == l4) or (l1 == l4 and l2 == l3):
        return "rectángulo"
    else:
        return "algun otro cuadrilátero"
    
lados = registro_lados()
tipo = identificar_tipo(lados)
print("El cuadrilátero ingresado es:", tipo)