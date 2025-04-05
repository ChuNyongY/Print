from PIL import Image
import os

def merge_images_vertically(image_paths, output_path="merged.jpg"):
    """
    여러 이미지를 세로로 이어붙이는 함수
    :param image_paths: 이미지 경로 리스트
    :param output_path: 저장할 파일 이름
    """
    # 이미지 열기
    images = [Image.open(path) for path in image_paths]

    # 가장 넓은 이미지에 맞춰 가로 너비 설정
    max_width = max(img.width for img in images)
    total_height = sum(img.height for img in images)

    # 새 이미지 생성 (RGB, 흰 배경)
    merged_image = Image.new("RGB", (max_width, total_height), color=(255, 255, 255))

    # 이미지 이어붙이기
    y_offset = 0
    for img in images:
        # 필요한 경우 이미지 크기 조정 (가로 폭 맞추기)
        if img.width != max_width:
            img = img.resize((max_width, int(img.height * (max_width / img.width))))
        
        merged_image.paste(img, (0, y_offset))
        y_offset += img.height

    # 저장
    merged_image.save(output_path)
    print(f"이미지가 성공적으로 합쳐졌습니다: {output_path}")

# 사용 예시
image_folder = "C:\\Users\\YongE\\Desktop\\추뇽이\\동국대 수업\\3학년\\1학기\\Computer Network"  # 이미지 폴더 경로
image_files = ["345번.jpg","91011번.jpg"]        # 합칠 이미지 파일명들
image_paths = [os.path.join(image_folder, fname) for fname in image_files]

merge_images_vertically(image_paths, "merged.jpg")
