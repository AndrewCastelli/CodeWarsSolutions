def make_readable(seconds):
    hour = seconds // 3600
    mini = (seconds - hour * 3600) // 60
    sec = seconds - (hour * 3600 + mini * 60)

    return "{:0>2}:{:0>2}:{:0>2}".format(hour, mini, sec)

