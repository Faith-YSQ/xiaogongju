import os

os.mkdir('Temp')

li_1 = os.listdir(os.getcwd())

while True:
    print('文件类型有JPG\nPNG')
    file_class = input('请输入你要排序的图片文件类型')
    if file_class == 'JPG':
        s='.jpg'
        break
    elif file_class == 'PNG':
        s = '.png'
        break
    else:
        print('你输入的格式有误，请按提示规范输入')

print(s)

index = 1
for old_name in li_1:
    if old_name.endswith(s):
        w_old_name_1 = os.getcwd() + '\\' + old_name
        # print(w_old_name)
        w_new_name_1 = os.getcwd() + '\\Temp\\' + str(index) + s
        index += 1
        # print(w_new_name)
        os.rename(w_old_name_1, w_new_name_1)
    else:
        pass

li_2 = os.listdir(os.getcwd() + '\\Temp')

for new_name in li_2:
    w_old_name_2 = os.getcwd() + '\\Temp\\' + new_name
    w_new_name_2 = os.getcwd() + '\\'+ new_name
    os.rename(w_old_name_2, w_new_name_2)

os.rmdir('Temp')
