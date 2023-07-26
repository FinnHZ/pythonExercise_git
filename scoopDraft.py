
import numpy as np
import os
import matplotlib.pyplot as plt
import struct
from sklearn import preprocessing   #pip install -U scikit-learn
import pywt  #pip install PyWavelets
import copy




def wave_del_zero(ecgt):
    #ecg = pywt.data.ecg()
    ecg = copy.deepcopy(ecgt)
    index = []
    data = []
    for i in range(len(ecg)-1):
        X = float(i)
        Y = float(ecg[i])
        index.append(X)
        data.append(Y)

    db8 = 'db8'
    # db8 = 'coif'

    w = pywt.Wavelet(db8)
    maxlev = pywt.dwt_max_level(len(data), w.dec_len)
    print("maximum level is " + str(maxlev))

    threshold = 0.04

    coeffs = pywt.wavedec(data, 'db8', level=maxlev)

    plt.figure()
    for i in range(1, len(coeffs)):
        coeffs[i] = pywt.threshold(coeffs[i], threshold*max(coeffs[i]))

    datarec = pywt.waverec(coeffs, 'db8')

    mintime = 0
    maxtime = mintime + len(data) + 1
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(index[mintime:maxtime], data[mintime:maxtime])
    plt.xlabel('time(s)')
    plt.ylabel('microvolt()')
    plt.title("Raw signal")
    plt.subplot(2, 1, 2)
    plt.plot(index[mintime:maxtime], datarec[mintime:maxtime-1])
    plt.xlabel('time(s)')
    plt.ylabel('microvolt()')
    plt.title("De-noiesd signal using wavelet techniques")
    plt.tight_layout()
    plt.show()
    print()



def visulizationBIN():
    file_dir = './'
    file_name = "scope_5.bin"
    file_path =  os.path.join(file_dir, file_name)

    data_bin = open(file_path, 'rb+')
    data_size = os.path.getsize(file_path)
    data_list = []

    for i in range(data_size):
        data_i = data_bin.read(1)
        # print(data_i)
        num = struct.unpack('b', data_i)
        data_list.append(num[0])
        # print(num[0])
        print(data_i, num)

    data_bin.close()

    min_max = preprocessing.MinMaxScaler(feature_range=(-1, 1))
    data_list_scale = min_max.fit_transform(np.array(data_list).reshape(-1, 1))
    data_list_scale_part = data_list_scale[:10240]

    #Option1:
    # wave_del_zero(data_list_scale_part)


    #Option2:
    plt.plot(data_list_scale_part)
    plt.show()




    # plt.plot(data_list)
    # plt.show()
    # print(data_list)

if __name__ == '__main__':
    visulizationBIN()

