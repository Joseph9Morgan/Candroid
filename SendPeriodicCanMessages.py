import can
import time


def send_periodic(msg, bus):
    try:
        # send periodic message every n seconds
        task = bus.send_periodic(msg, 1)
        assert isinstance(task, can.CyclicSendTaskABC)
        return task
        print("Message was sent on {}".format(bus.channel_info))

        # while True:
        #     message = bus.recv()
        #     print(message)

        #     if (message.arbitration_id == 0x01):
        #         msg = can.Message(arbitration_id=0x02, data=[
        #                           1, 57, 17, 13, 31], is_extended_id=False)
        #         bus.send(msg)
        time.sleep(10)
    except can.CanError:
        print("Message was not sent properly")


if __name__ == '__main__':
    msg = can.Message(arbitration_id=0xfee, data=[
                      1, 5, 3, 76, 34, 83, 31], is_extended_id=False)
    bus = can.interface.Bus(bustype='vector', channel=1,
                            bitrate=500000, app_name='python-can')
    tasks = []
    tasks.append(send_periodic(msg,bus))

