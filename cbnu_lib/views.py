from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from cbnu_lib import wooyeol

def add_enter(get_list):
    count = 0
    for n in get_list:
          if (count % 7) == 0:
             get_list.insert(count,"\n")
          count = count + 1
    return get_list

def get_string(return_list):
    string = " ".join(map(str,return_list))
    return string

def keyboard(request):
 
    return JsonResponse({
        'type':'buttons',
        'buttons':['중앙도서관','과기도','편의기능']
    })
 
@csrf_exempt
def answer(request):
 
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    crawl = list()
    count = 0
    if datacontent == '중앙도서관':
        return JsonResponse({
                'message': {
                    'text': '열람실을 선택해주세요'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['1열람실','2열람실','3열람실','뒤로가기']
                }
 
            })
 
    elif datacontent == '과기도':
        crawl = wooyeol.get_crawl("15")
        count = len(crawl)
        string = get_string(add_enter(crawl))
        return JsonResponse({
                'message': {
                    'text': "--------------------\n\n과학 기술 도서관 열람실 현황 입니다.\n\nㅇ사용가능좌석: " + str(count) + " / 180 \nㅇ남은좌석\n\n--------------------\n" + string + "\n\n--------------------",
                    'photo': {
                        'url': "http://cfile26.uf.tistory.com/image/9955E7385AEAEF962E9891",
                        'width': 960,
                        'height': 620
                    }
                },
	        'keyboard': {
                    'type':'buttons',
                    'buttons':['중앙도서관','과기도','편의기능']
                } 
            })
    elif datacontent == '뒤로가기':
        crawl = "test"
 
        return JsonResponse({
                'message': {
                    'text': "장소를 선택해주세요."
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['중앙도서관','과기도','편의기능']
                } 
            })
    elif datacontent == '편의기능':
        #crawl = "test"
        return JsonResponse({
                'message': {
                    'text': "기능을 선택해주세요."
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['예약연장 및 반납','뒤로가기']
                } 
            })
    elif datacontent == '예약연장 및 반납':
        #crawl = "test"
        return JsonResponse({
                'message': {
                    'text': "예약연장 및 반납 링크로 이동합니다.",
                    'message_button': {
                       'label': "이동하기",
                       'url': "http://libroom.chungbuk.ac.kr/login.aspx"
                    }
                },
                'keyboard': {
                    'type':'buttons',
                    #'buttons':['예약연장','날씨']
                    'buttons':['중앙도서관','과기도','편의기능']
                } 
            })
#아직구현안함
    elif datacontent == '날씨':
        return JsonResponse({
                'message': {
                    'text': "미구현입니다."
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['중앙도서관','과기도','편의기능']
                } 
            })
#고렇다고합니다
    elif datacontent == '1열람실':
        crawl = wooyeol.get_crawl("1")
        count = len(crawl)
        string = get_string(add_enter(crawl))
        return JsonResponse({
                'message': {
                    'text': "--------------------\n\n중앙도서관 1열람실 현황 입니다.\n\nㅇ사용가능좌석: " + str(count) + " / 360 \nㅇ남은좌석\n\n--------------------\n" + string + "\n\n--------------------",
                    'photo': {
                        'url': "http://cfile29.uf.tistory.com/image/99BE78385AEAEF9422D8E5",
                        'width': 960,
                        'height': 640
                    }
                },
	        'keyboard': {
                    'type':'buttons',
                    'buttons':['중앙도서관','과기도','편의기능']
                } 
            })
    elif datacontent == '2열람실':
        crawl = wooyeol.get_crawl("2")
        count = len(crawl)
        string = get_string(add_enter(crawl))
        return JsonResponse({
                'message': {
                    'text': "--------------------\n\n중앙도서관 2열람실 현황 입니다.\n\nㅇ사용가능좌석: " + str(count) + " / 264 \nㅇ남은좌석\n\n--------------------\n" + string + "\n\n--------------------",
                    'photo': {
                        'url': "http://cfile7.uf.tistory.com/image/9982A6385AEAEF950FC8F2",
                        'width': 960,
                        'height': 640
                    }
                },
	        'keyboard': {
                    'type':'buttons',
                    'buttons':['중앙도서관','과기도','편의기능']
                } 
            })
    elif datacontent == '3열람실':
        crawl = wooyeol.get_crawl("3")
        count = len(crawl)
        string = get_string(add_enter(crawl))
        return JsonResponse({
                'message': {
                    'text': "--------------------\n\n중앙도서관 3 열람실 현황 입니다.\n\nㅇ사용가능좌석: " + str(count) + " / 408 \nㅇ남은좌석\n\n--------------------\n" + string + "\n\n--------------------",
                    'photo': {
                        'url': "http://cfile24.uf.tistory.com/image/99635C385AEAEF952D88A7",
                        'width': 960,
                        'height': 640
                    }
                },
	        'keyboard': {
                    'type':'buttons',
                    'buttons':['중앙도서관','과기도','편의기능']
                } 
            })

