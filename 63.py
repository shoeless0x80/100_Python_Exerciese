import time

counter = 0
while counter < 4:
    print("Hello")
    time.sleep(counter)
    counter += 1

print("End of the Loop")

'''
i = 0
while True:
    print("Hello")
    i = i + 1
    if i > 3:
        print("End of loop")
        break
    time.sleep(i)
'''
