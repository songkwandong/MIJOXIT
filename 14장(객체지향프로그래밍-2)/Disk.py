
class Disk(object):
    __capacity = 0 #용량
    __rpm = 0 #속도

    def __init__(self, capacity, rpm) -> None:
        self.__capacity = capacity
        self.__rpm = rpm
    
    def get_capacity(self):
        return self.__capacity

    def get_rpm(self):
        return self.__rpm

    def show_print(self) -> str:
        print(f"디스크의 용량은 {self.get_capacity()}GB 이며, " \
                f"RPM은 {self.get_rpm()}입니다.")