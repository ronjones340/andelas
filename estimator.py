from periodtype import (days,weeks,months)

def estimator(data):
    ptype = data["periodType"]
    if (str(ptype) == 'days'):
        x = days(data)
    elif (str(ptype) == 'weeks'):
        x = weeks(data)
    else:
        x = months(data)
    return x


#estimator(data)
