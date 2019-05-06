def bouncing_balls(height, bounce, window):
    bounce_count = 1

    if float(height) <= 0 or float(bounce) >= 1 or float(bounce) <= 0 or float(window) >= float(height):
        return -1
    else:
        while height > window:
            height = height * bounce
            if height > window:
                bounce_count += 2
        return bounce_count

print(bouncing_balls(1.5, 0.66, 1.5))
print(bouncing_balls(3, 1, 1.5))


