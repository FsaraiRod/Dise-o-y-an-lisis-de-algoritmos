unidades = ['','uno', 'dos', 'tres', 'cuatro', 'cinco', 'seís', 'siete', 'ocho', 'nueve']
decenas_1 = ['', 'díez', 'veinte', 'treita', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
decenas_2 = ['', 'once', 'doce', 'trece', 'catrorce', 'quince', 'dieciseis', 'diecisiete', 'dieciocho', 'diecinueve']
centenas =  ['', 'cien', 'docientos', 'trecientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']

def conversor(numero):
    if numero == 0:
        return 'cero'
    
    if numero < 10:
        return unidades[numero]
    
    if numero < 20:
        return decenas_2[numero-10]
    
    if numero < 100:
        decena = numero//10
        unidad = numero%10
        if unidad == 0:
            return decenas_1[decena]
        elif decena != 2 and unidad != 0:
            return decenas_1[decena] + " y " + unidades[unidad]
        else:
            return 'veinti'+unidades[unidad]
    
    if numero < 1000:
        centena = numero // 100
        residuo = numero % 100
        if residuo == 0:
            return centenas[centena]
        if centena == 1 and residuo !=0:
            return 'ciento' + ' ' + conversor(residuo)
        else:
            return centenas[centena] + ' ' + conversor(residuo)
        
    if numero <1000000:
        milesima = numero // 1000
        residuo = numero % 1000
        if residuo == 0:
            if milesima == 1:
                return ' mil '
            else:
                return conversor(milesima)+ ' mil '
        else:
            if milesima == 1:
                return ' mil ' +conversor(residuo)
            else:
                return conversor(milesima)+ ' mil ' + conversor(residuo)
    
    if numero < 1000000000:
        millonesima = numero // 1000000
        residuo = numero % 1000000
        if residuo == 0:
            if millonesima == 1:
                return 'un millon'
            else:
                return conversor(millonesima) + ' millones'
        else:
            if millonesima == 1:
                return 'un millon '+ conversor(residuo)
            else:
                return conversor(millonesima) + ' millones '+ conversor(residuo)
            
    if numero < 1000000000000:
        billonesima = numero // 1000000000
        residuo = numero % 1000000000
        if residuo == 0:
            if billonesima == 1:
                return 'un billon'
            else:
                return conversor(billonesima) + ' billones'
        else:
            if billonesima == 1:
                return 'un billon '+ conversor(residuo)
            else:
                return conversor(billonesima) + ' billones '+ conversor(residuo)
        
    if numero < 1000000000000000:
        trillonesima = numero // 1000000000000
        residuo = numero % 1000000000000
        if residuo == 0:
            if trillonesima == 1:
                return 'un trillon'
            else:
                return conversor(trillonesima) + ' trillones'
        else:
            if trillonesima == 1:
                return 'un trillon '+ conversor(residuo)
            else:
                return conversor(trillonesima) + ' trillones '+ conversor(residuo)

        

numero= int(input("Ingresar número en digitos:"))
print(conversor(numero))