
import numpy as np
import os
import matplotlib.pyplot as plt
import struct
from sklearn import preprocessing   #pip install -U scikit-learn
import pywt  #pip install PyWavelets
import copy



def visulizationBIN():
    file_dir = './'
    file_name = "scope_5.bin"
    file_path =  os.path.join(file_dir, file_name)

    data_bin = open(file_path, 'rb+')
    data_size = os.path.getsize(file_path)
    data_list = []

    for i in range(data_size):
        data_i = data_bin.read(1)
        num = struct.unpack('b', data_i)
        data_list.append(num[0])


    for item in data_list:
        if " " in str(item):
            print("*************************************")
        else:
            print(item)
    
    # print(ord ("2" ))   #ASCII code
    # for c in u"cafe":
    #     print( repr(c), ord(c))
    # print(ord(b'\xc2'))



if __name__ == '__main__':
    visulizationBIN()

