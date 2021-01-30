# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/30/2021  
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
| St. Louis-Farmington | 4119 | 241348 | 966 | 1068 | 1365 |
| Kansas City | 2099 | 164918 | 789 | 844 | 1009 |
| Missouri non-MSA | 1705 | 105810 | 289 | 311 | 486 |
| Springfield | 533 | 34573 | 118 | 122 | 193 |
| Columbia-Jefferson City | 261 | 33131 | 81 | 84 | 126 |
| Joplin | 255 | 15472 | 52 | 52 | 71 |
| Cape Girardeau-Sikeston | 201 | 12318 | 29 | 26 | 44 |
| St. Joseph | 174 | 9772 | 26 | 28 | 40 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1681 | 83094 | 401 | 400 | 475 |
| Kansas City | Kansas | Johnson | 655 | 49641 | 249 | 333 | 359 |
| Kansas City | Missouri | Kansas City | 439 | 35440 | 172 | 145 | 188 |
| Kansas City | Missouri | Jackson | 308 | 28261 | 156 | 136 | 169 |
| St. Louis-Farmington | Illinois | Madison | 499 | 25953 | 134 | 150 | 170 |
| St. Louis-Farmington | Illinois | St. Clair | 469 | 23525 | 106 | 120 | 155 |
| St. Louis-Farmington | Missouri | St. Charles | 344 | 31363 | 78 | 100 | 148 |
| Springfield | Missouri | Greene | 379 | 22247 | 76 | 79 | 124 |
| St. Louis-Farmington | Missouri | Jefferson | 169 | 18107 | 63 | 72 | 106 |
| Kansas City | Kansas | Wyandotte | 230 | 18114 | 51 | 64 | 84 |
| Columbia-Jefferson City | Missouri | Boone | 61 | 15237 | 46 | 49 | 65 |
| St. Louis-Farmington | Missouri | St. Louis City | 349 | 20148 | 42 | 63 | 92 |
| Joplin | Missouri | Jasper | 195 | 11551 | 40 | 41 | 55 |
| Kansas City | Missouri | Cass | 69 | 6833 | 39 | 34 | 44 |
| Kansas City | Missouri | Clay | 124 | 7456 | 33 | 30 | 41 |
| Kansas City | Kansas | Leavenworth | 59 | 6186 | 31 | 37 | 38 |
| St. Louis-Farmington | Missouri | Franklin | 131 | 7997 | 29 | 34 | 51 |
| Springfield | Missouri | Christian | 63 | 6558 | 23 | 25 | 38 |
| St. Louis-Farmington | Illinois | Clinton | 91 | 5289 | 20 | 24 | 28 |
| St. Louis-Farmington | Illinois | Monroe | 72 | 3789 | 19 | 19 | 23 |
| St. Louis-Farmington | Illinois | Macoupin | 100 | 4112 | 19 | 24 | 29 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 110 | 7213 | 18 | 16 | 27 |
| St. Joseph | Missouri | Buchanan | 121 | 6742 | 16 | 18 | 25 |
| Columbia-Jefferson City | Missouri | Cole | 104 | 8323 | 16 | 14 | 24 |
| Missouri non-MSA | Missouri | Taney | 68 | 4395 | 15 | 15 | 22 |
| Kansas City | Kansas | Miami | 28 | 2482 | 14 | 19 | 22 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 4060 | 13 | 13 | 18 |
| St. Louis-Farmington | Missouri | St. Francois | 83 | 7330 | 13 | 15 | 29 |
| Joplin | Missouri | Newton | 60 | 3921 | 11 | 10 | 16 |
| Missouri non-MSA | Missouri | Pettis | 69 | 4607 | 11 | 11 | 19 |
| Kansas City | Missouri | Platte | 36 | 2896 | 11 | 9 | 17 |
| St. Louis-Farmington | Illinois | Jersey | 63 | 2348 | 10 | 12 | 12 |
| Springfield | Missouri | Webster | 46 | 2915 | 10 | 10 | 17 |
| Missouri non-MSA | Missouri | Johnson | 35 | 3658 | 9 | 10 | 15 |
| Columbia-Jefferson City | Missouri | Callaway | 34 | 4246 | 9 | 9 | 16 |
| Missouri non-MSA | Missouri | Butler | 24 | 3215 | 9 | 11 | 14 |
| Missouri non-MSA | Missouri | Adair | 7 | 1980 | 8 | 9 | 13 |
| Missouri non-MSA | Missouri | Camden | 74 | 3600 | 8 | 8 | 16 |
| Kansas City | Missouri | Lafayette | 46 | 2391 | 8 | 8 | 11 |
| St. Louis-Farmington | Missouri | Warren | 12 | 1974 | 7 | 9 | 11 |
| Missouri non-MSA | Missouri | Laclede | 58 | 2818 | 7 | 7 | 11 |
| Kansas City | Missouri | Ray | 17 | 1401 | 7 | 7 | 9 |
| Missouri non-MSA | Missouri | Macon | 10 | 1158 | 7 | 8 | 8 |
| Missouri non-MSA | Missouri | Lawrence | 61 | 2638 | 7 | 8 | 12 |
| Cape Girardeau-Sikeston | Missouri | Scott | 71 | 3666 | 7 | 6 | 12 |
| Missouri non-MSA | Missouri | Henry | 28 | 1648 | 7 | 5 | 7 |
| Missouri non-MSA | Missouri | Stone | 32 | 1915 | 7 | 7 | 10 |
| Missouri non-MSA | Missouri | Howell | 41 | 2728 | 7 | 8 | 15 |
| Missouri non-MSA | Missouri | Washington | 41 | 2065 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2226 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Audrain | 50 | 2012 | 6 | 5 | 8 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2342 | 6 | 6 | 9 |
| Missouri non-MSA | Missouri | Phelps | 107 | 2877 | 6 | 8 | 14 |
| Missouri non-MSA | Missouri | Crawford | 24 | 1980 | 6 | 5 | 10 |
| Missouri non-MSA | Missouri | Livingston | 32 | 1263 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Saline | 30 | 2325 | 5 | 7 | 11 |
| Missouri non-MSA | Missouri | Harrison | 12 | 789 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Barry | 41 | 2094 | 5 | 5 | 10 |
| St. Joseph | Kansas | Doniphan | 12 | 894 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Miller | 45 | 2277 | 5 | 5 | 9 |
| Springfield | Missouri | Polk | 25 | 2065 | 5 | 4 | 9 |
| Kansas City | Kansas | Linn | 4 | 710 | 4 | 4 | 6 |
| Kansas City | Missouri | Bates | 16 | 1026 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Carroll | 18 | 783 | 4 | 3 | 4 |
| St. Louis-Farmington | Illinois | Bond | 27 | 1806 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 12 | 1564 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 34 | 2905 | 4 | 4 | 12 |
| Missouri non-MSA | Missouri | Marion | 36 | 2578 | 4 | 5 | 8 |
| Missouri non-MSA | Missouri | St. Clair | 6 | 553 | 4 | 3 | 3 |
| Kansas City | Missouri | Clinton | 60 | 1464 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Wright | 24 | 1319 | 4 | 5 | 9 |
| Missouri non-MSA | Missouri | Gasconade | 33 | 841 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Ripley | 10 | 781 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Pike | 17 | 1443 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Vernon | 32 | 1327 | 3 | 4 | 12 |
| Missouri non-MSA | Missouri | Mississippi | 21 | 1217 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Osage | 10 | 1348 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | McDonald | 24 | 1864 | 3 | 4 | 7 |
| Springfield | Missouri | Dallas | 20 | 788 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Linn | 10 | 521 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 10 | 561 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Gentry | 19 | 714 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Madison | 13 | 1328 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Perry | 22 | 1991 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Ozark | 10 | 518 | 2 | 3 | 4 |
| St. Joseph | Missouri | Andrew | 17 | 1244 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Benton | 20 | 1382 | 2 | 3 | 7 |
| Missouri non-MSA | Missouri | Cedar | 9 | 638 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Morgan | 34 | 1589 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Barton | 9 | 910 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1380 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dent | 11 | 795 | 2 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1637 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Wayne | 9 | 784 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 41 | 1739 | 2 | 2 | 4 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1649 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Oregon | 3 | 659 | 2 | 2 | 4 |
| St. Joseph | Missouri | DeKalb | 24 | 892 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Douglas | 23 | 743 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Texas | 21 | 1495 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | Clark | 6 | 438 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Monroe | 7 | 579 | 1 | 1 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1027 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ralls | 10 | 734 | 1 | 1 | 2 |
| Kansas City | Missouri | Caldwell | 8 | 617 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Dade | 12 | 410 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 5 | 345 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2501 | 1 | 3 | 7 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 260 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Maries | 7 | 517 | 1 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 691 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Iron | 1 | 461 | 1 | 0 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 412 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 739 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shannon | 10 | 457 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Lewis | 3 | 619 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Holt | 10 | 357 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Grundy | 30 | 792 | 0 | 1 | 4 |
| Missouri non-MSA | Missouri | Chariton | 3 | 402 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 10 | 459 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 136 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 5 | 453 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 2 | 171 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 161 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 217 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 237 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 288 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 256 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 8 | 409 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 550 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Randolph | 24 | 1783 | 0 | 2 | 6 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
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
