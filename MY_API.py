from flask import Flask, request, jsonify
import pandas as pd
from joblib import load

app = Flask(__name__)

# 加载模型和编码器
model = load('decision_tree_model.joblib')
encoder = load('one_hot_encoder.joblib')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    new_data = pd.DataFrame([data])

    # 应用One-Hot编码和模型预测逻辑（如上所述）
    # 注意，这里省略了实际的转换代码

    predictions = model.predict(features_new)
    return jsonify(predictions.tolist())


if __name__ == '__main__':
    app.run(debug=True)
