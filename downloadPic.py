#coding:utf-8
import requests
import os
import re
import time
import traceback
import random

print 'start--------> '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def pic_url(url,path):
    print('picurl-------------begin')
    if os.path.exists(path):
        print('The path is exist')
    else:
        os.makedirs(path)
    html = ''
    print(url)
    try:
        while True:
            r = requests.get(url)
            #r.encoding('UTF-8')
            #print(r.text)
            html = r.text
            if html == '':
                print ('url error')
                break
            else:
                break
        print(str(len(html)))
        rePicList = '<img src="(http.*?)"'
        reVideoList ='<video.*? src="(http.*?)"'
        PicContent = re.findall(rePicList, html, re.S)
        print(str(len(PicContent)))
        if len(PicContent) <= 0:
            print('===============load false, please check================')
            return False
        else:
            pic_list(PicContent,path)
    except Exception:
        print('There is an exception.')




def pic_list(PicContent,path):
    picurl = ''
    for picurl in PicContent:
        save_pic(picurl,path)



def save_pic(picurl,path):
    searchname = '(http(s?)://.*?\.(jpg|gif|png|bmp))'
    name = re.findall(searchname,picurl)
    #name = str.decode(name, )
    print('picurl---->'+picurl)
    print('name---->'+str(name))
    if len(name)==0:
        print('name is null')
    #     searchname = '.*?\.gif'
    #     name = re.findall(searchname,picurl)
    # if len(name)==0:
        return False
    filename1 = name[0]
    filenamelist = filename1[0].split('/')
    filename = filenamelist[len(filenamelist)-1]
    print('filename------>'+filename)
    tryTimes = 10
    while tryTimes != 0:
        tryTimes -= 1
        if os.path.exists(filename):
            print(filename,' exist, skip~~~')
            return True

        if download(filename,name,path):
            break

    if tryTimes != 0:
        print(filename,' is download over')
    else:
        print(picurl+' is failed to download, please check')



def download(filename,name,path):
    try:
        print('begin download ====>'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        #requests.
        namestr = name[0][0].replace("u'", "'", 1)
        r = requests.get(namestr, params=None, timeout=10)
        f= open(path+'/'+filename, 'wb')
        f.write(r.content)
        f.close()
        print('end download ====>'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        return True
    except Exception, e:
        print('unknown exception : '+e.message)
        return ''


url = ''
pic_url(url, '/Users/Shotacon/Desktop/pic')
