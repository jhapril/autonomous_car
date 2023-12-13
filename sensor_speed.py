import RPi.GPIO as GPIO
import time

# 초음파 센서 핀 설정
TRIG_PIN = 5
ECHO_PIN = 6

# 모터 드라이버 핀 설정
ENA = 17
IN1 = 27  # 왼쪽 전진
IN2 = 22  # 왼쪽 후진
ENB = 18
IN3 = 23  # 오른쪽 후진
IN4 = 24  # 오른쪽 전진

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

motor_pwm1 = GPIO.PWM(ENA, 1000)  # 왼쪽 전력 공급
motor_pwm2 = GPIO.PWM(ENB, 1000)  # 오른쪽 전력 공급

# 초기화
motor_pwm1.start(0)
motor_pwm2.start(0)


# 거리 측정
def measure_distance():
    # 트리거 신호 발생
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # 초음파 수신 및 펄스 시작 시간 기록
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start_time = time.time()

    # 초음파 수신 및 펄스 종료 시간 기록
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end_time = time.time()

    # 펄스 지속 시간 계산 및 거리 계산
    pulse_duration = pulse_end_time - pulse_start_time
    distance = pulse_duration * 34300 / 2

    return distance


# 속도 제어
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
    while True:
        dist = measure_distance()
        print(dist)
        time.sleep(0.5)
        motor_forward_right(30)
        motor_forward_left(30)

        if dist < 10:
            stop()

except KeyboardInterrupt:
    stop()
    GPIO.cleanup()

