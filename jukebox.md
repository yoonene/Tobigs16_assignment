# OpenAI Jukebox
## 모델 구조
* AutoEncoder 구조

<img src="https://user-images.githubusercontent.com/56261032/140885344-e62c78e4-06db-419d-b5f2-7a19eefba61e.png" width="500" height="200">

### Encoding, Embedding
* Top-level : 필수 음악 정보만 보존 (128x로 압축) <br>
  Middel-level (32x로 압축) <br>
  Bottom-level (8x로 압축)
* 이 3가지 level에 대해 각자 인코딩, 디코딩
* CNN을 통해 Encoding -> VQ-VAE를 통해 양자화 임베딩하여 오디오 압축
### 음악 생성
* 위 과정으로 압축된 이산 공간을 이용해 음악을 생성
* prior 모델 사용: 단순하게 변형된 sparse transformer를 활용한 autoregressive 모델 사용
  - Top-level의 prior 모델의 결과는 오디오 품질이 낮지만 노래 및 멜로디 등 높은 수준(중요한 정보)에 대해 포착함
  - 그 밑의 middle, bottom level은 음색과 같은 로컬 음악 구조를 추가하여 오디오 품질을 크게 향상시킴
### Upsampling, Decoding
* prior 모델 학습이 완료되면 Top-level에서 코드를 생성하고 업샘플러를 통해 업샘플링한 후 VQ-VAE 디코더를 통해 디코딩하여 완성
## DPR-martini blue.mp3를 bonny M 스타일, pop 장르로 생성해봄.
* prior 모델까지만 거쳐서 Top-level에서 생성된 결과만 본거라 지저분함.
* 그 뒤 upsampling은 시간이 없어서 못해봄. <br>
-> 결과: 당연히 bonny M과 pop장르로 학습시켰던 노래들처럼 생성된 음악에 비트, 보컬 등 여러 구성이 추가됨.
## 내 생각
학습된 스타일대로 음악의 패턴이 transform되는 식이니까 앞 노래를 뒷 노래 스타일로 각색한다는 개념으로,
뒷 노래만 띡 학습시키고 앞 노래를 오토인코더에 입력하고 생성된 패턴을 뒷 노래 스타일로 transform하고 복원하는 방식은 어떨까
