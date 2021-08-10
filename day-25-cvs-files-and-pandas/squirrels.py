import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color_list = ['Gray', 'Cinnamon', 'Black']

counter_list = []
for color in color_list:
    counter_list.append(int(data[data['Primary Fur Color'] == color]['Primary Fur Color'].count()))

squirrel_dic = {
    'Fur Color': color_list,
    'Count': counter_list,
}
squirrel_data = pandas.DataFrame(squirrel_dic)
squirrel_data.to_csv('squirrel_count.csv')
