import sys
from function import *

def main():
	try:
		Q3 = raw_input('Display the distribution of income per person across all countries in the world for any given year?\ny/n?\n')
		if Q3=='y':
			try:
				year=int(raw_input('Enter the year, from 1800 to 2012? '))
				print 'Saving All_Country_in_{}.png'.format(year)
				display(year)
			except:
				print 'Invalid year. Please check.'
		else:
			print 'Next question.'
			
		Q4_1 = raw_input('See boxplots to explore the distribution of the income per person by region in given year?\ny/n?\n')
		if Q4_1=='y':
			try:
				year=int(raw_input('Enter the year, from 1800 to 2012? '))
				print 'Saving boxplot_region_in_{}.png'.format(year)
				display_by_region(year)
			except:
				print 'Invalid year. Please check.'
		else:
			print 'Next question.'
			
		Q4_2 = raw_input('See changes in recent years?\ny/n?\n')
		if Q4_2=='y':
			try:
				start_year = int(raw_input('Enter the start year, from 1800 to 2012? '))
				end_year = int(raw_input('Enter the end year, from 1800 to 2012? '))
				print 'Saving change_from_{}_to_{}.png'.format(start_year,end_year)
				display_change(start_year,end_year)
			except:
				print 'Invalid year. Please check.'
		else:
			print 'Work done.'
			
	except(KeyboardInterrupt):
		print 'Exit'
		sys.exit()
	
if __name__=='__main__':
		main()