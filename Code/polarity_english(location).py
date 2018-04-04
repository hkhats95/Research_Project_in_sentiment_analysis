from xlrd import open_workbook
from textblob import TextBlob

file_bad = "Sentimented Reviews text/bad_TajMahalEnglish.txt"
f_bad = open(file_bad, "w", encoding='utf-8')
headers = "rating, location, title, review\n"
f_bad.write(headers)

file_good = "Sentimented Reviews text/good_TajMahalEnglish.txt"
f_good = open(file_good, "w", encoding='utf-8')
headers = "rating, location, title, review\n"
f_good.write(headers)

wb = open_workbook('WebScrape/TajMahalEnglish.xlsx')
for sheet in wb.sheets():
    #print 'Sheet:',s.name

    for row in range(sheet.nrows):
        value = sheet.row_values(row)
        # print (value)
        if value[0] == 'bubble_30':
            text = value[2] + ", " + value[3]
            text = TextBlob(text)
            textPolarity = text.sentiment
            if textPolarity.polarity < 0.3:
                print(text)
                f_bad.write(value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n")
            else:
                f_good.write(value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n")
        elif value[0] == 'bubble_10' or value[0] == 'bubble_20':
            f_bad.write(value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n")
        elif value[0] == 'bubble_40' or value[0] == 'bubble_50':
            f_good.write(value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n")

f_bad.close()
f_good.close()