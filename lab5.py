#!/usr/bin/env python3

import simpy
import random
from functools import *
from itertools import count

log = []
result = 0

def uniform(c, d): return round(random.uniform(c - d, c + d), 2)

def customer(env, ops, rand):
  global log
  global result
  bad = 0
  for n in count(1):
    def try_queue(i):
      t = i.current is None or not i.current.is_alive
      if t: i.run(n)
      return t
    if not reduce(lambda s, i: s or try_queue(i), ops, False):
      log.append("Клиент {0} не может попасть в очередь!".format(n))
      bad += 1
    if n % 1000 == 0:
      result = bad / n
      return
    yield env.timeout(rand())

class Operator:
  def __init__(self, env, name, queue, rand):
    self.env = env
    self.current = None
    self.name = name
    self.queue = queue
    self.rand = rand

  def run(self, n):
    self.current = self.env.process(self.process(n))

  def process(self, n):
    global log
    log.append("Клиент {0} разговаривает с оператором {1}".format(n, self.name))
    yield self.env.timeout(self.rand())
    log.append("Оператор {0} кладет заявку клиента {1} в очередь {2}".format(self.name, n, self.queue.name))
    self.queue.queue.put(n)

class Computer:
  def __init__(self, env, name, time):
    self.queue = simpy.Store(env)
    self.name = name
    env.process(self.process(env, time))

  def process(self, env, time):
    global log
    while True:
      n = yield self.queue.get()
      log.append("Комьютер {0} начинает обрабатывать заявку {1}".format(self.name, n))
      yield env.timeout(time)
      log.append("Компьютер {0} обработал заявку {1}".format(self.name, n))

def model():
  global log
  global result
  log = []
  result = 0
  env = simpy.Environment()
  comps = [Computer(env, "1", 15),
           Computer(env, "2", 30),
  ]
  ops = [Operator(env, "1", comps[0], partial(uniform, 20, 5)),
         Operator(env, "2", comps[0], partial(uniform, 40, 10)),
         Operator(env, "3", comps[1], partial(uniform, 40, 20)),
  ]
  env.process(customer(env, ops, partial(uniform, 10, 2)))
  env.run()
  return (result, log)
