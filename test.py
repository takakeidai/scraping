


import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd



def find_table_target_word(th_elms, td_elms, target:str):
    # tableのthからtargetの文字列を探し一致する行のtdを返す
    for th_elm,td_elm in zip(th_elms,td_elms):
        if th_elm.text == target:
            return td_elm.text


def set_driver(driver_path, headless_flg):

    if "chrome" in driver_path:
          options = ChromeOptions()
    else:
      options = Options()

    if headless_flg == True:
        options.add_argument('--headless')

    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')        

    driver_path = ChromeDriverManager().install()
    return Chrome(executable_path=driver_path, options=options)



def main():
    search_keyword = "高収入"
    driver_path = ChromeDriverManager().install()
    driver = set_driver(driver_path, False)
    driver.get("https://tenshoku.mynavi.jp/")
    time.sleep(5)
    driver.execute_script('document.querySelector(".karte-close").click()')
    time.sleep(5)
    driver.execute_script('document.querySelector(".karte-close").click()')
    driver.find_element_by_class_name(
        "topSearch__text").send_keys(search_keyword)
    driver.find_element_by_class_name("topSearch__button").click()


    df = pd.DataFrame()
    company_name = []
    title = []


    ## 　①ページが正しく変更されているか見るために、最小限の動作を行ってみた。ページが変わるごとにaが出力される。 

    ##　以前実行した時は13ページ分aが出力されたが、今回やってみると3ページ分しか出力されない。
    
    # while True:
    #     print('a')
        
    #     try:
    #         driver.find_element_by_css_selector(".iconFont--arrowLeft").click()
    #     except:
    #         print('最終ページです')
    #         break


    ##　②会社名だけ取り出そうとする。以前行った時は3000件を超える会社名が出力されたが、今回は100件ほど。

    # while True:


    #     name_list = driver.find_elements_by_class_name("cassetteRecruit__name")


    #     for name in name_list:
    #         target = ' '
    #         idx = name.text.find(target)
    #         company_name.append(name.text[:idx])

    #     for i in range(0, len(company_name)):
    #         df = df.append(
    #             {'会社名':company_name[i]}, 
    #             ignore_index=True)

    #     try:
    #         driver.find_element_by_css_selector(".iconFont--arrowLeft").click()
    #     except:
    #         print('最終ページです')
    #         break


    # df.to_csv("会社一覧.csv", encoding = "utf-8_sig")




    # ## ③タイトルだけ取り出そうとする。これもうまくいかない。

    # while True:
    #     name_list = driver.find_elements_by_class_name("cassetteRecruit__name")


    #     for name in name_list:
    #         target = ' '
    #         idx = name.text.find(target)
    #         company_name.append(name.text[:idx])

    #     for i in range(0, len(company_name)):
    #         df = df.append(
    #             {'会社名':company_name[i]}, 
    #             ignore_index=True)

    #     try:
    #         driver.find_element_by_css_selector(".iconFont--arrowLeft").click()
    #     except:
    #         print('最終ページです')
    #         break


    # df.to_csv("会社一覧.csv", encoding = "utf-8_sig")
    

    



# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()



