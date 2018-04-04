import threading
from datetime import datetime
from bs4 import BeautifulSoup
import requests

def scraper(count, n_threads):
    print("I STARTED")
    refIds = []
    locations = []
    ratings = []
    titles = []
    reviews = []
    global textToBeWrittenTemp
    textToBeWrittenTemp = [""] * n_threads

    if count == 0:
        url1 = "https://www.tripadvisor.in/Attraction_Review-g297683-d317329-Reviews-Taj_Mahal-Agra_Agra_District_Uttar_Pradesh.html"
    else:
        url1 = "https://www.tripadvisor.in/Attraction_Review-g297683-d317329-Reviews-or" + str(count) + "0-Taj_Mahal-Agra_Agra_District_Uttar_Pradesh.html"

    webpage1 = requests.get(url1)
    data1 = webpage1.text
    soup1 = BeautifulSoup(data1, "html.parser")

    containers1 = soup1.find_all("div", class_="reviewSelector")
    for container in containers1:
        if container.find("span", onclick="widgetEvCall('handlers.clickExpand',event,this);"):
            refIds.append(container["data-reviewid"])
        else:
            if container.find('div', {"class": "location"}):
                locations.append(container.find('div', {"class": "location"}).span.text)
            else:
                locations.append("not given")
            ratings.append(container.find("span", class_="ui_bubble_rating")["class"][1])
            titles.append(container.find("span", class_="noQuotes").text)
            reviews.append(container.find("p", class_="partial_entry").text)

    refIdStr = '%2C'.join(str(i) for i in refIds)
    url2 = "https://www.tripadvisor.in/OverlayWidgetAjax?Mode=EXPANDED_HOTEL_REVIEWS&metaReferer=Attraction_Review&reviews=" + refIdStr
    webpage2 = requests.get(url2)
    data2 = webpage2.text
    soup2 = BeautifulSoup(data2, "html.parser")

    containers2 = soup2.find_all("div", class_="reviewSelector")
    for container in containers2:
        if container.find('div', {"class": "location"}):
            locations.append(container.find('div', {"class": "location"}).span.text)
        else:
            locations.append("not given")
        ratings.append(container.find("span", class_="ui_bubble_rating")["class"][1])
        titles.append(container.find("span", class_="noQuotes").text)
        reviews.append(container.find("p", class_="partial_entry").text)

    i = count%n_threads
    for location, rating, title, review in zip(locations, ratings, titles, reviews):
        textToBeWrittenTemp[i] += (location.replace(",", " |").replace("\n", " ... ").replace("lenbrek", " ... ").replace("denbrek", " ... ") + " , " + rating + " , " + title.replace(",", " ..").replace("\n"," ... ").replace("lenbrek", " ... ").replace("denbrek", " ... ") + " , " + review.replace(",", " ..").replace("\n", " ... ").replace("lenbrek", " ... ").replace("denbrek", " ... ") + "\n")

    print(ratings)
    print("I FINISHED")


def main():
    startTime = datetime.now()
    pages = 5
    n_threads = 100
    count = 0
    threads = []
    textToBeWritten = ""
    global textToBeWrittenTemp

    file = "TajMahalEnglis2015-20170.txt"
    f = open(file, "w", encoding='utf-8')
    headers = "location, rating, title, review \n"
    f.write(headers)

    while pages:
        thread = threading.Thread(target=scraper, args=(count,n_threads))
        threads.append(thread)
        thread.start()
        count += 1
        pages -=1

        if count%n_threads == 0:
            for thread in threads:
                thread.join()
            for i in range(0, n_threads):
                textToBeWritten += textToBeWrittenTemp[i]
                textToBeWrittenTemp[i] = ""
            f.write(textToBeWritten)
            threads = []
            textToBeWritten = ""


    for thread in threads:
        thread.join()
    for i in range(0, count%n_threads):
        textToBeWritten += textToBeWrittenTemp[i]
    f.write(textToBeWritten)

    f.close()
    print(datetime.now() - startTime)

if __name__ == '__main__':
    main()