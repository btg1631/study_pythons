# datetime은 1~100 일시 증가 방식
# 2월 29일 + 5일 = 3월 5일
# 229 + 5 = 234
from datetime import datetime

start_time = datetime.now()
now = datetime.now()

pass

first_date = datetime(2023, 12, 20)
# datetime.datetime(2023, 12, 20, 0, 0)

second_date = datetime.strptime("2023-12-25", "%Y-%m-%d")
# datetime.datetime(2023, 12, 25, 0, 0)

# "2023-12-20" - "2023-12-25"
result_date = first_date - second_date

end_time = datetime.now()

duration = end_time - start_time
pass