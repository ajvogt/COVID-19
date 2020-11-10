# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/10/2020  
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
| St. Louis-Farmington | 1986 | 100829 | 1704 | 1370 | 1016 |
| Kansas City | 965 | 70877 | 1035 | 919 | 676 |
| Missouri non-MSA | 639 | 49659 | 893 | 777 | 620 |
| Columbia-Jefferson City | 70 | 16392 | 381 | 309 | 227 |
| Springfield | 206 | 16504 | 211 | 204 | 165 |
| Joplin | 106 | 8558 | 108 | 97 | 79 |
| Cape Girardeau-Sikeston | 93 | 5946 | 105 | 92 | 69 |
| St. Joseph | 60 | 4659 | 72 | 53 | 50 |
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
| St. Louis-Farmington | Missouri | St. Louis | 897 | 36172 | 524 | 443 | 334 |
| Kansas City | Kansas | Johnson | 235 | 18783 | 323 | 300 | 205 |
| St. Louis-Farmington | Missouri | St. Charles | 157 | 13640 | 258 | 211 | 165 |
| Kansas City | Missouri | Kansas City | 227 | 17226 | 233 | 208 | 138 |
| St. Louis-Farmington | Illinois | Madison | 169 | 9364 | 210 | 153 | 102 |
| Kansas City | Missouri | Jackson | 145 | 12170 | 199 | 159 | 128 |
| Columbia-Jefferson City | Missouri | Boone | 15 | 7541 | 154 | 112 | 76 |
| St. Louis-Farmington | Missouri | Jefferson | 90 | 7121 | 141 | 113 | 75 |
| St. Louis-Farmington | Illinois | St. Clair | 241 | 9409 | 134 | 101 | 74 |
| Springfield | Missouri | Greene | 153 | 10677 | 130 | 123 | 98 |
| Columbia-Jefferson City | Missouri | Cole | 26 | 4230 | 103 | 92 | 71 |
| St. Louis-Farmington | Missouri | St. Louis City | 225 | 9612 | 101 | 88 | 69 |
| Joplin | Missouri | Jasper | 84 | 6199 | 84 | 73 | 51 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 56 | 3385 | 68 | 52 | 38 |
| St. Louis-Farmington | Missouri | St. Francois | 30 | 3572 | 63 | 52 | 36 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 1941 | 62 | 52 | 36 |
| Kansas City | Kansas | Wyandotte | 167 | 9282 | 62 | 64 | 56 |
| Kansas City | Missouri | Clay | 51 | 3220 | 59 | 51 | 41 |
| Missouri non-MSA | Missouri | Pettis | 24 | 2235 | 56 | 44 | 31 |
| St. Louis-Farmington | Missouri | Franklin | 50 | 3385 | 55 | 51 | 43 |
| Springfield | Missouri | Christian | 17 | 2822 | 46 | 39 | 32 |
| St. Joseph | Missouri | Buchanan | 45 | 3445 | 45 | 34 | 32 |
| Kansas City | Missouri | Cass | 33 | 2533 | 42 | 36 | 26 |
| St. Louis-Farmington | Illinois | Clinton | 36 | 2207 | 38 | 29 | 26 |
| St. Louis-Farmington | Illinois | Macoupin | 13 | 1144 | 37 | 23 | 16 |
| St. Louis-Farmington | Illinois | Jersey | 22 | 764 | 36 | 20 | 11 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1856 | 34 | 26 | 19 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1559 | 32 | 26 | 20 |
| St. Louis-Farmington | Illinois | Monroe | 40 | 1304 | 31 | 27 | 17 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1488 | 30 | 25 | 19 |
| Missouri non-MSA | Missouri | Taney | 36 | 2124 | 29 | 29 | 21 |
| Missouri non-MSA | Missouri | Marion | 14 | 1222 | 27 | 22 | 15 |
| Missouri non-MSA | Missouri | Washington | 20 | 931 | 27 | 19 | 12 |
| Missouri non-MSA | Missouri | Lawrence | 26 | 1410 | 26 | 22 | 19 |
| Cape Girardeau-Sikeston | Missouri | Scott | 31 | 1773 | 26 | 26 | 21 |
| Kansas City | Kansas | Leavenworth | 21 | 2913 | 25 | 21 | 17 |
| Joplin | Missouri | Newton | 22 | 2359 | 24 | 24 | 27 |
| Missouri non-MSA | Missouri | Perry | 8 | 1052 | 23 | 17 | 11 |
| Missouri non-MSA | Missouri | Camden | 37 | 1861 | 23 | 19 | 18 |
| Columbia-Jefferson City | Missouri | Cooper | 4 | 846 | 23 | 16 | 11 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 658 | 22 | 18 | 13 |
| Missouri non-MSA | Missouri | Butler | 8 | 1546 | 21 | 26 | 23 |
| Kansas City | Missouri | Lafayette | 26 | 1089 | 21 | 18 | 13 |
| Missouri non-MSA | Missouri | Henry | 8 | 616 | 21 | 17 | 10 |
| Missouri non-MSA | Missouri | Miller | 18 | 1134 | 20 | 19 | 16 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1350 | 20 | 16 | 13 |
| Missouri non-MSA | Missouri | Phelps | 31 | 1091 | 20 | 18 | 16 |
| St. Louis-Farmington | Illinois | Bond | 9 | 687 | 20 | 12 | 10 |
| Missouri non-MSA | Missouri | Laclede | 25 | 1414 | 19 | 16 | 16 |
| Missouri non-MSA | Missouri | Saline | 11 | 1162 | 19 | 15 | 10 |
| Missouri non-MSA | Missouri | Barry | 19 | 1074 | 18 | 19 | 16 |
| Springfield | Missouri | Webster | 23 | 1384 | 18 | 17 | 15 |
| Missouri non-MSA | Missouri | Randolph | 3 | 811 | 18 | 14 | 13 |
| Missouri non-MSA | Missouri | Crawford | 9 | 838 | 17 | 14 | 11 |
| Kansas City | Missouri | Platte | 13 | 1186 | 17 | 14 | 12 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 953 | 16 | 13 | 10 |
| Columbia-Jefferson City | Missouri | Moniteau | 13 | 835 | 16 | 15 | 14 |
| Missouri non-MSA | Missouri | Adair | 0 | 696 | 16 | 13 | 9 |
| Missouri non-MSA | Missouri | Pike | 8 | 513 | 15 | 11 | 7 |
| Missouri non-MSA | Missouri | Pulaski | 11 | 1197 | 15 | 15 | 12 |
| Kansas City | Missouri | Ray | 2 | 439 | 15 | 11 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 672 | 14 | 13 | 14 |
| Missouri non-MSA | Missouri | Stone | 13 | 869 | 14 | 12 | 9 |
| Missouri non-MSA | Missouri | Texas | 5 | 745 | 13 | 11 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 1059 | 13 | 13 | 13 |
| Missouri non-MSA | Missouri | Macon | 1 | 344 | 12 | 9 | 5 |
| Missouri non-MSA | Missouri | Vernon | 3 | 465 | 12 | 9 | 7 |
| St. Joseph | Missouri | DeKalb | 5 | 407 | 11 | 7 | 7 |
| St. Louis-Farmington | Missouri | Warren | 2 | 764 | 11 | 10 | 8 |
| Missouri non-MSA | Missouri | Pemiscot | 14 | 853 | 11 | 9 | 7 |
| Missouri non-MSA | Missouri | Audrain | 10 | 745 | 11 | 12 | 8 |
| Missouri non-MSA | Missouri | Morgan | 8 | 840 | 11 | 12 | 11 |
| Kansas City | Kansas | Miami | 2 | 680 | 11 | 10 | 7 |
| Missouri non-MSA | Missouri | Benton | 7 | 586 | 10 | 7 | 5 |
| Kansas City | Missouri | Clinton | 33 | 643 | 10 | 10 | 10 |
| Springfield | Missouri | Polk | 11 | 1161 | 10 | 16 | 12 |
| Missouri non-MSA | Missouri | Lewis | 2 | 305 | 10 | 7 | 5 |
| Missouri non-MSA | Missouri | Howell | 16 | 1357 | 9 | 15 | 15 |
| Missouri non-MSA | Missouri | Madison | 3 | 614 | 8 | 8 | 8 |
| St. Joseph | Missouri | Andrew | 8 | 537 | 7 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 327 | 7 | 5 | 4 |
| St. Joseph | Kansas | Doniphan | 2 | 270 | 7 | 4 | 4 |
| Missouri non-MSA | Missouri | Carroll | 4 | 273 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Ripley | 5 | 346 | 7 | 5 | 6 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 516 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Chariton | 0 | 124 | 7 | 4 | 2 |
| Springfield | Missouri | Dallas | 2 | 460 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Gentry | 10 | 257 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 3 | 431 | 6 | 9 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 4 | 606 | 6 | 9 | 7 |
| Missouri non-MSA | Missouri | Grundy | 11 | 332 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Ralls | 0 | 268 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Monroe | 2 | 238 | 6 | 5 | 4 |
| Kansas City | Missouri | Caldwell | 1 | 237 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 337 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 171 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Clark | 2 | 176 | 5 | 4 | 3 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 125 | 5 | 4 | 1 |
| Missouri non-MSA | Missouri | Dade | 3 | 193 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Dent | 4 | 318 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Barton | 4 | 494 | 5 | 4 | 5 |
| Kansas City | Missouri | Bates | 8 | 310 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Cedar | 4 | 297 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Oregon | 0 | 290 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Harrison | 1 | 239 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Holt | 1 | 167 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 86 | 5 | 3 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 2 | 235 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Linn | 7 | 211 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Livingston | 9 | 622 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Hickory | 4 | 292 | 4 | 6 | 4 |
| Missouri non-MSA | Missouri | Wayne | 3 | 368 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Maries | 1 | 256 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Daviess | 4 | 263 | 4 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 182 | 4 | 4 | 2 |
| Kansas City | Kansas | Linn | 1 | 166 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Douglas | 13 | 335 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Wright | 9 | 651 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Shannon | 6 | 298 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | McDonald | 14 | 1287 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | Iron | 0 | 140 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Atchison | 1 | 109 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 100 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 1 | 112 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 127 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 84 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Ozark | 1 | 242 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 3 | 207 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Mercer | 0 | 48 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 67 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 38 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
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
