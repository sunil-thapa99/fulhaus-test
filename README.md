## Train model

Model: "sequential_3"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d_12 (Conv2D)          (None, 128, 128, 64)      1792      
                                                                 
 max_pooling2d_6 (MaxPooling  (None, 64, 64, 64)       0         
 2D)                                                             
                                                                 
 conv2d_13 (Conv2D)          (None, 64, 64, 128)       73856     
                                                                 
 conv2d_14 (Conv2D)          (None, 64, 64, 128)       147584    
                                                                 
 conv2d_15 (Conv2D)          (None, 64, 64, 128)       147584    
                                                                 
 max_pooling2d_7 (MaxPooling  (None, 32, 32, 128)      0         
 2D)                                                             
                                                                 
 flatten_3 (Flatten)         (None, 131072)            0         
                                                                 
 dense_9 (Dense)             (None, 128)               16777344  
                                                                 
 dense_10 (Dense)            (None, 64)                8256      
                                                                 
 dropout_3 (Dropout)         (None, 64)                0         
                                                                 
 dense_11 (Dense)            (None, 3)                 195       
                                                                 
=================================================================
Total params: 17,156,611
Trainable params: 17,156,611
Non-trainable params: 0
_________________________________________________________________

## Test model
-   Run python app.py to start flask

## Output
``` 
{
    "predictions": "Bed"
}
```