# -*- coding: utf-8 -*-  
  
from PIL import Image  
import glob, os  


dir_20 = ['Amphiprioninae',
'Arapaima',
'Blacktip_Reef_Shark',
'Blue_Chromis',
'Common_Dragonet',
'Emerald_Toucanet',
'Eudocimus_Ruber',
'Foxface_Rabbitfish',
'Goldbelly_Damsel',
'Grey_Heron',
'Lemon_Damsel',
'Leporinus_Fasciatus',
'Pied_Tamarin',
'Red-Bellied_Piranha',
'Red_Sea_Sailfin_Tang',
'Starfish',
'Stingray',
'Sunbittern',
'Thornback_Ray',
'Toco_Toucan',
'Yellowfin_Surgeonfish']

#图片批处理  
def timage():  
    for _dir in dir_20:
        img_num = 1
        for files in glob.glob('./bak/{}/*.JPG'.format(_dir)):
            filepath,filename = os.path.split(files)  
            filterame,exts = os.path.splitext(filename)  
            #输出路径  
            opfile1 = r'./1/{}/'.format(_dir)
            opfile2 = r'./2/{}/'.format(_dir)
            opfile4 = r'./4/{}/'.format(_dir)
            #判断opfile是否存在，不存在则创建  
            if (os.path.isdir(opfile1)==False):  
                os.mkdir(opfile1)  

            if (os.path.isdir(opfile2)==False):  
                os.mkdir(opfile2)  

            if (os.path.isdir(opfile4)==False):  
                os.mkdir(opfile4)  

            im = Image.open(files)  
            w,h = im.size  
            #im_ss = im.resize((400,400))  
            #im_ss = im.convert('P')  
            im_ss = im.resize((int(w*1), int(h*1)))  
            im_ss.save(opfile1+_dir+str(img_num)+'.jpg')

            im_ss = im.resize((int(w*0.5), int(h*0.5)))  
            im_ss.save(opfile2+_dir+str(img_num)+'.jpg')

            im_ss = im.resize((int(w*0.25), int(h*0.25)))  
            im_ss.save(opfile4+_dir+str(img_num)+'.jpg')

            img_num += 1  
        print("finish {}".format(_dir))
    


if __name__=='__main__':  
    timage()  
    print("Detail Completed!")