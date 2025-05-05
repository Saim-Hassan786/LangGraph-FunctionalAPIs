from langgraph.func import entrypoint , task
import time

@task
def multiply_by_two(num):
    print("multiply by two",num)
    time.sleep(6)
    return num*2

@task
def multiply_by_three(num):
    print("multiply by three",num)
    time.sleep(3)
    return num*3

@entrypoint()
def parallel_workflow(num):
    start_time = time.time()
    futures = [multiply_by_two(num),multiply_by_three(num)]
    res = [future.result() for future in futures]
    end_time = time.time()
    print(f"Time Taken {end_time - start_time} Seconds")
    return {"results":res}
    

def main():
    result = parallel_workflow.invoke(100)
    print(result)
