def newGame():
  guesses=[]
  correct_guesses = 0
  question_num = 1

  for key in questions:
    print ('--------------')
    print (key)
    for i in options[question_num-1]:
      print(i)
    guess = input('Enter (A B C OR D): ')
    guess = guess.upper()
    guesses.append(guess)

    correct_guesses += checkAnswer(questions.get(key),guess)
    question_num+=1

  displayScore(correct_guesses,guesses)

def checkAnswer(answer,guess):
  if answer == guess:
    print('correct')
    return 1
  else:
    print('Wrong')
    return 0
  
def displayScore(correct_guesses,guesses):
  print('------------')
  print('Results')
  print('------------') 
  print('Answers: ', end ='')
  for i in questions:
    print (questions.get(i),end =' ')
  print()
 
  print('Guesses: ', end = '')
  for i in guesses: 
    print (i, end=' ')
  print()

  score = correct_guesses/len(questions)*100
  print ('Your score is: ' , score, '%')
  

  
def playAgain():
  response = input('Do you want to play again?(yes or no): ')
  response = response.upper()

  if response == 'YES':
    return True
  else: 
    return False


questions ={
  'Who won the champions league last year?':'A',
  'What team is know as the Red Devils':'C',
  'What national team has the most World Cups?': 'D',
  'Who is the Prem all time leading scorer': 'B'
}

options= [['A. ManCity','B. Chelsea', 'C. Benfica', 'D. Real Madrid'],
          ['A. ManCity','B. Chelsea', 'C. ManUnited', 'D. Liverpool'],
          ['A. Palestine  ','B. Israel', 'C. Ghana', 'D. Brazil'],
          ['A. Andy_Cole','B. Shearer', 'C. Ruud', 'D. Henry']] 

newGame()

while playAgain() is True:
  newGame()

print('Ciaooo')