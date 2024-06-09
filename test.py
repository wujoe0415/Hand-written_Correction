import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# 加載模型
model = load_model('cn_ocr_model.h5')

# 定義類別標籤
classes = sorted([d for d in os.listdir('datasets/all_data/cleaned_data') if os.path.isdir(os.path.join('datasets/all_data/cleaned_data', d))])

# 定義測試數據資料夾路徑
test_data_dir = 'Traditional_Chinese_Testing_Data'

# 遍歷測試數據資料夾中圖片
results = []
for filename in os.listdir(test_data_dir):
    if filename.endswith('.png'):
        print(filename)
        # 加載圖片並進行預處理
        img_path = os.path.join(test_data_dir, filename)
        img = load_img(img_path, color_mode = 'grayscale', target_size = (64, 64))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis = 0)  # 添加 batch

        # 使用模型進行預測
        predictions = model.predict(img_array)
        predicted_class_index = np.argmax(predictions)
        predicted_class = classes[predicted_class_index]
        
        print(predicted_class)

        # 紀錄預測結果
        results.append((filename, predicted_class))

# 輸出預測結果
with open('predictions.txt', 'w') as f:
    for filename, predicted_class in results:
        f.write(f'{filename}: {predicted_class}\n')

print('Results have been saved')
