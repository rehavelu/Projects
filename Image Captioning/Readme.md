## Aim:To recognize the context of an image and annotating it with relevant captions using deep learning.
* The dataset consists of 8k images and 5 captions for each image. The features are extracted from both the image and the text captions for input.
* The features will be concatenated to predict the next word of the caption. CNN is used for image and LSTM is used for text. BLEU Score is used as a metric to evaluate the performance of the trained model.
* VGG16 is object detection and classification algorithm which is able to classify 1000 images of 1000 different categories with 92.7% accuracy. It is one of the popular algorithms for image classification and is easy to use with transfer learning.
* Fully connected layer of the VGG16 model is not needed, just the previous layers to extract feature results.
* BLEU Score is used to evaluate the predicted text against a reference text, in a list of tokens.
* The reference text contains all the words appended from the captions data (actual_captions)
* BLEU-score obtained: 0.516880



