s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
s=s.replace(",","").replace(".","").upper()

l=s.split(" ")
lst = list(set(l))
lst.sort()

for wd in lst:
    print(wd)   

for wd in lst:
    print(wd,": ",s.count(wd))

  