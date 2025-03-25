import cv2
import numpy as np

def cartoonize_image(img_path):
    # 이미지 불러오기
    img = cv2.imread(img_path)
    img = cv2.resize(img, (800, 600))  # 원하는 크기로 조정

    # 1. 노이즈 제거를 위한 이미지 축소 + 반복적인 bilateral filter
    img_color = img
    for _ in range(5):
        img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=75, sigmaSpace=75)

    # 2. 엣지 검출을 위한 그레이스케일 + 블러 + adaptiveThreshold
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY,
                                     blockSize=9,
                                     C=2)

    # 3. 컬러 이미지를 축소된 색상 영역으로 만들기 (색상 단순화)
    # 위에서 이미 bilateral filter로 충분히 부드럽게 했기 때문에 생략 가능

    # 4. 엣지 이미지를 컬러 이미지와 결합
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
    cartoon = cv2.bitwise_and(img_color, img_edge)

    return cartoon

# 실행 예제
if __name__ == "__main__":
    cartoon_img = cartoonize_image("image_name.jpg")  # 여기에 이미지 경로 지정
    cv2.imshow("Cartoonized", cartoon_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
