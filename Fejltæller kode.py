import serial

def read_data_from_arduino():

    serial_port = serial.Serial(port='COM5', baudrate=38400, timeout=1)  # Tilpas port og baudrate efter behov

    data = []
    errors = 0
    last_value = None

    while len(data) < 4000:
        line = serial_port.readline().decode().strip()  # Læs en linje fra Arduinoen
        try:
            value = int(line)
            print(value)
            if value == last_value:
                errors += 1

            data.append(value)
            last_value = value
        except ValueError:
            pass  # Håndter fejl i dataformat

    if errors > 0:
        print(f"Der opstod {errors} fejl i data.")
    else:
        print("der er ingen fejl i koden")

    return data

# Kør funktionen for at læse data fra Arduinoen
arduino_data = read_data_from_arduino()
