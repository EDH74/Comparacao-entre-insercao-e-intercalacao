class ordenacao:
        
    def insertion_sort(self, arr):
        contComparacoes = 0
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                contComparacoes+=1
                self.arr[j + 1] = self.arr[j]
                j = j - 1
            self.arr[j + 1] = key
            
            return (arr, contComparacoes)
    
    def merge_sort(self, arr):
        contComparacoes = 0
        
        #o array passado tem que ter o tamanho maior que 1 para ser ordenado
        if len(self.arr) > 1:
            qntComparacoes+=1
            #gerando lista dividida para cada comparacao
            mid = len(self.arr) // 2
            leftHalf = self.arr[:mid]
            rightHalf = self.arr[mid:]

            self.mergeSort(leftHalf)
            self.mergeSort(rightHalf)

            
            leftIndex=0
            rightIndex=0
            dataIndex=0

          
            while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):

                
                if leftHalf[leftIndex] < rightHalf[rightIndex]:
                    self.arr[dataIndex]=leftHalf[leftIndex]
                    leftIndex=leftIndex+1

                
                else:
                    self.arr[dataIndex]=rightHalf[rightIndex]
                    rightIndex=rightIndex+1
                dataIndex=dataIndex+1

            
            while leftIndex < len(leftHalf):
                self.arr[dataIndex]=leftHalf[leftIndex]
                leftIndex=leftIndex+1
                dataIndex=dataIndex+1

            
            while rightIndex < len(rightHalf):
                self.arr[dataIndex]=rightHalf[rightIndex]
                rightIndex=rightIndex+1
                dataIndex=dataIndex+1
            
            return (arr, contComparacoes)
        