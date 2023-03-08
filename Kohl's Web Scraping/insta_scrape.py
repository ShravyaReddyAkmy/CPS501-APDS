from bs4 import BeautifulSoup
import requests

def scrapeInstagram(soup):
    insta_data=[]
    for data in soup.find_all(name='meta', attrs={'property':'og:description'}):
        insta_data=data['content'].split()
        print(insta_data)
    followers = insta_data[0]
    following = insta_data[2]
    posts = insta_data[4]
    print(f'Instagram User > {instagram_user} \nNo.of Followers > {followers} \nNo.of Following > {following} \nNo.of Posts > {posts}')

instagram_user="shravz_11"
instagram_url=f'https://www.instagram.com/{instagram_user}'
instagram_page_req=requests.get(instagram_url)
soup = BeautifulSoup(instagram_page_req.text, "html.parser")
if(instagram_page_req.status_code==200):
    scrapeInstagram(soup)
else:
    print("Instagram user does not exist")

#course_cards=soup.find_all('div',class_='card')
#for course in course_cards:
 #   course_name = course.h5.text
  #  course_price =course.a.txt.split()[-1] # to get the last one
   # print(f'{course_name} costs {course_price}')
