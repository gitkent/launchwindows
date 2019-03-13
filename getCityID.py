def getCityID(c):
    switcher = {
        'Melbourne':Mel(),
        'Darwin':Dar(),
        'Hobart':Hob(),
        'Perth':Per()
    }
    return switcher.get(c,All())

def Mel():
  return '7839805'

def Dar():
  return '2073124'

def Hob():
  return '2163355'

def Per():
  return '2063523'

def All():
    return '7839805,2073124,2163355,2063523'.split(',')