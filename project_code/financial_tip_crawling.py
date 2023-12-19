"""
금융소비자 정보포털 '파인'에 있는 금융 관련 꿀팁을 크롤링
크롤링 결과물을 csv 파일로 저장
"""

#필요한 라이브러리 호출
import requests
from bs4 import BeautifulSoup
import pandas as pd
import chardet

def detect_encoding(text):
    result = chardet.detect(text.encode())
    return result['encoding']

def crawl_all_content(url, max_pages=15):
    data = {'Title': [], 'Link': []}

    for page_index in range(1, max_pages + 1):
        # 페이지별 URL 구성
        page_url = f'{url}&pageIndex={page_index}'

        # 웹페이지의 HTML 가져오기
        response = requests.get(page_url)
        html = response.text

        # HTML 문자셋 감지
        encoding = detect_encoding(html)

        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(html, 'html.parser')

        # 특정 클래스("title")에 속한 모든 링크와 텍스트 추출
        title_elements = soup.find_all('td', class_='title')
        for title_element in title_elements:
            link = title_element.find('a')
            if link:
                title = link.text
                href = f'https://fine.fss.or.kr{link.get("href")}'  # 주소를 붙여서 절대 경로로 변환
                data['Title'].append(title)
                data['Link'].append(href)

    # 데이터프레임 생성
    df = pd.DataFrame(data)

    # csv 파일(금융꿀팁)을 저장하기
    file_path = './../project_data/financial_tip.csv'
    df.to_csv(file_path, index=False, encoding='utf-8-sig')

# 크롤링할 웹페이지의 URL
url_to_crawl = 'https://fine.fss.or.kr/fine/bbs/B0000340/list.do?menuNo=900014&viewType='

# 함수 호출 (최대 15페이지까지 크롤링)
crawl_all_content(url_to_crawl, max_pages=15)
