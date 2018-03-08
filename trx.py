import PyLora
import time
PyLora.init()
PyLora.set_frequency(433000000)
PyLora.enable_crc()
while True:
    PyLora.receive()   # put into receive mode
    while not PyLora.packet_available():
        # wait for a package
        time.sleep(0)
    rec = PyLora.receive_packet()
    print 'Packet received: {}'.format(rec)
