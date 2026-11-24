# HW6
김아란 24011476
## 실행 방법
.venv에서 jupyter로 hw6.ipynb를 Run All
flask --app app run 뒤 http://127.0.0.1:5000/api/docs
## 단계③답
Linear Regression은 수량과 단가의 선형 결합으로 총액을 예측하기 때문에 두 변수의 곱셈 관계를 정확히 표현하지 못한다.
수량과 단가를 곱한 qp를 특성으로 추가하면 실제 총액 계산 공식을 표현할 수 있으므로 R^2가 1.0이 된다.
## 단계⑤결정과 이유
max_depth = 8
depth 12와 비교했을 때 cross-validation 평균 R^2의 차이는 0.003에 불과하지만 잎의 수는 250개와 781개로 차이가 크기 때문에 성능이 비슷하면서 구조가 단순한 depth 8을 선택했다.
## 단계⑦답
수량 40, 단가 200,000의 실제 총액은 8,000,000원이다. Decision Tree(depth 8)는 7,362,301원으로 예측했지만, Linear Regression + qp는 실제 총액과 동일한 8,000,000원으로 예측했다. 따라서 실제 계산 규칙을 정확히 표현할 수 있는 Linear Regression + qp를 최종 모델로 선정하였다.