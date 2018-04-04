from textblob import TextBlob
from datetime import datetime

startTime = datetime.now()
file1 = "SoupTajMahalEnglish2.txt"
file2 = "parsedTextTest.txt"

# f = open(file, "r")
f1 = open(file1, "r", encoding='utf-8')
f2 = open(file2, "w", encoding='utf-8')

textToBeWritten = ""
text = f1.read()
text = TextBlob(text)
tuples = text.tags
for tuple in tuples:
    if tuple[0] != 'lenbrek':
        if tuple[0] != 'delbrek':
            if tuple[1] == "JJ" or tuple[1] == "JJR" or tuple[1] == "JJS" or tuple[1] == "NN" or tuple[1] == "NNS" or tuple[1] == "NNP" or tuple[1] == "NNPS" or tuple[1] == "RB" or tuple[1] == "RBR" or tuple[1] == "RBS" or tuple[1] == "VB" or tuple[1] == "VBD" or tuple[1] == "VBG" or tuple[1] == "VBN" or tuple[1] == "VBP" or tuple[1] == "VB2" or tuple[0] == "no":
                textToBeWritten += tuple[0] + " "
        else:
            textToBeWritten += ","
    else:
        textToBeWritten += "\n"
        f2.write(textToBeWritten)
        textToBeWritten = ""
print(tuples)
f1.close()
f2.close()

print(datetime.now() - startTime)
