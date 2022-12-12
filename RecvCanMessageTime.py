# import can
# bus = can.interface.Bus(bustype='vector', channel=1,
#                         bitrate=500000, app_name='python-can')
# while True:
#     recv_message = bus.recv(timeout=1)
#     if recv_message != None:
#         print('Received message : %s' % recv_message)



import can
bus = can.interface.Bus(bustype='TOSUN', channel=1,
                        bitrate=500000, app_name='python-can')
while True:
    recv_message = bus.recv(timeout=1)
    if recv_message != None:
        print('Received message : %s' % recv_message)


socketcan
serial
slcan
usb2can



# PS E:\python can related\python-can-project> python .\RecvCanMessageTime.py  
# Traceback (most recent call last):
#   File "E:\python\lib\site-packages\can\interfaces\usb2can\usb2canabstractionlayer.py", line 119, in __init__
#     self.__m_dllBasic = windll.LoadLibrary(dll)
#   File "E:\python\lib\ctypes\__init__.py", line 452, in LoadLibrary
#     return self._dlltype(name)
#   File "E:\python\lib\ctypes\__init__.py", line 374, in __init__
# FileNotFoundError: Could not find module 'usb2can.dll' (or one of its dependencies). Try using the full path with constructor syntax.

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "E:\python can related\python-can-project\RecvCanMessageTime.py", line 12, in <module>
#     bus = can.interface.Bus(bustype='usb2can', channel=1,
#   File "E:\python\lib\site-packages\can\interface.py", line 120, in __new__
#     bus = cls(channel, *args, **kwargs)
#   File "E:\python\lib\site-packages\can\interfaces\usb2can\usb2canInterface.py", line 102, in __init__
#     self.can = Usb2CanAbstractionLayer(dll)
#   File "E:\python\lib\site-packages\can\interfaces\usb2can\usb2canabstractionlayer.py", line 125, in __init__
#     raise can.CanInterfaceNotImplementedError(message) from error
# can.exceptions.CanInterfaceNotImplementedError: DLL failed to load at path: usb2can.dll
# PS E:\python can related\python-can-project> python .\RecvCanMessageTime.py
# Traceback (most recent call last):
#   File "E:\python\lib\site-packages\can\interfaces\usb2can\usb2canabstractionlayer.py", line 119, in __init__
#     self.__m_dllBasic = windll.LoadLibrary(dll)
#   File "E:\python\lib\ctypes\__init__.py", line 452, in LoadLibrary
#     return self._dlltype(name)
#   File "E:\python\lib\ctypes\__init__.py", line 374, in __init__
# FileNotFoundError: Could not find module 'usb2can.dll' (or one of its dependencies). Try using the full path with constructor syntax.

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "E:\python can related\python-can-project\RecvCanMessageTime.py", line 12, in <module>
#     bus = can.interface.Bus(bustype='usb2can', channel='6D3C640E7D7D',
#   File "E:\python\lib\site-packages\can\interface.py", line 120, in __new__
#     bus = cls(channel, *args, **kwargs)
#     self.can = Usb2CanAbstractionLayer(dll)
#   File "E:\python\lib\site-packages\can\interfaces\usb2can\usb2canabstractionlayer.py", line 125, in __init__
#     raise can.CanInterfaceNotImplementedError(message) from error
# can.exceptions.CanInterfaceNotImplementedError: DLL failed to load at path: usb2can.dll
# PS E:\python can related\python-can-project> python .\RecvCanMessageTime.py
# You won't be able to use the serial can backend without the serial module installed!
# Traceback (most recent call last):
#   File "E:\python can related\python-can-project\RecvCanMessageTime.py", line 12, in <module>
#     bus = can.interface.Bus(bustype='serial', channel='6D3C640E7D7D',
#   File "E:\python\lib\site-packages\can\interface.py", line 120, in __new__
#     bus = cls(channel, *args, **kwargs)
#   File "E:\python\lib\site-packages\can\interfaces\serial\serial_can.py", line 81, in __init__
#     raise CanInterfaceNotImplementedError("the serial module is not installed")
# can.exceptions.CanInterfaceNotImplementedError: the serial module is not installed
# PS E:\python can related\python-can-project> python .\RecvCanMessageTime.py
# fcntl not available on this platform
# socket.CMSG_SPACE not available on this platform
# Traceback (most recent call last):
#   File "E:\python can related\python-can-project\RecvCanMessageTime.py", line 12, in <module>
# fcntl not available on this platform
# socket.CMSG_SPACE not available on this platform
# Traceback (most recent call last):
#   File "E:\python can related\python-can-project\RecvCanMessageTime.py", line 12, in <module>
#     bus = can.interface.Bus(bustype='socketcan', channel='6D3C640E7D7D',
#   File "E:\python\lib\site-packages\can\interface.py", line 120, in __new__
#     bus = cls(channel, *args, **kwargs)
#   File "E:\python\lib\site-packages\can\interfaces\socketcan\socketcan.py", line 646, in __init__
#     self.socket = create_socket()
#     sock = socket.socket(PF_CAN, socket.SOCK_RAW, CAN_RAW)
#   File "E:\python\lib\socket.py", line 232, in __init__
#     _socket.socket.__init__(self, family, type, proto, fileno)
# OSError: [WinError 10047] 使用了与请求的协议不兼容的地址。
# PS E:\python can related\python-can-project> python .\RecvCanMessageTime.py
# You won't be able to use the serial can backend without the serial module installed!
# Traceback (most recent call last):
#   File "E:\python can related\python-can-project\RecvCanMessageTime.py", line 12, in <module>
#     bus = can.interface.Bus(bustype='serial', channel='6D3C640E7D7D',
#   File "E:\python\lib\site-packages\can\interface.py", line 120, in __new__
#     bus = cls(channel, *args, **kwargs)
#   File "E:\python\lib\site-packages\can\interfaces\serial\serial_can.py", line 81, in __init__
#     raise CanInterfaceNotImplementedError("the serial module is not installed")
# can.exceptions.CanInterfaceNotImplementedError: the serial module is not installed
# PS E:\python can related\python-can-project> python .\RecvCanMessageTime.py
# You won't be able to use the slcan can backend without the serial module installed!
# Traceback (most recent call last):
#   File "E:\python can related\python-can-project\RecvCanMessageTime.py", line 12, in <module>
#     bus = can.interface.Bus(bustype='slcan', channel='6D3C640E7D7D',
#   File "E:\python\lib\site-packages\can\interface.py", line 120, in __new__
#     bus = cls(channel, *args, **kwargs)
#   File "E:\python\lib\site-packages\can\interfaces\slcan.py", line 91, in __init__
#     raise CanInterfaceNotImplementedError("The serial module is not installed")
# can.exceptions.CanInterfaceNotImplementedError: The serial module is not installed
# PS E:\python can related\python-can-project> python .\RecvCanMessageTime.py
# Traceback (most recent call last):
#   File "E:\python\lib\site-packages\can\interfaces\usb2can\usb2canabstractionlayer.py", line 119, in __init__
#     self.__m_dllBasic = windll.LoadLibrary(dll)
#   File "E:\python\lib\ctypes\__init__.py", line 452, in LoadLibrary
#     return self._dlltype(name)
#   File "E:\python\lib\ctypes\__init__.py", line 374, in __init__
#     self._handle = _dlopen(self._name, mode)
# FileNotFoundError: Could not find module 'usb2can.dll' (or one of its dependencies). Try using the full path with constructor syntax.

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "E:\python can related\python-can-project\RecvCanMessageTime.py", line 12, in <module>
#     bus = can.interface.Bus(bustype='usb2can', channel='6D3C640E7D7D',
#   File "E:\python\lib\site-packages\can\interface.py", line 120, in __new__
#     bus = cls(channel, *args, **kwargs)
#   File "E:\python\lib\site-packages\can\interfaces\usb2can\usb2canInterface.py", line 102, in __init__
#     self.can = Usb2CanAbstractionLayer(dll)
#   File "E:\python\lib\site-packages\can\interfaces\usb2can\usb2canabstractionlayer.py", line 125, in __init__
#     raise can.CanInterfaceNotImplementedError(message) from error
# can.exceptions.CanInterfaceNotImplementedError: DLL failed to load at path: usb2can.dll