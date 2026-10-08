class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):

            last = (i == 0) or (flowerbed[i-1] == 0)
            right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

            if last and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n-=1
                if n == 0:
                    return True
        return False