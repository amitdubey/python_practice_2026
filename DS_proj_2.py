"""Chatbot Responses



0

Download Datasets (3.34 MB)
Start Solving
More about this project
Company
Spectrm
Job Positions
ML Engineer
Topics
Spectrm: Exploring incomplete dialog transcripts and candidate replies to uncover patterns, insights, and key questions.

Assignment
Knowing what to say is not always easy - especially if you're a chatbot.

Generating answers from scratch is very difficult and would most likely result in nonsense or worse - but definitely not a pleasant user experience. Therefore we're taking one step back and instead provide the correct replies which now "only" have to be chosen in the right dialog context.

In this challenge you're given a dataset with fictional dialogs (adapted from [1]) from which one reply is missing and additionally a list with all missing replies. Your task is to map all missing replies to the correct conversation.

Data Description
The dataset consists of 4 files: train_dialog.txt and test_dialog.txt each contain the conversations. The format is always c##### indicating the conversation number separated by +++$+++ from the reply text. For example one conversation from the training set is the following:

c03253 +++$+++ Wow! This is like my dream room! Are these all records!
c03253 +++$+++ I have about fifteen hundred 78s at this point. I've tried to pare down my collection to the essential...
c03253 +++$+++ God, look at this poster!  I can't believe this room! You're the luckiest guy in the world! I'd kill to have stuff like this!
c03253 +++$+++ Please... go ahead and kill me! This stuff doesn't make you happy, believe me.
c03253 +++$+++ You think it's healthy to obsessively collect things? You can't connect with other people so you fill your life with stuff...  I'm just like all the rest of these pathetic collector losers.
All original conversations are at least four lines long and always the second to last line is missing in the dialogs.

The missing replies are found in the files train_missing.txt and test_missing.txt respectively. For the training dialogs, the conversation number is given with the reply as in the dialog files, e.g. the missing line to the above conversation would be

c03253 +++$+++ Oh, come on! What are you talking about?
The missing lines for the test dialogs always have c00000 as the conversation number but are otherwise formatted the same as the training file. While some of the short replies might be the same, every missing reply belongs to exactly one conversation.

Practicalities
Your task is now to take the missing test replies and map them to the corresponding dialogs. More specifically you should write a script which can be called with the path to a file with the incomplete dialogs and the path to the missing replies and then outputs a file test_missing_with_predictions.txt in the same format as test_missing.txt only with actual conversation numbers from test_dialog.txt instead of c00000.

You can choose whatever approach you want to solve the task and if you use any external libraries provide a requirements.txt file from which these libraries can be installed with pip install -r requirements.txt (you might want to use a virtual environment and when you're done call pip freeze > requirements.txt).

While it is okay to use other resources such as pretrained word embeddings to solve the task, we ask you not to train your algorithm using the original conversations provided with [1] as this would lead to overfitting, i.e. considered cheating.

Besides the accuracy of the predicted conversation labels, we will also evaluate your code with respect to efficiency, maintainability, and readability (it might not hurt to have a look at some style guides).

In addition to the code which solves the task please turn in a text file or pdf with answers to the following questions:

Describe your approach. Which methods did you choose and why?
How do you evaluate your performance?
Where are the weaknesses of your approach? What has to be considered when applying an approach like this in practice?
"""

# read train_dialog.txt and test_dialog.txt
with open('train_dialog.txt', 'r') as f:
    train_dialog = f.readlines()
with open('\\Users\\amitdubey\\Desktop\\gitrepoamit\\learningpython\\chat\\test_dialog.txt', 'r') as f:
    test_dialog = f.readlines()
# read train_missing.txt and test_missing.txt
with open('\\Users\\amitdubey\\Desktop\\gitrepoamit\\learningpython\\chat\\train_missing.txt', 'r') as f:
    train_missing = f.readlines()
with open('\\Users\\amitdubey\\Desktop\\gitrepoamit\\learningpython\\chat\\test_missing.txt', 'r') as f:
    test_missing = f.readlines()
# create a dictionary to map conversation number to dialog
train_dialog_dict = {}
for line in train_dialog:
    conv_num, reply = line.split(' +++$+++ ')
    if conv_num not in train_dialog_dict:
        train_dialog_dict[conv_num] = []
    train_dialog_dict[conv_num].append(reply.strip())
test_dialog_dict = {}
for line in test_dialog:
    conv_num, reply = line.split(' +++$+++ ')
    if conv_num not in test_dialog_dict:
        test_dialog_dict[conv_num] = []
    test_dialog_dict[conv_num].append(reply.strip())
# create a dictionary to map conversation number to missing reply
train_missing_dict = {}
for line in train_missing:
    conv_num, reply = line.split(' +++$+++ ')
    train_missing_dict[conv_num] = reply.strip()
test_missing_dict = {}
for line in test_missing:
    conv_num, reply = line.split(' +++$+++ ')
    test_missing_dict[conv_num] = reply.strip()
# create a dictionary to map missing reply to conversation number
missing_reply_dict = {}
for conv_num, reply in train_missing_dict.items():
    missing_reply_dict[reply] = conv_num
# predict conversation number for test missing replies
predicted_conv_num = {}
for reply in test_missing_dict.values():
    if reply in missing_reply_dict:
        predicted_conv_num[reply] = missing_reply_dict[reply]
    else:
        predicted_conv_num[reply] = 'c00000'
# write predictions to test_missing_with_predictions.txt
with open('test_missing_with_predictions.txt', 'w') as f:
    for reply, conv_num in predicted_conv_num.items():
        f.write(f'{conv_num} +++$+++ {reply}\n')

# Describe your approach. Which methods did you choose and why?
# I read the dialog and missing files and created dictionaries to map conversation numbers to dialogs and missing replies. Then I created a dictionary to map missing replies to conversation numbers. Finally, I predicted the conversation number for each test missing reply by checking if it exists in the missing_reply_dict and wrote the predictions to a new file.

#How do you evaluate your performance?
# I evaluate my performance by checking the accuracy of the predicted conversation numbers against the actual conversation numbers in the test dialog file.
# Where are the weaknesses of your approach? What has to be considered when applying an approach like this in practice?
# The weakness of my approach is that it relies on the exact match of missing replies to predict conversation numbers. If there are any variations in the wording or if the missing reply is not present in the training data, it will not be able to predict the correct conversation number. In practice, it would be important to consider using more sophisticated natural language processing techniques to handle variations in wording and to improve the accuracy of predictions.


