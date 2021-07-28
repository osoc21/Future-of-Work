def calculateGap(supply,demand):
    '''Calculate the gap in between the supply and demand'''
    gap = []
    # We go over each year
    for yearSupply,yearDemand in zip(supply,demand):
        # We take the supply and demand data
        dataSupply = yearSupply["data"]
        dataDemand = yearDemand["data"]
        dataGap = {}
        # We go over all jobs per family
        for familySupply,familyDemand in zip(dataSupply,dataDemand):
            jobsSupply = dataSupply[familySupply]
            jobsDemand = dataDemand[familyDemand]
            jobsGap = []
            # We go over each job
            for jobSupply,jobDemand in zip(jobsSupply,jobsDemand):
                jobGap = {}
                # We substract the supply from the demand
                for jobTitleSupply,jobTitleDemand in zip(jobSupply,jobDemand):
                    jobGap[jobTitleDemand] = jobDemand[jobTitleDemand] - jobSupply[jobTitleSupply]
                jobsGap.append(jobGap)
            dataGap[familySupply] = jobsGap
        # We store the gap
        gap.append({"year":yearSupply["year"],"data":dataGap})        
    return gap