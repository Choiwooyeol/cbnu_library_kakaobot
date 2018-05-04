from bs4 import BeautifulSoup
import requests

def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

def get_crawl(num):
	URL = "http://libroom.chungbuk.ac.kr/RoomStatus_ms.aspx?room_no="+num
	lib_list = list()
	sorted_list = list()
	html = get_html(URL)
	soup = BeautifulSoup(html, 'html.parser')
	style1 = soup.find_all('td','Style1')
	count = 0 
	for n in style1:
		count = count + 1
		lib_list.append(n.get_text())
	style1_split = ' '.join(lib_list).split()
	for n in style1_split:
		sorted_list.append(int(n))
	sorted_list.sort()
	print(sorted_list)
	# count = len(sorted_list) # list 요소 세기
	return sorted_list

"""
def get_string(getted_list):
	setted_str = ''.join(getted_list)
	print(setted_str)
	return setted_str
"""

#
#### get_crawl("1") 와 같이 호출
########## num list ############

## 중도1열람실 1
## 중도2열람실 2
## 중도3열람실 3
## 과기도      15


## 형설관 차후 추가
### 공지사항 크롤링 차후 추가

#print(get_string(get_crawl("1")))
