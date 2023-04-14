import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 6, 5, 3]
namelist = ['Freshmen', 'Sophomores', 'Juniors', 'Seniors']
colorlist = ['blue', 'green', 'red', 'cyan' ]
explodelist = [0.5, 0.0, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.2f%%', colors=colorlist,
    	explode = explodelist, startangle = 90)
plot.axis('equal')
plot.savefig('Piechart.png')
