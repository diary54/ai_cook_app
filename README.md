# AI Cook App

写真から野菜を自動判別し、料理提案につなげるAIアプリです。  
Flask を用いた Web API と、PyTorch / TensorFlow の推論モデルで構成されています。

## 技術スタック

### 言語
- Python 3.10 / 3.11（動作確認済み）

### バックエンド
- Flask（Web API）
- Gunicorn（アプリケーションサーバ）

### 機械学習 / 画像処理
- PyTorch / TensorFlow（画像分類モデルの推論）
- OpenCV（画像前処理）
- NumPy（数値計算）

### 実行環境
- ローカル環境（Python venv）

### インフラ・デプロイ
- 未デプロイ
- Render 無料プランでは推論時のメモリ制限により動作困難
- AWS EC2 / ECS(Fargate) でのデプロイを検討中

## デプロイについて

本アプリは推論モデルのサイズおよび実行時メモリ使用量の関係上、
Render の無料プランでは安定して動作させることができませんでした。

そのため現在はローカル環境での実行を前提としています。
今後は以下の構成でのデプロイを検討しています。

- AWS EC2 + Gunicorn + Nginx
- または ECS(Fargate) によるコンテナ実行


# ローカルでの起動方法

## 1. リポジトリをローカルにクローン（コピー）する
```
git clone https://github.com/diary54/ai_cook_app.git
cd ai_cook_app
```

## 2. 仮想環境の作成

### Windows の場合
```
python -m venv my_env
my_env\Scripts\activate
```
### Mac / Linux の場合
```
# python -m venv my_env
# source my_env/bin/activate
```
## 3. pip を最新版にアップデート
```
pip install --upgrade pip
```
## 4. 依存パッケージをインストール
```
pip install -r requirements.txt
```
## 5. Flask アプリを起動
```
python -m src.app
```






