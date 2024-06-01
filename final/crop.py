import cv2
import numpy as np

'''水平投影'''
def getHProjection(image):
    hProjection = np.zeros(image.shape,np.uint8)
    #图像高与宽
    (h,w)=image.shape
    #长度与图像高度一致的数组
    h_ = [0]*h
    #循环统计每一行白色像素的个数
    for y in range(h):
        for x in range(w):
            if image[y,x] == 255:
                h_[y]+=1
    #绘制水平投影图像
    for y in range(h):
        for x in range(h_[y]):
            hProjection[y,x] = 255
    # cv2.imshow('hProjection2',hProjection)

    return h_

def getVProjection(image):
    vProjection = np.zeros(image.shape,np.uint8)
    #图像高与宽
    (h,w) = image.shape
    #长度与图像宽度一致的数组
    w_ = [0]*w
    #循环统计每一列白色像素的个数
    for x in range(w):
        for y in range(h):
            if image[y,x] == 255:
                w_[x]+=1
    #绘制垂直平投影图像
    for x in range(w):
        for y in range(h-w_[x],h):
            vProjection[y,x] = 255
    #cv2.imshow('vProjection',vProjection)
    return w_

def resize_to_area(image, target_area):
    # Calculate the aspect ratio of the original image
    aspect_ratio = image.shape[1] / image.shape[0]

    # Calculate the width and height for the target area
    target_width = int(np.sqrt(target_area * aspect_ratio))
    target_height = int(target_area / target_width)

    # Resize the image to the target width and height
    resized_image = cv2.resize(image, (target_width, target_height))

    return resized_image

def go_crop(img_fp, blocks):
    #读入原始图像
    origineImage = cv2.imread(img_fp)
    origineImage = resize_to_area(origineImage, 100000)
    # 图像灰度化
    #image = cv2.imread('test.jpg',0)
    image = cv2.cvtColor(origineImage,cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray',image)
    # exit
    # 将图片二值化
    retval, img = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
    # cv2.imshow('binary',img)
    #图像高与宽
    (h,w)=img.shape
    Position = []
    #水平投影
    H = getHProjection(img)

    start = 0
    H_Start = []
    H_End = []
    #根据水平投影获取垂直分割位置
    for i in range(len(H)):
        if H[i] > 0 and start ==0:
            H_Start.append(i)
            start = 1
        if H[i] <= 0 and start == 1:
            H_End.append(i)
            start = 0
    #分割行，分割之后再进行列分割并保存分割位置
    for i in range(len(H_Start)):
        #获取行图像
        cropImg = img[H_Start[i]:H_End[i], 0:w]
        #cv2.imshow('cropImg',cropImg)
        #对行图像进行垂直投影
        W = getVProjection(cropImg)
        Wstart = 0
        Wend = 0
        W_Start = 0
        W_End = 0
        for j in range(len(W)):
            if W[j] > 0 and Wstart ==0:
                W_Start =j
                Wstart = 1
                Wend=0
            if W[j] <= 0 and Wstart == 1:
                W_End =j
                Wstart = 0
                Wend=1
            if Wend == 1:
                Position.append([W_Start,H_Start[i],W_End,H_End[i]])
                Wend =0
    #根据确定的位置分割字符
    counter = 0
    # print(blocks)
    for m in range(len(Position)):
        if (counter in blocks):
            cv2.rectangle(origineImage, (Position[m][0],Position[m][1]), (Position[m][2],Position[m][3]), (229 ,0 ,238), 1)
        else:
            cv2.rectangle(origineImage, (Position[m][0],Position[m][1]), (Position[m][2],Position[m][3]), (0 ,229 ,238), 1)
        counter = counter + 1
    cv2.imshow('image',origineImage)
    cv2.waitKey(0)
