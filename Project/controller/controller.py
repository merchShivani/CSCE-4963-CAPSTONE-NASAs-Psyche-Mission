import pygame

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

            # Events when key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                if event.key == pygame.K_LEFT:
                    self.model.orbit_speed = (self.model.orbit_speed / 4)
                if event.key == pygame.K_RIGHT:
                    self.model.orbit_speed = (self.model.orbit_speed * 4)

            # Events when key released
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.model.orbit_speed = (self.model.orbit_speed * 4)
                if event.key == pygame.K_RIGHT:
                    self.model.orbit_speed = (self.model.orbit_speed / 4) 

            # Events when mouse clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.handle_mouse_click(event.pos)

            # Add more event handling as needed

    def handle_mouse_click(self, mouse_position):
        # Check if the mouse click is within the spawn button area
        pass


    def update_model(self):
        # Update model and view
        self.model.update()
        self.view.update_display()

    def quit_game(self):
        pygame.quit()
        exit()

