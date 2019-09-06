from torch.utils.data import DataLoader

from .model import BERT
from .trainer import BERTTrainer
from .dataset import BERTDataset, WordVocab#, build

corpus_path='G:/SMERT/corpus.txt'
vocab_path='G:/SMERT/vocab.pkl'
train_dataset
seq_len
on_memory = True

#build()
print("Loading Vocab", vocab_path)
vocab = WordVocab.load_vocab(vocab_path)
print("Vocab Size: ", len(vocab))

print("Loading Train Dataset", train_dataset)
train_dataset = BERTDataset(train_dataset, vocab, seq_len=seq_len, on_memory=on_memory)






#with open(args.corpus_path, "r", encoding=args.encoding) as f:
#    vocab = WordVocab(f)

#print("VOCAB SIZE:", len(vocab))
#vocab.save_vocab(args.output_path)