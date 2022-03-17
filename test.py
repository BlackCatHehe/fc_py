
from asyncio import ALL_COMPLETED
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.connection import wait
import time

urls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

def getUrl(a):
    time.sleep(3)
    print(a)

def downloadByThreadPoolExecutor(poolSize=3):
    count = len(urls)
    # 构造线程参数
    args = []
    for index in range(0, count):
      args.append(urls[index])
    # 线程池大小
    if count < poolSize:
        poolSize = count
    # 构造线程池
    pool = ThreadPoolExecutor(max_workers=poolSize)
    tasks = []
    for arg in args:
        task = pool.submit(getUrl, arg)
        tasks.append(task)
    wait(tasks, return_when=ALL_COMPLETED)
    
    
if __name__ == '__main__':
    downloadByThreadPoolExecutor()