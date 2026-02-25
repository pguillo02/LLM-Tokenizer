import utils

class BPE_tokenizeer:
    
    def __init__(self, merges):
        self.merges = merges

    @classmethod
    def train(cls, training_text, training_iterations):
        tokens = list(training_text.encode("utf-8"))
        return cls(utils.training_tokenizer(tokens, training_iterations))

    def encoder(self):
        pass

    def decoder(self):
        pass

if __name__ == "__main__":

    text_type: str = """The original  BPE algorithm operates by iteratively replacing the most common contiguous sequences of characters in a target text with unused 'placeholder' bytes. The iteration ends when no sequences can be found, leaving the target text effectively compressed. Decompression can be performed by reversing this process, querying known placeholder terms against their corresponding denoted sequence, using a lookup table. In the original paper, this lookup table is encoded and stored alongside the compressed text."""

    tok = BPE_tokenizeer.train(text_type, 3)

    print(tok.merges)