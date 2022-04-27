# Goodreads Webscraper
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

<a href="https://www.goodreads.com">goodreads</a> python script to collect book data 

<img width="1425" alt="Screen Shot 2022-04-27 at 7 55 09 PM" src="https://user-images.githubusercontent.com/71937852/165579430-ff15c4ca-1843-4705-b622-319ce7ae3c62.png">

## Setup
```bash
git clone https://github.com/KingAzizz/goodread-webscraper.git
```
&

```bash
cd goodread-webscraper
```


## What You Need
To run these scripts, you will need [Python 3](https://www.anaconda.com/distribution/).

-   [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://docs.python-requests.org/en/latest/)


You can install these Python libraries by running   
```bash
pip install -r requirements.txt
```

## book.py

### Input

This script takes as input a book's URL. For example, the book url for *Red Queen* ([https://www.goodreads.com/book/show/22328546-red-queen?from_search=true&from_srp=true&qid=Fli1luHo0z&rank=1](https://www.goodreads.com/book/show/22328546-red-queen?from_search=true&from_srp=true&qid=Fli1luHo0z&rank=1)) is `Red Queen`. 

### Output

This script outputs a CSV file for each book with the following information:
- Book Title
- Author Name
- Book Image Url 
- Number of Pages
- Book Description
- Genre
- Published Date
- Rating
- Rating Count
- Review Count
- ISBN
- ISBN13

### Usage

```
python3 book.py
```

## Credit
This code is written by Abdulaziz Alsunaydi.
 The code is licensed under a  [MIT](https://choosealicense.com/licenses/mit/).
