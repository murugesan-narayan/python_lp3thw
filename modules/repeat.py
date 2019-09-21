import sched, time
from datetime import datetime as dt
from decimal import Decimal, ROUND_UP
#import schedule
import threading

def do_something(name, longitude, latitude):
    now = dt.now().strftime("Start_Time_%d%b%Y_%H_%M_%S_%f")
    print(f"{now}_Doing stuff...{name}, {longitude}, {latitude}")

def call_with_scheduler(no_of_times=1, with_in_minutes=1, delay_in_seconds=0.1):
    s = sched.scheduler(time.time, time.sleep)
    total_delay_in_secs = no_of_times * delay_in_seconds
    total_with_in_secs = with_in_minutes * 60
    if (no_of_times + total_delay_in_secs) < total_with_in_secs:
        print('Number of Call:', no_of_times)
        start = 0.0
        for i in range(no_of_times):
            s.enter(start, delay_in_seconds, do_something, kwargs={'name':str(i)+'_CALL', 'longitude': 15.0, 'latitude': 72.0})
            start += delay_in_seconds
    else:
        count = (no_of_times + total_delay_in_secs) / total_with_in_secs
        call_per_trigger = int(Decimal(count).to_integral_value(rounding=ROUND_UP))
        no_of_trigger = no_of_times/call_per_trigger
        no_of_trigger = int(Decimal(no_of_trigger).to_integral_value(rounding=ROUND_UP))
        print('Number of Call:', no_of_times, 'No of triggers:', no_of_trigger, 'Call per Trigger', call_per_trigger)
        start = 0.0
        trg_count_loop = 1
        for i in range(no_of_trigger):
            print('Trigger:', i)
            for j in range(call_per_trigger):
                if trg_count_loop == no_of_times:
                    break
                print('____Call:', j)
                s.enter(start, delay_in_seconds, do_something, kwargs={'name':str(trg_count_loop)+'_CALL', 'longitude': 15.0, 'latitude': 72.0})
                trg_count_loop = trg_count_loop + 1
    s.run()


if __name__ == '__main__':
    print(dt.now().strftime("Start_Time_%d%b%Y_%H_%M_%S_%f"))
    call_with_scheduler(no_of_times=60, with_in_minutes=1, delay_in_seconds=1)
    print(dt.now().strftime("End_Time_%d%b%Y_%H_%M_%S_%f"))
    print('====================================================================')
    call_with_scheduler(no_of_times=215, with_in_minutes=1, delay_in_seconds=0.1)
    print(dt.now().strftime("End_Time_%d%b%Y_%H_%M_%S_%f"))
    print('====================================================================')
