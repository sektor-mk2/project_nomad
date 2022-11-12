# SHAPES
# if width is 0, fills

pygame.draw.line(surface, color, start_point, end_point, width)
pygame.draw.lines(surface, color, closed: Bool, pointlist, width)
pygame.draw.polygon(surface, color, pointlist, width)
pygame.draw.circle(surface, color, center_point, radius, width)

my_color = (0, 0, 0)
my_surface.fill(my_color)
