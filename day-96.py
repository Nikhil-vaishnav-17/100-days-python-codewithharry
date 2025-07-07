#AsyncIO
import asyncio

#It is a module that runs multiple function parallely

async def func1():
    print("Func 1")
    await asyncio.sleep(3)
    print("Func 1 completed")

async def func2():
    print("Func 2")
    await asyncio.sleep(3)
    print("Func 2 completed")

async def func3():
    print("Func 3")
    await asyncio.sleep(3)
    print("Func 3 completed")

async def main():
    await asyncio.gather(
        func1(),
        func2(),
        func3()
    ) #This will run all the function parallely

    #IF we run them separately then it will run one by one
    await func1()
    await func2()
    await func3()

asyncio.run(main())