class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return[]
        common_chars=list(words[0])
        for word in words[1:]:
     #update common_chars to only keep characters that appear in both
            new_common_chars=[]
            for char in common_chars:
                if char in word:
                    new_common_chars.append(char)
                    word=word.replace(char,'',1) #remove the char from word once
                    common_chars=new_common_chars
        return common_chars
