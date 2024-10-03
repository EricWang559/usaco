MAX_N = 50

N = 0
x = [0] * MAX_N
y = [0] * MAX_N
tstop = [0] * MAX_N
dir = [''] * MAX_N

class Intersection:
    def __init__(self, i, j, time_i, time_j, active):
        self.i = i
        self.j = j
        self.time_i = time_i
        self.time_j = time_j
        self.active = active

I = [Intersection(0, 0, 0, 0, 0) for _ in range(MAX_N * MAX_N)]

def find_all_intersections():
    current = 0
    for i in range(N):
        for j in range(N):
            if dir[i] == dir[j]:
                continue  # no intersection if same direction (or same cow)

            # Possibly flip coordinates so that for simplicity, we can
            # assume without loss of generality that cow i is moving north, and cow j east
            xi, yi, xj, yj = x[i], y[i], x[j], y[j]
            if dir[i] == 'E':
                xi, yi, xj, yj = yi, xi, yj, xj

            if yi > yj:
                continue  # cow i already north of cow j?
            if xi < xj:
                continue  # cow i already west of cow j?
            if xi >= xj + yj - yi:
                continue  # cow i passes before cow j can cut her off

            Inew = Intersection(i, j, yj - yi, xi - xj, 1)
            I[current] = Inew
            current += 1

N = int(input())
for i in range(N):
    dir[i], x[i], y[i] = input().split()
    x[i] = int(x[i])
    y[i] = int(y[i])

find_all_intersections()

# Repeatedly find earliest remaining intersection and process it
while True:
    earliest = -1
    for i in range(MAX_N * MAX_N):
        if I[i].active:
            if earliest == -1 or I[i].time_i < I[earliest].time_i:
                earliest = i
    if earliest == -1:
        break
    E = I[earliest]
    if tstop[E.i] == 0 and (tstop[E.j] == 0 or tstop[E.j] > E.time_j):
        tstop[E.i] = E.time_i
    E.active = 0

for i in range(N):
    if tstop[i] == 0:
        print("Infinity")
    else:
        print(tstop[i])

