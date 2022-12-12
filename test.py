##print ("hello this is the initial project for a whole lots of things for can")

import can
from can import Message
test = Message(data=[1, 43, 6, 4, 6, 45, 6, 3])
print(test)
print(Message(is_extended_id=False,
      arbitration_id=100, data=[3, 6, 5, 89, 65]))

bus = can.interface.Bus(bustype='vector', channel=1,
                        bitrate=500000, app_name='python-can')
msg = can.Message(arbitration_id=0xa1, data=[1, 43, 6, 4, 6, 45, 6, 3])
bus.send(msg)
