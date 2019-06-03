# Car class: 정적특징(channel), 동적특징(stop, start)
# 정적특징: 멤버변수
# 동적특징: 함수

class Tv:
    # 정적특징
    channel = 0
    volume = 0
    onOff = False

    # 생성자 : 객체 생성될 때 자동 호출됨
    def __init__(self, channel, volume, onOff):
        self.channel = 'Ch.' + str(channel)
        self.volume = 'Vol.' + str(volume)
        if onOff == True:
            self.onOff = 'ON'
        else:
            self.onOff = 'OFF'

    def __str__(self):
        return self.channel + ", " + self.volume + ", " + self.onOff

myTV = Tv(7, 9, True)
yourTV = Tv(9, 12, False)

print(myTV)
print(yourTV)
