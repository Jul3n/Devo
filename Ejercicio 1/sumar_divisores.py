def sumar_divisores(pX):
    #Precondición: Todos los números de pX serán enteros positivos. Si son negativos se realizará el cálculo en |pX| (Valor absoluto).
    #Postcondición: Se ha devuelto la suma de sus divisores bajo la siguiente premisa: 
        #SUMA > pX: No seguimos puesto que ya está confirmado que es ABUNDANTE.
        #SUMA <= pX: Hemos llegado a pX/2 (todos los divisores de X estarás siempre entre 1 y X/2) sin que SUMA exceda pX (PERFECTO o DEFECTIVO).
    
    if pX < 0: #Si el valor en negativo lo calcularemos en valor absoluto.
        pX = pX*-1
    if (pX==1): #Si pX es 1 no hacemos nada ya que, por definición, el resultado solo será 1.
        return 1
    else:
        div=1 #Inicializamos el divisor a uno.
        x=pX #Realizamos una copia del parámetro para no perder el valor.
        suma=0 #Inicializamos la suma a cero.
        #Mientras (la suma sea menor o igual al parámetro que nos pasan) y (el divisor con el que trabajamos este entre 1 y X/2) seguimos.
        while (suma <= x) and (div <=(x/2)): 
            if (x % div == 0): #Si el resto es cero, el divisor nos vale para sumarlo.
                suma = suma + div #Suma de los divisores.
            div = div +1 #Pasamos al siguiente divisor.
        return suma #Devolvemos el restultado de la suma.
