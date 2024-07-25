#import os
#path='data/empty/'
#imgList=os.listdir(r'D:\Urban\yolov4\darknet\build\darknet\x64\data\empty')
#file = open('train.txt', 'a')
#for img in imgList:
#    name = img.split(".")[0]
#    if img.split(".")[1] == 'jpg':
#        imgPath = path + img +'\n'
#        #open(rf"D:\Urban\yolov4\darknet\build\darknet\x64\data\empty\{name}.txt", "w+")
#        print(imgPath)
#        file.write(imgPath)
#file.close()

#data/empty/Trassa_Pust 36787.jpg


def has_letters(text):
  """
  Проверяет, содержит ли строка хотя бы одну букву.

  Args:
    text: Строка, которую нужно проверить.

  Returns:
    True, если строка содержит хотя бы одну букву, иначе False.
  """

  for char in text:
    if char.isalpha():
      return True
  return False

# Пример использования
text1 = "Привет мир!"
text2 = "123в45"
text3 = ""

print(f"Строка '{text1}' содержит буквы: {has_letters(text1)}")
print(f"Строка '{text2}' содержит буквы: {has_letters(text2)}")
print(f"Строка '{text3}' содержит буквы: {has_letters(text3)}")