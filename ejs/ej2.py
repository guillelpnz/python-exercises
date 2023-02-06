# Escribe un script que borre los ceros por la izquierda de una dirección IP pasada por parámetros.
from socket import socket
    
def valid_address(address):
    if not isinstance(address, str):
        return False

    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False

    return True

def delete_zeros(input_ip_address):
    if not valid_address(input_ip_address):
        return

    return ".".join(map(lambda group: str(int(group)), input_ip_address.split('.')))

if __name__ == '__main__':
    input_string_list = ["Invalid string", "210.010.090.180", 9, ""]

    for input_string in input_string_list:
        print(f"La direccion sin ceros de -> {input_string} es -> {delete_zeros(input_string)}")