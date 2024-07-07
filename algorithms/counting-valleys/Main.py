import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    # Write your code here

    altitude = 0
    valleys = 0
    isValley = False
    for x in path:
        if x == 'U':
            altitude += 1
        elif x == 'D':
            altitude -= 1

        if altitude < 0:
            isValley = True

        if altitude == 0 and isValley:
            valleys += 1
            isValley = False

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
