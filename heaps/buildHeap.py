# Max Heap Array implementation 
class Heap:
    def heapify(self,arr,n,i):
        largest = i
        left = 2*i+1
        right = 2*i+2

        if left< n and arr[left] > arr[i]:
            largest=left
        if right< n and arr[right] > arr[largest]:
            largest=right
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            self.heapify(arr,n,largest)


    def buildMaxHeap(self,arr,n):
        for i in range(n//2,-1,-1):
            self.heapify(arr,n,i)

    def heapSort(self,arr):
        n=len(arr)
        self.buildMaxHeap(arr,n)
       
        for i in range(n-1,0,-1):
          #swap arr[0] with arr[-1]
          arr[0],arr[i] = arr[i],arr[0]
          self.heapify(arr,i,0)


h = Heap()

arr = [4,1,3,2,16,9,10,14,8,7]

h.heapSort(arr)
print(arr)
