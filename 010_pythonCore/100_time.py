import time

unixTime = time.time()  # время в секундах с начала эпохи юникс, т.е. 01.01.1970
localTime = time.ctime(unixTime)
localTime_str = time.localtime(unixTime)
unixTime_2 = time.mktime(localTime_str)
localTime_2 = time.asctime(localTime_str)

utcTime_str = time.gmtime(unixTime)
utcTime = time.asctime(utcTime_str)
unixTime_3 = time.mktime(utcTime_str)
