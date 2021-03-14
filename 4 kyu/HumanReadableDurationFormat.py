def format_duration(seconds):
    if seconds == 0:
        return "now"

    sec = 1
    min = sec * 60
    hr = 60 * min
    day = 24 * hr
    yr = 365 * day

    digits = (
        (yr, 'year'),
        (day, 'day'),
        (hr, 'hour'),
        (min, 'minute'),
        (sec, 'second'),
    )

    time_list = []
    for digit in digits:
        period, word = digit
        if seconds >= period:
            now = int(seconds / period)
            time_list.append(add_s(now, word))
            seconds -= now * period

    return ' and'.join(', '.join(time_list).rsplit(',', 1))


def add_s(n, word):
    if n == 1:
        return '%d %s' % (n, word)

    return '%d %ss' % (n, word)
