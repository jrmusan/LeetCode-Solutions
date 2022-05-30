class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        total = 0
        
        # Loop through all the known jewels
        for jewel in jewels:
            
            # Check if this stone is a jewel, if so add it to the list and get the total length
            total += len([stone for stone in stones if stone == jewel])
            
        return total
