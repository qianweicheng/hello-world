# 常见算法
## Top N
- 局部排序法(选择排序，冒泡排序)，选择出前N个数
- 堆排序法
    ```
        heap[k] = make_heap(arr[1, k]);
        for(i=k+1 to n){
            adjust_heap(heep[k],arr[i]);
        }
        return heap[k];
    ```
- 减治法
## 数1
- 位移法
- 求与法 x & (x-1)  
```
    while(n){
    result++;
    n&=(n-1);
    }
```
## 斐波那契
- 递归法
    ```
        def feb2(n):
            if n <= 2:
                return 1
            return feb2(n-1)+feb2(n-2)
    ```
- 递推法
    ```
    def feb1(n):
        if n < 2:
            return 1
        a=b=1
        for x in xrange(n-2):
            a,b = b, a+b
        return b
    ```
- 通项公式法