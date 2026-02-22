"""Next Word Prediction


Download Datasets (220.50 KB)
Start Solving
More about this project
LGM: Exploring next word prediction using long-form text data to uncover patterns, insights, and key questions.

Assignment
You've certainly heard about the GPT language models that are used by many AI tools such as ChatGPT. What these models do, in simple terms, they try to accurately predict what the most logical next word would be given an input. In this project, you will try to implement a similar model, of course, much less advanced. Select a set of training data with a lot of real-life text (e.g. a book) and use it to train a neural network which, given input with a couple of words, returns the list of the most probable words that would make for a logical continuation.

Tips

Start by reading in the text data and splitting the long text into individual words;
Feel free to explore, analyze and describe the text using statistics such as you would do with any other dataset; look for the most and least frequently occurring words as well as common combinations of two consecutive words - you can use these findings for testing later;
For simplicity, let's select a set length of input X, e.g. 5 words; feel free to experiment with different lengths;
Iterate through all words from the dataset and for all possible sets of X consecutive words (input) note what is the word that comes next (output);
Encode the input and output words in form of Boolean arrays where each value corresponds to a unique word that appears in the original text; Don't forget to split the data into training, testing, and possibly, validation sets;
Train and evaluate a neural network using these input and output sets; Start with a simple model and experiment by adding and tuning layers;
Test the final model yourself by specifying a sentence with X words that doesn't necessarily exist in the source text and observe which words will the model suggest as logical continuations;
Data Description
The file book.txt contains the entire eBook 'The Adventures of Sherlock Holmes' by Arthur Conan Doyle in Plain Text (UTF-8) format. This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever under the terms of the Project Gutenberg License (https://www.gutenberg.org/).

However, you can use any other long text or book as input for this project.

Practicalities
Make sure that the solution reflects your entire thought process - it is more important how the code is structured rather than the final results."""

# load book.txt
with open('book.txt', 'r') as f:
    text = f.read()
# split text into words
words = text.split()
# create a set of unique words
unique_words = set(words)
# create a dictionary to map each word to an index
word_to_index = {word: i for i, word in enumerate(unique_words)}
# create input and output pairs
X = []
y = []
for i in range(len(words) - 5):
    X.append([word_to_index[words[j]] for j in range(i, i + 5)])
    y.append(word_to_index[words[i + 5]])
# convert X and y to numpy arrays
import numpy as np
X = np.array(X)
y = np.array(y)
# split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# build a simple neural network model
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
model = Sequential()
model.add(Embedding(len(unique_words), 100, input_length=5))
model.add(LSTM(100))
model.add(Dense(len(unique_words), activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# train the model
model.fit(X_train, y_train, epochs=10, batch_size=128)
# evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')
# test the model with a new input
def predict_next_word(model, input_text):
    input_words = input_text.split()[-5:]
    input_indices = [word_to_index.get(word, 0) for word in input_words]
    input_array = np.array(input_indices).reshape(1, -1)
    predicted_index = model.predict(input_array).argmax()
    for word, index in word_to_index.items():
        if index == predicted_index:
            return word
input_text = "The detective was very"
predicted_word = predict_next_word(model, input_text)
print(f'Predicted next word: {predicted_word}')
