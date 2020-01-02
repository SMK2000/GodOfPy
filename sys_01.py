# Introducing sys module
import sys
print("System version is {}".format(sys.version))
# Since we're testing on windows
# print(sys.getwindowsversion)
# use platform module instead - explained later
sys.stderr.write('This is stderr test\n')
sys.stderr.flush()
sys.stdout.write('This is stdout test\n')
# To get file path , use sys.argv
print(sys.argv)
