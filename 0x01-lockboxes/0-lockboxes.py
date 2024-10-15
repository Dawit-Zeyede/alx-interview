#!/usr/bin/python3
'''
determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''Determines if all the boxes in a list of boxes can be unlocked
    starting from the first box.
    '''
    n = len(boxes)
    boxesPresent = {0}
    keys_to_check = list(boxes[0])

    while keys_to_check:
        boxIdx = keys_to_check.pop(0)
        if 0 <= boxIdx < n and boxIdx not in boxesPresent:
            boxesPresent.add(boxIdx)
            keys_to_check.extend(boxes[boxIdx])
    return len(boxesPresent) == n


def main():
    """Entry point"""
    boxes = [[1, 2], [3], [0, 4], [], []]
    print(canUnlockAll(boxes))


if __name__ == '__main__':
    main()
