Step 2.2:
1) What is the “size” of this relationship? In your own words, what does this mean? Does this match what you observed in your plots in step 2.1?
	The R-squared (a measure of the "size" of the relationship) is 0.228 (or 0.226 adjusted). This means that 22.8% of the variance in the number of maternally inherited DNMs can be explained by the variance in maternal age. This does make sense with my plots, as there was a discernible though relatively weak linear relationship between the variables, with a higher maternal age generally corresponding to a higher number/likelihood of matnerally inherited DNMs.
2)  this relationship significant? How do you know?
	Yes, this relationship is significant: the F-statistic according to the OLS Regression results for this relationship is 116.0, and the F-statistic probability is 6.88e-24 (essentially 0). This means that there is essentially a 0% chance that the null hypothesis (that there is no relationship between maternal age and the number of maternally inherited DNMs) is correct. That in turn means that there is a statistically significant relationship between maternal age and the number of maternally inherited DNMs, according to the data.

Step 2.3:
1) What is the “size” of this relationship? In your own words, what does this mean? Does this match what you observed in your plots in step 6?
	The R-squared (a measure of the "size" of the relationship) is 0.619 (or 0.618 adjusted). This means that 61.9% of the variance in the number of paternally inherited DNMs can be explained by the variance in paternal age. This does make sense with my plots, as there appeared to be a relatively robust linear relationship between the variables, with a higher paternal age very often corresponding to a higher number/likelihood of patnerally inherited DNMs.
2) Is this relationship significant? How do you know?
	Yes, the relationship is significant: the F-statistic according to the OLS Regression results for this relationship is 639.6, and F-statistic probability is 1.55e-84 (essentially 0). As in the case above with the relationship between maternal age and maternally inherited DNMs, this means that there is essentially a 0% chance that the null hypothesis (that there is no relationship between paternal age and the number of paternally inherited DNMs) is correct. That in turn means that there is a statistically significant relationship between paternal age and the number of paternally inherited DNMs, according to the data.

Step 2.4:
1) Predicted # of paternal DNMs: 78.695457
2) How I got this answer:
	I created a new pandas dataframe called "new", which included the key "Father_age" and the value 50.5. I then defined the OLS regression model I was using to analyse the "paternal_dnm" data based on "Father_age", and subsequently used the "predict" function to predict the new "paternal_dnm" value based on the "Father_age" value provided in "new" based on this regression model. This resulted in a predicted value of about 79 DNMs from a father that is 50.5 years old.

Step 2.6:
1) What statistical test did you choose? Why?
	I chose to use the scipy.stats.ttest_ind because this is used to compare the means of two independent samples, where the null hypothesis is that the samples have an identical average (i.e., there is no difference bewteen the average number of maternal vs pateral DMS per proband). By disproving the null hypothesis, this would suggest that there is a statistically significant difference between the number of maternally vs paternally inherited DNMs per proband.
2) Was your test result statistically significant? Interpret your result as it relates to the number of paternally and maternally inherited DNMs.
	Yes, my test was statistically significant (statistic = -53.403565, pvalue = 2.1986e-264, df = 790.0). Such a small pvalue indicates that there is a negligible likelihood that my samples would have such different average numbers of maternally vs paternally derived DNMs if the true mean of each were equal.