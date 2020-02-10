import request as r
import login as l

tag = l.run()
print(tag)
test = r.getAll("pc", "eu", tag)

print(test)