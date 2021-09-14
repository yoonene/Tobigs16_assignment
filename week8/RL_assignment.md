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

# Background
