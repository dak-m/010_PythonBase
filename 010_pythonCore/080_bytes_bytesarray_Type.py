# bytes относится к неизменяемым последователностям
# bytesarray относится к изменяемым последователностям

tobytes = (256 ** 2 - 2).to_bytes(4, byteorder='big')  # число в байты
frombytes = int.from_bytes(tobytes, byteorder='big')  # число из байтов

ba = bytearray(b'qwerty')
ba[0] = ord('s')

