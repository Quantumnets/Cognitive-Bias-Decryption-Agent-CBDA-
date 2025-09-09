from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

class BiasDetector:
    def __init__(self, model_name="bert-base-uncased"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.bias_categories = {
            0: "confirmation_bias",
            1: "anchoring_bias",
            2: "dunning_kruger",
            3: "sunk_cost_fallacy",
            4: "bandwagon_effect"
        }
    
    def detect_bias(self, text):
        """Detect cognitive biases in text"""
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        probabilities = torch.softmax(outputs.logits, dim=-1)
        predicted_class = torch.argmax(probabilities, dim=1).item()
        
        return {
            "bias_type": self.bias_categories.get(predicted_class, "unknown"),
            "confidence": probabilities[0][predicted_class].item(),
            "text": text
        }

# Global instance for easy import
detector = BiasDetector()

def detect_bias(text):
    return detector.detect_bias(text)
