from re import I
from scipy.signal import find_peaks
import csv


# fp = "C:\\Users\\f.he\\OneDrive - AuCom Group\\Desktop\\1111111111111111111111111111111111111111\\2022-6-15 8-20-28 hp34970a_34901adf_10s_Trise_Data.csv"
fp = "C:\\Users\\f.he\\OneDrive - AuCom Group\\Desktop\\1111111111111111111111111111111111111111\\2022-6-14 10-25-40 hp34970a_34901adf_30s_Trise_Data.csv"


file = open(fp, "r")
fContent = list(csv.reader(file))
lengthItem = len(fContent[0])
titleList = fContent[0]
bigList = []
fg = 0
while fg < lengthItem:
    temList = []
    for i in range(2273, len(fContent)):
        item = fContent[i]
        temList.append(item[fg])
    bigList.append(temList)
    fg += 1


def findAvg(num, titles, bigs):
    # timePoints = bigList[0]
    lst = bigs[num]

    maxValue = max(lst)

    lowLimit = int(float(maxValue) * 0.7)
    verticallimit = float("%.2f" % (float(maxValue) * 0.1 * 0.05))

    # print(maxValue, lowLimit, verticallimit)

    peaks, _ = find_peaks(lst, height=lowLimit, threshold=verticallimit, distance=3) #distance
    # print(peaks, type(peaks), len(peaks), lst[333], timePoints[333])

    peaksList = peaks.tolist()

    # print(peaksList)


    finalPeaksContentList = []
    for item in peaksList:
        
        finalPeaksContentList.append(float(lst[item]))

    # print(sum(finalPeaksContentList)/len(finalPeaksContentList))
    return titles[num], sum(finalPeaksContentList)/len(finalPeaksContentList)

# avgsList = []
# for i in range(1, len(bigList)):
#     try:
#         result_avg = list(findAvg(i, titleList, bigList))
#         avgsList.append(result_avg)
#     except:
#         print(i)

# print(avgsList)




def findAvg_specific(num, titles, bigs, lowLimit, verticallimit):  # tune the 'num', 'lowLimit' and 'verticallimit' based on the graph of the data manually.
    lst = bigs[num]
    peaks, _ = find_peaks(lst, height=lowLimit, threshold=verticallimit, distance=3) #distance
    peaksList = peaks.tolist()
    finalPeaksContentList = []
    for item in peaksList:
        finalPeaksContentList.append(float(lst[item]))
    return titles[num], sum(finalPeaksContentList)/len(finalPeaksContentList)




result_avg = list(findAvg_specific(23, titleList, bigList, 13, 0))
print(result_avg)
