import heapq


def gift_wrap(length, width, height):
    """Return gift wrap needed in square feet
    for given dimensions of a present.
    """
    # get slack from product of 2 smallest sides
    side1, side2 = heapq.nsmallest(2, (length,width,height))
    slack = side1 * side2
    
    area = 2*length*width + 2*width*height + 2*height*length

    return slack + area


def ribbon_length(length, width, height):
    """Return total ribbon length needed in feet
    for given dimensions of a present.
    """
    # get shortest perimeter around present
    # for base ribbon length
    side1, side2 = heapq.nsmallest(2, (length,width,height))
    base_length = 2 * side1 + 2 * side2
    # bow length determined by cubic feet
    # of volume of present
    bow_length = length * width * height

    return base_length + bow_length


with open('clue.txt') as f:
    dimensions = [tuple(map(int, dimension.split('x'))) for dimension in f]

print('Part 1:', sum(gift_wrap(*d) for d in dimensions))
print('Part 2:', sum(ribbon_length(*d) for d in dimensions))
