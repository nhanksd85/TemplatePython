import struct
import serial

class Modbus485:
    def __init__(self, _rs485):
        self.rs485 = _rs485
        return

    def modbus485_send(self, data):
        ser = self.rs485
        self.modbus485_clear_buffer()
        try:
            ser.write(serial.to_bytes(data))
        except:
            print("Modbus485**","Failed to write data")
            return 0
        return

    def modbus485_read(self):
        return
    def modbus485_clear_buffer(self):
        ser = self.rs485
        bytesToRead = ser.inWaiting()
        if bytesToRead > 0:
            out = ser.read(bytesToRead)
            print("Buffer: ", out)

    def modbus485_read_big_endian(self):
        ser = self.rs485
        bytesToRead = ser.inWaiting()
        return_array = [0, 0, 0, 0]
        if bytesToRead > 0:
            out = ser.read(bytesToRead)
            data_array = [b for b in out]
            print(data_array)

            if len(data_array) >= 7:

                return_array[0] = data_array[5]
                return_array[1] = data_array[6]
                return_array[2] = data_array[3]
                return_array[3] = data_array[4]
                print("Modbus485**","Raw Data: ",  return_array)

                [value] = struct.unpack('>f',bytearray(return_array))
                return value
            else:
                return 400
        return 404