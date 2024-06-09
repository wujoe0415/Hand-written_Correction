# Hand-written Article Correction

## Introduction

In a formal situation, we need to ensure that everything is correct. So here is what we are working on, “**How can we accurately digitalize and correct hand-written traditional Chinese articles to ensure they are coherent and error-free**?”. And the problem is composed of these two things. Translate the input image to text and try to find any errors or unreasonable words. Finally, we will provide the correction version to the user.

## Pipeline

![image-20240610013022812](https://hackmd.io/_uploads/H1bSuwQr0.png)

## Main Approach

![image-20240610013346234](https://hackmd.io/_uploads/BkNUOvQH0.png)

There are 4 steps in the training process. 

![image-20240610013314907](https://hackmd.io/_uploads/HyZOdD7r0.png)

![image-20240610013403578](https://hackmd.io/_uploads/ryY5_vXHA.png)

![image-20240610013414762](https://hackmd.io/_uploads/B1Ij_DXBC.png)

## Result

![image-20240610013516588](https://hackmd.io/_uploads/B1rh_PmH0.png)

![image-20240610013533068](https://hackmd.io/_uploads/BJlTdPmrA.png)

## Reference

- ocrcn_tf2: https://github.com/jjcheer/ocrcn_tf2
- CnOCR: https://github.com/breezedeus/CnOCR
- Tesseract: https://github.com/tesseract-ocr/tesseract
- Traditional Chinese Handwriting text dataset: https://github.com/chenkenanalytic/handwritting_data_all
- Google Cloud Vision API: https://cloud.google.com/vision/docs/ocr
- Adobe Acrobat: https://experienceleague.adobe.com/zh-hant/docs/document-cloud-learn/acrobat-learning/getting-started/scan-and-ocr

- Word spliting method: https://www.cnblogs.com/zxy-joy/p/10687152.html 
