immutable_var = (0, 1, "Word", [6, 7, 8])
print(immutable_var)
# immutable_var[1] = 2 # не работает, так как идет обращение к неизменяемому кортежу
mutable_list = ["Alex", "Peter", "Sergey"]
mutable_list[2] = "Ivan"
print (mutable_list)