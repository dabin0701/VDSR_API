# VDSR_API
## VDSR을 활용한 저화질 비디오 프레임 업샘플링
### 주제 선정 이유 및 목적
현재 미디어 산업은 현대인들의 삶에 필수적인 요소로 자리잡았다. 하지만 영상처리 기술이 발전되기 전 과거 영상 프레임의 화질은 대부분 저화질이었다. ‘네셔널 지오그래픽’의 영상을 이에 대한 예시다.  13년 전, 최대 화질이 480p로 매우 낮은 프레임을 지원하였던 기술이 현재 2024년에는 최대 1080p 화질을 제공한다. 이로 인해 10년이라는 짧은 시간 내에 미디어 산업의 기술발전이 매우 빠르게 성장했음을 알 수 있다. 

> 이미지 출처 : https://www.youtube.com/@NatGeo/videos

> ### <2017년 National GeoGraphic /최대 화질 480p>
> 
> <img src="https://github.com/dabin0701/VDSR_API/blob/main/Introduction/National_1.png"  width="500" height="300"/>

> 인물의 얼굴과 자막이 매우 흐릿하게 보이며, 영상의 크기도 비교적 작다.
> 
> ### <2024년 National GeoGraphic /최대 화질1080p>
> <img src="https://github.com/dabin0701/VDSR_API/blob/main/Introduction/National_2.png"  width="600" height="300"/>

> 동물의 털 질감과 수염이 잘 보이며, 깨지는 현상 없이 마치 직접 눈으로 관찰한 듯한 고화질의 이미지다.

저화질 이미지가 고화질로 변경되는 구조에 대한 궁금증으로 인해 해당 프로젝트 주제로 선정하게 되었고, 화질 개선에 특화된 모델인 VDSR(Very Deep Super Resolution)을 적용하여 저화질 이미지를 고화질 이미지로 업샘플링 하는 것을 목적으로 한다.
***
## 프로젝트 개요
VDSR을 구현하는 세 개의 실험을 통해 가장 높은 성능을 나타낸 모델을 선별하고, 세개의 실험에서 가장 높은 성능을 나타낸 효과를 뽑아, Ablation Study를 구성한다.

1. VDSR의 residual 반복 횟수 별 성능

2. Relu와 Conv2d layer 사이에 BatchNorm2d layer 적용 성능
  
3. Residual block + BatchNorm2d 적용하였을 때의 성능
***
## VDSR Github & library list
- ‘twtygqyy’가 구현한 VDSR 모델 코드
  깃허브 주소 : https://github.com/twtygqyy/pytorch-vdsr/blob/master/vdsr.py
  
- library list

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"> <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/pillow-60C65F?style=for-the-badge&logo=pillow&logoColor=white"> <img src="https://img.shields.io/badge/matplotlib-019933?style=for-the-badge&logo=matplotlib&logoColor=white">
<img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"> <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"> <img src="https://img.shields.io/badge/tqdm-4B8BBE?style=for-the-badge&logo=tqdm&logoColor=white">

