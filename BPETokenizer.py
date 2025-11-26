import Utils 

class BPETokenizer: 
    def __init__(self, vocab_size: int = 256):
        self.vocab_size = vocab_size
        self.vocab={i:chr(i) for i in range(256)} 
        self.merges={}

    def train(self, text: str) -> list[int]:
        ids= list(text.encode('utf-8'))
        ids,merges= Utils.create_vocab(ids, self.vocab_size)
        self.merges=merges
        for w1,w2 in merges.keys():
          self.vocab[self.merges[(w1,w2)]]=self.vocab[w1]+ self.vocab[w2]
        return ids
   
    def tokenize(self,text:str)->list[int]:
        tokens= list(text.encode('utf-8'))
        while len(tokens)>1:
            freqs=Utils.freqs(tokens)
            pair=min(freqs, key=lambda p: self.merges[p], default=None)
            if pair is None or pair not in self.merges:
                break
            ids=self.merges[pair]
            tokens=Utils.merge(tokens, pair, ids)
        return tokens


    def get_merges(self) -> dict[tuple[int,int],int]:
        return self.merges
    
    def decode(self, ids: list[int]) -> str:
        text= "".join([self.vocab[id] for id in ids])
        return text
    
    def get_vocab(self) -> dict[int,str]:
        return self.vocab