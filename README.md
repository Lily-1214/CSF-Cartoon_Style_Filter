# CSF(Cartoon Style Filter)

## 필터 설명

윤관선을 강조하고, 색상을 단순화합니다.
그리고 엣지와 색상을 합성하여 카툰 스타일 필터를 생성합니다.

```python
    # 1. 노이즈 제거를 위한 이미지 축소 + 반복적인 bilateral filter (=색상 단순화)
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

    # 3. 엣지 이미지를 컬러 이미지와 결합
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
    cartoon = cv2.bitwise_and(img_color, img_edge)
```



### 느낌이 잘 표현되는 이미지

<img width="601" alt="Image" src="https://github.com/user-attachments/assets/71461aae-05ab-403b-81e3-21fde49643a8" />

<img width="601" alt="Image" src="https://github.com/user-attachments/assets/4d9ed7e2-726f-4859-9640-f44e8f4b10fc" />



### 느낌이 잘 표현되지 않는 이미지

<img width="1200" alt="Image" src="https://github.com/user-attachments/assets/8075d84f-7072-4ace-9596-6b9ca682bcd6" />

<img width="601" alt="Image" src="https://github.com/user-attachments/assets/20f332e5-89e5-4102-8ff2-c3e1946a33a1" />



### 알고리즘의 한계점
  색상이 너무 압축(bilateral Filter)되어 디테일이 날아감으로 인해 색상의 부드러운 뉘앙스가 사라진다.
텍스처가 많거나 밝기 변화가 미묘한 영역에서도 라인을 잡아서 얼굴이나 기타 무늬등이 주름처럼 보인다.
그리고 픽셀마다 경계를 이분법적으로 나눠서 윤곽선이 과하게 뭉툭하고 두껍고, 
부드러운 색상변화도 딱 끊어진 선처럼 처리되어 어색하다.
  색상의 압축을 좀 더 덜 진행하고, 밝기 변화 감지를 좀 더 둔감하게 할 필요가 있어보인다.
