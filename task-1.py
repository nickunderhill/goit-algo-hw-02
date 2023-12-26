import queue
import time

requests_queue = queue.Queue()
request_id = 1

def generate_request(request_id):
    requests_queue.put(request_id)
    print(f"Створено заявку {request_id}")

def process_request():
    if not requests_queue.empty():
        request = requests_queue.get()
        print(f"Оброблено заявку {request}")

def main():
    global request_id
    try:
        while True:
            generate_request(request_id)
            request_id += 1
            process_request()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Програма зупинена користувачем")

if __name__ == "__main__":
    main()
