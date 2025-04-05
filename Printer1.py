from PIL import Image
import os
import shutil

def image_to_ascii(image_path): # 이미지를 터미널 크기에 맞춰 ASCII 아트로 변환하여 출력하는 함수.
    
    img = Image.open(image_path).convert("L")

    columns, rows = shutil.get_terminal_size()
    scale = 0.5  # 픽셀의 비율 보정 (세로를 줄여서 가로로 긴 형태 유지)

    width = columns - 0  # 여백 고려
    height = int((img.height / img.width) * width * scale)  # 비율 유지

    img = img.resize((width, height))

    ascii_chars = "@%#*+=-:. "

    pixels = img.getdata()
    ascii_str = "".join(ascii_chars[min(max(pixel // 25, 0), 9)] for pixel in pixels)
    ascii_str = "\n".join(ascii_str[i: i + width] for i in range(0, len(ascii_str), width))

    print(ascii_str)  # 터미널에 출력

image_path = "test.jpg" # 변환할 이미지 파일과 같은 경로에 위치해야함
image_to_ascii(image_path)

