# --- from https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        print('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

# def line_intersect( line1, line2 ):
#     """ returns a (x, y) tuple or None if there is no intersection """
#     Ax1 = line1[0][0]
#     Ay1 = 
#     Ax2
#     Ay2
#     Bx1
#     By1
#     Bx2
#     By2
#     d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
#     if d:
#         uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
#         uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
#     else:
#         return
#     if not(0 <= uA <= 1 and 0 <= uB <= 1):
#         return
#     x = Ax1 + uA * (Ax2 - Ax1)
#     y = Ay1 + uA * (Ay2 - Ay1)
#     return x, y