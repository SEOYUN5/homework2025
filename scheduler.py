import time
import threading

# 1. 주기적으로 실행할 작업(함수) 정의
def periodic_task():
    """5초마다 실행될 작업을 정의하는 함수."""
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[Worker] 작업 실행됨: 현재 시간은 {current_time} 입니다.")

# 2. 작업을 예약하고 실행하는 스케줄러 함수
def scheduler(interval_seconds):
    """지정된 시간 간격으로 작업을 반복 실행하는 스케줄러."""
    print("=== 스케줄러 시작 ===")
    
    # 무한 루프를 돌며 작업을 반복 실행
    while True:
        # 실행할 작업을 별도의 스레드로 실행 (비동기 처리 흉내)
        task_thread = threading.Thread(target=periodic_task)
        task_thread.start()
        
        # 다음 실행을 위해 지정된 시간(interval_seconds)만큼 대기
        time.sleep(interval_seconds)

# 3. 메인 실행 부분 (스케줄러 구동)
if __name__ == "__main__":
    # 작업을 5초마다 실행하도록 설정
    run_interval = 5 
    
    # 스케줄러를 메인 스레드가 아닌 별도의 스레드로 실행
    # 이렇게 하면 메인 프로그램이 멈추지 않고 다른 작업도 수행할 수 있지만, 
    # 여기서는 스케줄러를 계속 실행하는 역할만 합니다.
    try:
        scheduler_thread = threading.Thread(target=scheduler, args=(run_interval,))
        # 메인 프로그램이 종료될 때 스레드도 함께 종료되도록 설정
        scheduler_thread.daemon = True 
        scheduler_thread.start()

        # 스케줄러가 백그라운드에서 실행되는 동안, 메인 프로그램은 여기서 대기
        print("백엔드 스케줄러가 백그라운드에서 실행 중입니다. (Ctrl+C를 눌러 종료하세요)")
        
        # 무한 대기 (스케줄러가 계속 실행되도록 유지)
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n=== 스케줄러 종료됨 ===")
