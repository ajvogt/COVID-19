# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/08/2021  
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


## Missouri New Daily Deaths by Metropolitan Statistcal Areas
![](images/mo_daily_deaths.png)

## Missouri New Daily Confirmed Cases by Metropolitan Statistcal Areas
![](images/mo_daily_cases.png)

## Missouri Metropolitan Statistical Area Totals
<!-- msa_table start -->
| MSA | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|
| St. Louis-Farmington | 3533 | 212671 | 1536 | 1421 | 1602 |
| Kansas City | 1732 | 143173 | 1120 | 1038 | 1135 |
| Missouri non-MSA | 1485 | 96585 | 628 | 568 | 666 |
| Springfield | 437 | 30959 | 267 | 218 | 237 |
| Columbia-Jefferson City | 218 | 30740 | 173 | 163 | 183 |
| Joplin | 226 | 14087 | 89 | 78 | 73 |
| Cape Girardeau-Sikeston | 185 | 11511 | 61 | 57 | 62 |
| St. Joseph | 141 | 8971 | 51 | 48 | 51 |
<!-- msa_table end -->

## STL-Farmington MSA New Daily Deaths by County
![](images/stl_daily_deaths.png)

## STL-Farmington MSA New Daily Confirmed Cases by County
![](images/stl_daily_cases.png)

