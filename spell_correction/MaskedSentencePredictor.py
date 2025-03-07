import torch
from transformers import BertTokenizer, BertModel, BertForMaskedLM

class MaskedSentencePredictor:
    def __init__(self) -> None:
        # Initializes the tokenizer and model for a Persian BERT model
        self.tokenizer = BertTokenizer.from_pretrained('HooshvareLab/bert-fa-base-uncased')
        self.model = BertForMaskedLM.from_pretrained('HooshvareLab/bert-fa-base-uncased')
        self.model.eval()  
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def predict_masked_sent(self, text: str, top_words: int = 5) -> list:
        # Predicts the top words to replace the [MASK] token in the input text
        # Args:
        #   text (str): Input sentence containing a [MASK] token
        #   top_words (int): Number of top predictions to return (default is 5)
        # Returns:
        #   list: A list of top predicted words for the [MASK] token

        text = "[CLS] %s [SEP]" % text  
        tokenized_text = self.tokenizer.tokenize(text)  
        masked_index = tokenized_text.index("[MASK]")  
        indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokenized_text)  
        tokens_tensor = torch.tensor([indexed_tokens]) 

        with torch.no_grad():  
            outputs = self.model(tokens_tensor)  
            predictions = outputs[0]  

        # Compute probabilities and find the top predicted tokens
        probs = torch.nn.functional.softmax(predictions[0, masked_index], dim=-1)
        top_k_weights, top_k_indices = torch.topk(probs, top_words, sorted=True)

        mighty_tokens = []
        for i, pred_idx in enumerate(top_k_indices):
            predicted_token = self.tokenizer.convert_ids_to_tokens([pred_idx])[0]  
            token_weight = top_k_weights[i]  
            mighty_tokens.append(predicted_token)  

        return mighty_tokens
