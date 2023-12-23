
### Setup an OpenAI account

Step 1: If you don't have an OpenAI account yet, go to openai.com and create a new account.

Step 2: Go to https://platform.openai.com/account/billing/overview and update payment information.


### Install OpenAI

Step 1: Create a new conda environment:

       conda create -n cmpe244

Step 2: Activate the environment:

       conda activate cmpe244

Step 3: Install OpenAI:

       pip install openai==0.28
   

### Model Training and Testing

Step 1: Go to [OpenAI website](https://platform.openai.com/api-keys) and create a new kew.

My key is saved in [key.txt](https://github.com/Ezgii/CMPE244-Project/blob/main/ChatGPT/key.txt).

Step 2: First, fine tune the `gpt-3.5-turbo` model with 10 questions about "describing the cmpe244 project", using [train_fine_tuning.py](https://github.com/Ezgii/CMPE244-Project/blob/main/ChatGPT/train_fine_tuning.py).

> The model ID of the resulting fine tuned model: `ft:gpt-3.5-turbo-0613:personal::8NEuPpAn`

> (Note: The model ID of the fine tuned models can be seen [here](https://platform.openai.com/finetune?filter=all).)

Step 3: Test the fine tuned model using [test_fine_tuning.py](https://github.com/Ezgii/CMPE244-Project/blob/main/ChatGPT/test_fine_tuning.py).

Step 4: Fine tune the `ft:gpt-3.5-turbo-0613:personal::8NEuPpAn` model with 10 questions about "showing a demo".

> The model ID of the resulting fine tuned model: `ft:gpt-3.5-turbo-0613:personal::8NFEYSMJ`

Step 5: Test the fine tuned model. 

Step 6: Test the model further through [live chat](https://github.com/Ezgii/CMPE244-Project/blob/main/ChatGPT/live_chat.py).

### Embedding the Custom Model into Webpage

Step 1: Install and activate the AI Engine plug-in (by Jordy Meow) in WordPress.

Step 2: Select the below settings:

![image](https://github.com/Ezgii/CMPE244-Project/assets/4748948/932ef6dc-fb71-4707-abc0-b1a76a7de07a)

![image](https://github.com/Ezgii/CMPE244-Project/assets/4748948/3bb81757-912d-43a5-addf-349a93b627b6)

![image](https://github.com/Ezgii/CMPE244-Project/assets/4748948/4efbd5a3-3e3d-41ed-ac27-3475cf7dc83d)

![image](https://github.com/Ezgii/CMPE244-Project/assets/4748948/2cbd2dbb-0a7c-4a7d-90fc-cfa0161b9b96)

Step 3: On the webpage, add the shortcode: [mwai_chatbot_v2]

Step 4: Save and try it out!

![image](https://github.com/Ezgii/CMPE244-Project/assets/4748948/b8a703e8-7ac1-463f-8edf-a9411d918eae)


