from cnocr import CnOcr
import cv2
from PIL import ImageFont, ImageDraw, Image
from gpt import get_response
from crop import go_crop
import re
img_fp = './src/14.jpg'
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

with open("wrong.txt", 'r', encoding='utf-8') as file:
    Lines = file.readlines()
    blocks = []

    if len(Lines) < 4: 
        print("All correct!")
    else:
        num_of_characters = len(Lines[0]) - 7 # remove '正确比率: ' 和 '\n'
        num_of_wrong = len(Lines) - 4
        print(f'总字数: {num_of_characters}, 错误字数: {num_of_wrong}')
        print(f'正确比率: {(num_of_characters - num_of_wrong) / num_of_characters}')

        for i in range(4, len(Lines)):
            print(Lines[i][2:])
            # print(Lines[i].split('|')[1].strip())
            blocks.append(int(Lines[i].split('|')[1].strip()) - 1) # 0-based index

        # print(f'blocks: {blocks}')

    go_crop(img_fp, blocks)
