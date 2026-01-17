# AI Cook App

このアプリは、写真から野菜を判別する **Flask + PyTorch / TensorFlow アプリ** です。  


# 1. リポジトリをローカルにクローン（コピー）する
```
git clone https://github.com/diary54/ai_cook_app.git
cd ai_cook_app
```

# 2. 仮想環境の作成

# Windows の場合
```
python -m venv my_env
my_env\Scripts\activate
```
# Mac / Linux の場合
```
# python -m venv my_env
# source my_env/bin/activate
```
# 3. pip を最新版にアップデート
```
pip install --upgrade pip
```
# 4. 依存パッケージをインストール
```
pip install -r requirements.txt
```
# 5. Flask アプリを起動
# Render 用に PORT 環境変数に対応している場合も、ローカルでは 5000 にアクセス可能
```
python -m src.app
```
# 起動後、ブラウザで以下を開く
# http://127.0.0.1:5000






