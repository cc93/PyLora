import PyLora
import time
PyLora.init()
PyLora.set_frequency(433000000)
PyLora.enable_crc()
while True:
    PyLora.send_packet('Hello World')
    print 'Packet sent...'
    time.sleep(2)
