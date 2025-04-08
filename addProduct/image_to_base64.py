import base64

def imgToBase64(img):
        base64_str = base64.b64encode(img.read()).decode("utf-8") 
        return base64_str

