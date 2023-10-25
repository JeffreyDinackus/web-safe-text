input_string = 'cats@catmanager.com ex@mple-string "inquotes"'

dict = {
  '{' : "&#123;",
  '}' : "&#125;",
  '@' : "&#64;",
  '&' : "&#amp;",
  '(' : "&#40;",
  '#' : "&#35;",
  ')' : "&#41;",
  '[' : "&#91;",
  ']' : "&#93;",
  "^" : "&#94;",
  "*" : "&ast;",
  "\"" : "&quot;",
  '%' : "&#37;",
  '$' : "&#36;"
  # add any more
}

answer = ""


for i in input_string:
  if i in dict:
    answer+= dict[i]
  else:
    answer+=i


f = open("file.txt", "w")

f.write(answer)