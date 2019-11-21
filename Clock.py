from time import sleep


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        if hour >= 24 or minute >= 60 or second >= 60 or hour < 0 or minute < 0 or second < 0:
            print("time is wrong")
            exit(2)
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 57)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
