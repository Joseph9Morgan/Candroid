import can
from can import Message
from argparse import ArgumentParser, Namespace
import os
import time 


def test():
    print("The test message is sent as %s:" % Message(is_extended_id=False,
                                                      arbitration_id=0xa1, data=[1, 43, 6, 4, 6, 45, 6, 3]))
    bus = can.interface.Bus(bustype='vector', channel=1,
                            bitrate=500000, app_name='python-can')
    while True:
        msg = can.Message(arbitration_id=0xa1, data=[1, 43, 6, 4, 6, 45, 6, 3])
        bus.send(msg)
        time.sleep(1)


def send_one(arbitration_id, data):

    msg = can.Message(arbitration_id=args.arb, data=[
                      1, 5, 3, 76, 34, 83, 31], is_extended_id=False)

    try:
        bus.send(msg)
        print("Message was sent on {}".format(bus.channel_info))
    except can.CanError:
        print("Message was not sent properly")


def recv_message():
    bus = can.interface.Bus(bustype='vector', channel=1,
                            bitrate=500000, app_name='python-can')
    print("Message is now being received:")
    while True:
        recv_message = bus.recv(timeout=1)
        if recv_message != None:
            print('Received message : %s' % recv_message)


def read_blf_file(filename):
    # filename = "2022-11-09-16-19-09.blf"
    can_log = can.BLFReader(filename)
    for msg in can_log:
        print(msg)


def multiple_send(msg, bus):
    task = bus.send_periodic(msg, 0.20)
    assert isinstance(task, can.CyclicSendTaskABC)
    bus = can.interface.Bus(bustype='vector', channel=1,
                            bitrate=500000, app_name='python-can')
    can_ids = [
        0x01, 0x02, 0x03, 0x04, 0x05, 0x06,
        0x07, 0x08, 0x08, 0x10
    ]
    tasks = []

    for can_id in can_ids:
        msg_volt = can.Message(arbitration_id=can_id,
                               data=[1, 0, 50, 0, 0, 4, 0, 0],
                               is_extended_id=False)
        tasks.append(multiple_send(msg_volt, bus))
        msg_temp = can.Message(arbitration_id=can_id,
                               data=[2, 0, 0, 0, 40, 0, 20, 0],
                               is_extended_id=False)
        tasks.append(multiple_send(msg_temp, bus))

    time.sleep(200)
    return task


def send_periodic(msg, bus):
    try:
        # send periodic message every n seconds
        task = bus.send_periodic(msg, 1)
        assert isinstance(task, can.CyclicSendTaskABC)

        print("Message was sent on {}".format(bus.channel_info))
        msg = can.Message(arbitration_id=0xfee, data=[
            1, 5, 3, 76, 34, 83, 31], is_extended_id=False)
        bus = can.interface.Bus(bustype='vector', channel=1,
                                bitrate=500000, app_name='python-can')
        tasks = []
        tasks.append(send_periodic(msg, bus))
        # while True:
        #     message = bus.recv()
        #     print(message)

        #     if (message.arbitration_id == 0x01):
        #         msg = can.Message(arbitration_id=0x02, data=[
        #                           1, 57, 17, 13, 31], is_extended_id=False)
        #         bus.send(msg)
        time.sleep(10)
        return task
    except can.CanError:
        print("Message was not sent properly")


def main(args: Namespace):
    if not os.path.exists(args.o):
        os.mkdir(args.o)    # create output_dir if not exist
    ##Note that we should check virtual/real device connectivity before parsering the data. Lack prior check!!


if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument('-t', '--test', action='store_true',
                    help="send a test message")
    ap.add_argument('-r', '--recv', action='store_true',
                    help="start receiving messages")
    ap.add_argument('-a', '--arbitration_id', type=int,
                    dest='arbitration_id', help="assign msg.arbitration_id")
    ap.add_argument('-d', '--data',  type=bytearray, dest='data',
                    default=False, help="assign msg.data")
    ap.add_argument('-so', '--send_one', action='store_true',
                    help="send one can message")
    ap.add_argument('-rblf', '--read_blf_file',
                    action='store_true', help="read .blf file")
    ap.add_argument('-o', default = False, help="output dir")
    # ap.add_argument('', '', action='store_true', type=, dest=, default=False, help="")
    ap.add_argument('-v', '--verbose', action='store_true',
                    help="print verbose")
    args = ap.parse_args()

    if args.test:
        test()
    if args.recv:
        recv_message()
    if args.read_blf_file:
        print("%s blf file is parsed as:" % args.filename)
        read_blf_file()
