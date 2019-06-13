# Stock Chatbot

## **Requirements**
- Python(==3.6)
- Twisted
- Rasa NLU
- chatito
- rasa-nlu-trainer
- wxpy

## **Installation**
<code>git clone https://github.com/mathfather/StockBot</code>

## **Generate training and testing data**
Open the root folder. Generate the data using the following command:</p>
<code>npx chatito data_generator/intent.chatito --format=rasa --outputPath=data --trainingFileName=trainingset.json --testingFileName=testingset.json intent.chatito</code>

The training and testing date will be saved in a seperate folder called ***data***, which is under the root folder.

If you want to check out the data by yourself, try the following:</p>
<code>rasa-nlu-trainer</code>

And the data visualization will be shown in the browser.

## **Train the model**
Train the model using the following command:</p>
<code>python model.py</code>

After the training process, the trained model will be saved in ***models/default***, with its name looks like this: 'model_20190531-173549'.

## **Use the bot to search information about security**

To run the bot on wechat, run:</p>
<code>python wechat.py</code> 

Scanned the QR code on screen with your wechat app to make your account the host of the bot.

Then, use your own language to ask the chatbot your question. An Example is listed belowed.
![](https://github.com/mathfather/StockBot/blob/master/display/chat_example.png)

## **Use the automatic generated testing set to verify your model's accuracy**

To test your model's ability in information extraction, use the following:</p>
<code>python accuracy.py</code>

It will output the accuracy in the terminal.
