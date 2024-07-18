import os 
path='data/empty/'
imgList=os.listdir(r'D:\Urban\yolov4\darknet\build\darknet\x64\data\empty')
file = open('train.txt', 'a')
for img in imgList:
    name = img.split(".")[0]
    if img.split(".")[1] == 'jpg':
        imgPath = path + img +'\n'
        #open(rf"D:\Urban\yolov4\darknet\build\darknet\x64\data\empty\{name}.txt", "w+")
        print(imgPath)
        file.write(imgPath)
file.close()

#data/empty/Trassa_Pust 36787.jpg
