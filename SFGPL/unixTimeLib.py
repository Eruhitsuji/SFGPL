class unixTime:

    DEFAULT_UNIX_EPOCH_YEAR=1970

    DEFAULT_DAYS_IN_400YEARS=146097
    DEFAULT_SECONDS_IN_DAY=86400
    DEFAULT_SECONDS_IN_HOUR=3600
    DEFAULT_SECONDS_IN_MINUTE=60

    @staticmethod
    def isLeapYear(year:int):
        if(year%400==0):
            return True
        if(year%100==0):
            return False
        if(year%4==0):
            return True
        return False
    
    @staticmethod
    def daysInMonth(year:int,month:int):
        days_in_months =[
            31,
            29 if unixTime.isLeapYear(year) else 28,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31
        ]
        return days_in_months [month-1]
    
    @staticmethod
    def daysOfYear(year):
        return 366 if unixTime.isLeapYear(year) else 365
    
    @staticmethod
    def convUnixTimeDays2Date(unix_time_days:int):
        year=unixTime.DEFAULT_UNIX_EPOCH_YEAR

        year+=(unix_time_days//unixTime.DEFAULT_DAYS_IN_400YEARS)*400
        days=unix_time_days%unixTime.DEFAULT_DAYS_IN_400YEARS
            
        if(days<0):
            while(days<0):
                days_in_year=unixTime.daysOfYear(year)
                year-=1
                days+=days_in_year
        else:
            while(True):
                days_in_year=unixTime.daysOfYear(year)
                if(days>=days_in_year):
                    days-=days_in_year
                    year+=1
                else:
                    break

        month=1
        while(True):
            days_in_this_month=unixTime.daysInMonth(year,month)
            if(days>=days_in_this_month):
                days-=days_in_this_month
                month+=1
            else:
                break
        
        day=days+1
        return [year,month,day]

    @staticmethod
    def convUnixTime2DateTime(unix_time_sec:int):
        days=unix_time_sec//unixTime.DEFAULT_SECONDS_IN_DAY
        remaining_seconds=unix_time_sec%unixTime.DEFAULT_SECONDS_IN_DAY
        
        if(remaining_seconds<0):
            days-=1
            remaining_seconds+=unixTime.DEFAULT_SECONDS_IN_DAY
        
        year,month,day=unixTime.convUnixTimeDays2Date(days)
        hour=remaining_seconds//unixTime.DEFAULT_SECONDS_IN_HOUR
        remaining_seconds%=unixTime.DEFAULT_SECONDS_IN_HOUR
        minute=remaining_seconds//unixTime.DEFAULT_SECONDS_IN_MINUTE
        second=remaining_seconds%unixTime.DEFAULT_SECONDS_IN_MINUTE
        return [year,month,day,hour,minute,second]

    @staticmethod
    def convUnixTimeNanoSec2DateTime(unix_time_ns:int):
        DEFAULT_NANO_IN_SECOND=1_000_000_000

        unix_time_sec=unix_time_ns//DEFAULT_NANO_IN_SECOND
        remaining_ns=unix_time_ns%DEFAULT_NANO_IN_SECOND

        year,month,day,hour,minute,second=unixTime.convUnixTime2DateTime(unix_time_sec)

        return [year,month,day,hour,minute,second,remaining_ns]
    
    
    @staticmethod
    def convUnixTime(unix_time:int,mode:str="dt"):
        if(mode=="d"):
            return unixTime.convUnixTimeDays2Date(unix_time)
        elif(mode=="dt"):
            return unixTime.convUnixTime2DateTime(unix_time)
        elif(mode=="dtn"):
            return unixTime.convUnixTimeNanoSec2DateTime(unix_time)
        else:
            return []

    """
    dt_list=[
        year,
        month,
        day,
        (hour),
        (minute),
        (second),
        ((nano_second))
    ]
    """
    @staticmethod
    def convDateTimeStr(dt_list:list):
        dt_list_len=len(dt_list)
        s=""
        
        #date
        if(dt_list_len>=3):
            s+=f"{dt_list[0]}-{dt_list[1]:02}-{dt_list[2]:02}"
        
        #time
        if(dt_list_len>=6):
            s+=f" {dt_list[3]:02}:{dt_list[4]:02}:{dt_list[5]:02}"
        
        #nano sec
        if(dt_list_len>=7):
            s+=f".{dt_list[6]:09}"

        return s