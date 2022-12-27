# Hate-Speech-Detection

Main motive for this project is to detect any kind of hate speech or obscene behavior on Twitter. 
We have a dataset of tweets that we worked on, to create a model that helps us categorize those tweets as offensive.

Text:
We have processed the Twitter data and categorized tweets into “Hateful” and “Normal”.
we have used the Logistic Regression algorithm. 
The reason why we went with this algorithm is that it gave us the best accuracy compared to other models
like Naive Bayes, SVM, Random Forest, etc. 
Dataset of almost 86000 tweets and concatenated the texts and emojis.
Data-preprocessing.
lemmatize the texts to remove all the spaces and special characters.
Tokenize the text to get the root words out of the phrases.
Vectorize them to convert the text data into numerical data.
Used the library textblob calculates the subjectivity, which is basically scored in a range of 0, 1, as well as polarity, which is
scoured from -1, 1, and based on these, we get to categorize the tweets into hateful and normal.

Emoji:
Created a function for emoticons where we first tokenize each word of the sentence using word_tokenize. 
Then we check whether the word is an emoji or not, if no then we add it to the sentence else we convert the emoji
into its corresponding meaning (ie 😀 turns to smile) using the ‘emoji.demojize’ function
imported from library emoji, convert the customary ':' sign attached to it to a space,
remove extra spaces and then add it to the sentence. 
Then we convert our words into root words after analyzing their context in the sentence. 
Then, once we have the data in text form, we repeat all the steps we did above in the text part.

Memes:
We first used pytesseract for optical character recognition (OCR).
Extracts the texts in an image and concatenates that into strings or lists.
Treated the data just like the text data and repeated all the steps we did above in the text part.
