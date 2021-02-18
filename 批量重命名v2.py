import os

aname=[]
for i in os.walk("."):
    base_path = i[0]
    for u in i[2]:
        bname = u
        a = base_path+'\\'+bname
        aname.append(a)
for j in aname:
    if j.find('[获取更多资源请加V：aixuexi158]') != -1:
        c = j.replace('[获取更多资源请加V：aixuexi158]','',1)
        os.rename(j,c)
    else:
        print('此文件不需要重命名')
