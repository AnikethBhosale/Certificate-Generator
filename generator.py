from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pandas as pd
import cv2
import cvzone


#DF 
df = pd.read_csv('test.csv')
n=len(df.columns)
#print(n)
r=len(df)
#print(r)

#Getting cordinates
image = cv2.imread('TechFusioncertificate.png')
coordinates=[]
def getCoordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates.append((x, y))
        if len(coordinates) == n:
            cv2.destroyAllWindows()


print(f'Choose {n} coordinates\n')



# Resize Image
original_height, original_width, _ = image.shape
display_width = original_width // 2
display_height = original_height // 2
resized_img = cv2.resize(image, (display_width, display_height))

# Display 
cv2.imshow('resized_image', resized_img)
cv2.setMouseCallback('resized_image', getCoordinates)
cv2.waitKey(0)
print(coordinates)



#final certificates 
fontSize = []
for i in range(n):
    s = input(f"Enter font size for column {i+1}: ")
    fontSize.append(int(s))

for i in range(r):
  img = Image.open('TechFusioncertificate.png')
  I1 = ImageDraw.Draw(img)
  for j in range(n):
    bbox =I1.textbbox((0, 0),str(df.iloc[i,j]) , ImageFont.truetype('C:\\Windows\\Fonts\\MTCORSVA.ttf', fontSize[j] ))

    adjusted_x = coordinates[j][0]*2 -  (bbox[2] - bbox[0]) //2
    adjusted_y = coordinates[j][1]*2 - (bbox[3] - bbox[1]) // 2

    I1.text((adjusted_x,adjusted_y) , text=str(df.iloc[i,j]), font=ImageFont.truetype('C:\\Windows\\Fonts\\MTCORSVA.ttf', fontSize[j]), fill=(225, 0, 0))
  img.save(f'test_{i+1}.png')