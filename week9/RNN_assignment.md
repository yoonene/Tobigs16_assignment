# Abstract
* recurrence와 convolution을 제거하고 오로지 attention에만 기반한 새로운 network 제안.
* 병렬 처리 가능, 학습 시간 단축, 2014년 WMT 영어-독일어 번역 대회에서 sota 달성.
* 다른 task에도 일반화 가능.
<br>

# Introduction
* recurrent 모델의 sequential한 특성은 훈련 과정에서 병렬화를 배제. -> 샘플간 배치화를 제한하여 처리할 시퀀스의 길이가 길수록 치명적.
* attention mechanisms도 아직까지 recurrent network와 함께 사용됨.
* recurrnet 모델의 제약 사항을 극복하고 입력과 출력의 전역 의존성을 이끌어내기 위해 Transformer 제안.
<br>

# Model Architecture
* 가장 경쟁력 있는 신경망 기반 시퀀스 변형 모델은 encoder-decoder 구조를 가지고 있음. -> Auto-Regressive
* Transformer도 이와 같은 encoder-decoder 구조 사용.
* self-attention과 point-wise fully connected layer를 encoder와 decoder 에 쌓아서 사용.
## Encoder
* N = 6 의 동일한 layer로 구성.
* multi-hear self-attention mechanisms와 단순 position-wise FC feed-forward network의 sub-layer로 구성.
* sub-layer마다 residual connection, layer normalization 사용. 이를 위해 512의 output 차원을 가짐.
## Decoder
* N = 6 의 동일한 layer로 구성.
* 2개의 sub-layers 외에도 Encoder 스택의 출력을 통해 multi-head self-attention을 수행하는 sub-layer 사용.
* 순차적인 결과를 도출하기 위해 masking 기법을 통해 position i보다 작은 output 위치에만 의존.
<br>

# Attention
* attention 함수는 query, key, value, output이 모두 벡터일 때, query와 key-value 쌍의 집합을 output에 mapping 하는 것.
* query와 대응되는 key의 compatibility function에 의해 계산된 attention 가중치로 value를 weighted sum하여 output 계산.
## Multi-Head Attention
* query, key, value를 각각의 차원으로 변환하는 서로 다른 h개의 학습이 가능한 linear projection 후, 각각의 projected version에 대해 병렬적으로 attention을 진행하는 것이 병렬처리가 가능하기 때문에 단일 attention function을 수행하는 것보다 더 좋음.
* 각각의 keys, values, queries를 h개로 나눈 값들의 attention을 구하고 concat.
## Positional Encoding
* 제안하는 모델이 recurrence나 convolution을 포함하지 않기 때문에 순차적인 시퀀스의 위치 정보를 주입하기 위해 encoder 및 decoder stack 하단에 positional encodings을 추가함.
* positional encodings는 dmodel과 동일한 차원을 가지기 때문에 이를 더하는 작업이 가능했음.
* 해당 연구에는 다른 주기의 싸인, 코싸인 함수를 사용하였고 두 방식이 거의 동일한 결과로 나왔음.
* 모델이 훈련한 시퀀스의 길이보다 더 긴 시퀀스에 대해서도 extrapolate 할 수 있는 sinusodial version을 선정
<br>

# Why Self-Attention
1. 레이어 당 총 계산 복잡도가 줄어듦.
2. 병렬처리 될 수 있는 계산량이 늘어남.
3. rnn보다 훨씬 먼 거리의 시퀀스를 학습할 수 있음.
* 해석 가능성이 높아짐.
