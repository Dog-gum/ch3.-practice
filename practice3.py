# 예제3
# 첫 줄에 숫자카드들의 행의 개수(N), 열의 개수(M)이 주어짐.
# 둘째 줄부터 숫자가 주어진다.
# 행을 선택하고, 행에서 제일 작은 숫자들을 비교해서 가장 큰 수가 있는 행을 택하면 된다.
# 그 수를 출력한다.

N,M = map(int,input().split())
card=[]

for n in range(N):
  N_n = list(map(int, input().split()))
  N_n.sort()
  card.append(N_n[0]) # 각 행에서 가장 작은 수들로 리스트를 구성.

card.sort()
print(card[-1])  # 각 행에서 가장 큰 수 출력.