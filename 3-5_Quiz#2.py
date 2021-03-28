'''코딩 스터디 모임
월 4회 스터디
3회 온라인
1회 오프라인
조건 1 랜덤으로 날짜
조건 2 최소 일수인 28 이내
매월 1~3일은 스터디 준비때문에 제외
'''

from random import *

offline_day = str (randint (4, 28) )
print ('오프라인 스터디 모임 날짜는 매월', offline_day , '일로 선정되었습니다', end= '.')