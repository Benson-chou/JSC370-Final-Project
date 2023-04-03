from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import json

driver = webdriver.Chrome()
diamond_list = []
for i in range(1, 586):
    url = f"https://www.brilliantearth.com/loose-diamonds/list/?shapes=All&cuts=Fair,Good,Very Good,Ideal,Super Ideal&colors=J,I,H,G,F,E,D&clarities=SI2,SI1,VS2,VS1,VVS2,VVS1,IF,FL&polishes=Good,Very Good,Excellent&symmetries=Good,Very Good,Excellent&fluorescences=Very Strong,Strong,Medium,Faint,None&min_carat=0.25&max_carat=13.42&min_table=48.00&max_table=88.00&min_depth=3.50&max_depth=90.70&min_price=0&max_price=912285&stock_number=&row=0&page={i}&requestedDataSize=200&order_by=price&order_method=asc&currency=CAD &has_v360_video=&dedicated=&abv=&sid=&min_ratio=1.00&max_ratio=2.75&shipping_day=&suppler_shipping_day=&exclude_quick_ship_suppliers=&MIN_PRICE=555&MAX_PRICE=1930485&MIN_CARAT=0.25&MAX_CARAT=13.42&MIN_TABLE=48&MAX_TABLE=88&MIN_DEPTH=3.5&MAX_DEPTH=90.7&category=Loose Diamonds&fill_most_popular=true&most_popular_order_by=recommended&most_popular_order_method="
    driver.get(url)
    time.sleep(2)
    # Access the body text and save it as a json file
    body = driver.find_element(By.TAG_NAME, "body")
    text = body.text

    parsed_data = json.loads(text)["diamonds"]
    for d in parsed_data:
        dia_item = {"price": d["price"],
                    "shape": d["shape"],
                    "carat": d["carat"], 
                    "cut": d["cut"], 
                    "color": d["color"], 
                    "clarity": d["clarity"], 
                    "table": d["table"],
                    "depth": d["depth"]}
        diamond_list.append(dia_item)
df = pd.DataFrame(diamond_list)
df.to_csv("/Users/bensonchou/JSC370/JSC370 Midterm:Final/brilliant.csv", index=False)

    
# Update the url, save html as json, update the csv file
# while loop to go through
# Wait for the page to load


# diamonds = driver.find_elements(By.CSS_SELECTOR, ".inner.item")

# n = len(diamonds)
# i = 1

# diamond_list = []
# for diamond in diamonds: 
#     if i == 20: 
#         i += 1
#         continue
#     try:
#         price = diamond.find_element(By.XPATH, f'//*[@id="diamonds_search_table"]/div[{i}]/a/table/tbody/tr/td[4]').text
#         carat = diamond.find_element(By.XPATH, f'//*[@id="diamonds_search_table"]/div[{i}]/a/table/tbody/tr/td[5]').text
#         cut = diamond.find_element(By.XPATH, f'//*[@id="diamonds_search_table"]/div[{i}]/a/table/tbody/tr/td[6]').text
#         color = diamond.find_element(By.XPATH, f'//*[@id="diamonds_search_table"]/div[{i}]/a/table/tbody/tr/td[7]').text
#         clarity = diamond.find_element(By.XPATH,f'//*[@id="diamonds_search_table"]/div[{i}]/a/table/tbody/tr/td[8]').text
#         print(price, carat, cut, color, clarity)
#         i += 1
#         dia_item = {
#             "price": price,
#             "carat": carat,
#             "cut": cut,
#             "color": color,
#             "clarity": clarity 
#         }
#         diamond_list.append(dia_item)
#     except NoSuchElementException:
#         break

# df = pd.DataFrame(diamond_list)
# df.to_csv("/Users/bensonchou/JSC370/JSC370 Midterm:Final/brilliant.csv", index=False)