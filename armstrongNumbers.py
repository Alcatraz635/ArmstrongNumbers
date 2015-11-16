import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    nums = [int(i) for i in list(test.strip())]
    if(int(test) == reduce(lambda x,y: x+y, map(lambda x: (x**len(nums)),nums))): print True
    else: print False

test_cases.close()
exit(0)