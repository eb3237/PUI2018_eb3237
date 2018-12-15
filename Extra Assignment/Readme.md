## Analyzing real estate market and factors influencing "hottness" of specific markets¶

When buyers or real estate professionals consider a market for their investments, they need to know which areas/cities show higher growth, and which markets are “hot”.

This study is two-fold:

- first, I analyze the national markets and price dynamics for five major US cities

- second, I concentrate on NYC, the "hot" and "cold" Zip code areas within the city and see how well can we predict the overall hotness of the NYC market with some real estate and population statistic parameters. As the result, the model is overfitted and cannot be considered as strong.


Data: 
1) I am considering to use a score published by Realtor.com (https://www.realtor.com/research/reports/hottest-markets/) as a ground truth.
2) Dataset from Realtor.com (https://www.realtor.com/research/data/) which contains information about the medium listing price, days on the market, price increase/decrease, etc.
3) Datasets from NYC big apple

I merged relevant datasets, cleaned data and then to work on the features.
I will explore the features and the correlation coefficients of each features.
I used Random forest and OLS regression methods. 

References: 
1)	Dean De Cock. Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project. Journal of Statistics Education, Volume 19, Number 3(2011).  http://jse.amstat.org/v19n3/decock.pdf
2)	Zhu S, Pace RK. Factors underlying short sales. Journal of Housing Economics. 2015;27:60-70. doi:10.1016/j.jhe.2015.02.001.
3)	Chow YL yuenleng@nus. edu. s., Hafalir IE 2. isaemin@cmu. ed., Yavas A ayavas@us. wisc. ed. Auction versus Negotiated Sale: Evidence from Real Estate Sales. Real Estate Economics. 2015;43(2):432-470. doi:10.1111/1540-6229.12056.
4)	Pardoe, I. (2008). “Modeling home prices using realtor data”, Journal of Statistics Education, Volume 16,
Number 2. http://www.amstat.org/publications/jse/v16n2/datasets.pardoe.html

Deliverable: The project delivery will include analysis, statistical conclusion, and possible  algorithm 

