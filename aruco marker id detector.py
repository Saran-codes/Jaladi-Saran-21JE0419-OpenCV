import cv2

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
arucoParams = cv2.aruco.DetectorParameters_create()

n = int(input("No of markers:"))
for i in range(0,n):
    path = input("Enter the path of the marker:")
    image = cv2.imread(path)
    ids = cv2.aruco.detectMarkers(image, arucoDict,parameters=arucoParams)[1]
    print(path,"is the marker with id::",ids[0][0])
      


#marker 1 = LMAO
#marker 2 = XD
#marker 3 = Ha
#marker 4 = HaHa

