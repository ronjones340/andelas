from periodtype import (days,weeks,months)

data = {
    "region": {
    "name": "Africa",
    "avgAge": 19.7,
    "avgDailyIncomeInUSD": 4,
    "avgDailyIncomePopulation": 0.73
    },
    "periodType": "days",
    "timeToElapse": 38,
    "reportedCases": 2747,
    "population": 92931687,
    "totalHospitalBeds": 678874

    }
def estimator(data):
    ptype = data["periodType"]
    if (str(ptype) == 'days'):
        x = days(data)
        return x
    elif (str(ptype) == 'weeks'):
        x = weeks(data)
        return x
    else:
        x = months(data)
        return x


#estimator(data)
