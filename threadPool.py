import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f"done sleeping {seconds}..."


with concurrent.futures.ThreadPoolExecutor() as executor:
    # 3:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

# 2:
# results=[executor.submit(do_something,1) for _ in range(10)]
# for f in concurrent.futures.as_completed(results):
# print(f.result())

# 1:
# f1= executor.submit(do_something,1)
# f2= executor.submit(do_something,1)
# print(f1.result())
# print(f2.result())
# if we want to excute a function once at a time ==> we use submit()
# submit(): schedule a function to be excuted at a time and returns a future object

finish = time.perf_counter()

print(f'finisjed in {round(finish - start, 2)} seconds')
