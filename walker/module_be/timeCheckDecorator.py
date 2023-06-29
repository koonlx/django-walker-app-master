import datetime
import time


def logging_time(original_fn):
    def wrapper_fn(*args, **kwargs):
        start = time.time()
        result = original_fn(*args, **kwargs)
        end = time.time()
        print(f"WorkingTime[{original_fn.__name__}]: {str(datetime.timedelta(seconds=end-start))} sec")
        return result
    return wrapper_fn
