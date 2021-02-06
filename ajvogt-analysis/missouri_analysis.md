# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/06/2021  
Source: [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)  
Source Code: `/ajvogt-analysis/mo_analysis_script.py`  
[Release Notes found below](#release-notes)

This analysis shows the Johns Hopkins University COVID-19 data broken down by 
[Metropolitan Statistcal Area](https://en.wikipedia.org/wiki/Metropolitan_statistical_area) (MSA)
 combinations within the state of Missouri. The list of counties in each MSA comibination can be found in the 
[table](#msa-counties) 
below. The [detailed map of MSAs](https://www2.census.gov/geo/maps/metroarea/us_wall/Sep2018/CBSA_WallMap_Sep2018.pdf) 
can be found here.  The clusters used in the charts and tables below 
are a custom combination of MSAs and 
[Combined Statistical Areas](https://en.wikipedia.org/wiki/Combined_statistical_area) (CSA). 
County populations are pulled from this 
[JHU CSSE repository file](https://github.com/ajvogt/COVID-19/blob/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv).

## Missouri New Daily Confirmed Cases by Metropolitan Statistcal Areas
![](images/mo_daily_cases.png)

## Missouri New Daily Deaths by Metropolitan Statistcal Areas
![](images/mo_daily_deaths.png)

## Missouri Cumulative Deaths by Metropolitan Statistcal Areas
![](images/mo_cumulative_deaths.png)

## Missouri Metropolitan Statistical Area Totals
<!-- msa_table start -->
| MSA | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|
| St. Louis-Farmington | 4133 | 246531 | 740 | 853 | 1189 |
| Kansas City | 2208 | 168363 | 492 | 640 | 868 |
| Missouri non-MSA | 1817 | 107430 | 231 | 260 | 394 |
| Springfield | 553 | 35146 | 81 | 100 | 148 |
| Columbia-Jefferson City | 277 | 33690 | 79 | 80 | 107 |
| Joplin | 270 | 15821 | 49 | 51 | 61 |
| Cape Girardeau-Sikeston | 207 | 12489 | 24 | 26 | 36 |
| St. Joseph | 185 | 9914 | 20 | 23 | 33 |
<!-- msa_table end -->

## STL-Farmington MSA New Daily Confirmed Cases by County
![](images/stl_daily_cases.png)

## STL-Farmington MSA New Daily Deaths by County
![](images/stl_daily_deaths.png)

## STL-Farmington MSA Cumulative Deaths by County
![](images/stl_cumulative_deaths.png)

<a name="msa-counties"></a>
## Metropolitan Statistical Area (MSA) Counties
<!-- county_table start -->
| MSA | State | County | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|---|---|
| St. Louis-Farmington | Missouri | St. Louis | 1770 | 84861 | 252 | 326 | 432 |
| Kansas City | Kansas | Johnson | 682 | 50922 | 183 | 216 | 318 |
| St. Louis-Farmington | Illinois | Madison | 437 | 26666 | 101 | 117 | 153 |
| Kansas City | Missouri | Jackson | 324 | 28884 | 89 | 122 | 148 |
| St. Louis-Farmington | Illinois | St. Clair | 435 | 24145 | 88 | 97 | 137 |
| St. Louis-Farmington | Missouri | St. Charles | 376 | 31847 | 69 | 73 | 121 |
| Kansas City | Missouri | Kansas City | 458 | 35921 | 68 | 120 | 151 |
| St. Louis-Farmington | Missouri | St. Louis City | 363 | 20594 | 63 | 53 | 76 |
| Springfield | Missouri | Greene | 388 | 22630 | 54 | 65 | 95 |
| St. Louis-Farmington | Missouri | Jefferson | 182 | 18486 | 54 | 58 | 86 |
| Kansas City | Kansas | Wyandotte | 245 | 18414 | 42 | 47 | 70 |
| Joplin | Missouri | Jasper | 208 | 11846 | 42 | 41 | 48 |
| Columbia-Jefferson City | Missouri | Boone | 69 | 15509 | 38 | 42 | 56 |
| Kansas City | Kansas | Leavenworth | 66 | 6378 | 27 | 29 | 36 |
| St. Louis-Farmington | Missouri | Franklin | 138 | 8146 | 21 | 25 | 40 |
| Kansas City | Missouri | Clay | 131 | 7605 | 21 | 27 | 35 |
| St. Louis-Farmington | Illinois | Clinton | 85 | 5428 | 19 | 20 | 25 |
| Kansas City | Missouri | Cass | 72 | 6965 | 18 | 29 | 38 |
| Springfield | Missouri | Christian | 71 | 6680 | 17 | 20 | 30 |
| Columbia-Jefferson City | Missouri | Cole | 107 | 8434 | 15 | 16 | 20 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 116 | 7322 | 15 | 17 | 22 |
| Columbia-Jefferson City | Missouri | Callaway | 37 | 4350 | 14 | 12 | 14 |
| St. Louis-Farmington | Illinois | Monroe | 75 | 3892 | 14 | 17 | 20 |
| St. Louis-Farmington | Missouri | St. Francois | 92 | 7432 | 14 | 14 | 22 |
| St. Joseph | Missouri | Buchanan | 126 | 6833 | 13 | 14 | 21 |
| Kansas City | Missouri | Platte | 37 | 2980 | 12 | 11 | 14 |
| St. Louis-Farmington | Illinois | Macoupin | 73 | 4194 | 11 | 15 | 26 |
| St. Louis-Farmington | Missouri | Lincoln | 27 | 4137 | 11 | 12 | 15 |
| Missouri non-MSA | Missouri | Taney | 73 | 4465 | 10 | 12 | 18 |
| Missouri non-MSA | Missouri | Pettis | 71 | 4674 | 9 | 10 | 16 |
| Missouri non-MSA | Missouri | Laclede | 64 | 2884 | 9 | 8 | 9 |
| Missouri non-MSA | Missouri | Butler | 27 | 3280 | 9 | 9 | 12 |
| Kansas City | Missouri | Lafayette | 48 | 2456 | 9 | 8 | 10 |
| Missouri non-MSA | Missouri | Johnson | 38 | 3721 | 9 | 9 | 13 |
| Missouri non-MSA | Missouri | Camden | 75 | 3661 | 8 | 8 | 13 |
| Joplin | Missouri | Newton | 62 | 3975 | 7 | 9 | 12 |
| St. Louis-Farmington | Illinois | Jersey | 44 | 2397 | 7 | 8 | 11 |
| Missouri non-MSA | Missouri | Stone | 33 | 1964 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Saline | 33 | 2373 | 6 | 6 | 9 |
| St. Louis-Farmington | Missouri | Warren | 13 | 2021 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Lawrence | 65 | 2679 | 5 | 6 | 8 |
| Missouri non-MSA | Missouri | Barry | 43 | 2134 | 5 | 5 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2264 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Phelps | 115 | 2915 | 5 | 6 | 10 |
| Missouri non-MSA | Missouri | Ripley | 11 | 818 | 5 | 4 | 4 |
| Kansas City | Kansas | Miami | 30 | 2517 | 5 | 9 | 17 |
| Cape Girardeau-Sikeston | Missouri | Scott | 71 | 3699 | 4 | 6 | 9 |
| Springfield | Missouri | Webster | 46 | 2948 | 4 | 7 | 13 |
| Kansas City | Missouri | Ray | 20 | 1433 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Livingston | 32 | 1294 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Adair | 11 | 2011 | 4 | 6 | 10 |
| Missouri non-MSA | Missouri | Pulaski | 37 | 2935 | 4 | 4 | 11 |
| Missouri non-MSA | Missouri | Henry | 30 | 1678 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Crawford | 28 | 2009 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Audrain | 51 | 2041 | 4 | 5 | 6 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1665 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Carroll | 21 | 811 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2369 | 3 | 5 | 7 |
| Missouri non-MSA | Missouri | Marion | 39 | 2605 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Benton | 23 | 1409 | 3 | 3 | 5 |
| Kansas City | Missouri | Bates | 19 | 1053 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Wright | 26 | 1345 | 3 | 4 | 6 |
| Kansas City | Missouri | Clinton | 60 | 1489 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Howell | 42 | 2753 | 3 | 5 | 11 |
| Columbia-Jefferson City | Missouri | Osage | 12 | 1373 | 3 | 3 | 4 |
| Springfield | Missouri | Polk | 26 | 2089 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Nodaway | 23 | 2525 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Texas | 21 | 1519 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Harrison | 14 | 813 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Pike | 21 | 1466 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Barton | 10 | 933 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 13 | 1585 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Macon | 12 | 1179 | 3 | 5 | 7 |
| Missouri non-MSA | Missouri | McDonald | 25 | 1884 | 2 | 3 | 6 |
| Missouri non-MSA | Missouri | New Madrid | 43 | 1759 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Washington | 42 | 2085 | 2 | 4 | 8 |
| Missouri non-MSA | Missouri | Grundy | 32 | 811 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Vernon | 33 | 1346 | 2 | 3 | 6 |
| Missouri non-MSA | Missouri | Perry | 22 | 2010 | 2 | 2 | 3 |
| St. Joseph | Kansas | Doniphan | 16 | 913 | 2 | 4 | 5 |
| St. Joseph | Missouri | Andrew | 17 | 1262 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Ozark | 11 | 536 | 2 | 2 | 4 |
| St. Louis-Farmington | Illinois | Bond | 21 | 1824 | 2 | 3 | 7 |
| Missouri non-MSA | Missouri | Daviess | 11 | 578 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Shannon | 10 | 473 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 22 | 1233 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Miller | 48 | 2293 | 2 | 3 | 6 |
| Missouri non-MSA | Missouri | Cedar | 10 | 654 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 569 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Clark | 6 | 453 | 2 | 1 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1042 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 25 | 1395 | 2 | 2 | 3 |
| St. Joseph | Missouri | DeKalb | 26 | 906 | 2 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 426 | 2 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1663 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Dent | 14 | 809 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Morgan | 36 | 1603 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Randolph | 27 | 1796 | 1 | 1 | 5 |
| Missouri non-MSA | Missouri | Douglas | 23 | 754 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Madison | 15 | 1339 | 1 | 2 | 3 |
| Springfield | Missouri | Dallas | 22 | 799 | 1 | 2 | 2 |
| Kansas City | Kansas | Linn | 6 | 721 | 1 | 3 | 4 |
| Missouri non-MSA | Missouri | Linn | 10 | 532 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 33 | 851 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Gentry | 19 | 724 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Wayne | 9 | 793 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Maries | 7 | 526 | 1 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 461 | 1 | 0 | 2 |
| Kansas City | Missouri | Caldwell | 10 | 625 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ralls | 12 | 742 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Chariton | 3 | 408 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Holt | 10 | 362 | 0 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 696 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Mercer | 2 | 166 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 13 | 415 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Lewis | 3 | 623 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 175 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 6 | 349 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Oregon | 3 | 662 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Carter | 8 | 412 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 240 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 263 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 742 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Monroe | 8 | 582 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 258 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 219 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 11 | 461 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 137 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 550 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 3 | 456 | 0 | 0 | 1 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
* 1/17/2021: including cumulative deaths plots
* 1/4/2021: small fix for including 2021 data
* 7/20/2020:
  * update table insertion code
  * fix cases vs. deaths total header bug
  * include MSA totals table
  * added STL-Farmington County-level Deaths & Cases plots
  * including release notes in missouri_analysis.md
* 7/19/2020: 
  * code refactor
  * updating color scheme for plots
  * updating county numbers to table to include
  latest new daily case average numbers and
  sorting by last 7-day average
* 6/19/2020: Added description of MSAs & CSAs
* 6/16/2020: Including individual county totals (only) in analysis md table
* 6/11/2020:
  * Updated MSA definitions
  * Including table of individual county case counts
* 6/7/2020: Creating markdown & script
  * Including list of county-MSA/CSA associations to markdown
  * Including cumulative totals in MSA/CSA plots
* 5/30/2020: including plots of cumulative cases/deaths in jupyter notebook
* 5/17/2020: Initial analysis jupyter notebook created
* 4/4/2020: Cloned JHU CSSE Repository and set up development environment

### To-Do (updated 1/17/2021)
- [ ] Verify county population data

#### Analysis Page
- [x] Update description to accurately reflect CSA vs. MSA
- [x] Make table for CSA info
- [x] Include 7, 14, & 30 day changes for each county
- [ ] Plot top CSAs (for latest daily case change) with testing data
- [x] Analysis breakdown of St. Louis-Farmington counties
- [x] Include release notes and to-do list
- [ ] ~~Update color scheme~~, plot markers, and line thickness
- [ ] Include table of contents

#### Analysis Script
- [x] Simplify data ingestion and summarization functionality
- [x] Simplify plotting functionality
- [x] Include ability to update markdown with table between markdown sections
