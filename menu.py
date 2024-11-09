#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:33:38 2023

@author: sarah
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)

    
# STARBUCKS
driver.get("https://www.starbucks.co.kr/menu/drink_list.do")
    
item = driver.find_elements(By.CLASS_NAME, "menuDataSet")

# PRINT
for i in range(len(item)) :
    print(str(i + 1) + ' ' + item[i].text)

driver.close()