class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # Loop through all the letters that are supposed to be there
        for letter in s:
            
            # If the letter is in t, remove it, place doesn't matter
            if letter in t:
                t = t.replace(letter, "", 1)

        # Lastly, just find the one item left in the t str
        for item in t:
            if item:
                return item
