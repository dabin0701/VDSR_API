# VDSR_API
## VDSR을 활용한 저화질 비디오 프레임 업샘플링
### 주제 선정 이유 및 목적
현재 미디어 산업은 현대인들의 삶에 필수적인 요소로 자리잡았다. 하지만 영상처리 기술이 발전되기 전 과거 영상 프레임의 화질은 대부분 저화질이었다. ‘네셔널 지오그래픽’의 영상을 이에 대한 예시다.  13년 전, 최대 화질이 480p로 매우 낮은 프레임을 지원하였던 기술이 현재 2024년에는 최대 1080p 화질을 제공한다. 이로 인해 10년이라는 짧은 시간 내에 미디어 산업의 기술발전이 매우 빠르게 성장했음을 알 수 있다. 

> 이미지 출처 : https://www.youtube.com/@NatGeo/videos

> ### <2011년 National GeoGraphic /최대 화질 480p> 
> ![image](https://github.com/dabin0701/VDSR_API/assets/144203473/af2d6ebf-e184-4d7c-8c27-3284a2407dcc)

> ### <2024년 National GeoGraphic /최대 화질1080p>
> ![image](https://github.com/dabin0701/VDSR_API/assets/144203473/b22d0cd9-f459-402c-800d-795d74085d57)

저화질 이미지가 고화질로 변경되는 구조에 대한 궁금증으로 인해 해당 프로젝트 주제로 선정하게 되었고, 화질 개선에 특화된 모델인 VDSR(Very Deep Super Resolution)을 적용하여 저화질 이미지를 고화질 이미지로 업샘플링 하는 것을 목적으로 한다.

***
### 프로젝트 개요
VDSR 모델 구현을 위해 깃허브에서 코드를 불러왔고, Train data는 Test data는 'Set5'를


***
### 필요한 라이브러리(버전) 또는 프로그램 목록
VDSR 모델 구현을 위해 ‘twtygqyy’가 구현한 코드를 불러왔고, 
주소 https://github.com/twtygqyy/pytorch-vdsr/blob/master/vdsr.py  
Train data -
validation data - NationalgeoGraphic
Test dataSet - 'Set5'
***
### 추후 개선 사항 : 추가로 개선해야할 내용에 대해 정리 또는 프로젝트 한계점 설명
