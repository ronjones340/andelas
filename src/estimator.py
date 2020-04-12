from periodtype import days,weeks,months
data ={
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
        results = days(data)
        return results
    elif (str(ptype) == 'weeks'):
        results = weeks(data)
        return results
    else:
        results = months(data)
        return results


#print(estimator(data))
