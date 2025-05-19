# AI解決方案中心專案

## 專案架構

這是一個基於Flask框架開發的Web應用程式，主要架構如下：

- **前端**：使用HTML/CSS/JavaScript開發的響應式網頁
- **後端**：Python Flask框架處理API請求
- **資料**：CSV檔案作為資料來源

## 專案功能

1. 提供企業AI解決方案展示平台
2. 分類瀏覽不同類型的AI解決方案
3. 管理員登入功能
4. 從CSV檔案讀取解決方案資料並轉換為JSON API

## 檔案功能說明

### app.py
- Flask應用程式主檔案
- 提供以下路由功能：
  - `/`: 首頁
  - `/category/<category>`: 分類頁面
  - `/api/csv-to-json`: 將CSV轉換為JSON的API

### class0515改.csv
- 專案的主要資料來源
- 包含以下欄位：
  - id: 解決方案ID
  - title: 解決方案標題
  - description: 解決方案描述
  - url: 解決方案連結
  - category: 解決方案分類
  - status: 狀態標籤
  - icon: 圖示
  - feature: 特色說明

### templates/index.html
- 專案首頁模板
- 主要功能：
  - 展示登入表單
  - 顯示所有解決方案分類
  - 響應式設計，支援手機瀏覽

### templates/category.html
- 分類詳情頁面模板
- 主要功能：
  - 顯示特定分類下的所有解決方案
  - 提供返回首頁連結
  - 響應式設計