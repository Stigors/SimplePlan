import datetime as dt


def date():
    return (dt.datetime.utcnow() + dt.timedelta(hours=3)).strftime('%D')
