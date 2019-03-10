class Message:
    def __init__(self,content, sender):
        self.content = content
        self.sender = sender

class User:
    def __init__(self,name, friends = None):
        self.name = name
        if friends is None:
            friends = {}
        self.friends = friends

    def receive_message(self,message):
        if message.sender not in self.friends:
            self.friends[message.sender] = []