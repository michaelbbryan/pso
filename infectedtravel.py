# Basic infection models assume bounded communities, like petri dishes
#
# Let's add interaction between communities:
#     each community has an original population - see US census PEP_2018_PEPCUMCHG.US24PR
#        metropolitan statistical areas (MSAs)
#        consolidated metropolitan statistical areas (CMSAs)
#        primary metropolitan statistical areas (PMSAs)
#        within each area there may also be "incorporated places" like boroughs or areas within cities
#     each community has a different urban density that affect infection rate
#       https://www.governing.com/gov-data/population-density-land-area-cities-map.html
#        one measure of density is the number of incorporated places > 10000
#        Louisville is the 45th largest city in US but the 10th most dense
#     add a square matrix of travel from/to or origination/destination
#        the diagonal should be zero or meaningless
#        the upper triangular does not equal the lower triangular
#           infected travel Chicago to NY is different than NY to Chicago rather than a net number
#        taken from air travel Bureau of Transportation Safety
#           https://www.transtats.bts.gov/Tables.asp?DB_ID=125&DB_Name=Airline%20Origin%20and%20Destination%20Survey%20%28DB1B%29&DB_Short_Name=Origin%20and%20Destination%20Survey
#        train travel is complex, statistics have origination but not destination
#        car travel

import pandas as pd

