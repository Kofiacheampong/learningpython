coin_denominations = [5,10, 25]
amount_due = 50
while amount_due > 0:
  print(f'Amount Due : {amount_due}')
  coin =  int(input('Insert Coin: '))
  
  while coin not in coin_denominations:
      coin =  int(input('Invalid coin, Insert Coin: '))
  
  amount_due -= coin







