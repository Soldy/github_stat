import time, sys, concurrent.futures,  tty


def commandIn():
    return sys.stdin.read(1)

def slave():
    return True

def doIt(command):
    if(command.rstrip() == 'q'):
        print(u"\u001b[?25h")
        sys.exit()

print(u"\u001b[?25l")
tty.setraw(sys.stdin.fileno())
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
commander = executor.submit(commandIn)
slave = executor.submit(slave)
while True:
    time.sleep(0.1)
    if commander.done():
        doIt(commander.result())
        commander = executor.submit(commandIn)

