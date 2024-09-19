#Para concatenar o combinar dos cadenas se utiliza el operador +.
text1 = "Fundamentos con "
text2 = "Python"
result = text1 + text2
print(result)


#ejemplo
name = "Luis"
lastName = "Jimenez"
fullName = name + " " + lastName
print(fullName)


#Mostrar el precio de un producto con dos decimales,Se agrega dos puntos : seguido de un tipo de formato .2f
price = 97
text3 = f"The price is {price: .2f} dollars"
print(text3)


#Realizar operaciones matemáticas dentro de una cadena
text4 = f"La multiplcacion es {20 * 59}"
print(text4)


#cambia la primera letra a mayuscula
text5 = "python es un lenguaje de alto nivel de programacion"
result =text5.capitalize()
print(result)


#cambia la primera letra a minuscula
title = "Cien años de soledad"
titleConvert = title.casefold()
print(titleConvert)


#Agrega caracteres ocupando los espacios establecidos
fruit = "banana"
textCenter = fruit.center(  20, "-")
print(textCenter)


#Devuelve el número de veces que aparece un valor en la cadena.
title1 =  "I love apples, apple are my favorite fruit "
result2 = title1.count("apple")
print(result2)


#Función que comprueba si la cadena termina con un signo de puntuación (.).
text6 = "Curso, fundamentos con Python."
result3 = text6.endswith(".")
print(result3)


#La función establece el tamaño de tabulaciones en la cantidad especificada de espacios en blanco.
letter = "F\tU\tP"
letterSpaces = letter.expandtabs(2)
print(letterSpaces)


#Esta función encuentra la primera aparición del valor especificado.
text7 = "Hola, bienvenidos a Colombia."
result4 = text7.find("bienvenidos")
print(result4)


#Esta función escribe en mayúscula la primera letra de cada palabra
text8 = "welcome to my world"
result5 = text8.title()
print(result5)


#Esta función devuelve Verdadero si todos los caracteres de la cadena son alfanuméricos.
alphanumeric = "Pythom321"
result6 = alphanumeric.isalnum()
print(result6)


#Esta función devuelve Verdadero si todos los caracteres de la cadena están en el alfabeto.
letters = "Space X"
result7 = letters.isalpha()
print(result7)




