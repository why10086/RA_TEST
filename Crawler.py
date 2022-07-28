from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECS
from selenium.webdriver.common.by import By
import time

url = 'https://etherscan.io/token/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d'
opt = webdriver.ChromeOptions()  # 创建浏览
driver = webdriver.Chrome(options=opt)  # 创建浏览器对象
driver.get(url)  # 打开网页

pageSum = 2  # 爬取多少页
all_list = []  # A数据总表

for q in range(1, pageSum + 1):
    print('开始爬取第' + str(q) + '页...')
    try:
        # 定位页面中的table表格元素
        table_loc = (By.CSS_SELECTOR,
                     '#root > div > section > section > main > div > div > div.page-container > '
                     'div:nth-child(2) > div > div > div > div > div > div > table')
        # 等待timeOut秒，直到发现元素
        timeOut = 20
        WebDriverWait(driver, timeOut).until(ECS.presence_of_element_located(table_loc))
    except:
        # timeOut秒后没有发现元素则会执行该方法
        print('执行except方法 : 没有找到对应元素! 当前已爬取到第', q, '页')
        driver.quit()
    finally:
        # 发现元素则执行下面的方法
        # 定位页面中的table表格元素
        element = driver.find_element_by_css_selector(
            '#root > div > section > section > main > div > div > div.page-container > '
            'div:nth-child(2) > div > div > div > div > div > div > table')
        # 找到table元素下面的tr标签元素集合
        tr_content = element.find_elements_by_tag_name("tr")
        # 遍历tr元素
        for tr in tr_content:
            # 在当前表格行tr元素下查找类名为contract-tx-icon的元素
            icon = tr.find_elements_by_class_name('contract-tx-icon')
            type = ''
            if len(icon) != 0:
                type = '合约地址'
            else:
                type = '外部地址'
            # 保存当前行的数据
            tempList = [type]
            # 在当前表格行tr元素下查找td表格块集合
            td_list = tr.find_elements_by_tag_name('td')
            # 获取当前行数据中的地址字段上附带的链接
            for td in td_list:
                urls = td.find_elements_by_tag_name('a')
                for u in urls:
                    tempList.append(u.get_attribute('href'))
                tdText = str(td.text).strip().replace(',', '')
                if len(tdText) > 0:
                    tempList.append(tdText)
            tempLen = len(tempList)
            if tempLen == 8:
                del tempList[4]
            if tempLen > 1:
                del tempList[5]
                with open('../data/A.txt', 'a+', encoding='utf-8') as f:
                    f.write(",".join(tempList))
                    f.write("\n")
                all_list.append(tempList)
    # 打印本页内容并点击分页按钮继续执行下一页的内容
    print('第' + str(q) + '页爬取结束!')
    # 点击下一页按钮
    driver.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/div/div[2]/div[3]/div/ul/li[2]/div[3]/i') \
        .click()
    # 点击完分页按钮后等待一秒再进行下页的数据操作，否则会报错
    time.sleep(0.5)

print("全部爬取结束!!! 共", pageSum, '页')
for line in all_list:
    print(line)

driver.quit()
