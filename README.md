# VDSR_API
## VDSR을 활용한 저화질 비디오 프레임 업샘플링
현재 미디어 산업은 현대인들의 삶에 필수적인 요소로 자리잡았다. 하지만 영상처리 기술이 발전되기 전의 영상 프레임의 화질은 대부분 저화질이었다. 이에 대한 예시로 13년 전 ‘네셔널 지오그래픽’의 영상의 최대 화질은 480p로 매우 낮은 프레임을 지원한다. 하지만 2024년의 네셔널 지오그래픽의 영상은 최대 1080p 화질을 제공한다. 
<2011년 National GeoGraphic /최대 화질 480p> 
![image](https://github.com/dabin0701/VDSR_API/assets/144203473/af2d6ebf-e184-4d7c-8c27-3284a2407dcc)

<2024년 National GeoGraphic /최대 화질1080p>

기술의 발전에 따라 고화질 영상으로 발전될 수 있던 기술에 대한 궁금증이 생겼고, 저화질 이미지가 고화질로 변경되는 구조에 대한 궁금증이 생겼다. 때문에 저화질 이미지를 고화질로 바꾸는 것에 특화된 모델인 VDSR(Very Deep Super Resolution)을 적용하여 저화질 이미지를 고화질 이미지로 업샘플링 하는 것을 목적으로 두었다.
