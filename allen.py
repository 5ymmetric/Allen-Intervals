# Data type to store time points in seconds
class TimePoint:
    def __init__(self, time):
        self.time = time

    def __eq__(self, other):
        return (self.time == other.time)

    def __ne__(self, other):
        return (self.time != other.time)

    def __lt__(self, other):
        return (self.time < other.time)

    def __le__(self, other):
        return (self.time <= other.time)

    def __gt__(self, other):
        return (self.time > other.time)

    def __ge__(self, other):
        return (self.time >= other.time)

    def __str__(self):
        return str(self.time)

# Data type to store the interval of time points
class Interval:
    def __init__(self, beginTime, endTime):
        self.beginTime = beginTime
        self.endTime = endTime
    def __str__(self):
        return "[" + str(self.beginTime.time) + ", " + str(self.endTime.time) + "]"

# Start Method: returns the begin time of an interval
def Start(interval):
    return interval.beginTime

# End Method: returs the end time of an interval
def End(interval):
    return interval.endTime

# Utility function
def printIntervals(i, j):
    print("i <-- ", end="")
    print(i)
    print("j <-- ", end="")
    print(j)
    print()

# Meet Predicate
def Meet(i, j):
    print("Meet")
    printIntervals(i, j)
    return End(i) == Start(j)

# Before Predicate
def Before(i, j):
    print("Before")
    printIntervals(i, j)
    return End(i) < Start(j)

# After Predicate
def After(i, j):
    print("After")
    printIntervals(i, j)
    return End(j) < Start(i)

# During Predicate
def During(i, j):
    print("During")
    printIntervals(i, j)    
    return ((Start(j) <= Start(i)) and (End(i) <= End(j)))

# Overlap Predicate
def Overlap(i, j):
    print("Overlap")
    printIntervals(i, j)    
    return ((Start(i) <= Start(j)) and (End(i) >= Start(j)) and (End(i) <= End(j)) or (Start(j) <= Start(i)) and (End(j) >= Start(i)) and (End(j) <= End(i)))

# Equals Predicate
def Equals(i, j):
    print("Equals")
    printIntervals(i, j)    
    return ((Start(i) == Start(j)) and (End(i) == End(j)))

# Finishes Predicate
def Finishes(i, j):
    print("Finishes")
    printIntervals(i, j)    
    return End(i) == End(j)

# Contains Predicate
def Contains(i, j):
    print("Contains")
    printIntervals(i, j)    
    return ((Start(i) < Start(j)) and (End(i) > End(j)))

# Utility function
def visualize(i, j):
    print(" " * Start(i).time, end="")
    print("|", end="")
    print("-" * (End(i).time - Start(i).time), end="")
    print("|")

    print(" " * Start(j).time, end="")
    print("|", end="")
    print("-" * (End(j).time - Start(j).time), end="")
    print("|")

# Default test case
def defaultTest():
    # To use a different test case, please change values here.
    i = Interval(TimePoint(5), TimePoint(10))
    j = Interval(TimePoint(7), TimePoint(13))

    visualize(i, j)

    print()

    print("=" * 15)
    print(Meet(i, j))
    print("=" * 15)

    print("=" * 15)
    print(Before(i, j))
    print("=" * 15)

    print("=" * 15)
    print(After(i, j))
    print("=" * 15)

    print("=" * 15)
    print(During(i, j))
    print("=" * 15)

    print("=" * 15)
    print(Overlap(i, j))
    print("=" * 15)

    print("=" * 15)
    print(Equals(i, j))
    print("=" * 15)

    print("=" * 15)
    print(Finishes(i, j))
    print("=" * 15)

    print("=" * 15)
    print(Contains(i, j))
    print("=" * 15)

defaultTest()