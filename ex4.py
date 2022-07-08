import random

def main():
  cnt_h = 0
  cnt_t = 0
  
  name = raw_input('Who are you?\n')
  print('Hello, {}!'.format(name))

  print('Tossing a coin...')
  for i in range(3):
    number = random.randint(0, 4) % 2
    value = 'Heads' if number == 0 else 'Tails'
    if number == 0: cnt_h += 1
    else: cnt_t += 1
    print('Round {}, {}'.format(i+1, value))

  print('Heads: {}, Tails: {}'.format(cnt_h, cnt_t))

  return



if __name__ == '__main__':
  main()
Footer
© 2022 GitHub, Inc.
