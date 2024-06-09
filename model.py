from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Layer

def build_net_1(input_shape, num_classes):
    model = Sequential()
    
    model.add(Conv2D(32, (3, 3), activation = 'relu', input_shape = input_shape))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    model.add(Conv2D(64, (3, 3), activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    model.add(Flatten())

    model.add(Dense(128, activation = 'relu'))
    ##model.add(Dropout(0.5))

    model.add(Dense(num_classes, activation = 'softmax'))

    return model

def build_net_2(input_shape, num_classes):

    CNN = Sequential()

    CNN.add( Conv2D( 5, kernel_size = (2,2), padding = 'same', 
                 input_shape = input_shape, name = 'Convolution' ) )
    CNN.add( MaxPooling2D( pool_size = (2,2), name = 'Pooling' ) )
    CNN.add( Flatten( name = 'Flatten' ) )
    CNN.add( Dropout( 0.5, name = 'Dropout_1' ) )
    CNN.add( Dense( 512, activation = 'relu', name = 'Dense' ) )
    CNN.add( Dropout( 0.5, name = 'Dropout_2' ) )
    CNN.add( Dense( num_classes, activation = 'softmax', name = 'Softmax' ) )
    CNN.summary()

    return CNN

def build_net_3(input_shape, num_classes):
    model = Sequential()

    model.add(Conv2D(input_shape = input_shape, filters = 32, kernel_size = (3, 3), strides = (1, 1),
                     padding = 'same', activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)), padding = 'same')

    model.add(Conv2D(filters = 64, kernel_size = (3, 3), padding = 'same'))
    model.add(MaxPooling2D(pool_size = (2, 2), padding = 'same'))

    model.add(Flatten())

    model.add(Dense(num_classes, activation = 'softmax'))

    return model