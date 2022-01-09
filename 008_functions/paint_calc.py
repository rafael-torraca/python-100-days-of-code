def paint_calc(height, width, cover):
    from math import ceil
    area = height * width
    num_of_cans = ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")
    