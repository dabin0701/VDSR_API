# VDSR_API
## VDSR을 활용한 저화질 비디오 프레임 업샘플링
### 주제 선정 이유 및 목적
현재 미디어 산업은 현대인들의 삶에 필수적인 요소로 자리잡았다. 하지만 영상처리 기술이 발전되기 전 과거 영상 프레임의 화질은 대부분 저화질이었다. ‘네셔널 지오그래픽’의 영상을 이에 대한 예시다.  13년 전, 최대 화질이 480p로 매우 낮은 프레임을 지원하였던 기술이 현재 2024년에는 최대 1080p 화질을 제공한다. 이로 인해 10년이라는 짧은 시간 내에 미디어 산업의 기술발전이 매우 빠르게 성장했음을 알 수 있다. 

> 이미지 출처 : https://www.youtube.com/@NatGeo/videos

> ### <2017년 National GeoGraphic /최대 화질 480p>
> 그냥 이미지로 넣자잉 ... 굳이 영상 넣는데 시간 쓰지 말기
> ![Image](https://github.com/dabin0701/VDSR_API/blob/main/Introduction/National_1.png?raw=true)
> 
> 인물의 얼굴이 흐릿하게 보이며, 영상의 크기도 비교적 작다.
> ### <2024년 National GeoGraphic /최대 화질1080p>
> ![Image](https://github.com/dabin0701/VDSR_API/blob/main/Introduction/National_0.png?raw=true)
> 
> 동물의 털질감과 수염이 잘 보이며 깨지는 현상 없이 마치 직접 눈으로 관찰한 듯한 고화질의 영상이다다.

저화질 이미지가 고화질로 변경되는 구조에 대한 궁금증으로 인해 해당 프로젝트 주제로 선정하게 되었고, 화질 개선에 특화된 모델인 VDSR(Very Deep Super Resolution)을 적용하여 저화질 이미지를 고화질 이미지로 업샘플링 하는 것을 목적으로 한다.

***
### 필요한 라이브러리(버전) 또는 프로그램 목록
VDSR 모델 구현을 위해 ‘twtygqyy’가 구현한 코드를 불러왔고, 
주소 https://github.com/twtygqyy/pytorch-vdsr/blob/master/vdsr.py  

***
### Data set 출처 및 설명
Train dataset -
Validation dataset - NationalgeoGraphic
Test dataset -
***
### 모델 설명
VDSR의 기존 구조를 개선하여 중간 평가때 보다 높은 성능의 모델을 만들었다.
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
***
## 추후 개선 사항 : 추가로 개선해야할 내용에 대해 정리 또는 프로젝트 한계점 설명
