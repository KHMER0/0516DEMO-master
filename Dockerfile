# 使用官方Python輕量級映像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# 複製requirements.txt
COPY requirements.txt .

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 複製所有檔案
COPY . .

# 暴露端口
EXPOSE 5000

# 運行應用程式
CMD ["python", "DEMO0515/app.py"]