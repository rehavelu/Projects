# Stock-Price-Prediction-using-Keras-and-Recurrent-Neural-Network
This repository contains a Python implementation of using Long Short-Term Memory (LSTM) neural networks to predict the stock price of a company. The implementation uses the Keras deep learning library, along with other Python libraries such as Pandas, NumPy, and Matplotlib.

The code uses Google stock price data to train the LSTM model, and then predicts the future stock prices of the company based on the trained model. The repository also includes a Jupyter notebook with a step-by-step walkthrough of the implementation, along with sample data for the Google stock price.
LSTM has logic gates (input, output and forget gates) which give inherent ability for it to retain information that is more relevant and forgo unnecessary information. This makes LSTM a good model for interpreting patterns over long periods.
The important thing to note about LSTM is the input, which needs to be in the form of a 3D vector (samples, time-steps, features). Hence, the input has to be reshaped to fit this.
