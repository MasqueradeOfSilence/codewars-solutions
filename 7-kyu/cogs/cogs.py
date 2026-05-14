def cog_RPM(cogs):
    # RPM of next cog = RPM of current cog × (current teeth / next teeth)
    rpm = 1 # first one is rpm 1
    for index, cog_teeth_count in enumerate(cogs):
        if (index == len(cogs) - 1):
            break
        rpm = rpm * -(cog_teeth_count / cogs[index + 1])
    
    return rpm