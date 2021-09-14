# Abstraction
* 강화 학습(Reinforcement Learning)을 사용하여 high-dimensional sensory input으로부터 policy를 control하는 법을 학습하는 모델을 제시.
* CNN 기반, Q-learning 사용.
* Input: raw pixels, output: value function(future rewards의 추정값)
* 이를 Atari 2600에 적용시켜 좋은 성과를 얻음.

<br>

# Introduction
* vision, speech 등 high-dimensional sensory input으로부터 agents를 control하기 위해 기존의 연구는 hand-crafted features를 사용. 이는 데이터의 품질에 큰 영향을 받음.
* 딥러닝은 raw data로부터 higt-level feature를 추출 가능. -> CNN, mlp, restricted Boltzmann machine, RNN 등의 방법이 RL에 효과적인지 확인해보려고 함.
* 하지만 딥러닝을 RL에 적용하는데 여러 문제점이 있음.
  * 딥러닝은 hand-labelled 데이터가 필요한데, RL은 sparse, noisy, delayed로 발생하는 scalar reward로부터 학습함. action과 resulting rewards로 인한 지연 발생.
  * 딥러닝의 데이터는 독립적이어야 하지만, RL은 highly-correlated state들의 시퀀스는 서로 연관되어 있음.
  * 딥러닝은 고정확률 분포를 가정하지만, RL은 새로운 행동마다 데이터의 분포가 바뀜.
* 본문에서는 위와 같은 문제를 CNN을 사용하여 극복하고 polices를 훈련시킴.
* 변형된 Q-Learning 알고리즘과 Stochastic gradient descent를 사용하여 훈련.
* 데이터끼리 연관되어있는 문제를 해결하기 위해 experience replay mechanism을 사용. -> 이전 행동에 대한 학습 분포(training data distribution)를 완화.

<br>

# Deep Reinforcement Learning
* 딥러닝은 vision, speech 분야에서 효과적.
* RL에 딥러닝을 접목.
* SGD 업데이트를 통해 RGB 이미지를 효과적으로 처리.
* 이 논문에서 제시하는 구조의 시작점:  Tesauro's TD-Gammon architecture
* TD-Gammon과 on-policy와 다르게 제안하는 알고리즘은 experience replay를 사용.
 * time-stemp에서 episode를 agent의 experience로 replay memory에 저장. 
 * replay memory에서 episode를 무작위로 가져와서 Q-Learning 업데이트.
 * 이렇게 sampling한 episode를 기반으로 e-greedy policy를 적용.
* 이 방식의 장점
 * 각 experience는 학습과정에 여러번 사용됨. -> 데이터의 효율성 증가
 * randomizing sampling을 통해 experience data간 correlation을 줄이고 업데이트의 variance를 감소시킴.
 * on-policy로 학습하면 current parameter가 next data sample을 결정함. -> 안정적인 학습.

<br>

# Preprocessing anf Model Architecture
* Atari game의 이미지 크기: 210 x 160
* resize to 110 x 84, gray scaling
* cropping 84 x 84 
* 모델 구조
 * input: 84x84x4
 * convlove 16 8x8 filters(stride 4), ReLU
 * convlove 32 4x4 filters(stride2), ReLU
 * 256 hidden units fully-connected layer, ReLU
 * fully-connected layer(output layer) action 사이즈의 output

# Experiments
* 7개의 Atari game에 대해서 DQN 성능을 테스트.
* 모든 게임에 동일한 조건.
* 각 게임의 score 단위가 달라 positive reward: 1, negative reward: -1, 변화 없음: 0 으로 설정.
* Optimizer: RMSProp, mini-batch: 32
* 1000만 프레임을 학습. replay memory에는 100만 프레임만 사용.
### Training ad Stability
* RL은 evaluation metrics를 정하기 어려움. 
* evaluation metrics: 
 1) average award
 2) average action value(Q)
* 둘 중 average action value의 덜 noisy 한 것을 확인.
* 7개의 Atari game 모두에서 좋은 성능을 보임.
 
