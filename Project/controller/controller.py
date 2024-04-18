import pygame

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.instructions_displayed = False
        self.spectrometer_instructions_displayed = False
        self.magnetic_instructions_displayed = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                elif event.key == pygame.K_LEFT:
                    self.model.orbit_speed /= 4
                elif event.key == pygame.K_RIGHT:
                    self.model.orbit_speed *= 4
                elif event.key == pygame.K_UP:
                    self.model.psyche_spacecraft.move_out = True
                elif event.key == pygame.K_DOWN:
                    self.model.psyche_spacecraft.move_in = True
                elif event.key == pygame.K_s:
                    if not self.spectrometer_instructions_displayed:
                        self.show_spectrometer_instructions_popup()
                    else:
                        self.model.spectroGame_bool = True
                elif event.key == pygame.K_m:
                    if not self.magnetic_instructions_displayed:
                        self.show_magnetic_instructions_popup()
                    else:
                        self.model.magfieldGame_bool = True
                elif event.key == pygame.K_i:
                    self.show_main_instructions_popup()
                elif event.key == pygame.K_e:
                    self.model.spectroGame_bool = False
                    print("Exiting the game")
                elif event.key == pygame.K_j:
                    self.model.magfieldGame_bool = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.model.orbit_speed *= 4
                elif event.key == pygame.K_RIGHT:
                    self.model.orbit_speed /= 4 
                elif event.key == pygame.K_UP:
                    self.model.psyche_spacecraft.move_out = False
                elif event.key == pygame.K_DOWN:
                    self.model.psyche_spacecraft.move_in = False

    def handle_mouse_click(self, mouse_position):
        pass

    def update_model(self):
        self.model.update()
        self.view.update_display()

    def quit_game(self):
        pygame.quit()
        exit()

    def show_main_instructions_popup(self):
        instructions = [
            "Welcome to the Mission to Psyche game!",
            "",
            "This is a game where you will learn about NASA's Psyche mission.",
            "You will be able to go through mini-games that are fun and educational and relate to the instruments NASA is using on this mission.",
            "There are currently two mini-games to select from: The Spectrometer mini-game and the Magnetic Field mini-game.",
            "Press the key 's' to start the Spectrometer mini-game or press 'm' to start the Magnetic Field mini-game.",
            "",
            "Press any key to close."
        ]
        self.display_instructions_popup(instructions)

    def show_spectrometer_instructions_popup(self):
        instructions = [
            "Spectrometer Mini-Game Instructions:",
            "",
            "In NASA's Psyche mission, they use an instrument called the spectrometer which measures gamma rays and neutrons with the Psyche asteroid.",
            "Your job is to collect all the gamma rays and neutrons.",
            "",
            "Controls:",
            "Left arrow key: increase the orbit speed of the spacecraft.",
            "Right arrow key: decrease the orbit speed of the spacecraft.",
            "Up arrow key: increase the size of the spacecraft's orbit.",
            "Down arrow key: decrease the size of the spacecraft's orbit.",
            "",
            "Double tap 's' again to start the Spectrometer mini-game or any other key to close."
        ]
        self.spectrometer_instructions_displayed = True
        self.display_instructions_popup(instructions)

    def show_magnetic_instructions_popup(self):
        instructions = [
            "Magnetic Field Mini-Game Instructions:",
            "",
            "NASA's Psyche team will measure the asteroid's magnetic field using a magnetometer.",
            "Your job is to scan the asteroid by completing this memorization mini-game.",
            "",
            "Controls:",
            "There are white squares and gray squares.",
            "The white squares are the ones you need to memorize because they will disappear.",
            "Your goal is to correctly match the pattern that was displayed on the screen.",
            "Each time you get a pattern correctly, you will scan the asteroid for its magnetic field.",
            "If you correctly match 3 patterns, you will win the game and advance to the next mini-games!",
            "",
            "Double tap 'm' again to start the Magnetic Field mini-game or any other key to close."
        ]
        self.magnetic_instructions_displayed = True
        self.display_instructions_popup(instructions)

    def display_instructions_popup(self, instructions):
        font = pygame.font.SysFont('arial black', 25)
        text_y = 50

        for instruction in instructions:
            text_render = font.render(instruction, True, (255, 255, 255))  # Black font color
            text_rect = text_render.get_rect(center=(self.view.screen.get_width() // 2, text_y))
            self.view.screen.blit(text_render, text_rect)
            text_y += 40

        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting = False
                    break

    def run_game(self):
        running = True
        while running:
            self.handle_events()
            self.update_model()

    def start(self):
        self.run_game()
