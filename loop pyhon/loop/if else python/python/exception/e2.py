import os
print("At the start....")
try:
    os._exit(0)
except SystemExit:
    print("systemexit  caught ....")
print("At the end...")