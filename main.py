"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
  if n <= 1:
    return n
  else:
    return a * simple_work_calc(n//b, a, b) + n


def test_simple_work():
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(8, 2, 2) == 32
  assert simple_work_calc(8, 3, 2) == 65

def work_calc(n, a, b, f):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return a * work_calc(n//2, a, b, f) + f(n)
  """Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

  Params:
  n......input integer
  a......branching factor of recursion tree
  b......input split factor
  f......a function that takes an integer and returns 
           the work done at each node 

  Returns: the value of W(n).
  """

def span_calc(n, a, b, f):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return span_calc(n//2, a, b, f) + f(n)
  """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

  Params:
  n......input integer
  a......branching factor of recursion tree
  b......input split factor
  f......a function that takes an integer and returns 
           the work done at each node 

  Returns: the value of W(n).
  """

def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(8, 2, 2,lambda n: n) == 32 
  assert work_calc(8, 1, 2, lambda n: n*n) == 85
  assert work_calc(8, 3, 2, lambda n: 1) == 40

def test_span():
  assert span_calc(10, 2, 2, lambda n: 1) == 4
  assert span_calc(20, 1, 2, lambda n: n*n) == 530
  assert span_calc(30, 3, 2, lambda n: n) == 56
  assert span_calc(10, 2, 2, lambda n: n) == 18
  assert span_calc(10, 2, 2, lambda n: n*n) == 130

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  
  result = []
  for n in sizes:
    work_fn1 = lambda n: work_calc(n, 4, 2, lambda n: n)
    work_fn2 = lambda n: work_calc(n, 4, 2, lambda n: n*n)
    result.append((
      n,
      work_fn1(n),
      work_fn2(n)
      ))
  print_results(result)

def compare_span(span_fn1, span_fn2, sizes = [10, 20, 50, 100, 1000, 5000, 10000]):
  result = []
  for n in sizes:
    span_fn1 = lambda n: span_calc(n, 4, 2, lambda n: n)
    span_fn2 = lambda n: span_calc(n, 4, 2, lambda n: n*n)
    result.append((
      n,
      span_fn1(n),
      span_fn2(n)
    ))
  print_results(result)

def print_results(results):
	print(tabulate.tabulate(results,
							headers=['n', 'F_1', 'F_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
  work_fn1 = lambda n: work_calc(n, 4, 2, lambda n: n)
  work_fn2 = lambda n: work_calc(n, 4, 2, lambda n: n*n)

  res = compare_work(work_fn1, work_fn2)
  print(res)

def test_compare_span():
  span_fn1 = lambda n: work_calc(n, 4, 2, lambda n: n)
  span_fn2 = lambda n: work_calc(n, 4, 2, lambda n: n*n)

  res = compare_work(span_fn1, span_fn2)
  print(res)