# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 04/10/2021  
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
| St. Louis-Farmington | 4925 | 285524 | 426 | 418 | 863 |
| Kansas City | 2615 | 199809 | 188 | 181 | 732 |
| Missouri non-MSA | 2134 | 135072 | 93 | 92 | 812 |
| Springfield | 650 | 44276 | 28 | 30 | 256 |
| Columbia-Jefferson City | 334 | 38052 | 21 | 18 | 112 |
| Joplin | 305 | 20684 | 11 | 11 | 142 |
| Cape Girardeau-Sikeston | 236 | 15247 | 7 | 6 | 78 |
| St. Joseph | 212 | 13276 | 5 | 5 | 104 |
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
| St. Louis-Farmington | Missouri | St. Louis | 2106 | 94195 | 161 | 150 | 147 |
| St. Louis-Farmington | Missouri | St. Charles | 438 | 41854 | 60 | 66 | 289 |
| Kansas City | Kansas | Johnson | 741 | 56694 | 56 | 55 | 53 |
| St. Louis-Farmington | Missouri | St. Louis City | 458 | 22963 | 46 | 42 | 39 |
| St. Louis-Farmington | Missouri | Jefferson | 234 | 22521 | 45 | 44 | 113 |
| Kansas City | Missouri | Kansas City | 557 | 42946 | 43 | 39 | 201 |
| Kansas City | Missouri | Jackson | 409 | 37550 | 33 | 34 | 240 |
| St. Louis-Farmington | Illinois | St. Clair | 498 | 26895 | 31 | 29 | 34 |
| St. Louis-Farmington | Illinois | Madison | 511 | 29512 | 29 | 34 | 38 |
| Springfield | Missouri | Greene | 451 | 27862 | 17 | 18 | 141 |
| Kansas City | Kansas | Wyandotte | 276 | 19829 | 17 | 16 | 15 |
| Columbia-Jefferson City | Missouri | Boone | 86 | 17678 | 13 | 10 | 55 |
| Kansas City | Missouri | Cass | 99 | 9055 | 13 | 10 | 57 |
| St. Louis-Farmington | Missouri | Franklin | 177 | 10509 | 11 | 13 | 67 |
| St. Louis-Farmington | Missouri | Lincoln | 39 | 5660 | 11 | 11 | 44 |
| Joplin | Missouri | Jasper | 231 | 15404 | 7 | 7 | 103 |
| St. Louis-Farmington | Illinois | Monroe | 90 | 4269 | 7 | 6 | 5 |
| Kansas City | Missouri | Clay | 161 | 9879 | 6 | 6 | 63 |
| Springfield | Missouri | Christian | 88 | 8342 | 5 | 4 | 47 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 131 | 8939 | 5 | 3 | 46 |
| St. Louis-Farmington | Missouri | Warren | 20 | 3066 | 5 | 4 | 31 |
| Missouri non-MSA | Missouri | Crawford | 35 | 2543 | 4 | 6 | 15 |
| Columbia-Jefferson City | Missouri | Cole | 122 | 9079 | 4 | 4 | 15 |
| Missouri non-MSA | Missouri | Butler | 40 | 4178 | 4 | 3 | 20 |
| Missouri non-MSA | Missouri | Dunklin | 20 | 2791 | 4 | 4 | 12 |
| Missouri non-MSA | Missouri | Phelps | 127 | 3768 | 4 | 6 | 23 |
| St. Louis-Farmington | Missouri | St. Francois | 110 | 8814 | 4 | 3 | 39 |
| St. Louis-Farmington | Illinois | Macoupin | 81 | 4534 | 4 | 3 | 4 |
| Joplin | Missouri | Newton | 74 | 5280 | 4 | 3 | 39 |
| Kansas City | Missouri | Platte | 46 | 4097 | 4 | 4 | 31 |
| Missouri non-MSA | Missouri | Randolph | 30 | 2684 | 4 | 2 | 28 |
| Missouri non-MSA | Missouri | Taney | 90 | 5212 | 3 | 2 | 19 |
| Kansas City | Kansas | Leavenworth | 91 | 7096 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Macon | 15 | 1590 | 3 | 3 | 12 |
| Missouri non-MSA | Missouri | Dent | 17 | 944 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Camden | 85 | 4037 | 3 | 2 | 9 |
| St. Louis-Farmington | Illinois | Jersey | 47 | 2589 | 3 | 3 | 2 |
| St. Joseph | Missouri | Buchanan | 141 | 9284 | 3 | 3 | 76 |
| Missouri non-MSA | Missouri | Marion | 43 | 3630 | 3 | 2 | 32 |
| Missouri non-MSA | Missouri | Madison | 16 | 1635 | 2 | 1 | 9 |
| Missouri non-MSA | Missouri | Vernon | 42 | 1981 | 2 | 3 | 19 |
| Missouri non-MSA | Missouri | McDonald | 26 | 2364 | 2 | 2 | 14 |
| Springfield | Missouri | Polk | 32 | 3283 | 2 | 4 | 35 |
| Kansas City | Kansas | Miami | 41 | 2686 | 2 | 1 | 1 |
| Springfield | Missouri | Webster | 53 | 3534 | 2 | 2 | 17 |
| Missouri non-MSA | Missouri | Pettis | 78 | 5084 | 2 | 1 | 8 |
| Kansas City | Missouri | Ray | 27 | 1956 | 2 | 1 | 14 |
| Missouri non-MSA | Missouri | Ripley | 15 | 1072 | 2 | 1 | 7 |
| Missouri non-MSA | Missouri | Nodaway | 25 | 2670 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Johnson | 49 | 4939 | 1 | 2 | 34 |
| Missouri non-MSA | Missouri | Lawrence | 78 | 3420 | 1 | 1 | 21 |
| Missouri non-MSA | Missouri | Stone | 40 | 2386 | 1 | 1 | 11 |
| Cape Girardeau-Sikeston | Missouri | Scott | 83 | 4717 | 1 | 1 | 28 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1950 | 1 | 1 | 1 |
| Kansas City | Missouri | Bates | 27 | 1328 | 1 | 1 | 7 |
| St. Louis-Farmington | Illinois | Clinton | 90 | 5687 | 1 | 1 | 3 |
| Kansas City | Missouri | Lafayette | 56 | 3088 | 1 | 1 | 16 |
| Missouri non-MSA | Missouri | Dade | 15 | 576 | 1 | 1 | 5 |
| St. Joseph | Missouri | Andrew | 18 | 1878 | 1 | 1 | 19 |
| Missouri non-MSA | Missouri | Laclede | 68 | 3265 | 1 | 1 | 10 |
| Missouri non-MSA | Missouri | Saline | 38 | 2896 | 1 | 1 | 15 |
| Missouri non-MSA | Missouri | Howell | 43 | 3506 | 1 | 2 | 22 |
| Missouri non-MSA | Missouri | Miller | 53 | 2522 | 1 | 1 | 6 |
| Kansas City | Kansas | Linn | 8 | 791 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Washington | 49 | 2736 | 1 | 1 | 20 |
| Missouri non-MSA | Missouri | Stoddard | 37 | 2497 | 1 | 1 | 5 |
| Missouri non-MSA | Missouri | Wayne | 11 | 1041 | 1 | 0 | 7 |
| Missouri non-MSA | Missouri | Barry | 45 | 2899 | 1 | 1 | 23 |
| Missouri non-MSA | Missouri | New Madrid | 43 | 2115 | 1 | 1 | 11 |
| Columbia-Jefferson City | Missouri | Callaway | 47 | 4914 | 1 | 1 | 12 |
| Kansas City | Missouri | Clinton | 65 | 2044 | 1 | 0 | 17 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 16 | 1816 | 1 | 1 | 6 |
| Missouri non-MSA | Missouri | Mississippi | 28 | 1447 | 1 | 1 | 5 |
| Missouri non-MSA | Missouri | Pike | 23 | 1800 | 1 | 0 | 10 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 1037 | 1 | 1 | 15 |
| Missouri non-MSA | Missouri | Perry | 29 | 2174 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Ralls | 12 | 1059 | 1 | 0 | 10 |
| Missouri non-MSA | Missouri | Audrain | 57 | 2769 | 0 | 0 | 22 |
| Missouri non-MSA | Missouri | Carroll | 23 | 1065 | 0 | 0 | 7 |
| Missouri non-MSA | Missouri | Holt | 11 | 430 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Texas | 22 | 1830 | 0 | 0 | 9 |
| Missouri non-MSA | Missouri | Benton | 29 | 1671 | 0 | 1 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 43 | 1573 | 0 | 1 | 22 |
| Missouri non-MSA | Missouri | Shelby | 7 | 588 | 0 | 1 | 7 |
| Missouri non-MSA | Missouri | Livingston | 39 | 1728 | 0 | 0 | 13 |
| Columbia-Jefferson City | Missouri | Cooper | 27 | 1912 | 0 | 0 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 29 | 1549 | 0 | 0 | 4 |
| Missouri non-MSA | Missouri | Chariton | 6 | 672 | 0 | 0 | 8 |
| Missouri non-MSA | Missouri | Maries | 8 | 632 | 0 | 0 | 3 |
| Missouri non-MSA | Missouri | Henry | 38 | 2016 | 0 | 1 | 8 |
| Columbia-Jefferson City | Missouri | Moniteau | 31 | 1776 | 0 | 0 | 3 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 385 | 0 | 0 | 4 |
| Missouri non-MSA | Missouri | Pulaski | 50 | 3456 | 0 | 1 | 15 |
| Missouri non-MSA | Missouri | Schuyler | 5 | 333 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Wright | 29 | 1559 | 0 | 0 | 6 |
| Columbia-Jefferson City | Missouri | Osage | 14 | 1631 | 0 | 1 | 7 |
| St. Joseph | Kansas | Doniphan | 23 | 964 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 11 | 1016 | 0 | 0 | 13 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1129 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Cedar | 20 | 1094 | 0 | 0 | 12 |
| Missouri non-MSA | Missouri | Linn | 12 | 1213 | 0 | 0 | 22 |
| Missouri non-MSA | Missouri | Daviess | 11 | 738 | 0 | 0 | 5 |
| Missouri non-MSA | Missouri | Ozark | 17 | 679 | 0 | 0 | 4 |
| Missouri non-MSA | Missouri | Shannon | 12 | 594 | 0 | 0 | 3 |
| Missouri non-MSA | Missouri | Adair | 18 | 2405 | 0 | 1 | 10 |
| Springfield | Missouri | Dallas | 26 | 1255 | 0 | 0 | 14 |
| St. Joseph | Missouri | DeKalb | 30 | 1150 | 0 | 0 | 7 |
| Missouri non-MSA | Missouri | St. Clair | 8 | 792 | 0 | 0 | 6 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 10 | 462 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 385 | 0 | 0 | 6 |
| Missouri non-MSA | Missouri | Lewis | 12 | 1043 | 0 | 0 | 13 |
| Missouri non-MSA | Missouri | Carter | 9 | 551 | 0 | 0 | 4 |
| Missouri non-MSA | Missouri | Scotland | 3 | 309 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 506 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 3 | 850 | 0 | 0 | 5 |
| Missouri non-MSA | Missouri | Morgan | 42 | 1708 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Atchison | 6 | 444 | 0 | 0 | 5 |
| Missouri non-MSA | Missouri | Barton | 14 | 1165 | 0 | 0 | 6 |
| Missouri non-MSA | Missouri | Mercer | 2 | 305 | 0 | 0 | 4 |
| Kansas City | Missouri | Caldwell | 11 | 770 | 0 | 0 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 14 | 860 | 0 | 0 | 3 |
| Missouri non-MSA | Missouri | Douglas | 27 | 901 | 0 | 0 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 7 | 1062 | 0 | 0 | 11 |
| Missouri non-MSA | Missouri | Gentry | 20 | 838 | 0 | 0 | 3 |
| Missouri non-MSA | Missouri | Grundy | 34 | 1009 | 0 | 0 | 5 |
| Missouri non-MSA | Missouri | Putnam | 4 | 296 | 0 | 0 | 2 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | -2300 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 14 | 646 | 0 | 0 | 5 |
| Missouri non-MSA | Missouri | Worth | 2 | 164 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 14 | 924 | 0 | 0 | 3 |
| Missouri non-MSA | Missouri | Clark | 7 | 672 | 0 | 0 | 6 |
| Missouri non-MSA | Missouri | Iron | 6 | 901 | 0 | 0 | 14 |
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
