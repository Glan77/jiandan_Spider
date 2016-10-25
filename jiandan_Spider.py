import requests
from bs4 import BeautifulSoup

index = 1
headers={'referer':'http://jandan.net/', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}

def downloadImg(new_url):
    global index
    html = requests.get(new_url,headers=headers).text
    soup = BeautifulSoup(html,'html.parser')
    links = soup.find_all('a', class_='view_img_link')
    for link in links:
        with open('E:/Spider/4/'+str(index)+'.jpg','wb') as f:
            f.write(requests.get(link.get('href')).content)
            index += 1


if __name__ == '__main__':
    url = 'http://jandan.net/ooxx/page-888#comments'
    for i in range(0,2):
        print("I'm crawling page %d.Please wait for a moment." % (i+1) )
        downloadImg(url)
        html = requests.get(url,headers=headers).text
        soup = BeautifulSoup(html,'html.parser')
        url = soup.find('a', class_='previous-comment-page').get('href')

    print('Over!')
