
from transformers import PretrainedConfig
class CustomAIConfig(PretrainedConfig):
    model_type = "CustomAI"  # Change to the appropriate model type name

    def __init__(
        self,
        vocab_size:int=1000,
        n_embd:int=384,
        n_head:int=4,
        n_layer:int=4,
        dropout:float=0.2,
        **kwargs
    ):
        self.vocab_size = vocab_size
        self.n_embd = n_embd
        self.n_head = n_head
        self.n_layer = n_layer
        self.dropout = dropout
        super().__init__(**kwargs)
