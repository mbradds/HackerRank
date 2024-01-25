# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cat_a_distance = abs(z-x)
    cat_b_distance = abs(z-y)
    
    if cat_a_distance > cat_b_distance:
        return "Cat B"
    elif cat_a_distance < cat_b_distance:
        return "Cat A"
    elif cat_a_distance == cat_b_distance:
        return "Mouse C"


if __name__ == '__main__':
    x = 2
    y = 5
    z = 4
    result = catAndMouse(x, y, z)
    