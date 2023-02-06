# Escribe un script que sume todos los números de una cadena de texto pasada por parámetros.

def clean_word(word):
    cleaned = "".join(filter(lambda char: char.isdigit(), word))
    
    # Negative numbers
    if len(word) > 1 and word[0] == '-' and word[1].isdigit():
        return '-'+cleaned

    return cleaned

def sum_string(input_str):

    if not isinstance(input_str, str):
        return None 

    word_list = input_str.split(" ")
    acc = 0
    for word in word_list:
        cleaned = clean_word(word)
        if cleaned:
            acc += int(cleaned)

    return acc

if __name__ == '__main__':
    input_string_list = ["Frogtek se fundó en 2010 y ahora tiene 40 empleados", 
                         "Frogtek desarrolla un software para la gestión de tiendas de barrio", 
                         "[]", 9, "-50€ + 30€ es una operación"
                        ]

    for input_string in input_string_list:
        print(f"La suma de la cadena -> {input_string} es -> {sum_string(input_string)}")
