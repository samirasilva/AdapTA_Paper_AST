import scipy.stats as stats
import sys



def compute(sample1,sample2,scenario):

	# Perform the Mann-Whitney U test
	u_statistic, p_value = stats.mannwhitneyu(sample1, sample2, alternative='two-sided')

	print(scenario)
	# Output the results using .format() method
	print("Mann-Whitney U Statistic: {}, P-value: {}".format(u_statistic, p_value))

	# Interpret the result
	if p_value < 0.05:
	    print("There is a significant difference between the two samples.")
	else:
	    print("There is no significant difference between the two samples.")


def main(argv): 
	# Sample data S1
	scenario="Scenario 1"
	sample1 = [89.46, 84.17, 90.46, 89.75, 89.53]
	sample2 = [73.3, 68.12, 69.35, 59.12, 77.30]
	compute(sample1,sample2,scenario)
	
	# Sample data S2
	scenario="Scenario 2"
	sample1 = [92.22,90.72,89.68,84.33,90.92]
	sample2 = [72.16,82.57,73.36,66.13,68.23]
	compute(sample1,sample2,scenario)

	# Sample data S3
	scenario="Scenario 3"
	sample1 = [86.29,89.77,88.83,86.85,88.50]
	sample2 = [56.76,65.65,61.98,63.78,59.04]
	compute(sample1,sample2,scenario)


	


if __name__ == "__main__":
    main(sys.argv)



