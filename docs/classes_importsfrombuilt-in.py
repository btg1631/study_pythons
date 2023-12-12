import os

# 현재 폴더 위치 (CLI : pwd)
current_folder = os.getcwd()
print('현재 실행되는 python 위치 : {}'.format(current_folder))

# 현재 폴더에 있는 파일과 폴더 리스트 출력
file_forder_list = os.listdir(current_folder)
print("파일과 폴더 리스트 : {}".format(file_forder_list))



pass