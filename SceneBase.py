class SceneBase:
    def __init__(self):
        self.next = self

    def process_input(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def update(self):
        print("uh-oh, you didn't override this in the child class")

    def render(self, window_surface):
        print("uh-oh, you didn't override this in the child class")

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)