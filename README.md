# bird-identification
Small project to identify photos with and without birds using a convolutional neural network (CNN) from TensorFlow (Keras library).

This project was build using Google colab. The notebook `Birds.ipynb` can also be accessed on the link:
https://colab.research.google.com/drive/1MulvuK2NKyivPijppWD6BjofQjwHxFgS

The images used to train the CNN are not available due to space. However, the weights of the trained model are saved in the file `checkpoint`, that can be recovered using `model.load_weights(checkpoint_path)`. 
In the last epoch trained, the perfromance of the model was: ~97% accuracy on the traning set (70% of the images) and ~95% on the validation set (30% of the images).

The script `bird_identification.py` was used to label the original images, moving them to their respective folder ('birds' or 'nobirds').
