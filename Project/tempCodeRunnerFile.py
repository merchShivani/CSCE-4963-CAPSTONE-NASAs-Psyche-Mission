# Create button rectangles
for i, button in enumerate(buttons):
    button["rect"] = pygame.Rect(button_x, button_y + i * (button_height + 10), button_width, button_height)