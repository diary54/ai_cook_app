# AI Cook App

写真から野菜を自動判別し、料理提案につなげる AI アプリです。
Flask を用いた Web アプリケーションとして構築されており、
PyTorch による画像分類モデルの推論機能を備えています。

本アプリは Render 上にデプロイ済みで、ブラウザから利用可能です。
- PyTorch モデルは初回アクセス時にロードされるため、処理に時間がかかります。
- Render は応答が一定時間ないと 502 エラーとして返すことがあります。
- ページをリロードすると、モデルがロード済みのため**2回目以降は正常に判定できます**
※ この現象はアプリの機能上の問題ではなく、Render の無料プランにおける仕様によるものです。

👉 デモURL
https://ai-cook-app.onrender.com

## 技術スタック

### 言語
- Python 3.10 / 3.11（動作確認済み）

### バックエンド
- Flask（Web アプリケーション）
- Gunicorn（アプリケーションサーバ）

### 機械学習 / 画像処理
- PyTorch（画像分類モデルの推論）
- TorchVision
- OpenCV（画像前処理）
- NumPy

### 実行環境
- ローカル環境（Python venv）
- Render（Web Service / Free プラン）

### インフラ・デプロイ
- Render（Web Service）
- Gunicorn によるアプリケーション起動
- AWS EC2 / ECS(Fargate) でのデプロイも検討中


## Renderでの起動方法

### 起動コマンド
```
gunicorn --chdir src app:app --bind 0.0.0.0:$PORT --workers 1
```


## ローカルでの起動方法

### 1. リポジトリをローカルにクローン（コピー）する
```
git clone https://github.com/diary54/ai_cook_app.git
cd ai_cook_app
```

### 2. 仮想環境の作成

#### Windows の場合
```
python -m venv my_env
my_env\Scripts\activate
```
#### Mac / Linux の場合
```
# python -m venv my_env
# source my_env/bin/activate
```
### 3. pip を最新版にアップデート
```
pip install --upgrade pip
```
### 4. 依存パッケージをインストール
```
pip install -r requirements.txt
```
### 5. Flask アプリを起動
```
python -m src.app
```
### ブラウザで以下にアクセスしてください
http://localhost:5002






