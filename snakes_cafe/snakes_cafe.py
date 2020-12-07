print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**                                  **')
print('** To quit at any time, type "quit" **')
print('**************************************\n')
print('Appetizers')
print('----------')
print('Wings')
print('Cookies')
print('Spring Rolls\n')
print('Entrees')
print('-------')
print('Salmon')
print('Steak')
print('Meat Tornado')
print('A Literal Garden\n')
print('Desserts')
print('--------')
print('Ice Cream')
print('Cake')
print('Pie\n')
print('Drinks')
print('------')
print('Coffee')
print('Tea')
print('Unicorn Tears\n')
print('***********************************')
print('** What would you like to order? **')
print('***********************************')

# Dictonary

Orders = {
  'Wings': 0,
  'Cookies': 0,
  'Spring Rolls': 0,
  'Salmon': 0,
  'Steak': 0,
  'Meat Tornado': 0,
  'A Litheral Garden': 0,
  'Ice Cream': 0,
  'Cake': 0,
  'Pie': 0,
  'Coffee': 0,
  'Tea': 0,
  'Unicorn Tears': 0
}
while True:
    user_input = input('> ')
    if user_input == "quit":
      break
    print(user_input)   

    for key in Orders:
      if user_input == key:
        Orders[key] += 1
        print(Orders[key])
        print('** ' + str(Orders[key]) + ' Orders of ' + user_input + " have been added to your meal **")






























