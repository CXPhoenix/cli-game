import keyboard as kb
class keyDetect:
    def __init__(self):
        self.key_detect_moment = 'down'
        pass
    
    def getKey(self):
        self.__key = kb.read_event()
        if self.__key.event_type == self.key_detect_moment:
            return self.__key.name


if __name__ == '__main__':
    kd = keyDetect()
    print(kd.getKey())