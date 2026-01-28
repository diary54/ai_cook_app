from flask import Flask, request, render_template
import io
from PIL import Image
import base64
import torch
from pathlib import Path
from src.model import transform_image, Net


# パス設定
BASE_DIR = Path(__file__).resolve().parent          # aicook_app/src
BASE_ROOT = BASE_DIR.parent                        # aicook_app
MODEL_PATH = BASE_DIR / 'lightnet_resnet18.pt'


# Flask 設定（templates / static を明示）
app = Flask(
    __name__,
    template_folder=str(BASE_ROOT / 'templates'),
    static_folder=str(BASE_ROOT / 'src' / 'static')
)

# モデル（遅延ロード）
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
net = None

def get_model():
    global net
    if net is None:
        net = Net(num_classes=12).to(device)
        net.load_state_dict(torch.load(MODEL_PATH, map_location=device))
        net.eval()
    return net

# 推論
def predict(img):
    img = transform_image(img).to(device)
    model = get_model()

    with torch.no_grad():
        with torch.amp.autocast(device_type='cuda', enabled=torch.cuda.is_available()):
            y = torch.argmax(model(img), dim=1).cpu().numpy()
    return y

# ラベル
LABELS = [
    'かぼちゃ','きゅうり','じゃがいも','たまねぎ','だいこん',
    'とまと','なす','にんじん','ねぎ','ピーマン','レタス','キャベツ'
]

def getName(label):
    return LABELS[label]


# ルーティング
@app.route('/', methods=['GET', 'POST'])
def predicts():
    if request.method == 'POST':
        file = request.files.get('filename')

        if file:
            # 画像読み込み
            image = Image.open(file).convert('RGB')

            # ---------- 画像を base64 に変換 ----------
            buf = io.BytesIO()
            image.save(buf, format='PNG')
            base64_str = base64.b64encode(buf.getvalue()).decode('utf-8')
            base64_image = f'data:image/png;base64,{base64_str}'

            # ---------- 推論 ----------
            pred = predict(image)
            ingredientsName_ = getName(int(pred[0]))

            return render_template(
                'result.html',
                ingredientsName=ingredientsName_,
                image=base64_image
            )

    return render_template('index.html')


# アプリ起動
if __name__ == '__main__':
  app.run(debug=True, port=5002)

