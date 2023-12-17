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

    # CSV 파일로 저장 (UTF-8 인코딩 사용)
    df.to_csv('financial_tip.csv', index=False, encoding='utf-8-sig')

# 크롤링할 웹페이지의 URL
url_to_crawl = 'https://fine.fss.or.kr/fine/bbs/B0000340/list.do?menuNo=900014&viewType='

# 함수 호출 (최대 15페이지까지 크롤링)
crawl_all_content(url_to_crawl, max_pages=15)