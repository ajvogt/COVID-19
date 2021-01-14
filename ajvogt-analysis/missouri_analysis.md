# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/14/2021  
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
| St. Louis-Farmington | 3704 | 221821 | 1696 | 1564 | 1529 |
| Kansas City | 1867 | 151079 | 1254 | 1175 | 1121 |
| Missouri non-MSA | 1560 | 100293 | 672 | 648 | 621 |
| Springfield | 461 | 32467 | 251 | 264 | 235 |
| Columbia-Jefferson City | 238 | 31657 | 168 | 165 | 172 |
| Joplin | 237 | 14612 | 91 | 92 | 78 |
| Cape Girardeau-Sikeston | 193 | 11796 | 57 | 59 | 57 |
| St. Joseph | 155 | 9276 | 52 | 51 | 48 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1530 | 76601 | 671 | 555 | 525 |
| Kansas City | Kansas | Johnson | 587 | 44346 | 427 | 391 | 373 |
| Kansas City | Missouri | Kansas City | 375 | 33027 | 234 | 231 | 206 |
| Kansas City | Missouri | Jackson | 279 | 25970 | 218 | 199 | 179 |
| St. Louis-Farmington | Missouri | St. Charles | 315 | 29648 | 208 | 195 | 194 |
| St. Louis-Farmington | Illinois | St. Clair | 405 | 21420 | 199 | 182 | 163 |
| St. Louis-Farmington | Illinois | Madison | 445 | 23450 | 198 | 187 | 182 |
| Springfield | Missouri | Greene | 313 | 20888 | 161 | 168 | 150 |
| St. Louis-Farmington | Missouri | Jefferson | 153 | 16847 | 138 | 138 | 121 |
| Kansas City | Kansas | Wyandotte | 213 | 17039 | 107 | 104 | 115 |
| Columbia-Jefferson City | Missouri | Boone | 54 | 14405 | 82 | 81 | 85 |
| Joplin | Missouri | Jasper | 177 | 10864 | 68 | 70 | 58 |
| St. Louis-Farmington | Missouri | Franklin | 122 | 7381 | 64 | 65 | 56 |
| Kansas City | Missouri | Cass | 62 | 6222 | 59 | 51 | 51 |
| Kansas City | Missouri | Clay | 118 | 6935 | 58 | 51 | 48 |
| Springfield | Missouri | Christian | 60 | 6129 | 49 | 52 | 49 |
| St. Louis-Farmington | Missouri | St. Francois | 79 | 7051 | 42 | 42 | 42 |
| Kansas City | Kansas | Leavenworth | 50 | 5574 | 42 | 37 | 37 |
| St. Louis-Farmington | Illinois | Macoupin | 92 | 3704 | 41 | 33 | 30 |
| Columbia-Jefferson City | Missouri | Cole | 101 | 8062 | 35 | 34 | 35 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 106 | 6888 | 33 | 36 | 36 |
| Missouri non-MSA | Missouri | Pettis | 68 | 4399 | 32 | 27 | 28 |
| Missouri non-MSA | Missouri | Taney | 60 | 4134 | 32 | 30 | 23 |
| St. Joseph | Missouri | Buchanan | 109 | 6427 | 32 | 31 | 29 |
| St. Louis-Farmington | Illinois | Clinton | 82 | 4885 | 31 | 33 | 31 |
| Missouri non-MSA | Missouri | Pulaski | 32 | 2807 | 29 | 20 | 21 |
| St. Louis-Farmington | Illinois | Monroe | 66 | 3468 | 27 | 26 | 29 |
| Missouri non-MSA | Missouri | Camden | 66 | 3446 | 26 | 23 | 21 |
| Kansas City | Kansas | Miami | 17 | 2178 | 25 | 25 | 25 |
| Kansas City | Missouri | Platte | 26 | 2717 | 25 | 23 | 24 |
| Columbia-Jefferson City | Missouri | Callaway | 29 | 4086 | 24 | 24 | 25 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 3835 | 24 | 23 | 26 |
| Springfield | Missouri | Webster | 44 | 2718 | 23 | 24 | 20 |
| Joplin | Missouri | Newton | 60 | 3748 | 23 | 22 | 19 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3470 | 22 | 19 | 19 |
| Missouri non-MSA | Missouri | Howell | 40 | 2561 | 20 | 20 | 16 |
| Missouri non-MSA | Missouri | Lawrence | 60 | 2539 | 17 | 18 | 14 |
| Missouri non-MSA | Missouri | Adair | 6 | 1816 | 16 | 16 | 17 |
| Cape Girardeau-Sikeston | Missouri | Scott | 68 | 3531 | 16 | 16 | 15 |
| Missouri non-MSA | Missouri | Saline | 26 | 2193 | 16 | 15 | 13 |
| Missouri non-MSA | Missouri | Butler | 17 | 3020 | 16 | 17 | 15 |
| Missouri non-MSA | Missouri | Phelps | 93 | 2702 | 15 | 19 | 18 |
| Missouri non-MSA | Missouri | Laclede | 51 | 2691 | 14 | 15 | 15 |
| Missouri non-MSA | Missouri | Barry | 37 | 1962 | 14 | 13 | 11 |
| Missouri non-MSA | Missouri | Washington | 41 | 1935 | 13 | 12 | 10 |
| Springfield | Missouri | Polk | 25 | 1990 | 13 | 15 | 12 |
| Missouri non-MSA | Missouri | Vernon | 29 | 1246 | 13 | 20 | 14 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2227 | 13 | 11 | 12 |
| Missouri non-MSA | Missouri | Stone | 28 | 1794 | 13 | 14 | 12 |
| St. Louis-Farmington | Illinois | Bond | 22 | 1702 | 13 | 11 | 12 |
| Kansas City | Missouri | Lafayette | 44 | 2243 | 13 | 13 | 15 |
| Missouri non-MSA | Missouri | Miller | 44 | 2188 | 12 | 13 | 13 |
| Missouri non-MSA | Missouri | Livingston | 25 | 1153 | 12 | 8 | 9 |
| St. Louis-Farmington | Missouri | Warren | 11 | 1812 | 12 | 13 | 13 |
| Missouri non-MSA | Missouri | Crawford | 21 | 1869 | 12 | 13 | 15 |
| Kansas City | Missouri | Clinton | 60 | 1385 | 11 | 10 | 9 |
| Kansas City | Missouri | Ray | 11 | 1273 | 11 | 12 | 12 |
| St. Louis-Farmington | Illinois | Jersey | 52 | 2137 | 11 | 12 | 15 |
| Missouri non-MSA | Missouri | McDonald | 23 | 1783 | 11 | 9 | 9 |
| Missouri non-MSA | Missouri | Audrain | 43 | 1920 | 11 | 10 | 18 |
| Missouri non-MSA | Missouri | Marion | 32 | 2488 | 11 | 12 | 12 |
| Missouri non-MSA | Missouri | Wright | 24 | 1223 | 11 | 13 | 10 |
| Missouri non-MSA | Missouri | Henry | 25 | 1548 | 11 | 9 | 9 |
| Missouri non-MSA | Missouri | Randolph | 20 | 1722 | 11 | 9 | 9 |
| Missouri non-MSA | Missouri | Benton | 19 | 1317 | 9 | 10 | 8 |
| Missouri non-MSA | Missouri | Pike | 17 | 1365 | 9 | 7 | 8 |
| Missouri non-MSA | Missouri | Macon | 10 | 1028 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2444 | 9 | 11 | 8 |
| Kansas City | Missouri | Bates | 14 | 948 | 8 | 10 | 9 |
| Missouri non-MSA | Missouri | Barton | 9 | 858 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | Morgan | 31 | 1544 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2114 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 31 | 766 | 8 | 7 | 6 |
| St. Joseph | Kansas | Doniphan | 10 | 819 | 8 | 6 | 7 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17457 | 8 | 39 | 79 |
| Columbia-Jefferson City | Missouri | Moniteau | 20 | 1595 | 8 | 8 | 7 |
| Kansas City | Kansas | Linn | 4 | 634 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Oregon | 3 | 617 | 7 | 6 | 4 |
| Columbia-Jefferson City | Missouri | Osage | 9 | 1279 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Ozark | 5 | 448 | 7 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1567 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Grundy | 27 | 751 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Linn | 11 | 467 | 6 | 3 | 2 |
| Missouri non-MSA | Missouri | Texas | 20 | 1442 | 6 | 8 | 9 |
| Missouri non-MSA | Missouri | New Madrid | 39 | 1693 | 6 | 6 | 7 |
| St. Joseph | Missouri | Andrew | 15 | 1193 | 6 | 8 | 7 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 11 | 1503 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Madison | 11 | 1284 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Douglas | 20 | 694 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Perry | 20 | 1936 | 6 | 6 | 8 |
| St. Joseph | Missouri | DeKalb | 21 | 837 | 6 | 4 | 4 |
| Missouri non-MSA | Missouri | Harrison | 10 | 695 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Ripley | 9 | 734 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Wayne | 9 | 729 | 5 | 5 | 4 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1004 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Cedar | 9 | 588 | 5 | 6 | 3 |
| Missouri non-MSA | Missouri | Carroll | 18 | 718 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1339 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Daviess | 9 | 520 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Gentry | 16 | 665 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 11 | 704 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Iron | 1 | 444 | 3 | 3 | 4 |
| Springfield | Missouri | Dallas | 19 | 742 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Chariton | 3 | 373 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Ralls | 9 | 711 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Lewis | 3 | 588 | 3 | 3 | 3 |
| Kansas City | Missouri | Caldwell | 7 | 588 | 3 | 3 | 4 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 423 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Atchison | 6 | 285 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 504 | 3 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 663 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Shannon | 9 | 440 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Dent | 9 | 742 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Monroe | 7 | 558 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 234 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 19 | 1169 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 537 | 2 | 3 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 373 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 7 | 400 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 247 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 2 | 152 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 491 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Dade | 10 | 388 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Holt | 9 | 342 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 4 | 322 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Clark | 5 | 391 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 9 | 448 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 129 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 206 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 160 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 233 | 0 | 0 | 0 |
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
