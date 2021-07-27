

def calculateGap(supply,demand):
    gap = []

    for yearSupply,yearDemand in zip(supply,demand):
        dataSupply = yearSupply["data"]
        dataDemand = yearDemand["data"]
        dataGap = {}
        for familySupply,familyDemand in zip(dataSupply,dataDemand):
            jobsSupply = dataSupply[familySupply]
            jobsDemand = dataDemand[familyDemand]
            jobsGap = []
            for jobSupply,jobDemand in zip(jobsSupply,jobsDemand):
                jobGap = {}
                for jobTitleSupply,jobTitleDemand in zip(jobSupply,jobDemand):
                    jobGap[jobTitleDemand] = jobDemand[jobTitleDemand] - jobSupply[jobTitleSupply]
                jobsGap.append(jobGap)
            dataGap[familySupply] = jobsGap
        gap.append({"year":yearSupply["year"],"data":dataGap})
        
    return gap