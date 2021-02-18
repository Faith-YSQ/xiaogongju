import os

for i in os.listdir():
    if i.find('[获取更多资源请加V：aixuexi158]') != '1':
        a = i.replace('[获取更多资源请加V：aixuexi158]','',1)
        os.rename(i,a)
    else:
        print('此文件不需要重命名')