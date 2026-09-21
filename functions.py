from General_info import *
def circle_rect_collison(circle_center, circle_radius,rect:pygame.Rect):
    closest_x = max(rect.left, min(circle_center[0], rect.right))
    closest_y = max(rect.top, min(circle_center[1], rect.bottom))
    
    distance_x = circle_center[0] - closest_x
    distance_y = circle_center[1] - closest_y
    distance_squared = (distance_x ** 2) + (distance_y ** 2)
    
    return distance_squared <= (circle_radius ** 2)