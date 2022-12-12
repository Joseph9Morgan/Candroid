import can
from can import Message
test = Message(data=[1, 43, 6, 4, 6, 45, 6, 3])
print(test)
print(Message(is_extended_id=False,
      arbitration_id=100, data=[3, 6, 5, 89, 65]))


bus = can.interface.Bus(bustype='vector', channel=1,
                        bitrate=500000, app_name='python-can')


def send_one():

    msg = can.Message(arbitration_id=0x01, data=[
                      1, 5, 3, 76, 34, 83, 31], is_extended_id=False)

    try:
        bus.send(msg)
        print("Message was sent on {}".format(bus.channel_info))
    except can.CanError:
        print("Message was not sent properly")


if __name__ == '__main__':
    send_one()
