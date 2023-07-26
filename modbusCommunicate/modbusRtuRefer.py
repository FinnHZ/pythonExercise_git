modbusRtuRefer = {
    "StarterState":{
        "0": "Reserved",
        "1": "Ready",
        "2": "Starting",
        "3": "Running",
        "4": "Stopping",
        "5": "Not Ready",
        "6": "Tripped",
        "7": "Programming mode",  
        "8": "Jog forward",
        "9": "Jog reverse",          
    },

    "TripCode":{
        "1": "Excess start time",
        "2": "Motor overload",
        "3": "Motor thermistor",
        "4": "Current imbalance",
        "5": "Frequency", 
        "6": "Phase sequence", 
        "7": "Overcurrent",       
        "8": "Power loss", 
        "9": "Undercurrent", 
        "10": "Heatsink overtemperature",   
        "11": "Motor connection",
        "12": "Input A trip",
        "13": "FLC too high",
        "14": "Unsupported option", 
        "15": "Communications card fault",
        "16": "Network communications",
        "18": "Overvoltage",
        "19": "Undervoltage",
        "20": "Ground fault",
        "23": "Parameter out of Range",
        "24": "Input B trip",
        "26": "L1 phase loss",
        "27": "L2 phase loss",
        "28": "L3 phase loss",
        "29": "L1-T1 shorted",
        "30": "L2-T2 shorted",
        "31": "L3-T3 shorted",
        "33": "Time-overcurrent (Bypass overload)",
        "34": "SCR overtemperature",
        "35": "Battery/clock",
        "36": "Thermistor circuit",      
        "47": "Over power",
        "48": "Under power",
        "56": "Keypad disconnected", 
        "57": "Zero speed detect", 
        "58": "SCR ITSM", 
        "59": "Instantaneous overcurrent",
        "60": "Rating capacity",
        "70": "Current Read Err L1",
        "71": "Current Read Err L2",
        "72": "Current Read Err L3",
        "74": "Motor connection T1",
        "75": "Motor connection T2",
        "76": "Motor connection T3",
        "77": "Firing fail P1",
        "78": "Firing fail P2",
        "79": "Firing fail P3",
        "80": "VZC Fail P1",
        "81": "VZC Fail P2",
        "82": "VZC Fail P3",
        "83": "Low Control Volts",
        "84": "Internal fault 84",   
        "85": "Internal fault 85",
        "86": "Internal fault 86", 
        "87": "Internal fault 87",
        "88": "Internal fault 88",
        "89": "Internal fault 89",
        "90": "Internal fault 90",
        "91": "Internal fault 91",
        "92": "Internal fault 92",
        "93": "Internal fault 93",
        "94": "Internal fault 94",
        "95": "Internal fault 95",
        "96": "Internal fault 96",
        "255":"No trip"
    },

    "Initialisation":{
        "0":"Unintiallised",
        "1":"Intiallised"
    },

    "CommandSource":{
        "0":"Remote Keypad, Digital Inputs, Clock",
        "1":"Network"
    },

    "ParametersChange":{
        "0":"Parameter(s) have changed since last parameter read",
        "1":"No parameter(s) have changed"
    },

    "PhaseSequence":{
        "0":"Negative phase sequence",
        "1":"Postive phase sequence"
    },

    "Versions_Product":{
        "1": "MCD3000",
        "2": "IMS2",
        "3": "TMS7",
        "4": "Jake",
        "5": "MVS",
        "6": "EMX3",
        "7": "MCD500",
        "8": "Digistart",
        "9": "Jane",
        "10": "Aston",
        "11": "MVS Multi",
        "12": "EMX4e",
        "13": "EMX4i",  
    },

    "Versions_Model":{
        "1": "F1-A",
        "2": "F1-B",
        "3": "F1-C",
        "4": "F1-D-ph",
        "5": "F1-D",
        "6": "F1-E-ph",
        "7": "F1-E",
        "8": "F1-F",
        "9": "F2-A-ph1",
        "10": "F2-A-ph2",
        "11": "F2-A",
        "12": "F2-B",
        "13": "F3-A-ph",
        "14": "F3-A",
        "15": "F3-B",
        "16": "F4-A-ph",
        "17": "F4-A"
    },

    "PowerScale":{
        "0": "Multiply power by 10 to ger W",
        "1": "Multiply power by 100 to ger W",
        "2": "Power(kw)",
        "3": "Multiply power by 10 to ger kW",    
    },

    "DigitalInput_StartStop": {
        "0":"Open",
        "1":"Closed(shorted)"
    },

    "DigitalInput_Reserved": {
        "0":"Open",
        "1":"Closed(shorted)"
    },

    "DigitalInput_Reset": {
        "0":"Open",
        "1":"Closed(shorted)"
    },

    "DigitalInput_InputA": {
        "0":"Open",
        "1":"Closed(shorted)"
    },

    "DigitalInput_InputB": {
        "0":"Open",
        "1":"Closed(shorted)"
    }   
}
