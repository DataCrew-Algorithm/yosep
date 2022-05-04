# 49 그룹 애너그램
#실패 (시간 제한 초과)
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for word in strs:
            sorted_strs.append(''.join(sorted(word)))   # 각각의 문자열을 sort하여 재배열 
            # ['aet', 'aet', 'ant', 'aet', 'ant', 'abt']                           

        strs_set = set(sorted_strs) # 집합으로 만들어서 중복된 단어 제거 ['aet', 'ant', 'abt']

        result = []
        for element in strs_set: # ['aet', 'ant', 'abt']
            anagrams = []
            for word in strs:
                if ''.join(sorted(word)) == element: # strs에 포함된 문자열의 sort가 집합의 요소와 같다면
                    anagrams.append(word)            # anagrams에 추가
            result.append(anagrams) # result에 모든 anagrams묶음을 추가
        return result

strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(strs))

