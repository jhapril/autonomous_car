import RPi.GPIO as GPIO
import time

TRIG_PIN = 5  # 센서에게 초음파 발사하도록 명령
ECHO_PIN = 6  # 초음파가 물체에 부딪혀 반사되어 센서로 돌아오는 시간을 측정

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)  # 트리거핀 출력
GPIO.setup(ECHO_PIN, GPIO.IN)  # 에코핀 입력


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

try:
    while True:
        dist = measure_distance()
        print("distance : {}cm".format(dist))
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()