r = '''1967 DavidBowie
1969 SpaceOddity
1970 TheManWhoSoldTheWorld
1971 HunkyDory
1972 TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars
1973 AladdinSane
1973 PinUps
1974 DiamondDogs
1975 YoungAmericans
1976 StationToStation
1977 Low
1977 Heroes
1979 Lodger
1980 ScaryMonstersAndSuperCreeps
1983 LetsDance
1984 Tonight
1987 NeverLetMeDown
1993 BlackTieWhiteNoise
1995 1.Outside
1997 Earthling
1999 Hours
2002 Heathen
2003 Reality
2013 TheNextDay
2016 BlackStar'''.split()
a = {int(r[i]):[r[i+1]] for i in range(0,len(r),2)}
a[1977].append('Low')
a[1973].append('AladdinSane')
for i in range(input()):
    res = []
    x, y = map(int,raw_input().split())
    for j, u in a.items():
        if x <= j <= y:
            if len(u) == 1:
                res.append([j,u[0]])
            else:
                res.append([j,u[1]])
                res.append([j,u[0]])
    print len(res)
    for j in range(len(res)):
        print res[j][0], res[j][1]