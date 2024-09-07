# Statistic studies around brawl stars tier_lists
This repository uses the power of python's matplotlib library to make some calculations around the tier_list.json data:

## meta_points
I defined "meta_points" as the sum of the stars ot per brawler in every tier list. For exmaple, if there were two tier lists, and a brawler (i.e. Colt) got 2 stars in one and 3 in another, Colt's meta points will be 2 + 3 = 5.

## meta_percentage
The "meta_percentage" parameter is the percentage of stars got by a brawler, in reference to the maximum number of stars it could get.
For example:
If colt got 2 stars in one tier list and 3 in another, its meta_points will be 5.
He took place in 2 tier lists, and having in mind that the max number of stars in a single tier list is 5, the maximum number of stars that Colt could have got is 5 * 2 = 10 stars.
Then, a rule of three is made.

Having 10 stars would be a 100%, so having 5 stars is a $(5*100)/10$ %, so a 50%

## stars_mean
This parameter refers to the mean of stars got by a brawler in every tier_list.
It is calculated, as every mean, with this formula and knowing that meta_points = m, and the number of tier lists in which the brawler was involved = T,
$$\frac{m}{T}$$

## standard_deviation
This last parameter refers to the standard deviation related to a brawler's stars mean.
Having in mind that stars_mean = m, tier lists in which the brawler was involved = T, and the list with all the points he got in every tier list = s,
It is calculated using this formula:
$$\sqrt{\frac{\sum_{1}^{T}(s_i - m)^2}{T}}$$

All this data has been represented in horizontal bar graphs using the python's matplotlib module and stored in an image at the same directory that the .py file.
