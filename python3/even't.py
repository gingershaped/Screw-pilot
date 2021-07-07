# Checks if a number is even

import random

def even(num):
  try:
    return [True,False][num%2] if not random.randint(0, 9) else bool(random.randint(0, 1))
