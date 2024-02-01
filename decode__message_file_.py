# Función llamada decode(message_file) que lee un mensaje codificado desde un archivo de texto (.txt) y devuelve su versión 
# decodificada como una cadena de texto ordenando sus indices y escogiendo los datos a través de una resolución piramidal. 
# Es decir, si tenemos de indices 6, 5, 4, 3, 2, 1, los indices que devuelve son solo la esquina derecha y en orden: 1, 3, 6
# Test with "coding_qual_input.txt": 1 i, 3 love, 4 cosa, 6 computers, 5 es, 7 cosa, 9 ocho, 8 cosa, 10 and, 11 cosa, 12 cosa, 14 cosa, 13 catorce, 15 cats
# Goal: I love computers and cats

def decode(message_file):
    decoded_message = []

    with open(message_file, 'r') as file:
        lines = file.readlines()

        # Calcular la cantidad de líneas en la pirámide
        pyramid_height = int((8 * len(lines) + 1)**0.5 / 2 - 0.5)

        # Obtener y ordenar las líneas del archivo según los índices
        sorted_lines = sorted(lines, key=lambda x: int(x.split()[0]))

        # Obtener la esquina derecha de la pirámide
        corner_indices = [i * (i + 1) // 2 for i in range(1, pyramid_height + 1)]
        
        # Procesar las líneas en orden piramidal
        for i, line in enumerate(sorted_lines):
            if i + 1 in corner_indices:
                # Obtener la palabra de la línea
                word = line.split()[-1]
                decoded_message.append(word)

    return ' '.join(decoded_message)

# Llamar a la función desde el programa principal
if __name__ == "__main__":
    decoded_message = decode("coding_qual_input.txt")
    print("Decoded Message:", decoded_message)
