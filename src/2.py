def sqrt(x):
  return x ** 0.5

def solve_square_equation():
  print('Решим уравнине вида ax^2 + bx + c = 0')
  a = int(input('Введита a: '))
  b = int(input('Введита b: '))
  c = int(input('Введита c: '))
  d = b**2 - 4 * a * c
  if a == 0:
    print('Если a = 0, то это не квадратное уравнение!')
    print('У линейных уравнений всегда 1 корень')
    root = -c / b
    print(f'x = {root}')
    return
  if d > 0:
    print('D > 0, будет 2 корня')
    roots = [
      (-b + sqrt(d)) / (2 * a),
      (-b - sqrt(d)) / (2 * a)
    ]
    print(' или '.join(f'x = {root}' for root in roots))
    return
  elif d == 0:
    print('D = 0, будет 1 корень')
    root = (-b) / (2 * a)
    print(f'x = {root}')
    return
  else:
    print('D < 0, корней нет')
    return

solve_square_equation()
