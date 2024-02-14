import nidaqmx   #pip install nidaqmx
from nidaqmx import DigitalSingleChannelWriter

td = 0

limitTD = -6

while td > limitTD:
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")   #the value read from the 'AI0' input of the 'Dev0' device
        td = task.read()
        tw = task
        print(td, type(td))
    
    td = limitTD