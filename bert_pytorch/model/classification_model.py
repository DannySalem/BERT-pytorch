import torch.nn as nn

from .bert import BERT

class BERTLCM(nn.Module):
    """
    BERT Language Model
    Text Classification
    """

    def __init__(self, bert: BERT, vocab_size):
        """
        :param bert: BERT model which should be trained
        :param vocab_size: total vocab size for masked_lm
        """

        super().__init__()
        self.bert = bert
        self.class_model = ClassificationModel(self.bert.hidden, vocab_size)

    def forward(self, x, segment_label):
        x = self.bert(x, segment_label)
        #return self.bert(x, segment_label)
        return self.class_model(x)



class ClassificationModel(nn.Module):
    """
    predicting class of sentence 
    binary classification problem, 0->not toxic, 1-> toxic
    """

    def __init__(self, hidden, vocab_size):
        """
        :param hidden: output size of BERT model
        :param vocab_size: total vocab size
        """
        super().__init__()
        self.linear = nn.Linear(hidden, 2)
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, x):
        #return self.softmax(self.linear(x))#(x[:, 0]))
        return self.softmax(self.linear(x[:, 0]))
        #return self.linear(x)[:, 0]
