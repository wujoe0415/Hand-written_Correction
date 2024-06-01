from cnocr import CnOcr
import cv2
from PIL import ImageFont, ImageDraw, Image
from gpt import get_response
img_fp = './src/11.jpg'
result_path = '1bit.jpg'
# preprocess image
# _img = cv2.imread(img_fp)
# gray = cv2.cvtColor(_img, cv2.COLOR_BGR2GRAY)
# _, binary = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)
# _img = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
# cv2.imwrite(result_path, _img)
ocr = CnOcr(det_model_name="db_resnet34", rec_model_name='doc-densenet_lite_136-gru')
out = ocr.ocr(img_fp)
img = cv2.imread(img_fp)

texts = []
for line in out:
    p1, p2, p3, p4 = line['position']
    cv2.rectangle(img, (int(p1[0]), int(p1[1])), (int(p3[0]), int(p3[1])), color=(0, 255, 0), thickness=2)
    texts.append(line['text'])
    # show text on image
    # fnt = ImageFont.truetype("./src/MaShanZheng-Regular.ttf", 40, encoding='utf-8')
    # img_pil = Image.fromarray(img)
    # draw = ImageDraw.Draw(img)
    # draw.text((int(p1[0]), int(p1[1])), line['text'], font=fnt, fill=(255, 255, 255, 255))
    # img = np.array(img_pil)

with open("result.txt", "w", encoding='utf-8') as file:
    file.write("\n".join(texts))
cv2.imwrite("result.jpg", img)

get_response() # call gpt to get response