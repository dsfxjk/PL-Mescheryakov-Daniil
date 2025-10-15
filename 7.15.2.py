def dist(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**0.5

X = list(map(float, input("Координаты X (x1 x2 x3): ").split()))
Y = list(map(float, input("Координаты Y (y1 y2 y3): ").split()))
Z = list(map(float, input("Координаты Z (z1 z2 z3): ").split()))
T = list(map(float, input("Координаты T (t1 t2 t3): ").split()))

distances = [dist(X,Y), dist(X,Z), dist(X,T), dist(Y,Z), dist(Y,T), dist(Z,T)]
min_dist = min(distances)

print("Минимальное расстрояние точек друг от друга: ", min_dist)

'''Четыре точки заданы своими координатами X(x1, x2, x3), Y(y1, y2, y3), Z(z1, z2,
z3), T(t1,t2, t3). Выяснить, какие из них находятся на минимальном расстоянии
друг от друга и вывести на экран значение этого расстояния. Вычисление
расстояния между двумя точками оформить в виде процедуры.'''