# Introduction
* Matrix Factorization(MF):  추천시스템에서 널리 사용되는, user와 item의 latent feature vector를 사용하여 상호작용을 학습하는 방법.
* MF의 단점
  * 단순 inner product는 multipliaction of latent feature를 linear 방식에 기반하여 결합. <br>

-> 이를 해결하기 위한 방법 제시: neural architecture 활용한 협업필터링 NCF
<br><br>
# Preliminaries
* Learning from implicit data
  * user u와 item i가 interaction이 있을 경우 yui = 1, 없을 경우 0 (0 이라고 비선호하는 것이 아님)
  * 2가지 학습 방법
    * point wise loss: 회귀에 활용되는 방법, 잔차를 최소화
    * pair wise loss: 관측값이 관측되지 않은 값보다 큰 값을 가지도록 하여 두 값의 마진을 최대화
    * Neural Collaborative Filtering은 둘 다 사용.
<br>

# Matrix Factorization
![alt MF](https://media.vlpt.us/images/kimkj38/post/e32a656d-3313-4574-a320-6abe6fa4f078/image.png)
* User latent factor와 item latent factor의 양방향 interaction 모델링
* 각각 독립적, 같은 가중치로 선형 결합
* latent factor의 linear model
## MF의 한계
![alt limitation_MF](https://media.vlpt.us/images/kimkj38/post/c489d561-d30a-4760-b742-3d1edb755636/image.png)
* u4에 대해 u1>u3>u2 순으로 유사하지만 이를 기하학적으로 표현할 수 없다. 
* 이는 ranking loss가 커지는 현상을 초래.
<br>

# Neural Collaborative Filtering
## General Framework
![alt limitation_MF](https://media.vlpt.us/images/kimkj38/post/4ebe9eab-a775-400c-b493-ef6af7d464d1/image.png)
* input - user와 item의 One-Hot Encoding 벡터
* embedding layer - dense vector로 변환 (MF모델의 잠재 벡터 역할)
* Neural Collaborative Filtering layers - score 예측
* loss function: binary cross entropy
## Generalized Matrix Factorization(GMF)
![alt limitation_MF](https://media.vlpt.us/images/kimkj38/post/75ba3886-f12d-44ff-ad2f-1cff642a0b0f/image.png)
* element-wise product 사용
* activation function: sigmoid
## Multi-Layer Perceptron(MLP)
![alt limitation_MF](https://media.vlpt.us/images/kimkj38/post/0c271602-4cec-4084-a357-bcde9009bb2c/image.png)
* element-wise product 사용
* 네트워크로 그냥 넘겨주지 않고 Concatenate 후 네트워크로 입력
## Fusion of GMP and MLP
![alt limitation_MF](https://media.vlpt.us/images/kimkj38/post/e29264db-3ffd-4064-b2aa-e259cb8c2f42/image.png)
* GMF와 MLP를 각각 수행 후 concatenation으로 합친 모델
* 선형적 특성(GMF)와 비선형적 특성(MLP)를 합쳐 복잡한 관계를 표현할 수 있음.
* 두 모델을 각각 최적화하기 때문에 서로 다른 사이즈의 임베딩을 가짐.
<br>

# Experiments
* Outperform state-of-the-art를 달성하였는가? (RQ1)
* Log loss와 Negative Sampling의 효과 (RQ2)
* Layer가 깊어질수록 user-item interaction 학습에 효과적인가? (RQ3)
## RQ1
![alt limitation_MF](https://media.vlpt.us/images/kimkj38/post/64c0dcea-c064-48cc-9cc0-a9338ce57637/image.png)
<br>모델별 성능 평가 결과 NeuMF 모델이 모든 경우에서 가장 성능이 높은 것을 확인.
## RQ2
![alt limitation_MF](https://media.vlpt.us/images/kimkj38/post/b0e506d9-3800-4a1b-aa06-3b08fc41dd91/image.png)
* More iteration -> NeuMF 모델의 training loss는 감소하지만 성능은 내려감. (overfitting)
* NeuMF의 성능이 가장 좋음.
* 3~6개의 negative sampling ratio일 때 더 효과적.
## RQ3
![alt limitation_MF](https://media.vlpt.us/images/kimkj38/post/b0e506d9-3800-4a1b-aa06-3b08fc41dd91/image.png)
<br>layer가 깊어질수록 더 성능이 좋아짐.


