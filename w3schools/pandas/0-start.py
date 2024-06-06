import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

#print(myvar)
a = [97, 11, 21]
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pandas.Series(calories)

print(pandas.options.display.max_rows) #prints maximum rows
