import math

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

print("Введіть координати точки A (x y z), через пробіл: ")
x1, y1, z1 = map(float, input().split())

print("Введіть координати точки B (x y z), через пробіл:")
x2, y2, z2 = map(float, input().split())

print("Введіть координати точки C (x y z), через пробіл:")
x3, y3, z3 = map(float, input().split())


a = distance(x2, y2, z2, x3, y3, z3)  # BC
b = distance(x3, y3, z3, x1, y1, z1)  # CA
c = distance(x1, y1, z1, x2, y2, z2)  # AB


if a == 0 or b == 0 or c == 0:
    print("Помилка: одна з вершин збігається з іншою. Трикутник не існує.")
else:

    def safe_sqrt(x):
        return math.sqrt(max(0.0, x))

    m_a = 0.5 * safe_sqrt(2*b*b + 2*c*c - a*a)
    m_b = 0.5 * safe_sqrt(2*c*c + 2*a*a - b*b)
    m_c = 0.5 * safe_sqrt(2*a*a + 2*b*b - c*c)

    print(f"Довжини сторін: a={a:.6f}, b={b:.6f}, c={c:.6f}")
    print("Довжини медіан трикутника:")
    print(f"m_a (з вершини A до середини BC) = {m_a:.6f}")
    print(f"m_b (з вершини B до середини CA) = {m_b:.6f}")
    print(f"m_c (з вершини C до середини AB) = {m_c:.6f}")
