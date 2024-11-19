class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        A, B = len(word1), len(word2)   # length of both the words
        a, b = 0, 0                     # indeces of both words, initialized at 0. (index counters)
        s = []          # making a list, will convert to string later. (For effeciency)

        word = 1                            # starting at word 1
        while a < A and b < B:   # indeces will move from 0 till length of both the words.
            if word == 1:                   # is word 1? if yes then 
                s.append(word1[a])          # appending current word1 index element to "s" list.
                a = a + 1                   # incrementing the word1 index counter.
                word = 2                    # flipping to word2 (its turn of word2)
            else:                   # if word is not word1.
                s.append(word2[b])          # then append current word2 index element to "s" list.
                b = b + 1                   # incrementing the word2 index counter.
                word = 1                    # flipping to word1
        
        # in the case of remainging additional letters, just append normally.
        # Note: Only one of them will execute.

        while a < A:                # if word1 is longer than word 2
            s.append(word1[a])      # else this will not be executed.
            a = a + 1
        
        while b < B:                # if word2 is longer than word 1
            s.append(word2[b])      # else this will not be executed.
            b = b + 1
        
        # When everything is done, finlly change the list "s" to string.

        return ''.join(s)

        # Time: O(A + B), lengths of both the words.
        # Space: O(A + B)