# Class 초기화 방법
dict_initial = {}       # empty
dict_initial = dict()   # empty

list_car_info = ["ford", "Mustang", 1964]

# key(str) : value(여러 변수 종류 가능)
dict_car_info = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "items" : []
}

model = dict_car_info["model"]
print("dict_car_info 에 있는 model name : {}".format(model))

# key로 인한 값 변경
dict_car_info["year"] = 1970
# 새로운 key와 값 정의
dict_car_info["color"] = "red"
dict_car_info["color"] = ["red", "yellow", "brown"]

pass