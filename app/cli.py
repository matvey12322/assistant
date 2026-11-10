import argparse
import time
from app.client import call_with_stream, call

parser = argparse.ArgumentParser()
parser.add_argument('input', help='Запрос')
parser.add_argument("--stream", action='store_true')

args = parser.parse_args()

start_time = time.perf_counter()
if args.stream:
    try:
        first_text_ = True
        for event in call_with_stream(args.input):
            t = event.type

            if t == "response.output_text.delta":
                print(event.delta, end="")
                if first_text_:
                    first_text = time.perf_counter()
                    first_text_ = False

            elif t == "response.completed":
                print("\n",event.response.usage)
                break

            elif t == "response.incomplete":
                print("\n[ответ обрезан: max_output_tokens]")
                break

            elif t == "response.failed":
                print("\n[ошибка]", event.response.error)
                break
        all_call = time.perf_counter()
        print(f"Первый токен: {first_text - start_time}, всего: {all_call - start_time}")
    except KeyboardInterrupt:
        print("\nОтвет модели прерван")
else:
    print(*call(args.input), sep="\n")
    all_call = time.perf_counter()
    print(f"всего: {all_call - start_time}")

