import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import re
from sets import Set


def merge_by_year(countries, income, year):
	#Construct a empty dataframe with index of countries
	df = pd.DataFrame(index=countries.reset_index().index, columns=["Country", "Region", "Income"])

	#Set the column of Country, Region and Income with the given year
	df["Country"] = countries.index
	df["Region"] = countries["Region"].values
	df["Income"] = income[year][df["Country"]].values

	#Remove Nan
	df["Income"].replace(np.nan, 0, inplace=True)

	return df

def display_distribution(countries, income, year):

	#Initialization
	df = income[year]
	df.replace(np.nan, 0, inplace=True)

	#Set the figure size
	fig = plt.figure()
	fig.set_size_inches(75,30)

	#Arrange the plots
	ax0 = plt.subplot2grid((2, 10), (1, 0), colspan=10)
	ax1 = plt.subplot2grid((2, 10), (0, 0), colspan=3)

	#Plot for the income of all countries
	ax0.bar(np.arange(len(df)), df)
	ax0.set_title("Income per Person of all Countries ("+year+")")
	ax0.set_xticks(np.arange(len(df)))
        ax0.set_xticklabels(df.index,  rotation=80)
        ax0.set_xlim([-1, len(df)+1])
	ax0.set_ylabel("Income per Person")

	#Plot for the income distribution
	ax1.hist(df, 50, color="g")
	ax1.set_title("Income Distribution ("+year+")")
	ax1.set_xlim([np.min(df), np.max(df)])
	ax1.set_xlabel("Income per Person")
	ax1.set_ylabel("Number of Countries")

	plt.savefig("part3_"+year)
	plt.close()


def  exploratory_data_analysis(countries, income, year):

	#merge two datasets
	df = merge_by_year(countries, income, year)

	#Retrieve all the regions
	regions = list(Set(df["Region"].values))

	#Histogram
	fig, axarr = plt.subplots(2,3, figsize=(30,10))
	for i in range(2):
		for j in range(3):
			axarr[i, j].hist(df[df["Region"]==regions[i*3+j]]["Income"], 25)
			axarr[i, j].set_title(regions[i*3+j]+" ("+year+")")
			axarr[i, j].set_xlim([np.min(df["Income"]), np.max(df["Income"])])
			axarr[i, j].set_xlabel("Income per Person")
			axarr[i, j].set_ylabel("Number of Countries")

	plt.savefig("part5_hist_"+year)
	plt.close()


	#Boxplot
	fig, ax = plt.subplots(figsize=(20, 10))
	reg_data = [df[df["Region"]==r]["Income"] for r in regions]

	ax.boxplot(reg_data)
	ax.set_title("Boxplot (" + year + ")")
	ax.set_xticklabels(regions)
	ax.set_ylabel("Income per Person")

	plt.savefig("part5_box_"+year)
	plt.close()


def is_digit(input):
	#Return True only if the input is a positive int
	if re.match(r"^\d+$", input) == None:
		return False
	return True


def user_input():

	while True:
		y = raw_input("Please specify a year within 1800~2012 ")
		#Filter out the invalid inputs and out-of-range numbers
		if not is_digit(y):
			print "Invalid Input"
			continue
		elif int(y) < 1800 or int(y) > 2012:
			print "Out of Range"
			continue
		break

	return y


if __name__ == "__main__":

	print "========== Part 1 =========="
	#Read the datasets from each csv
	countries = pd.DataFrame.from_csv("../countries.csv")
	income = pd.DataFrame.from_csv("../indicator_gapminder_gdp_per_capita_ppp.csv")
	print "...Data loaded\n"


	print "========== Part 2 =========="
	df = income.T
        #Write results
        fp = open("part2.txt", "w")
        fp.write(df.head().to_string())
        fp.close()
	print "...Results saved as part2.txt\n"


	print "========== Part 3 =========="
	#Get the year specified by the user
	year = user_input()
	#Show the income distribution across all countries with plots
	display_distribution(countries, income, year)
	print "...Figures saved as part3_%s.png\n" % year
	

	print "========== Part 4 =========="
	#Merge two dataset with the given year
	df = merge_by_year(countries, income, year)
        #Write results
        fp = open("part4_"+year+".txt", "w")
        fp.write(df.to_string())
        fp.close()
	print "...Results saved as part4_%s.txt\n" % year


	print "========== Part 5 =========="
	#Show data analysis of income across regions
	exploratory_data_analysis(countries, income, year)
	print "...Figures saved as part5_hist_%s.png and part5_box_%s.png\n" % (year, year)

