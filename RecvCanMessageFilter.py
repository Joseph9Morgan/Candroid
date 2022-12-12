import can
bus = can.interface.Bus(bustype='vector', channel=1,
                        bitrate=500000, app_name='python-can')
while True:
    recv_message = bus.recv(timeout=1)
    if recv_message != None:
        print('Received message : %s' % recv_message)