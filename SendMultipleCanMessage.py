import can


def multiple_send(msg, bus):
    task = bus.send_periodic(msg, 0.20)
    assert isinstance(task, can.CyclicSendTaskABC)

    return task


if __name__ == "__main__":
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
