from xlrd import open_workbook

file1 = "Sentimented Reviews/good_TajMahalEnglish/good_TajMahalUnitedStates.txt"
f1 = open(file1, "w", encoding='utf-8')
headers = "rating,title,review\n"
f1.write(headers)

file2 = "Sentimented Reviews/good_TajMahalEnglish/good_TajMahalUnitedKingdom.txt"
f2 = open(file2, "w", encoding='utf-8')
headers = "rating,title,review\n"
f2.write(headers)

file3 = "Sentimented Reviews/good_TajMahalEnglish/good_TajMahalCanada.txt"
f3 = open(file3, "w", encoding='utf-8')
headers = "rating,title,review\n"
f3.write(headers)

file4 = "Sentimented Reviews/good_TajMahalEnglish/good_TajMahalAustralia.txt"
f4 = open(file4, "w", encoding='utf-8')
headers = "rating,title,review\n"
f4.write(headers)

file5 = "Sentimented Reviews/good_TajMahalEnglish/good_TajMahalBangladesh.txt"
f5 = open(file5, "w", encoding='utf-8')
headers = "rating,title,review\n"
f5.write(headers)



wb = open_workbook('Sentimented Reviews/good_TajMahalEnglish/good_TajMahalEnglish.xlsx')

for sheet in wb.sheets():
    for row in range(sheet.nrows):
        value = sheet.row_values(row)
        if "USA" in value[1] or "United States" in value[1] or "California" in value[1] or "Florida" in value[1] or "Texas" in value[1] or "Alaska" in value[1] or "georgia" in value[1] or "Maryland" in value[1] or "Washington" in value[1] or "New York" in value[1] or "Ohio" in value[1]:
            print(value[1])
            f1.write(value[0] + "," + value[2] + "," + value[3] + "\n")
        elif "UK" in value[1] or "United Kingdom" in value[1] or "England" in value[1] or "Scotland" in value[1] or "Wales" in value[1] or "Oxford" in value[1] or "London" in value[1] or "Wakefield" in value[1] or "Winchester" in value[1]:
            f2.write(value[0] + "," + value[2] + "," + value[3] + "\n")
        elif "Canada" in value[1] or "Ontario" in value[1] or "Toronto" in value[1] or "Ottawa" in value[1] or "Alberta" in value[1] or "Quebec" in value[1] or "Manitoba" in value[1]:
            f3.write(value[0] + "," + value[2] + "," + value[3] + "\n")
        elif "Australia" in value[1] or "Queensland" in value[1] or "Melbourne" in value[1] or "Sydney" in value[1]:
            f4.write(value[0] + "," + value[2] + "," + value[3] + "\n")
        elif "Bangladesh" in value[1] or "Malaysia" in value[1] or "Sri Lanka" in value[1] or "India" in value[1]:
            f5.write(value[0] + "," + value[2] + "," + value[3] + "\n")


f1.close()
f2.close()
f3.close()
f4.close()
f5.close()