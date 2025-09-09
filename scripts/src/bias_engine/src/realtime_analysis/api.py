from flask import Flask, request, jsonify
from flask_cors import CORS
from src.bias_engine.inference import detect_bias

app = Flask(__name__)
CORS(app)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "CBDA API"})

@app.route('/analyze', methods=['POST'])
def analyze_text():
    try:
        data = request.json
        text = data.get("text", "")
        
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        result = detect_bias(text)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/analyze/batch', methods=['POST'])
def analyze_batch():
    try:
        data = request.json
        texts = data.get("texts", [])
        
        if not texts:
            return jsonify({"error": "No texts provided"}), 400
        
        results = [detect_bias(text) for text in texts]
        return jsonify({"results": results})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
