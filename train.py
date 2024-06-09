import os
import tensorflow as tf
import logging
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import LearningRateScheduler
from model import build_net_1
from model import build_net_3

# Parameters setting
## How to determine the numbers of batch_size and nun_epochs to achieve 最佳訓練狀態
## Please understand the concepts of each parameters and refer to the sample code
#data_dir = 'datasets/all_data/cleaned_data'
data_dir = 'Traditional_Chinese_Data'
#ckpt_path = 'checkpoints/cn_ocr-{epoch:04d}.weights.h5'
image_height = 64
image_width = 64
batch_size = 32
num_epochs = 1000

def train_model():
    # Load all characters
    all_characters = sorted([d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))])
    num_classes = len(all_characters)
    print(f'Number of classes: {num_classes}')

    # 數據生成器：加載數據和增強
    ## Is the percentage of validation and training important for training?
    train_datagen = ImageDataGenerator(
        rescale = 1./255,
        rotation_range = 10,
        width_shift_range = 0.1,
        height_shift_range = 0.1,
        shear_range = 0.1,
        zoom_range = 0.1,
        horizontal_flip = True,
        validation_split = 0.2  # Use 20% for validation
    )

    train_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size = (image_height, image_width),
        batch_size = batch_size,
        class_mode = 'sparse',
        subset = 'training',
        color_mode = 'grayscale'
    )

    validation_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size = (image_height, image_width),
        batch_size = batch_size,
        class_mode = 'sparse',
        subset = 'validation',
        color_mode = 'grayscale'
    )

    # 初始化模型
    model = build_net_1((64, 64, 1), num_classes)
    model.summary()
    print('model loaded')

    # 編譯模型
    model.compile(optimizer = tf.keras.optimizers.Adam(),
                  loss = tf.keras.losses.SparseCategoricalCrossentropy(),
                  metrics = ['accuracy'])

    '''
    # 使用fit方法訓練模型
    model.fit(train_generator,
              validation_data = validation_generator,
              validation_steps = 1000,
              epochs = num_epochs,
              steps_per_epoch = 1024)
    '''

    try:
        model.fit(train_generator,
                  validation_data = validation_generator,
                  validation_steps = 1000,
                  epochs = num_epochs,
                  steps_per_epoch = 1024)
    except KeyboardInterrupt:
        model.save_weights('final_weights.weights.h5')
        model.save('cn_ocr_model.h5')
    
        
    # 保存模型權重和模型結構
    model.save_weights('final_weights.weights.h5')
    model.save('cn_ocr_model.h5')

    '''
    
    start_epoch = 0
    latest_ckpt = tf.train.latest_checkpoint(os.path.dirname(ckpt_path))
    if latest_ckpt:
        start_epoch = int(latest_ckpt.split('-')[1].split('.')[0])
        model.load_weights(latest_ckpt)
        logging.info('model resumed from: {}, start at epoch: {}'.format(latest_ckpt, start_epoch))
    else:
        logging.info('passing resume since weights not there. training from scratch')

    
    model.compile(optimizer = tf.keras.optimizers.Adam(),
                  loss = tf.keras.losses.SparseCategoricalCrossentropy(),
                  metrics = ['accuracy'])
    
    callbacks = [tf.keras.callbacks.ModelCheckpoint(ckpt_path,
                                                    save_weights_only = True,
                                                    verbose = 1,
                                                    save_freq = 'epoch')]
    try:
        model.fit(train_generator,
                  validation_data=validation_generator,
                  validation_steps=1000,
                  epochs=15000,
                  initial_epoch=start_epoch,
                  steps_per_epoch=1024,
                  callbacks=callbacks)
    except KeyboardInterrupt:
        model.save_weights(ckpt_path.format(epoch=0))
        logging.info('keras model saved.')
    
    model.save_weights(ckpt_path.format(epoch=0))
    model.save(os.path.join(os.path.dirname(ckpt_path), 'cn_ocr.h5'))
    '''

if __name__ == "__main__":
    train_model()