import asyncio
import random

# 模拟的5个异步方法
async def task(name):
    print(f"{name} 开始执行")
    await asyncio.sleep(random.uniform(0.5, 2))  # 模拟耗时操作
    print(f"{name} 执行完成")
    return f"{name} 的结果"

# 控制并发数为2的执行器
async def limited_task(semaphore, name):
    async with semaphore:  # 控制同时只能有两个任务进入
        return await task(name)

async def main():
    semaphore = asyncio.Semaphore(2)  # 最多允许两个并发
    task_names = ["任务1", "任务2", "任务3", "任务4", "任务5"]

    # 创建协程列表，每个任务都受限于 semaphore
    tasks = [limited_task(semaphore, name) for name in task_names]

    # 等待所有任务执行完毕，并收集结果
    results = await asyncio.gather(*tasks)

    print("所有任务执行完毕，最终结果：")
    print(results)

# Python 3.7+
if __name__ == "__main__":
    asyncio.run(main())