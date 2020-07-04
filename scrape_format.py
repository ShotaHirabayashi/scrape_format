from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re
#csvのデータに変換するツール
import pandas as pd
import datetime



def get_all_time():
    """
        return map
            date: 2020/07/03
            week: 火
            time : 15:30
    """
    try:
        time_obj = {}
        weekday = ["月","火","水","木","金","土","日"]
        today = datetime.date.today()
        date = today.strftime('%Y/%m/%d')
        d = datetime.datetime.strptime(date, "%Y/%m/%d")
        week = weekday[d.weekday()]
        t = datetime.datetime.now()
        time = t.strftime('%H:%M')
        time_obj["date"]  =date
        time_obj["week"]  =week
        time_obj["time"]  =time
        return time_obj
    except: 
        print('error')

#dfはcsv化するためのデータの形にする
df = pd.DataFrame()
# numpy用のリスト
dmyList =[]
#webdriverがURLを開く先を指定する
chrome = webdriver.Chrome()


for _ in range(3):
    try:
        chrome.get("")
        # ログイン用
        chrome.find_element_by_class_name('')
        chrome.find_element_by_xpath('//*[@id="pwd"]').send_keys('')
        chrome.find_element_by_xpath('//*[@id="login"]').click()

        # windowを変更
        handles = chrome.window_handles
        chrome.switch_to_window(handles[0])

        # frameを変更
        chrome.switch_to.default_content()
        # id name を指定する
        chrome.switch_to_frame("Main")


    except:
        # 処理中にエラー10秒後に再起
        time.sleep(10)
    # エラーなしで成功
    else:
        break
#3回とも失敗
else:
    chrome.close()

#csvのデータにするために型に代入       
df['dummy'] = dmyList
#csvに保存
df.to_csv('dmy.csv')
#chromeを閉じる
chrome.close()