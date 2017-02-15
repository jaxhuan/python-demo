from datetime import datetime, timedelta, timezone

tz_utc_8 = timezone(timedelta(hours=8))

now = datetime.now()
print(now, 'timestamp=>', now.timestamp())

dt = datetime(2017, 12, 28)

print(dt, 'timestamp=>', dt.timestamp())

# timestamp转换为当地时间
print('1487133633.646963 is mean time is =>', datetime.fromtimestamp(1487133633.646963))
# timestamp转换为utc标准时间
print('above to utc time =>', datetime.utcfromtimestamp(1487133633.646963))
# datetime转str(此处时区只能设置为本地时区)
print(now.replace(tzinfo=tz_utc_8).strftime('%Y-%b-%d %H:%M:%S %Z'))
# str转datetime
print(datetime.strptime('2017-02-15 12:46:40', '%Y-%m-%d %H:%M:%S'))

# 时间加减
print('now is time=>', now)
print('now later 2 hours time is:', now + timedelta(hours=2))
print('now before 3 hours time is:', now - timedelta(hours=3))

print('now before 26 days time is:', now - timedelta(days=26))

# 时区转换

# 获取到utc标准时间并强制设置时区为utc+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('\n', utc_dt)

utc_bj = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('\n', utc_bj)

utc_tokyo = datetime.now().replace(tzinfo=tz_utc_8).astimezone(timezone(timedelta(hours=9)))
print('\n', utc_tokyo)
