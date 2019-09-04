from torch.utils.data import DataLoader

from .model import BERT
from .trainer import BERTTrainer
from .dataset import BERTDataset, WordVocab, build

corpus_path='G:/SMERT/corpus.txt'
output_path='G:/SMERT/test.txt'

build()
print("Loading Vocab", output_path)
vocab = WordVocab.load_vocab(output_path)
print("Vocab Size: ", len(vocab))






#with open(args.corpus_path, "r", encoding=args.encoding) as f:
#    vocab = WordVocab(f)

#print("VOCAB SIZE:", len(vocab))
#vocab.save_vocab(args.output_path)