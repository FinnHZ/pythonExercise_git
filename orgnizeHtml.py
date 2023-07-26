
import xlwt


filePath = "./static/document/httpFiles.txt"

f = open(filePath,encoding = "utf-8")
contents = f.readlines()



firstList = []
for item in contents:
    target = item.split('" ADD_DATE="')
    firstList.append(target)

secondList = []
for item in firstList:
    temList = []
    temList.append((item[1].replace('</A>\n','').split('>'))[1])
    temList.append(item[0])
    secondList.append(temList) 


f.close()


workbook = xlwt.Workbook(encoding='utf-8')
sheet1 = workbook.add_sheet('http_orgnize')

for i in range(0, len(secondList)):
    sheet1.write(i, 0, secondList[i][0])
    sheet1.write(i, 1, secondList[i][1])

workbook.save(r'./static/document/collections.xls')



