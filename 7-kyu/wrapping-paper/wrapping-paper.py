def wrapping_paper(boxes):
    # boxes is a list of (l, w, h)
    # return total wrapping paper needed
    total = 0
    for box in boxes:
        # SA = 2lw + 2lh + 2wh
        length = box[0]
        width = box[1]
        height = box[2]
        surface_area = (2 * length * width) + (2 * length * height) + (2 * width * height)
        slack = min(length * width, length * height, width * height)
        total += surface_area + slack
    return total