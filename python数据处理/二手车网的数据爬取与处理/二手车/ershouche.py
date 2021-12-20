# 导入库， 爬取数据
import requests
import pandas as pd

# 初始化空列表
carname_lis, carage_lis, price_lis, mileage_lis = [], [], [], []


for a in range(1, 20):
    # https://www.guazi.com/zz/buy
    # 循环爬取数据
    url = "https://mapi.guazi.com/car-source/carList/pcList?minor=&sourceType=&ec_buy_car_list_ab=&location_city=&district_id=&tag=-1&license_date=&auto_type=&driving_type=&gearbox=&road_haul=&air_displacement=&emission=&car_color=&guobie=&bright_spot_config=&seat=&fuel_type=&order=&priceRange=0,-1&tag_types=&diff_city=&intention_options=&initialPriceRange=&monthlyPriceRange=&transfer_num=&car_year=&carid_qigangshu=&carid_jinqixingshi=&cheliangjibie=&page={}&pageSize=20&city_filter=103&city=103&guazi_city=103&qpres=&versionId=0.0.0.0&osv=Unknown&platfromSource=wap".format(a)


    # 设置请求头
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    # requests请求链接
    resp = requests.get(url, headers=headers).json()

    data = resp['data']['postList']

    # 进行数据处理
    for li in data:
        # 车名
        carname = li['title']
        # 车龄
        carage = li['license_date']
        # 里程
        milrage = li['road_haul']
        # 价格
        price = li['price']

        # 输出
        carname_lis.append(carname)
        carage_lis.append(carage)
        mileage_lis.append(milrage)
        price_lis.append(price)

# pandas中的模块将数据存入
df = pd.DataFrame({
    "型号": carname_lis,
    "车龄": carage_lis,
    "里程": mileage_lis,
    "价格": price_lis
})
# #储存为csv文件
df.to_csv("aodi.csv", encoding='utf_8_sig', index=False)