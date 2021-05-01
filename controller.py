from fastapi import FastAPI, File, UploadFile
from starlette.templating import Jinja2Templates  # new
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
import io
from typing import List


app = FastAPI(
    title='FastAPIでつくるtoDoアプリケーション',
    description='FastAPIチュートリアル：FastAPI(とstarlette)でシンプルなtoDoアプリを作りましょう．',
    version='0.9 beta'
)

app.mount("/static", StaticFiles(directory="static"), name="static")


# new テンプレート関連の設定 (jinja2)
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env  # Jinja2.Environment : filterやglobalの設定用


def index(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request}  # new 変更！
    )

def process(files: List[UploadFile] = File(...)):
    bin_data = io.BytesIO(files[0].file.read())
    img = read_image(bin_data)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("gray.png", img_gray)
    hist = cv2.calcHist([img_gray],[0],None,[256],[0,256])
    data = list(map(lambda v: v[0], hist))

    threshold = get_threshold(data, 0.3)
    print("threshold is ", threshold)
    ret, img_thresh = cv2.threshold(img_gray, threshold, 255, cv2.THRESH_BINARY)
    return {"tomato": "tomato"}

def get_threshold(hist, rate):
    total = sum(hist)
    print("total is ", total)
    threshNum = total * rate
    print("backgraund is ", threshNum)
    count = 0
    for i, v in enumerate(hist):
        count += v
        if count >= threshNum:
            index = i
            break
    return index

def read_image(bin_data, size=(224, 224)):
    file_bytes = np.asarray(bytearray(bin_data.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, size)
    return img
    