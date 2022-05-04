# 819. Most Common Word 가장 흔한 단어
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

# 입력d fvg
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]

# 출력
# "ball"

from typing import List
import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'^\w', '', paragraph).lower().split() if word not in banned]
    
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

