import sys, json
import torch
import os
import numpy as np

import encoder
import model
import framework


# Some basic settings
root_path = '.'

ckpt = 'ckpt/school_cnn_softmax.pth.tar'


with open(os.path.join(root_path, 'benchmark/school/rel2id.json'), 'r',encoding='utf-8') as data_file:    
    rel2id= json.load(data_file)

with open('benchmark/school/word2id.json', 'r',encoding='utf-8') as data_file:    
    wordi2d = json.load(data_file)
word2vec = np.load(os.path.join(root_path, 'benchmark/school/word2vec.npy'))

# Define the sentence encoder
sentence_encoder = encoder.CNNEncoder(
    token2id=wordi2d,
    max_length=40,
    word_size=50,
    position_size=5,
    hidden_size=230,
    blank_padding=True,
    kernel_size=3,
    padding_size=1,
    word2vec=word2vec,
    dropout=0.5
)

# Define the model
model = model.SoftmaxNN(sentence_encoder, len(rel2id), rel2id)

# # Define the whole training framework
# framework = framework.SentenceRE(
#     train_path=os.path.join(root_path, 'benchmark/school/train_dataset.txt'),
#     val_path=os.path.join(root_path, 'benchmark/school/test_dataset.txt'),
#     test_path=os.path.join(root_path, 'benchmark/school/test_dataset.txt'),
#     model=model,
#     ckpt=ckpt,
#     batch_size=32,
#     max_epoch=100,
#     lr=0.1,
#     weight_decay=1e-5,
#     opt='sgd'
# )

# # Train the model
# framework.train_model()

# # Test the model
# framework.load_state_dict(torch.load(ckpt)['state_dict'])
# result = framework.eval_model(framework.test_loader)

# # Print the result
# print('Accuracy on test set: {}'.format(result['acc']))
result = model.infer({"text": "包括专业英语测试、专业面试及心理素质测试，主要测试营员专业英语能力，掌握本专业系统知识的情况，攻读硕士、博士学位的目的，科研计划以及心理素质等。重在考查营员综合运用所学知识的能力，科研创新能力以及对本学科前沿领域及最新研究动态的掌握情况等。", "h": {"pos": [49,50]}, "t": {"pos": [54,55]}})
print(result)
