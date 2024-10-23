# LIAMA3_chatbot_Arabic_Engligh
This repository is for developing the chatbot on health care question and answer.
In this respository the LIAMA3 with 7 bilions paramters is trained using an RTX3090ti on the available datasets on the Hugging face.

The number of used questions and answers for training the model is 20 milions. The model support question and answers in Arabic, Persian, English and Espanish Languages.




# Requirements 
1. lingua-language-detector
2. torch == 2.4.1
3. torchvision
4. torchaudio
5. packaging
6. ninja
7. einops
8. flash-attn
9. xformers
10. trl
11. peft
12. accelerate
13. bitsandbytes


# GPU_Resource_Requirement
![Screenshot from 2024-10-23 11-21-28](https://github.com/user-attachments/assets/58f28ade-1348-4b87-871a-84f4c26e5853)

# Results 
# Question: I have COVID-19 and I can't breath very well and I am in california what should I do?
# Answer
![image](https://github.com/user-attachments/assets/d2b4a6f5-1c6a-4fea-8525-51f238d57bc9)

# Question: مرحبا أنا في السعودية ولدغتني بعوضة وأعاني من الحمى هل أنا مصاب بالملاريا؟
# Answer
![image](https://github.com/user-attachments/assets/2908298a-128c-42c4-9b47-efabd86c8f71)

# Question: من چه بیمه ای برای بیماری دیابت استفاده کنم؟
# Answer
![image](https://github.com/user-attachments/assets/33fbf3dd-c6db-42d8-8125-d193870026c7)

