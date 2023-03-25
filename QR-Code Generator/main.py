import requests
from io import BytesIO
import PIL

url = "https://qrcode3.p.rapidapi.com/qrcode/text"

payload = {
    "data": "https://linqr.app",
    "image": {
        "uri": "icon://appstore",
        "modules": True
    },
    "style": {
        "module": {
            "color": "black",
            "shape": "default"
        },
        "inner_eye": {"shape": "default"},
        "outer_eye": {"shape": "default"},
        "background": {}
    },
    "size": {
        "width": 200,
        "quiet_zone": 4,
        "error_correction": "M"
    },
    "output": {
        "filename": "qrcode",
        "format": "png"
    }
}

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "qrcode3.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)
print(response)
