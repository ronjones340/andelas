from periodtype import (days,weeks,months)

def estimator(data):
    ptype = data["periodType"]
    if (str(ptype) == 'days'):
        results = days(data)
        return results
    elif (str(ptype) == 'weeks'):
        results = weeks(data)
        return results
    else:
        results = months(data)
    return results


#estimator(data)
