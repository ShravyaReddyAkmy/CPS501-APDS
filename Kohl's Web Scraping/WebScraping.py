#####################################################################################################################
# This program is for Web scraping and Data visualization of products(Shoes,Socks,Ties) from Kohl's website
# Author: Shravya Reddy Akmy, Section: CPS_501-12
# Date: 12/3/2021
#####################################################################################################################

# Libraries Used
import math
import csv
import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# Lists to store data of selected products
data_list=[] #List of data of each item
label=[] # List of all item's labels 
price=[] # List of all item's prices 
review=[] # List of all item's reviews

# Function to get the url of selected product 
def get_url(user_choice):
    if user_choice==1:
        product_name='SHOES'
        product_url='https://www.kohls.com/search.jsp?submit-search=web-regular&search=shoes&kls_sbp=33169938159252114110011282254670134058'
    elif user_choice==2:
        product_name='SOCKS'
        product_url='https://www.kohls.com/search.jsp?submit-search=web-regular&search=socks&kls_sbp=33169938159252114110011282254670134058'
    elif user_choice==3:
        product_name='TIES'
        product_url='https://www.kohls.com/search.jsp?submit-search=web-regular&search=ties&kls_sbp=33169938159252114110011282254670134058'
    return product_url,product_name

# Function to scrape product data from url
def scrape_url(product_url):
    url_data=requests.get(product_url)
    soup=BeautifulSoup(url_data.text,'html.parser')
    if(url_data.status_code==200):
        product_data=soup.find_all('li',class_='products_grid')
    else:
        product_data='Not successful'
    return product_data

# Function to retrieve and cleanse product data
def cleanse_url(product_data):
    for data in product_data:
        product_label=data.find('div',class_='prod_nameBlock')
        pdt_label=product_label.p.text.strip('\n').strip('\t').strip('\n').strip('\t').strip('\n').split()
        pdt_label=[pdt_label[0],pdt_label[1]]
        pdt_label=' '.join(pdt_label)
        label.append(pdt_label)
        product_price=data.find('div',class_='prod_priceBlock')
        pdt_price=product_price.find('div',class_='prod_price_original').text
        if pdt_price=='':  # Making price=0 for the products attribute is 'None'
            price.append('$0')
        else:
            pdt_price=pdt_price.split()
            price.append(pdt_price[len(pdt_price)-1])
        product_review=data.find('div',class_='prod_ratingBlock')
        if str(product_review)=='None': # Making review = 0 for the product attribute is 'None'
            review.append(0)
        else:
            pdt_review=product_review.find('span',class_='prod_ratingImg')
            pdt_review=float((pdt_review.a['alt'].split())[0])
            review.append(pdt_review)
    return [label,price,review]

# Main program
print("\n********** Hey! This code helps you to get the product details of SHOES, SOCKS, or TIES from real time shopping website KOHL'S **********")
choice=int(input("\nSelect any product you like to get data of:\n1 - Shoes \n2 - Socks \n3 - Ties \nEnter:"))
url,product=get_url(choice)
scrape=scrape_url(url)
data=cleanse_url(scrape)
# Normalizing the data values to average value which are "0"
label=data[0]
price=[]
review=data[2]
for value in data[1]:
    value=value.strip('$')
    value=float(value)
    value=math.floor(value)
    price.append(value)
price_avg=sum(price)/len(price)
review_avg=sum(data[2])/len(data[2])
for item in price:
    if item==0:
        item_index=price.index(item)
        item=price_avg
        price[item_index]=item
for item in review:
    if item==0:
        item_index=review.index(item)
        item=review_avg
        review[item_index]=item
for item in label:
    item_index=label.index(item)
    data_list.append([label[item_index],price[item_index],review[item_index]])
# Writing data to csv file
with open('data_file.csv',mode='w',newline='') as file:
    header = csv.DictWriter(file, fieldnames = ["Brand", "Price in USD", "Rating out of 5"])
    header.writeheader()
    row_data=csv.writer(file)
    for item in data_list:
        row_data.writerow(item)
# Overall Data representation
data_read=pd.read_csv('data_file.csv')
display = pd.DataFrame(data_read)
size=display.shape
data_describe=display.describe()
print("\nDATA FOR",product,"\n",display,"\n\n",data_describe)
# Plotting graphs for data visualisation
display[['Price in USD', 'Rating out of 5']].hist(figsize=(15,6),
bins=5,linewidth='1',edgecolor='b',grid=False)
#plt.show()
display.plot(kind='bar', x ='Brand', y='Rating out of 5', color='blue')
plt.xlabel("Brand",color='brown')
plt.ylabel("Rating out of 5",color='brown')
plt.title("Rating vs Brand",color='brown')
#plt.show()
display.plot(kind='bar', x ='Brand', y='Price in USD', color='blue')
plt.xlabel("Brand",color='brown')
plt.ylabel("Pricing in USD",color='brown')
plt.title("Pricing vs Brand",color='brown')
plt.show()

#***************** END OF THE CODE *******************************


