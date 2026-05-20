#!/bin/bash

# 定義虛擬環境目錄
VENV_DIR="venv"

# 檢查虛擬環境是否存在，不存在則建立
if [ ! -d "$VENV_DIR" ]; then
    echo "正在建立虛擬環境..."
    python3 -m venv $VENV_DIR
fi

# 啟動虛擬環境
source $VENV_DIR/bin/activate

# 檢查並安裝依賴
if [ -f "requirements.txt" ]; then
    echo "正在安裝/更新依賴..."
    pip install --upgrade pip
    pip install -r requirements.txt
fi

# 檢查 .env 是否存在，不存在則提示
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        echo "警告: 找不到 .env 檔案。正在從 .env.example 複製..."
        cp .env.example .env
        echo "請記得編輯 .env 檔案並填入正確的 API Key。"
    else
        echo "錯誤: 找不到 .env 或 .env.example 檔案。"
    fi
fi

# 啟動 SnapInsight 應用程式
echo "正在啟動 SnapInsight..."
python3 app.py