<a name="msa-counties"></a>
## Metropolitan Statistical Area (MSA) Counties
<!-- county_table start -->
| MSA | State | County | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|---|---|
| St. Louis-Farmington | Missouri | St. Louis | 1456 | 73293 | 544 | 500 | 540 |
| Kansas City | Kansas | Johnson | 517 | 41357 | 356 | 330 | 371 |
| Kansas City | Missouri | Kansas City | 366 | 31709 | 238 | 207 | 205 |
| St. Louis-Farmington | Missouri | St. Charles | 299 | 28463 | 189 | 168 | 202 |
| St. Louis-Farmington | Illinois | St. Clair | 382 | 20347 | 185 | 164 | 167 |
| Kansas City | Missouri | Jackson | 262 | 24721 | 185 | 168 | 179 |
| St. Louis-Farmington | Illinois | Madison | 423 | 22258 | 172 | 156 | 190 |
| Springfield | Missouri | Greene | 298 | 19925 | 171 | 140 | 151 |
| St. Louis-Farmington | Missouri | Jefferson | 149 | 16066 | 138 | 118 | 121 |
| Kansas City | Kansas | Wyandotte | 201 | 16285 | 101 | 102 | 129 |
| Columbia-Jefferson City | Missouri | Boone | 50 | 13940 | 83 | 76 | 91 |
| Joplin | Missouri | Jasper | 167 | 10470 | 67 | 59 | 56 |
| St. Louis-Farmington | Missouri | Franklin | 116 | 7001 | 63 | 54 | 55 |
| Springfield | Missouri | Christian | 53 | 5837 | 55 | 44 | 51 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17413 | 55 | 73 | 105 |
| Kansas City | Missouri | Clay | 110 | 6603 | 47 | 46 | 49 |
| Kansas City | Missouri | Cass | 58 | 5872 | 45 | 43 | 51 |
| St. Louis-Farmington | Missouri | St. Francois | 75 | 6821 | 40 | 41 | 45 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 103 | 6726 | 38 | 36 | 39 |
| Columbia-Jefferson City | Missouri | Cole | 93 | 7871 | 38 | 37 | 38 |
| Kansas City | Kansas | Leavenworth | 46 | 5279 | 33 | 32 | 38 |
| St. Joseph | Missouri | Buchanan | 99 | 6240 | 32 | 28 | 32 |
| St. Louis-Farmington | Illinois | Clinton | 81 | 4695 | 30 | 27 | 33 |
| Columbia-Jefferson City | Missouri | Callaway | 25 | 3963 | 26 | 26 | 27 |
| Kansas City | Kansas | Miami | 15 | 2002 | 26 | 25 | 25 |
| St. Louis-Farmington | Illinois | Macoupin | 90 | 3454 | 25 | 25 | 28 |
| Missouri non-MSA | Missouri | Taney | 56 | 3929 | 25 | 20 | 23 |
| St. Louis-Farmington | Illinois | Monroe | 61 | 3311 | 25 | 27 | 31 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3704 | 24 | 22 | 30 |
| Kansas City | Missouri | Platte | 24 | 2587 | 23 | 25 | 23 |
| Missouri non-MSA | Missouri | Pettis | 66 | 4225 | 23 | 25 | 38 |
| Missouri non-MSA | Missouri | Camden | 65 | 3302 | 22 | 21 | 21 |
| Missouri non-MSA | Missouri | Howell | 38 | 2470 | 22 | 17 | 26 |
| Joplin | Missouri | Newton | 59 | 3617 | 21 | 18 | 17 |
| Springfield | Missouri | Webster | 43 | 2570 | 21 | 18 | 19 |
| Missouri non-MSA | Missouri | Lawrence | 57 | 2434 | 20 | 13 | 13 |
| Missouri non-MSA | Missouri | Phelps | 89 | 2613 | 19 | 18 | 19 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2414 | 18 | 9 | 9 |
| Missouri non-MSA | Missouri | Adair | 5 | 1722 | 18 | 15 | 17 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3338 | 17 | 15 | 19 |
| Missouri non-MSA | Missouri | Laclede | 48 | 2615 | 17 | 14 | 18 |
| Missouri non-MSA | Missouri | Saline | 26 | 2116 | 17 | 12 | 14 |
| Springfield | Missouri | Polk | 24 | 1910 | 16 | 11 | 12 |
| Cape Girardeau-Sikeston | Missouri | Scott | 63 | 3445 | 16 | 15 | 16 |
| Kansas City | Missouri | Lafayette | 42 | 2170 | 16 | 14 | 16 |
| Missouri non-MSA | Missouri | Butler | 16 | 2914 | 15 | 13 | 16 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1745 | 15 | 12 | 13 |
| Kansas City | Missouri | Ray | 9 | 1214 | 14 | 11 | 13 |
| Missouri non-MSA | Missouri | Miller | 42 | 2121 | 13 | 11 | 14 |
| Missouri non-MSA | Missouri | Stone | 27 | 1708 | 13 | 11 | 12 |
| St. Louis-Farmington | Illinois | Jersey | 47 | 2068 | 13 | 14 | 17 |
| Missouri non-MSA | Missouri | Marion | 30 | 2422 | 13 | 12 | 14 |
| Missouri non-MSA | Missouri | Benton | 16 | 1281 | 13 | 9 | 12 |
| Missouri non-MSA | Missouri | Crawford | 20 | 1796 | 12 | 14 | 15 |
| Missouri non-MSA | Missouri | Barry | 37 | 1871 | 12 | 9 | 10 |
| Missouri non-MSA | Missouri | Washington | 41 | 1870 | 12 | 11 | 10 |
| Missouri non-MSA | Missouri | Vernon | 24 | 1171 | 12 | 17 | 13 |
| Missouri non-MSA | Missouri | Wright | 24 | 1157 | 12 | 11 | 10 |
| Missouri non-MSA | Missouri | Pulaski | 29 | 2628 | 11 | 10 | 21 |
| St. Louis-Farmington | Illinois | Bond | 19 | 1632 | 11 | 10 | 13 |
| Kansas City | Missouri | Clinton | 59 | 1321 | 10 | 9 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2155 | 10 | 9 | 11 |
| Kansas City | Missouri | Bates | 13 | 901 | 9 | 9 | 9 |
| Missouri non-MSA | Missouri | Texas | 18 | 1405 | 9 | 8 | 11 |
| Missouri non-MSA | Missouri | Henry | 24 | 1498 | 9 | 7 | 9 |
| Columbia-Jefferson City | Missouri | Moniteau | 18 | 1552 | 9 | 7 | 7 |
| St. Joseph | Missouri | Andrew | 15 | 1155 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Audrain | 41 | 1857 | 9 | 21 | 20 |
| Missouri non-MSA | Missouri | Macon | 10 | 979 | 9 | 7 | 8 |
| Kansas City | Kansas | Linn | 3 | 579 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Oregon | 3 | 592 | 8 | 5 | 6 |
| Missouri non-MSA | Missouri | McDonald | 21 | 1712 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 9 | 1470 | 8 | 7 | 9 |
| Missouri non-MSA | Missouri | Randolph | 19 | 1657 | 8 | 7 | 10 |
| Missouri non-MSA | Missouri | Morgan | 24 | 1500 | 8 | 7 | 9 |
| Missouri non-MSA | Missouri | Livingston | 24 | 1092 | 8 | 7 | 8 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1240 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Madison | 11 | 1251 | 7 | 8 | 8 |
| Missouri non-MSA | Missouri | Gasconade | 30 | 726 | 7 | 5 | 6 |
| Missouri non-MSA | Missouri | Perry | 19 | 1902 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2063 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | New Madrid | 38 | 1660 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Gentry | 16 | 646 | 6 | 4 | 5 |
| Missouri non-MSA | Missouri | Cedar | 9 | 558 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Wayne | 7 | 703 | 5 | 4 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1532 | 5 | 5 | 9 |
| Missouri non-MSA | Missouri | Pike | 16 | 1314 | 5 | 6 | 9 |
| St. Joseph | Kansas | Doniphan | 7 | 762 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Barton | 8 | 803 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Carroll | 18 | 688 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Douglas | 20 | 654 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Ralls | 7 | 696 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Grundy | 26 | 714 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 22 | 1308 | 5 | 3 | 4 |
| St. Joseph | Missouri | DeKalb | 20 | 814 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Monroe | 6 | 545 | 4 | 3 | 4 |
| Kansas City | Missouri | Caldwell | 7 | 573 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 485 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 524 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Ozark | 4 | 404 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 10 | 682 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Lewis | 3 | 565 | 3 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 642 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Dent | 9 | 726 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Harrison | 10 | 658 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Ripley | 9 | 697 | 3 | 3 | 4 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 980 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Chariton | 3 | 353 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 9 | 489 | 3 | 2 | 3 |
| Springfield | Missouri | Dallas | 19 | 717 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Shannon | 9 | 428 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Atchison | 5 | 279 | 2 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 400 | 2 | 3 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 360 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 4 | 311 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 217 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 18 | 1155 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Maries | 7 | 480 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 9 | 442 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 1 | 424 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Carter | 6 | 387 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Linn | 10 | 430 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 235 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 5 | 383 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 335 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 10 | 377 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 139 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 233 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 156 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 124 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 202 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
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

### To-Do (updated 7/20/2020)

#### Analysis Page
- [ ] Update description to accurately reflect CSA vs. MSA
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
