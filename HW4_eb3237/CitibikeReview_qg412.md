# Assignment 1 of Homework 5

Hi Evgeniya! Here's my review :) Don't think we have met before, hope to say hi to you in person next time! 

# Summary of tasks for this assignment: 

1) Verify if null and alternative hypothesis are formulated correctly
2) Verify that the data supports the project
3) Choose an appropriate statistical test to test H0 given the type of data, and the question asked.

Write your comments, suggestions, and suggested an appropriate statistical test, motivating your test choice, in a markdown named CitibikeReview_<netID>.md. Suggest variations on the question, if you think it may be made more interesting.
Submit a pull request to the original repository to share your markdown.

# qg412's review:
### 1) On the formulation of the Null (H_0) and Alternative Hypothesis (H_A)

The given H_0: _The average trip time of men biking on weekdays is the same or lower than the average trip time of women biking on weekdays_

The given H_A: _The average trip time of men biking on weekdays is more than the average trip time of women biking on weekdays_

**Comments**: This is an interesting hypothesis- as a woman myself, I think there might be more factors inhibiting my willingness and ultimately, frequency and duration of cycling. For example, I don't want to cycle when I am wearing dress or skirt out of fear of my "modesty", something which men are not subjected to. It would be thus be interesting to see whether the analysis showed that men tend to cycle longer than women. 

**Suggestions for improvements**:   

- I think your null and alternative hypothesis has met the requirements of being mathematicaly testable and time specified. One thing that you might want to consider is specifying the geographical constraint, and modifying it to:

H_0: The average trip time of men biking on weekdays in _New York City_ is the same or lower than the average trip time of women biking on weekdays in _New York City_. 

H_A: The average trip time of men biking on weekdays in _New York City_ is more than the average trip time of women biking on weekdays in _New York City_.

- It would be nice to state the null and alternative hypothesis in mathematical sense, for example:

H_0: M - W <= 0

H_A: M - W >= 0

Where M is the average trip time of men biking on weekdays in NYC

While W is the average trip time of women biking on weekdays in NYC

- I think you can determine and state the significance level together with the hypothesis statements, for example "at a significance level of p=0.05". Rationale: Prof Bianco mentioned in lecture that it is very important to set the significance level at the outset, if not we risk being accused of setting the p-value at the end of analysis which is statistically (& morally) wrong. 

### 2) Verifying if data supports project

From the plots generated (1: Bar graph of average trip duration & Average trip duration for each gender, 2 & 3: Line graphs of average trip duration across the weekday for each gender respective), it seems that longer trip duration are taken by women instead of men, which is supporting the null hypothesis and not supporting the alterntive hypothesis. 

### 3) Chosing an appropriate statistical test

Decision tree resulting in the choice of statistical test (credits @ https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3116565/): 

What data type is the datasets? > Numerical due to trip duration > Does it follow normal distribution? > Yes, the average trip duration is likely to observe a bell shape normal distribution> Use Parametric Tests, but is the two samples paired or unpaired? > Unpaired, because there is an unlikely possibility of the values in the males cycling dataset being related to or being influenced by the values in the females cycling dataset > Therefore, choose **T-test** for 2 groups of unpaired sample. 

### 4) Additional suggestion on variation on question

I think one interesting question that we can ask further is: do men cycle a longer average trip duration than women from the same starting location? This will involve pairing the dataset and narrowing down the study area to selected locations. This can perhaps shed some light on travel patterns of different genders. For eg if we find that women travel shorter on bicycle- one of the many potential reason could be because of the fact that they tend to find jobs near homes so that they can reach home to care for their children? 
