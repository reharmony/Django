class Person:
    name = '사람'
    age = 100

    def eat(self):
        print('먹다.')

    def sleep(self):
        print('잠자다.')


class Man(Person): # Person클래스를 상속 -> class 자식클래스명(부모클래스명)
    name = '김한국' # override (오버라이드: 재정의) -> 변수의 재정의
    power = 100

    def sleep(self): # -> 함수의 재정의
        print('아주 많이 잔다.')
    def run(self):
        print('빨리 달리다.')

man1 = Man()
print(man1.name)
print(man1.age)
print(man1.power)
man1.sleep()