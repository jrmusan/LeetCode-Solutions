class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        # All we need to do is ensure there are 27 unique letters
        # If we cast this to a set we will have only unique elements
        return len(set(sentence)) ==26
