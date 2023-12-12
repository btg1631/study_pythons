# list 안 dict 구성

# key(str) : value(여러 변수 종류 가능)
dict_car_info_mustang = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "price" : 30000
}

dict_car_info_sonata = {
        "brand": "Hyundai",
        "model": "Sonata",
        "year": 2020,
        "color": "Black",
        "price": 30000
    }


list_car_info = [dict_car_info_mustang, dict_car_info_sonata]
list_car_info = [
    {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "price" : 30000
    },
    {
        "brand": "Hyundai",
        "model": "Sonata",
        "year": 2020,
        "color": "Black",
        "price": 30000
    }
]

pass
dict_car_info_k5 = {
        "brand": "Kia",
        "model": "K5",
        "year": 2021,
        "color": "White",
        "price": 28000
}

list_car_info.append(dict_car_info_k5)
pass


# list_car_info안에 있는 index 0번에 있는 "model" : "Mustang" 접근 방법
dict_car_info_index_first = list_car_info[0]
dict_car_info_index_first["model"]
pass
list_car_info[0]["model"]
pass
print(list_car_info[0])

# for로 각 dict 정보 출력
for dict_car_info in list_car_info:
    brand = dict_car_info['brand']
    model = dict_car_info['model']
    print("브랜드 : {}, 모델 : {}".format(brand, model))
    pass

