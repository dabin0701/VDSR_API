# VDSR_API
## VDSR을 활용한 저화질 비디오 프레임 업샘플링
### 주제 선정 이유 및 목적
현재 미디어 산업은 현대인들의 삶에 필수적인 요소로 자리잡았다. 하지만 영상처리 기술이 발전되기 전 과거 영상 프레임의 화질은 대부분 저화질이었다. ‘네셔널 지오그래픽’의 영상을 이에 대한 예시다.  13년 전, 최대 화질이 480p로 매우 낮은 프레임을 지원하였던 기술이 현재 2024년에는 최대 1080p 화질을 제공한다. 이로 인해 10년이라는 짧은 시간 내에 미디어 산업의 기술발전이 매우 빠르게 성장했음을 알 수 있다. 

> 이미지 출처 : https://www.youtube.com/@NatGeo/videos

> ### <2017년 National GeoGraphic /최대 화질 480p>
> 
> <img src="https://github.com/dabin0701/VDSR_API/blob/main/Introduction/National_1.png"  width="500" height="300"/>

> 인물의 얼굴과 자막이 매우우 흐릿하게 보이며, 영상의 크기도 비교적 작다.
> 
> ### <2024년 National GeoGraphic /최대 화질1080p>
> <img src="https://github.com/dabin0701/VDSR_API/blob/main/Introduction/National_2.png"  width="600" height="300"/>

> 동물의 털질감과 수염이 잘 보이며 깨지는 현상 없이 마치 직접 눈으로 관찰한 듯한 고화질의 이미지다.

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
### 모델 설명 및 선택 이유
VDSR의 기존 구조를 개선하여, 중간 평가때 보다 높은 성능의 모델을 만들었다.
Matle Lab을 이용하여 '91 datadet'을 196,560개의 이미지로 증강한 후 'h5' 형식으로 변환하여 학습한다.

> ## <기존 VDSR 구조 >
> ![image](https://github.com/dabin0701/VDSR_API/blob/main//Introduction/VDSR_1.png)

> ## <개선 한 VDSR 구조>
> ![image](https://github.com/dabin0701/VDSR_API/blob/main//Introduction/VDSR_0.png)

### 성능평가 과정
Validaion의 원본 이미지를 2배,3배,4배로 줄였다가 원본 크기로 늘려 저화질 이미지를 추출한다. 
추출 된 Validation의 bicubic과 VDSR의 PSNR 수치를 비교하여 Model의 성능을 확인한다.
***
## 실험 결과
<첫 번째 실험> 
- NationalGEO Validation일 때 세 실험 중 가장 낮은 PSNR 수치 
- 원인 : Train data로 학습한 이미지와(꽃과 자연) Validation data의(동물과 인물) 이미지의 결이 맞지 않았기 때문이다.
- 이를 해결하기 위해 Validation을 Flower로 변경 -> 매우 높은 성능을 나타냄
- 하지만 4배 줄였던 vdsr의 PSNR 수치가 개선되지 않았기 때문에 최종 모델로 선택되지 못함.
  
  - ↓ National_GEO Validation ↓
  
|Scale| Bicubi  PSNR|VDSR PSNR|VDSR-Bicubic|
| ------------ |:---------------------:| ---------:|------------:|
| 2x | 34.4860 | 29.9504 | -4.5356 |
| 3x | 31.3486 | 28.4402  | -2.9084 |
| 4x | 29.1305 | 28.759530 | -0.3709 |

  - ↓ Flower Validation ↓

|Scale| Bicubi  PSNR|VDSR PSNR|VDSR-Bicubic|
| ------------ |:---------------------:| ---------:|------------:|
| 2x | 34.4860 | 37.38969 | 2.99713 |
| 3x | 31.3486 | 32.2266 | 0.8780 |
| 4x | 29.1305 | 28.955213 | -0.17530 |

<두 번째 실험>
- Validation data를 꽃이 개화하는 이미지로 하여, 학습한 이미지와 결이 맞게하였다.
- 1번 실험보다는 좋은 성능을 보였으나 높은 성능을 보이지 않았다.

  - ↓ Flower Validation ↓
  
|Scale| Bicubi  PSNR|VDSR PSNR|VDSR-Bicubic|
| ------------ |:---------------------:| ---------:|------------:|
| 2x | 34.4860 | 35.3869 | 0.90097 |
| 3x | 31.3486 | 30.13440 | -1.21422 |
| 4x | 29.1305 | 27.641924 | -1.488590 |

<세 번째 실험>
- 위 세가지 실험 후 가장 높은 성능의 모델
- 두 번째 실험의 성능을 높이기 위해 Residual block에 BatchNorm2d 적용하였다.
- 코드 배포자 ‘twtygqyy’가 구현한 VDSR의 PSNR 수치에 가장 가깝게 성능을 낸 모델이다.

  - ↓ Flower Validation ↓

|Scale| Bicubi  PSNR|VDSR PSNR|VDSR-Bicubic|
| ------------ |:---------------------:| ---------:|------------:|
| 2x | 34.4860 | 36.1943 | 1.7083 |
| 3x | 31.3486 | 31.994 | 0.645645 |
| 4x | 29.1305 | 29.4922 | 0.36174 |

![image](https://github.com/dabin0701/VDSR_API/blob/main/Introduction/R_Bn_2x.png?raw=true)

## 순서대로 GT -BICUBIC -VDSR

![image](https://github.com/dabin0701/VDSR_API/blob/main/Introduction/R_Bn_GT.png?raw=true)
![image](https://github.com/dabin0701/VDSR_API/blob/main/Introduction/R_Bn_Bicubic.png?raw=true)
![image](https://github.com/dabin0701/VDSR_API/blob/main/Introduction/R_Bn_VDSR.png?raw=true)


***
## 추후 개선 사항 : 추가로 개선해야할 내용에 대해 정리 또는 프로젝트 한계점 설명
- Ablation Study

- 
- 기존 VDSR의 성능 보다 모두 PSNR 수치가 낮게 측정 되었다.
