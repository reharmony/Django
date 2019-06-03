# Car class: 정적특징(color), 동적특징(stop, start)
# 정적특징: 멤버변수
# 동적특징: 함수

class Car:
    # 정적특징
    color = '' # 인스턴스 변수: 객체(클래스의 인스턴스) 생성시 복사O
    price = 0
    count = 0 # 클래스 변수: 객체가 생성될 때 복사X, 클래스당 1개만 존재해서 객체간 공유

    # 생성자 : 객체 생성될 때 자동 호출됨
    def __init__(self, color, price):
        self.color = color
        self.price = price
        Car.count = Car.count + 1

    # 동적특징
    def start(self):
        print('빠르게 출발하다.')

    def stop(self):
        print('빠르게 멈추다.')

    def __str__(self):
        return self.color + ", " + str(self.price)

sedan = Car('red', 100)
taxi = Car('blue', 200)

print(sedan)
print(taxi)
print('-'*10)

print('내 차의 개수는 ', Car.count)
