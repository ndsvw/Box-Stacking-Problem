def maxHeightTry1(d1, d2, d3):
    """
    A method that calculates largest possible tower height of given boxes (bad approach 1/2).
    Problem description: https://practice.geeksforgeeks.org/problems/box-stacking/1
        time complexity: O(n*max(max_d1, max_d2, max_d3)^2)
        space complexity: O(n*max(max_d1, max_d2, max_d3)^2)

    Parameters
    ----------
    d1 : int[]
        a list of int values representing the 1st dimension of a / multiple 3d-box(es)
    d2 : int[]
        a list of int values representing the 2nd dimension of a / multiple 3d-box(es)
    d3 : int[]
        a list of int values representing the 3rd dimension of a / multiple 3d-box(es)

    Returns
    -------
    x  : int
        the largest possible tower height
    """

    assert(len(d1) >= 1)
    assert(len(d1) == len(d2) == len(d3))

    max_dimension = max([
        max(d1),
        max(d2),
        max(d3)
    ])

    boxes = zip(d1, d2, d3)
    boxes = map(sorted, boxes)
    boxes = sorted(boxes, key=lambda e: e[2])
    boxes = sorted(boxes, key=lambda e: e[1])
    boxes = sorted(boxes, key=lambda e: e[0])
    boxes = boxes + list(map(lambda e: [e[1], e[2], e[0]], boxes))
    boxes = sorted(boxes, key=lambda e: e[2])
    boxes = sorted(boxes, key=lambda e: e[1])
    boxes = sorted(boxes, key=lambda e: e[0])

    n = len(boxes)

    # dimension 1: i.th box
    # dimension 2: x-coordinate left
    # dimension 3: y-coordinate left
    max_height = {i: [[0 for _ in range(max_dimension + 1)]
                      for _ in range(max_dimension + 1)] for i in range(-1, n)}

    for i in range(n):
        box_x, box_y, box_z = boxes[i][0], boxes[i][1], boxes[i][2]
        for x in range(max_dimension + 1):
            for y in range(max_dimension + 1):
                max_tmp = max_height[i-1][x][y]
                if box_x <= x and box_y <= y:
                    max_tmp = max(
                        max_tmp, max_height[i-1][box_x-1][box_y-1] + box_z)
                if box_x <= x and box_z <= y:
                    max_tmp = max(
                        max_tmp, max_height[i-1][box_x-1][box_z-1] + box_y)
                if box_y <= x and box_z <= y:
                    max_tmp = max(
                        max_tmp, max_height[i-1][box_y-1][box_z-1] + box_x)
                max_height[i][x][y] = max_tmp
    return max_height[n-1][max_dimension][max_dimension]


def maxHeightTry2(d1, d2, d3):
    """
    A method that calculates largest possible tower height of given boxes (optimized, but bad approach 2/2).
    Problem description: https://practice.geeksforgeeks.org/problems/box-stacking/1
        time complexity: O(n*max(max_d1, max_d2, max_d3)^2)
        space complexity: O(max(max_d1, max_d2, max_d3)^2)

    Parameters
    ----------
    d1 : int[]
        a list of int values representing the 1st dimension of a / multiple 3d-box(es)
    d2 : int[]
        a list of int values representing the 2nd dimension of a / multiple 3d-box(es)
    d3 : int[]
        a list of int values representing the 3rd dimension of a / multiple 3d-box(es)

    Returns
    -------
    x  : int
        the largest possible tower height
    """

    assert(len(d1) >= 1)
    assert(len(d1) == len(d2) == len(d3))

    max_dimension = max([
        max(d1),
        max(d2),
        max(d3)
    ])

    boxes = zip(d1, d2, d3)
    boxes = map(sorted, boxes)
    boxes = sorted(boxes, key=lambda e: e[2])
    boxes = sorted(boxes, key=lambda e: e[1])
    boxes = sorted(boxes, key=lambda e: e[0])
    boxes = boxes + list(map(lambda e: [e[1], e[2], e[0]], boxes))
    boxes = sorted(boxes, key=lambda e: e[2])
    boxes = sorted(boxes, key=lambda e: e[1])
    boxes = sorted(boxes, key=lambda e: e[0])

    n = len(boxes)

    # dimension 1: x-coordinate left
    # dimension 2: y-coordinate left
    max_height = [[0 for _ in range(max_dimension + 1)]
                  for _ in range(max_dimension + 1)]

    for i in range(n):
        box_x, box_y, box_z = boxes[i][0], boxes[i][1], boxes[i][2]
        for x in range(box_x, max_dimension + 1):
            for y in range(box_y, max_dimension + 1):
                max_tmp = max_height[x][y]
                if box_x <= x and box_y <= y:
                    max_tmp = max(
                        max_tmp, max_height[box_x-1][box_y-1] + box_z)
                if box_x <= x and box_z <= y:
                    max_tmp = max(
                        max_tmp, max_height[box_x-1][box_z-1] + box_y)
                if box_y <= x and box_z <= y:
                    max_tmp = max(
                        max_tmp, max_height[box_y-1][box_z-1] + box_x)
                max_height[x][y] = max_tmp
    return max_height[max_dimension][max_dimension]


def maxHeightTry3(d1, d2, d3):
    """
    A method that calculates largest possible tower height of given boxes.
    Problem description: https://practice.geeksforgeeks.org/problems/box-stacking/1
        time complexity: O(n^2)
        space complexity: O(n)

    Parameters
    ----------
    d1 : int[]
        a list of int values representing the 1st dimension of a / multiple 3d-box(es)
    d2 : int[]
        a list of int values representing the 2nd dimension of a / multiple 3d-box(es)
    d3 : int[]
        a list of int values representing the 3rd dimension of a / multiple 3d-box(es)

    Returns
    -------
    x  : int
        the largest possible tower height
    """

    assert(len(d1) >= 1)
    assert(len(d1) == len(d2) == len(d3))

    boxes = zip(d1, d2, d3)
    boxes = map(sorted, boxes)
    boxes = sorted(boxes, key=lambda e: (e[0], e[1], e[2]))
    boxes = boxes + list(map(lambda e: [e[1], e[2], e[0]], boxes))
    boxes = boxes + list(map(lambda e: [e[0], e[2], e[1]], boxes))
    boxes = sorted(boxes, key=lambda e: (e[0], e[1], e[2]))

    n = len(boxes)
    max_height = {(b[0], b[1]): b[2] for b in boxes}

    for i in range(n):
        box1_x, box1_y = boxes[i][0], boxes[i][1]
        for j in range(i+1, n):
            box2_x, box2_y, box2_z = boxes[j][0], boxes[j][1], boxes[j][2]
            max_tmp = max_height[box2_x, box2_y]
            if box1_x < box2_x and box1_y < box2_y:
                max_tmp = max(max_tmp, max_height[box1_x, box1_y] + box2_z)
            max_height[box2_x, box2_y] = max_tmp
    return max([v for _, v in max_height.items()])
