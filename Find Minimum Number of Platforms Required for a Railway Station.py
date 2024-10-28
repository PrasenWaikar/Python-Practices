def find_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    
    n = len(arrivals)
    platform_needed = 1
    result = 1
    i = 1
    j = 0
    
    while (i < n and j < n):
        if arrivals[i] <= departures[j]:
            platform_needed += 1
            i += 1
        elif arrivals[i] > departures[j]:
            platform_needed -= 1
            j += 1
        if platform_needed > result:
            result = platform_needed
            
    return result

arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
print("Minimum platforms needed:", find_platforms(arrivals, departures))
