class Repl:
    def __init__(self, msg_handler):
        self.msg_handler = msg_handler

    def run(self):
        while True:
            user_input = input(">>> ")
            print(self.msg_handler(user_input))
