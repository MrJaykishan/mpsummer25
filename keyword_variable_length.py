#keyword variable length argumnent

def persondata(**data):
    print(data)
    for i in data.items():
        print(i)


persondata(name='ashwani',phone='9956477677',age=55,city='gkp',quali='btech',price=55.66)