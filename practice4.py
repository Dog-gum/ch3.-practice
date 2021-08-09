# 예제4
# N과 K가 주어질 때 다음 2가지 연산 중 하나만 해서 1을 만들 때까지 수행하는 최소 횟수 구하기.
# 첫 줄에 N과 K가 주어짐
# 1. N에서 1을 빼거나 2. N을 K로 나누거나.(2번은 나누어떨어질 때만)

N,K = map(int, input().split())
count = 0

while True:
  if N == 1:
    break
  elif N%K == 0:
    N = N/K
    count += 1
  elif N%K != 0:
    N = N - 1
    count += 1

print(count)


