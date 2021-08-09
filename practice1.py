# 예제1
# 주어진 돈(1260원)을 500, 100, 50, 10원으로 최소한의 동전 개수로 거슬러주기.

n = 1260
count = 0
mon_list = [500,100,50,10]

for money in mon_list:
  count += n//money
  n = n - money*(n//money)

print(count)