import time


# def using_while():
#     i = 0
#     while i < 500:
#         print(i)
#         i = i + 1
#
#
# def using_for():
#     for i in range(500):
#         print(i)
#
#
# init = time.time()
# using_while()
# t1 = time.time() - init
#
# init = time.time()
# using_for()
# t2 = time.time() - init
#
# print(f"Time for while loop: {t1}")
# print(f"Time for for loop: {t2}")

# print(3)
# time.sleep(3)
# print("This printed after 3 seconds")

time_in_secs = time.localtime()
time = time.strftime('%d-%m-%Y  %H:%M:%S', time_in_secs)
print(time)
