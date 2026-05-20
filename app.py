import os
import base64
from flask import Flask, render_template, request, Response, stream_with_context
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

# SnapInsight Configuration
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "gpt-4o")

client = OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return "No image uploaded", 400
    
    image_file = request.files['image']
    image_data = base64.b64encode(image_file.read()).decode('utf-8')
    
    def generate():
        try:
            response = client.chat.completions.create(
                model=LLM_MODEL_NAME,
                messages=[
                    {
                        "role": "system",
                        "content": "請精確輸出照片中原始文字內容。"
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_data}"
                                }
                            }
                        ]
                    }
                ],
                stream=True,
                temperature=0,
                reasoning_effort="none",
                extra_body={
                    "thinking": False,
                    "think": False
                }
            )
            for chunk in response:
                if chunk.choices and len(chunk.choices) > 0:
                    if chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"Error: {str(e)}"

    return Response(stream_with_context(generate()), mimetype='text/plain')

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return "No text provided", 400
    
    def generate():
        try:
            response = client.chat.completions.create(
                model=LLM_MODEL_NAME,
                messages=[
                    {
                        "role": "system",
                        "content": "你是一個專業的翻譯官。請將使用者提供的內容翻譯成流暢的繁體中文。不要進行推理或提供任何額外的解釋，僅輸出翻譯後的文字。"
                    },
                    {
                        "role": "user",
                        "content": text
                    }
                ],
                stream=True,
                temperature=0,
                reasoning_effort="none",
                extra_body={
                    "thinking": False,
                    "think": False
                }
            )
            for chunk in response:
                if chunk.choices and len(chunk.choices) > 0:
                    if chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"Error: {str(e)}"

    return Response(stream_with_context(generate()), mimetype='text/plain')

if __name__ == '__main__':
    port = int(os.getenv("PORT", 40000))
    app.run(host='0.0.0.0', port=port, debug=False)
