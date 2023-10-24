# 웹크롤링 차단 안 당하는 법

# 1. random.uniform을 활용한 time.sleep
import time
import random

random_sec = random.uniform(3, 5)
time.sleep(random_sec)

