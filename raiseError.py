import sys
import serial
import serial.tools.list_ports as stl


def detectCOM():
    detectFlag = True
    while detectFlag:
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        else:
            raise EnvironmentError('Unsupported platform')
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                print(port)
                s.close()
                result.append(port)
            except:
                pass
            # s = serial.Serial('COM6')
        
        if len(result) > 0:
            detectFlag = False
            break
        else:
            pass

def detects():
    # Finn>>>>>>>>>>>>>>>>>>>>
    detectFlag = True
    while detectFlag:
        plist = list(stl.comports())

        coResult = ''
        for item in plist:
            co = str(item)
            if 'USB' in co:
                coResult = co
        
        if 'USB' in coResult:
            detectFlag = False
            break
        else:
            pass
    #<<<<<<<<<<<<<<<<<<<<<<<Finn

    


# detectCOM()

detects()
