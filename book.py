import requests
from bs4 import BeautifulSoup
import pandas as pd
import os.path

url = "https://www.goodreads.com/book/show/6555517-the-dead-tossed-waves"
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")



bookName = soup.find(class_="infoBoxRowItem").get_text()

author = soup.find(class_="authorName").get_text()

bookImagediv = soup.find('div',{"class":"bookCoverPrimary"})

bookImage = bookImagediv.find('img').attrs['src']

numberofPages = soup.find(class_="row").contents[2].get_text()

description = soup.find(class_="readable stacked").contents[1].get_text()
genre = soup.find(class_="elementList").contents[1].get_text()

publishedAt = soup.find(class_="uitext darkGreyText").contents[3].get_text()

rating = soup.find("span",{"itemprop":"ratingValue"}).get_text()

ratingCountString = soup.findAll("meta", {"itemprop": "ratingCount"})[0].get_text()
ratingCount = ratingCountString.replace("ratings", "")

reviewCountString = soup.findAll("meta", {"itemprop": "reviewCount"})[0].get_text()
reviewCount = reviewCountString.replace("reviews","").replace(" ","")

ISBNString = soup.findAll(class_="infoBoxRowItem")[1].contents[0]
ISBN = ISBNString.replace(" ", "")

ISBN13 = soup.find("span",{"itemprop":"isbn"}).get_text()
csvfilePath = "./book.csv" 




dict = {'Name': [bookName],
        'Author': [author],
        'Image': [bookImage],
        'Number of pages':[numberofPages],
        'Description':[description],
        'Genre':[genre],
        'Published At':[publishedAt],
        'Rating':[rating],
       'RatingCount':[ratingCount],
       'ReviewCount':[reviewCount],
        'ISBN':[ISBN],
        'ISBN13':[ISBN13]
        }
df = pd.DataFrame(dict)


if os.path.isfile(csvfilePath):
        
        data = pd.read_csv(csvfilePath)
        data.head()
        data = data.append(df, ignore_index=True)
        data.to_csv(csvfilePath, index=False)
else:
        df.to_csv(csvfilePath, index=False, mode='a')


