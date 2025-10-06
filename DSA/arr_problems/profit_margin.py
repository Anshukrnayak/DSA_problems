

import numpy as np

class profit_margin:

    def __init__(self,arr):
        self.arr=arr 

    def maximum(self):
        max=0

        for i in self.arr:
            
            if max<i:
                max=i
        
        return max
     

    def minimum(self):
        min=self.arr[0]

        for i in self.arr:
            if min>i:
                min=i
        
        return min

    def profit_margin(self):
         return self.maximum()-self.minimum()


def main():
    arr=np.array([10,20,23,-10,24])

    pf=profit_margin(arr)

    ans=pf.profit_margin()

    print(f'profit margin : {ans} ')



if __name__=='__main__': main()
        