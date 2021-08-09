# 예제2
# 첫 줄에 N, M, K 의 자연수가 주어진다.
# 둘 째 줄에 N개의 자연수가 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.
# M: 더하는 횟수, K:같은 수가 최대로 연속될 수 있는 횟수
# 더해진 답을 출력하시오

N,M,K = map(int,input().split())
num = list(map(int,input().split()))

num = set(num)
num = list(num)
num.sort() # num을 오름차순으로 정리

count = 0
result = 0

for j in range(M):
  count += 1
  if (count)%(K+1) == 0:
    result += num[-2]
  else:
    result += num[-1]

print(result)