***
### Data set 출처 및 설명
- Train dataset - T91 dataset(https://www.kaggle.com/datasets/ll01dm/t91-image-dataset)

: 해당 이미지는 초해상도를 위해 신경망을 훈련하는 데 일반적으로 사용되는 91개의 꽃 이미지로 대부분의 이미지는 잘린 꽃 이미지다. 해당 data set을 선택한 이유는 잘린 이미지가 다양한 크기, 비율, 위치에서 추출되었기 때문에 원본 이미지에서 얻을 수 있는 다양한 시각적 패턴을 제공하기 때문에 모델이 다양한 상황에서 고해상도 이미지를 복원하는 능력을 향상시키는 데 도움을 줄 것이라 예측하여 T91 data set을 선택하게 되었다.

<p align="center">
<img src="https://raw.githubusercontent.com/dabin0701/VDSR_API/main/Train_dataset/000t1.bmp"  width="200" height="200"/>
</p>

- Validation dataset - NationalgeoGraphic(https://www.youtube.com/@NatGeo/videos)

: 해당 데이터 셋은 Nationageograpich에서 제공하는 꽃이 개화하는 영상이다. Train dataset이 꽃이기 때문에 모델의 학습 효과를 확인하기 위해 Validation data set을 꽃으로 선택했다.

<p align="center">
<img src="https://raw.githubusercontent.com/dabin0701/VDSR_API/main/Validation_dataset/u581.jpg"  width="200" height="200"/>
</p>

  - Test dataset - set5 dataset (https://figshare.com/articles/dataset/BSD100_Set5_Set14_Urban100/21586188)

: Set5는 많은 연구에서 사용되는 표준 데이터셋이기 때문에, 새로운 알고리즘의 성능을 이전의 연구 결과와 직접 비교할 수 있다. 이는 연구자들이 자신들의 방법이 얼마나 효과적인지를 쉽게 평가하고 비교할 수 있게 해주는 역할로 썼기 때문에, 마찬가지로 프로젝트에서 사용한 VDSR의 성능의 수준을 확인하고자 set5 dataset을 선택했다.

<p align="center">
<img src="https://raw.githubusercontent.com/dabin0701/VDSR_API/main/Test_dataset/baby_GT.bmp"  width="200" height="200"/>
</p>

***
### VDSR(Very Deep Super-Resolution) 설명
- Super Resolution의 종류 중 VDSR은 20개의 깊은 신경망 레이어를 사용하여 저해상도 이미지를 고해상도로 변환하는 알고리즘이다. 잔차 학습(Residual Learning)을 통해 빠르고 효율적으로 고품질의 이미지를 복원할 수 있는 모델이다.

- VDSR은 20개의 레이어로 구성된 깊은 신경망을 사용하기 때문에 더 복잡하고 섬세한 특징들을 학습할 수 있게 하여 고해상도 이미지를 더 정교하게 복원할 수 있으며, 잔차 학습을 활용하여 기울기 소실 문제를 해결한다는 장점이있다. 또한 SRCNN이나 Resnet과 같은 모델보다도 가볍고 간단한 구조를 가지지만 높은 성능을 보이기 때문에 VDSR 모델을 선택하게 되었다.

> ## <기존 VDSR 구조 >
> <p align="center">
<img src="https://raw.githubusercontent.com/dabin0701/VDSR_API/main/Introduction/VDSR_1.png"  width="600" height="350"/>
</p>

> ## <개선 한 VDSR 구조>
> > <p align="center">
<img src="https://raw.githubusercontent.com/dabin0701/VDSR_API/main/Introduction/VDSR_0.png"  width="600" height="350"/>
</p>

***
## 실험 결과
<첫 번째 실험> 
- Repeat num(residual 반복 횟수)를 정하여 12번,18번,24번,30번 반복하였을 때 가장 성능이 좋은 모델을 선택 -> repeat num =30 인 모델
- 중간 평가때 Validation data를 National_GEO를 적용한 것까지 발표
  - ↓ National_GEO Validation ↓

|Scale| Bicubic  PSNR|VDSR PSNR|VDSR-Bicubic|
| ------------ |:---------------------:| ---------:|------------:|
| 2x | 34.4860 | 37.299 | 2.813 |
| 3x | 31.3486 | 33.555  | 2.207 |
| 4x | 29.1305 | 31.2850 | 2.155 |

<img src="https://raw.githubusercontent.com/dabin0701/VDSR_API/main/Introduction/National_Demo_2x.png"  width="600" height="250"/>

***
## 중간 평가 이후 개선
- Flower Validation으로 data set을 변경했을 때 결과 이미지의 성능이 개선되길 기대하여 적용
- 낮은 화질의 결과 이미지 원인 :Train data로 학습한 이미지와(꽃과 자연) Validation data의(동물과 인물) 이미지의 결이 맞지 않았기 때문
- 하지만 해당 모델은 loss가 238.519로 매우 높고, 4배일 때의 성능이 -(마이너스)이이기 때문에 좋은 모델은 아니라 판단
  - ↓ Flower Validation ↓

|Scale| Bicubic  PSNR|VDSR PSNR|VDSR-Bicubic|
| ------------ |:---------------------:| ---------:|------------:|
| 2x | 34.4860 | 37.38969 | 2.99713 |
| 3x | 31.3486 | 32.2266 | 0.8780 |
| 4x | 29.1305 | 28.955213 | -0.17530 |

<img src="https://raw.githubusercontent.com/dabin0701/VDSR_API/main/Validation_dataset/u581.jpg"  width="200" height="200"/>

<두 번째 실험>
- Repeat num(residual 반복 횟수)를 정하여 12번,18번,24번,30번 반복하였을 때 가장 성능이 좋은 모델을 선택
- Relu와 Cnn 사이에 BatchNorm2d를 추가
- 첫 번째 모델의 성능보다 낮은 수준의 성능

  - ↓ Flower Validation ↓
  
|Scale| Bicubic  PSNR|VDSR PSNR|VDSR-Bicubic|
| ------------ |:---------------------:| ---------:|------------:|
| 2x | 34.4860 | 35.3869 | 0.90097 |
| 3x | 31.3486 | 30.13440 | -1.21422 |
| 4x | 29.1305 | 27.641924 | -1.488590 |

<세 번째 실험>
- 위의 두 실험 중 가장 낮은 loss 92.69, 2배,3배,4배 이미지 모두 개선 된 성능의 모델
- 두 번째 실험의 성능을 높이기 위해 Residual block에 BatchNorm2d 적용

  - ↓ Flower Validation ↓

|Scale| Bicubic  PSNR|VDSR PSNR|VDSR-Bicubic|
| ------------ |:---------------------:| ---------:|------------:|
| 2x | 34.4860 | 36.1943 | 1.7083 |
| 3x | 31.3486 | 31.994 | 0.645645 |
| 4x | 29.1305 | 29.4922 | 0.36174 |

![image](https://github.com/dabin0701/VDSR_API/blob/main/Introduction/R_Bn_2x.png?raw=true)
## ↓↓↓ 위 이미지 확대 모습 ↓↓↓ 

순서대로 (GT -BICUBIC -VDSR) 

![image](https://github.com/dabin0701/VDSR_API/blob/main/Introduction/R_Bn_GT.png?raw=true)
![image](https://github.com/dabin0701/VDSR_API/blob/main/Introduction/R_Bn_Bicubic.png?raw=true)
![image](https://github.com/dabin0701/VDSR_API/blob/main/Introduction/R_Bn_VDSR.png?raw=true)

***
## RESULT
가장 높은 성능을 나타낸 3번 모델을 Test set 'Set5'에 적용하여 최종 성능을 확인했다.

|Scale| Bicubic  PSNR|VDSR PSNR|VDSR-Bicubic|
| ------------ |:---------------------:| ---------:|------------:|
| 2x | 33.690 | 35.457 | 1.767 |
| 3x | 30.407 | 32.446 | 2.039 |
| 4x | 28.414 | 29.787 | 1.373 |

꽃 이미지로 학습된 모델이기 때문에 Set5 에 비교적 낮은 성능을 보였다. 
***
## 프로젝트의 한계점
- 개발자가 구현한 기존 VDSR의 성능에 도달하지 못했다.
- 더 많이 모델 구조를 변경해보지 못했고, 파라미터를 다양하게 조정해보지 않았기 때문에 높은 성능을 내지 못했다.

## 추후 개선 사항
- BatchNorm2d 외에도 이미지 개선에 효과적인 layer를 적용하고 싶다.
- Ablation Study를 통해 매 실험에 효과적이었던 파라미터만을 모아, 높은 성능의 모델로 개선하고싶다. 
