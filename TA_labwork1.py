import math

def median_length(p1, p2, p3):
    if p1 == p2 or p1 == p3 or p2 == p3:
        print("Помилка: дві або більше точок співпадають, медіана не існує.")
        return None

    mid = ( (p2[0] + p3[0]) / 2,
            (p2[1] + p3[1]) / 2,
            (p2[2] + p3[2]) / 2 )

    return math.sqrt((p1[0] - mid[0])**2 +
                     (p1[1] - mid[1])**2 +
                     (p1[2] - mid[2])**2)

def input_point(name):
    x = float(input(f"Введіть x координату точки {name}: "))
    y = float(input(f"Введіть y координату точки {name}: "))
    z = float(input(f"Введіть z координату точки {name}: "))
    return x, y, z

pointA = input_point("A")
pointB = input_point("B")
pointC = input_point("C")

ma = median_length(pointA, pointB, pointC)
mb = median_length(pointB, pointA, pointC)
mc = median_length(pointC, pointA, pointB)

if ma is not None and mb is not None and mc is not None:
    print("m_a =", round(ma, 6))
    print("m_b =", round(mb, 6))
    print("m_c =", round(mc, 6))
