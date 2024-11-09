#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 20:55:43 2024

@author: sarah
"""

# 모듈 import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 드라이버 생성
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://xn--2e0b040a4xj.com/reservation?branch=4&theme=12&date=2024-11-14#list") # 날짜 수정

# 웹페이지가 로드될 때까지 2초를 대기
driver.implicitly_wait(5)  

# 시간 선택
# 17:40
if driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div[2]/section/div/ul/li[7]/div/button/label').text == '예약가능' :
    driver.find_element(By.XPATH,'//*[@id="wrap"]/div/div[2]/section/div/ul/li[7]/div/button').click()
# 16:25
elif driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div[2]/section/div/ul/li[6]/div/button/label').text == '예약가능' :
    driver.find_element(By.XPATH,'//*[@id="wrap"]/div/div[2]/section/div/ul/li[6]/div/button').click()
# 15:10
elif driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div[2]/section/div/ul/li[5]/div/button/label').text == '예약가능' :
    driver.find_element(By.XPATH,'//*[@id="wrap"]/div/div[2]/section/div/ul/li[5]/div/button').click()
# 18:55
elif driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div[2]/section/div/ul/li[8]/div/button/label').text == '예약가능' :
    driver.find_element(By.XPATH,'//*[@id="wrap"]/div/div[2]/section/div/ul/li[8]/div/button').click()
# 20:10
elif driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div[2]/section/div/ul/li[9]/div/button/label').text == '예약가능' :
    driver.find_element(By.XPATH,'//*[@id="wrap"]/div/div[2]/section/div/ul/li[9]/div/button').click()

# 성함 입력
driver.find_element(By.XPATH,'//*[@id="wrap"]/form/div[1]/article/section[1]/div/table/tbody/tr[3]/td/input').send_keys('홍길동')
# 연락처 입력
driver.find_element(By.XPATH,'//*[@id="wrap"]/form/div[1]/article/section[1]/div/table/tbody/tr[4]/td/input').send_keys('010-1234-5678')
# 예약 인원 선택
Select(driver.find_element(By.XPATH, '//*[@id="evePeople"]')).select_by_value('4')
# 결제방식 선택
driver.find_element(By.XPATH,'//*[@id="wrap"]/form/div[1]/article/section[1]/div/table/tbody/tr[7]/td/label').click()
# 동의 체크
driver.find_element(By.XPATH,'//*[@id="wrap"]/form/div[1]/article/section[1]/div/div/label').click()

# 예약히가 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="eveReservationBtn"]').click()
