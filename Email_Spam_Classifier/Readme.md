## Email Spam Classifier
## Aim:To classify the email whether spam or not spam(ham)
* Naive Bayes work on dependent events and the probability of an event occurring in the future that can be detected from the previous occurring of the same event. 
* This technique can be used to classify spam e-mails, words probabilities play the main rule here. 
* If some words occur often in spam but not in ham, then this incoming e-mail is probably spam
## Fundamental steps involved in text preprocessing:  
A. Cleaning the raw data   
* Lowering case
* Removal of special characters
* Removal of stopwords
* Removal of hyperlinks
* Removal of numbers
* Removal of whitespaces
B. Tokenizing the cleaned data
* To get a clear idea about the most frequent words used we make a word cloud.
* In Naive Bayes algorithm the input columns should be numerical so we have to convert (VECTORIZE) the column.
* TF-ID Vectorizer
* Count-vectorizer are used
Using TF-ID vectorizer - classifier accuracy 96.41% ;F1-score: 0.856
Using Count vectorizer - classifier accuracy 98.44% ;F1-score: 0.944


