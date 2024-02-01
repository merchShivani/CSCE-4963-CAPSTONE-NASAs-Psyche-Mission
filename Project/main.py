from model.model import GameModel
from view.view import GameView
from controller.controller import GameController

def main():
    model = GameModel()
    view = GameView()
    controller = GameController(model, view)

    while True:
        controller.handle_events()
        controller.update_model()
        view.update_display()

if __name__ == "__main__":
    main()
