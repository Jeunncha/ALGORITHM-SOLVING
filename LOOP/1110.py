import sys

while True:
  try:
    N = int(sys.stdin.readline())
    A = N
    NN = N
    i = 0
    frontNum, backNum = divmod(N,10) #몫과 나머지 한번에 구하는 함수
    while True:
      N = frontNum + backNum
      if N >= 10:
        N = N%10
      NN = backNum*10 + N
      frontNum, backNum = divmod(NN,10)
      i += 1
      if A == NN:
        print(i)
        i=0
        break

  except:
    break