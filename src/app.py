import torch
from food import transform_image, Net 
from flask import Flask, request, render_template, redirect
import io
from PIL import Image # type: ignore
import base64

def predict(img):
    net = Net().cpu().eval()

    net.load_state_dict(torch.load('./src/ingredients.pt', map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu')))

    img = transform_image(img)

    y = torch.argmax(net(torch.tensor(img)), dim=1).cpu().detach().numpy()
    return y

def getName(label):
    if label == 0:
        return 'かぼちゃ'
    elif label == 1:
        return 'きゅうり'
    elif label == 2:
        return 'じゃがいも'
    elif label == 3:
        return 'たまねぎ'
    elif label == 4:
        return 'だいこん'
    elif label == 5:
        return 'とまと'
    elif label == 6:
        return 'なす'
    elif label == 7:
        return 'にんじん'
    elif label == 8:
        return 'ねぎ'
    elif label == 9:
        return 'ピーマン'
    elif label == 10:
        return 'レタス'
    elif label == 11:
        return 'キャベツ'
    
app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET', 'POST'])
def predicts():
    
    if request.method == 'POST':
        
        if 'filename' not in request.files:
            return redirect(request.url)
        
        file = request.files['filename']
        
        if file and allowed_file(file.filename):

            #　画像ファイルに対する処理
            buf = io.BytesIO()
            image = Image.open(file).convert('RGB')
         
            image.save(buf, 'png')
         
            base64_str = base64.b64encode(buf.getvalue()).decode('utf-8')
        
            base64_data = 'data:image/png;base64,{}'.format(base64_str)

            # 推論
            pred = predict(image)
            ingredientsName_ = getName(pred)
            return render_template('result.html', ingredientsName=ingredientsName_, image=base64_data)
        return redirect(request.url)

    elif request.method == 'GET':
        return render_template('index.html')
    
# アプリケーションの実行の定義
if __name__ == '__main__':
    app.run(debug=True, port=5002)
