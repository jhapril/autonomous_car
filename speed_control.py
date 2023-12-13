import RPi.GPIO as GPIO
import time

# 모터 드라이버 핀 설정
ENA = 17
IN1 = 27  # 왼쪽 전진
IN2 = 22  # 왼쪽 후진
ENB = 18
IN3 = 23  # 오른쪽 후진
IN4 = 24  # 오른쪽 전진

GPIO.setmode(GPIO.BCM)
GPIO.setup(ENA, GPIO.OUT)  # 왼쪽
GPIO.setup(IN1, GPIO.OUT)  # 왼쪽 전진
GPIO.setup(IN2, GPIO.OUT)  # 왼쪽 후진
GPIO.setup(ENB, GPIO.OUT)  # 오른쪽
GPIO.setup(IN3, GPIO.OUT)  # 오른쪽 후진
GPIO.setup(IN4, GPIO.OUT)  # 오른쪽 전진

motor_pwm1 = GPIO.PWM(ENA, 1000)  # 왼쪽 출력
motor_pwm2 = GPIO.PWM(ENB, 1000)  # 오른쪽 출력

# 초기화
motor_pwm1.start(0)
motor_pwm2.start(0)


# 속도 설정
def motor_forward_left(speed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    motor_pwm1.ChangeDutyCycle(speed)


def motor_forward_right(speed):
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    motor_pwm2.ChangeDutyCycle(speed)


def motor_backward_left(speed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    motor_pwm1.ChangeDutyCycle(speed)


def motor_backward_right(speed):
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    motor_pwm2.ChangeDutyCycle(speed)


def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)


try:
    motor_forward_left(20)
    motor_forward_right(20)

except KeyboardInterrupt:
    stop()
    GPIO.cleanup()

