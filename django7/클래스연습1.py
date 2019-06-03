# Car class: 정적특징(color), 동적특징(stop, start)
# 정적특징: 멤버변수
# 동적특징: 함수

class Car:
    # 정적특징
    color = ''
    price = 0

    # 동적특징
    def start(self):
        print('빠르게 출발하다.')

    def stop(self):
        print('빠르게 멈추다.')

    def __str__(self):
        return self.color + ", " + str(self.price)



sedan = Car() # Car 클래스를 복사해서 객체 생성
sedan.color = 'red'
sedan.price = 500

taxi = Car()
taxi.color = 'orange'
taxi.price = 300

print(sedan)
print(taxi)
