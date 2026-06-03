class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l=len(flowerbed)
        prev=1
        end=-1
        for i in range(l):
            if n==0:
                break
            if i+1==l: end=1
            if i-1==0: prev=-1
            if flowerbed[i]==1:
                continue
            else:
                if prev!=1 and end!=1:
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                        flowerbed[i]=1
                        n-=1
                elif prev!=1 and end==1:
                    end=-1
                    if flowerbed[i-1]==0:
                        flowerbed[i]=1
                        n-=1
                elif prev==1 and end!=1:
                    prev=-1
                    if flowerbed[i+1]==0:
                        flowerbed[i]=1
                        n-=1
                else:
                    flowerbed[i]=1
                    n-=1
        # print(n)
        return n==0

