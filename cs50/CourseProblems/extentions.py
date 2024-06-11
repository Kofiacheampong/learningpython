def main():
  file = input('File Name?: ')

  if file.lower().endswith(".gif"):
      print('image/gif')
  elif file.lower().endswith(".jpg"):
      print('image/jpg')
  elif file.lower().endswith(".jpeg"):
      print('image/jpeg')
  elif file.lower().endswith(".png"):
      print('image/png')     
  elif file.lower().endswith(".pdf"):
      print('doc/pdf') 
  elif file.lower().endswith(".txt"):
      print('doc/txt')
  else:
      print('application/octet-stream')

main()