import nidaqmx   #pip install nidaqmx
import numpy as np

# with nidaqmx.Task() as task:
#     task.ao_channels.add_ao_voltage_chan("Dev1/ao0")

#     task.timing.cfg_samp_clk_timing(1000)

#     print("1 Channel N Samples Write: ")
#     print(task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True))
#     task.wait_until_done()
#     task.stop()

#     task.ao_channels.add_ao_voltage_chan("Dev1/ao1:3")

#     print("N Channel N Samples Write: ")
#     print(
#         task.write(
#             [[1.1, 2.2, 3.3], [1.1, 2.2, 4.4], [2.2, 3.3, 4.4], [2.2, 3.3, 4.4]],
#             auto_start=True,
#         )
#     )
#     task.wait_until_done()
#     task.stop()



#************************************************************************************************************************************

with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")   #the value read from the 'AI0' input of the 'Dev0' device
    task.timing.cfg_samp_clk_timing(10000)
    # writer = DigitalSingleChannelWriter(task.out_stream, auto_start=True)
    # writer.write_many_sample_port_uint32(wave)
    commands = np.ndarray((4,), dtype=np.uint16)
    commands[:] = 0
    commands[-1] = 1

    print(commands)
    writeResult = task.write(commands, auto_start=True)  #Returns: int Specifies the actual number of samples this method successfully wrote.
    print(writeResult)

# limitTD = 1.2
# td = 0
# while td > limitTD:
with nidaqmx.Task() as task1:
    task1.ai_channels.add_ai_voltage_chan("Dev1/ai0")   #the value read from the 'AI0' input of the 'Dev0' device
    td = task1.read()
    print(td, type(td))

