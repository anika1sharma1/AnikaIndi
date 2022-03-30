def driver():
  InfoDb = []
  # List with dictionary records placed in a list
  InfoDb.append({
                 "song": "Hello",
                 "artist": "Adele",
                 "beat":["three count", "four count", "five count", "six count"]
                })
  InfoDb.append({
                 "song": "Hit me baby one more time",
                 "artist": "Britney Spears",
                 "beat":["three count", "four count", "five count", "six count"]
                })
  a = input("Type key: " )
  b = input("Type value: " )
  def for_loop(key, value):
    for data in InfoDb:
      if(data[key]) == value:
        print(data[key])
        return
  for_loop(a,b)
  def while_loop(key, value):
    i = 0
    while i < len(InfoDb):
      if (InfoDb[i][key] == value):
        print(InfoDb[i][key])
        return
      i +=1
  while_loop(a,b)
  def recur_loop(i, key, value):
    if (i < len(InfoDb)):
      if (InfoDb[i][key] == value):
        print(InfoDb[i][key])
        return
      i += 1
      recur_loop(i, key, value)
    return
  recur_loop(0,a,b)

if __name__ == "__main__":
    driver()