class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        freq = [0]*5 
        curr_frog, max_frog = 0, 0 

        for c in croakOfFrogs: 
            i = "croak".index(c)
            freq[i] += 1 

            if i == 0:
                curr_frog += 1
            # Check if croak is in sequence. 
            elif i and freq[i-1] < freq[i]:
                return -1 
            elif i == 4:
                curr_frog -= 1 
            
            max_frog = max(max_frog, curr_frog)
        
        return max_frog if curr_frog == 0 else -1 
