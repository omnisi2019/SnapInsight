# SnapInsight

SnapInsight 是一個高效的智慧視覺工作流工具，基於 Python Flask 開發。它能將圖片中的文字即時辨識 (OCR)，並整合 Google AI 搜尋與自動翻譯功能，幫助使用者從截圖中瞬間獲取深層洞察。

## 🚀 核心功能

- **多管道圖片輸入**: 支援 `Ctrl+V` 貼上、拖曳上傳或點選按鈕選取圖片。
- **極速 OCR 辨識**: 
  - 使用與 OpenAI 相容的 Vision 模型 API。
  - 支援 **Streaming (流式輸出)**，即時呈現辨識結果。
  - 深度優化 API 參數（關閉推理過程），極大化減少等待延遲。
- **自動化剪貼簿**: 辨識完成後自動將結果複製到系統剪貼簿。
- **Google AI Mode 整合**: 
  - 一鍵開啟 Google AI 搜尋 (`udm=50`)。
  - 支援自定義 **Google AI Mode Prompt**，自動串接提示詞與辨識結果進行深度查詢。
- **智慧翻譯**: 支援一鍵流式翻譯成繁體中文，適合處理外語格言、典故或技術截圖。
- **現代化介面**: 簡潔、響應式的網頁 UI，支援快捷鍵 `Enter` 快速送出。

## 🛠️ 技術棧

- **Backend**: Python 3, Flask
- **Frontend**: Vanilla JS, CSS (極簡現代風格)
- **API**: OpenAI Compatible Vision API
- **Version Control**: Git

## 📦 安裝與啟動

### 1. 複製專案
```bash
git clone <your-repo-url>
cd ocr
```

### 2. 設定環境變數
將 `.env.example` 複製為 `.env` 並填入您的 API 資訊：
```bash
cp .env.example .env
```
編輯 `.env`：
- `LLM_API_KEY`: 您的 API 金鑰。
- `LLM_BASE_URL`: API Endpoint (例如 https://api.openai.com/v1)。
- `LLM_MODEL_NAME`: 具備 Vision 能力的模型 (例如 gpt-4o)。

### 3. 一鍵啟動
專案提供了自動化腳本，會自動建立虛擬環境、安裝依賴並啟動服務：
```bash
chmod +x start.sh
./start.sh
```
啟動後，請訪問 `http://localhost:40000`。

## 📝 使用說明

1. **貼上圖片**: 直接在網頁上 `Ctrl+V` 貼上截圖。
2. **設定模式**:
   - 若想深入瞭解內容，勾選 **Auto Google AI Mode**。
   - 若需要更多上下文，在輸入框填入提示詞（例如：「解釋這段程式碼」）。
   - 若需要中文對照，勾選 **翻譯成繁體中文**。
3. **送出**: 按下 `Enter` 或點選「傳送」。
4. **獲取結果**: 文字會自動出現在畫面上並存入剪貼簿。

## 📄 授權
本專案採 MIT 授權。
