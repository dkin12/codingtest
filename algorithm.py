import time # time모듈 불러오기
#순차 탐색 a는 리스트, key는 탐색 키
def sequential_search(a,key) :
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

def unique_elements(A): #리스트 A입력
    n = len(A) # 입력의 크기 = 리스트의 크기
    for i in range (n-1): # 0~n-2
        for j in range(i+1,n): # i+1 ~ n-1
             if A[i] == A[j]: # 기본연산
                return False # 같은 항목이 있으면 False
    return True # 같은 항목이 없으면 True

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def selection_sort(A):
    n = len(A)
    for i in range (n-1):
        least = i
        for j in range(i+1,n):
            if(A[j]<A[least]):
                least = j
        A[i], A[least] = A[least], A[i]
        print(A,i+1)

def string_matching(T,P):
    n = len(T)
    m = len(P)
    for i in range (n-m+1):
        j = 0
        while j < m and p[j] == T[i+j]:
            j = j+1
        if j == m:
            return i
        return -1

def factorial_recur(n):
    if n==1:
        return 1
    else:
        return (n*factorial_recur(n-1))

def factorial_iter(n):
    result = 1
    for k in range(1,n+1):
        result = result * k
    return result

def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i -1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key

#알고리즘 테스트
data = [5,3,8,4,6,9,1,2,7]
print("original : ")
print(data)
insertion_sort(data)
print("Section:",data)


start = time.time()  # 현재 시각을 start에 저장
#실행시간을 측정하려는 알고리즘 호출
end = time.time() # 현재 시각을 end에 저장
print ("실행시간 = ", end-start)

def binary_search(A,key,low,high):
    if(low <= high):
        mid = (low + high) //2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binary_search(A,key,low,mid-1)
        else:
            return binary_search(A,key,mid+1,high)
    return -1

def binary_search_iter(A,key,low,high):
    while(low<=high):
        mid = ( low + high)//2
        if key==A[mid]:
            return mid
        elif key > A[mid]:
            low = mid + 1
        else:
            high = mid -1
    return -1

def slow_power (x,n):
    result = 1.0
    for i in range(n):
        result = result * x
    return result

def power(x,n):
    if n==0:
        return 1
    elif (n%2) == 0:
        return power(x*x,n//2)
    else:
        return x*power(x*x,(n-1)//2)