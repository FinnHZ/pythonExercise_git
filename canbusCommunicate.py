import can

# can.rc['interface'] = 'serial'
# can.rc['channel'] = 'COM9'
# can.rc['bitrate'] = 9600 #500000
# from can.interface import Bus

# bus = Bus()

# msg = can.Message(
#     arbitration_id=0x1, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=True
# )

# try:
#     bus.send(msg)
#     print(f"Message sent on {bus.channel_info}")
# except can.CanError:
#     print("Message NOT sent")



with can.interface.Bus(bustype='serial', channel='COM9', bitrate=19200) as bus:
    msg = can.Message(arbitration_id=0x08A8, data=[0, 0, 0, 0, 0, 0, 0, 1], is_extended_id=False)
    try:
        abc = bus.send(msg)
        print(f"Message sent on {bus.channel_info}")
        print(abc)
    except can.CanError:
        print("Message NOT sent")