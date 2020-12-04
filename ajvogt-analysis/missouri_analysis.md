# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/03/2020  
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
| St. Louis-Farmington | 2419 | 152325 | 1922 | 2121 | 2114 |
| Kansas City | 1219 | 101375 | 1079 | 1237 | 1258 |
| Missouri non-MSA | 913 | 71070 | 689 | 836 | 922 |
| Springfield | 253 | 22107 | 216 | 231 | 236 |
| Columbia-Jefferson City | 125 | 23765 | 212 | 269 | 334 |
| Cape Girardeau-Sikeston | 115 | 8994 | 94 | 115 | 126 |
| St. Joseph | 88 | 6823 | 86 | 96 | 88 |
| Joplin | 155 | 11445 | 75 | 106 | 121 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1008 | 52993 | 601 | 672 | 683 |
| Kansas City | Kansas | Johnson | 293 | 28078 | 306 | 375 | 385 |
| St. Louis-Farmington | Missouri | St. Charles | 219 | 20741 | 254 | 291 | 296 |
| Kansas City | Missouri | Kansas City | 299 | 23796 | 230 | 267 | 273 |
| St. Louis-Farmington | Illinois | Madison | 263 | 15129 | 224 | 235 | 241 |
| St. Louis-Farmington | Illinois | St. Clair | 266 | 14020 | 215 | 214 | 185 |
| Kansas City | Missouri | Jackson | 184 | 17812 | 214 | 222 | 234 |
| St. Louis-Farmington | Missouri | Jefferson | 108 | 11460 | 157 | 178 | 177 |
| St. Louis-Farmington | Missouri | St. Louis City | 240 | 13282 | 143 | 152 | 146 |
| Springfield | Missouri | Greene | 182 | 14317 | 142 | 151 | 151 |
| Kansas City | Kansas | Wyandotte | 180 | 11781 | 86 | 110 | 97 |
| Columbia-Jefferson City | Missouri | Boone | 25 | 10577 | 85 | 110 | 137 |
| Joplin | Missouri | Jasper | 117 | 8433 | 63 | 82 | 94 |
| Columbia-Jefferson City | Missouri | Cole | 60 | 6338 | 59 | 79 | 94 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 65 | 5177 | 57 | 68 | 75 |
| St. Joseph | Missouri | Buchanan | 63 | 4843 | 56 | 62 | 57 |
| St. Louis-Farmington | Missouri | Franklin | 86 | 4970 | 56 | 64 | 65 |
| Kansas City | Missouri | Clay | 77 | 4752 | 51 | 57 | 65 |
| Kansas City | Missouri | Cass | 40 | 3921 | 51 | 54 | 56 |
| St. Louis-Farmington | Illinois | Clinton | 62 | 3453 | 49 | 51 | 50 |
| St. Louis-Farmington | Illinois | Macoupin | 21 | 2385 | 47 | 53 | 50 |
| Springfield | Missouri | Christian | 24 | 3915 | 46 | 45 | 47 |
| St. Louis-Farmington | Missouri | St. Francois | 47 | 5194 | 46 | 62 | 68 |
| Kansas City | Kansas | Leavenworth | 32 | 3895 | 40 | 42 | 38 |
| St. Louis-Farmington | Missouri | Lincoln | 13 | 2540 | 33 | 40 | 40 |
| Missouri non-MSA | Missouri | Taney | 40 | 2941 | 33 | 35 | 34 |
| Columbia-Jefferson City | Missouri | Callaway | 11 | 2925 | 33 | 36 | 47 |
| Cape Girardeau-Sikeston | Missouri | Scott | 38 | 2739 | 30 | 38 | 38 |
| St. Louis-Farmington | Illinois | Monroe | 48 | 2167 | 30 | 36 | 36 |
| Missouri non-MSA | Missouri | Phelps | 49 | 1834 | 28 | 33 | 29 |
| St. Louis-Farmington | Illinois | Jersey | 24 | 1361 | 24 | 25 | 28 |
| Missouri non-MSA | Missouri | Johnson | 16 | 2582 | 24 | 29 | 32 |
| Missouri non-MSA | Missouri | Butler | 9 | 2232 | 22 | 30 | 27 |
| Kansas City | Missouri | Platte | 17 | 1741 | 22 | 24 | 22 |
| Missouri non-MSA | Missouri | Marion | 18 | 1832 | 21 | 23 | 26 |
| Missouri non-MSA | Missouri | Pulaski | 23 | 1673 | 21 | 22 | 19 |
| Missouri non-MSA | Missouri | Camden | 49 | 2520 | 21 | 26 | 27 |
| Missouri non-MSA | Missouri | Laclede | 32 | 1870 | 21 | 21 | 19 |
| Kansas City | Missouri | Lafayette | 30 | 1581 | 19 | 21 | 21 |
| Missouri non-MSA | Missouri | Lawrence | 39 | 1963 | 18 | 20 | 24 |
| St. Louis-Farmington | Illinois | Bond | 10 | 1108 | 18 | 17 | 18 |
| Missouri non-MSA | Missouri | Nodaway | 13 | 2037 | 18 | 20 | 25 |
| Missouri non-MSA | Missouri | Stoddard | 23 | 1678 | 17 | 22 | 23 |
| Kansas City | Kansas | Miami | 3 | 1091 | 17 | 19 | 16 |
| Missouri non-MSA | Missouri | Washington | 22 | 1490 | 16 | 21 | 24 |
| Missouri non-MSA | Missouri | Audrain | 14 | 1125 | 16 | 16 | 15 |
| St. Louis-Farmington | Missouri | Warren | 3 | 1256 | 15 | 19 | 19 |
| Missouri non-MSA | Missouri | Miller | 26 | 1546 | 15 | 17 | 18 |
| Missouri non-MSA | Missouri | Pike | 9 | 958 | 14 | 17 | 18 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1726 | 13 | 13 | 17 |
| Missouri non-MSA | Missouri | New Madrid | 24 | 1384 | 13 | 15 | 18 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1104 | 13 | 16 | 20 |
| Missouri non-MSA | Missouri | Stone | 18 | 1226 | 13 | 13 | 15 |
| Springfield | Missouri | Webster | 25 | 1850 | 13 | 18 | 19 |
| Missouri non-MSA | Missouri | Crawford | 14 | 1228 | 13 | 15 | 17 |
| Missouri non-MSA | Missouri | Randolph | 8 | 1239 | 12 | 14 | 18 |
| Missouri non-MSA | Missouri | Henry | 11 | 1119 | 12 | 17 | 21 |
| Missouri non-MSA | Missouri | Saline | 12 | 1610 | 12 | 16 | 19 |
| Missouri non-MSA | Missouri | Barry | 27 | 1480 | 12 | 14 | 17 |
| Joplin | Missouri | Newton | 38 | 3012 | 12 | 24 | 27 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1264 | 11 | 13 | 18 |
| Missouri non-MSA | Missouri | Mississippi | 7 | 903 | 11 | 17 | 14 |
| St. Joseph | Kansas | Doniphan | 2 | 534 | 11 | 12 | 10 |
| Springfield | Missouri | Polk | 12 | 1415 | 11 | 10 | 10 |
| Kansas City | Missouri | Ray | 5 | 728 | 11 | 10 | 13 |
| St. Joseph | Missouri | Andrew | 10 | 836 | 10 | 12 | 11 |
| Missouri non-MSA | Missouri | Madison | 9 | 912 | 10 | 13 | 11 |
| Missouri non-MSA | Missouri | Perry | 12 | 1570 | 10 | 16 | 22 |
| Missouri non-MSA | Missouri | Adair | 3 | 1110 | 10 | 13 | 17 |
| Missouri non-MSA | Missouri | Pemiscot | 19 | 1109 | 9 | 9 | 11 |
| Missouri non-MSA | Missouri | Pettis | 36 | 2700 | 9 | 13 | 28 |
| Kansas City | Missouri | Clinton | 46 | 913 | 9 | 9 | 11 |
| Missouri non-MSA | Missouri | Macon | 3 | 699 | 9 | 15 | 14 |
| Missouri non-MSA | Missouri | Ripley | 8 | 550 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Morgan | 12 | 1089 | 8 | 10 | 10 |
| Columbia-Jefferson City | Missouri | Cooper | 8 | 1187 | 8 | 11 | 16 |
| Columbia-Jefferson City | Missouri | Osage | 4 | 958 | 7 | 10 | 12 |
| Missouri non-MSA | Missouri | Ralls | 2 | 496 | 7 | 9 | 9 |
| St. Joseph | Missouri | DeKalb | 13 | 610 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 495 | 7 | 7 | 6 |
| Kansas City | Kansas | Linn | 1 | 324 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Dent | 4 | 531 | 7 | 9 | 8 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 516 | 6 | 8 | 8 |
| Missouri non-MSA | Missouri | Douglas | 15 | 450 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Howell | 30 | 1607 | 6 | 9 | 10 |
| Missouri non-MSA | Missouri | Vernon | 9 | 689 | 6 | 8 | 10 |
| Kansas City | Missouri | Bates | 9 | 557 | 6 | 10 | 9 |
| Missouri non-MSA | Missouri | Texas | 9 | 973 | 6 | 7 | 10 |
| Missouri non-MSA | Missouri | Benton | 9 | 785 | 6 | 5 | 9 |
| Missouri non-MSA | Missouri | Livingston | 16 | 792 | 5 | 7 | 6 |
| Kansas City | Missouri | Caldwell | 3 | 405 | 5 | 6 | 7 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 266 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Wright | 14 | 784 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 345 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Gentry | 13 | 428 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Monroe | 3 | 401 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Wayne | 3 | 509 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Carroll | 6 | 442 | 4 | 7 | 7 |
| Missouri non-MSA | Missouri | McDonald | 16 | 1417 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Shelby | 1 | 220 | 4 | 3 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 8 | 812 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Harrison | 3 | 408 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Putnam | 1 | 167 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Linn | 11 | 329 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Grundy | 14 | 515 | 3 | 6 | 7 |
| Missouri non-MSA | Missouri | Daviess | 8 | 346 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Oregon | 1 | 387 | 3 | 3 | 4 |
| Springfield | Missouri | Dallas | 10 | 610 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Maries | 4 | 376 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 354 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Barton | 5 | 638 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Sullivan | 6 | 572 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Chariton | 0 | 249 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Hickory | 6 | 376 | 2 | 3 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 4 | 266 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Iron | 1 | 242 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 184 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 3 | 298 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Clark | 4 | 303 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Carter | 6 | 300 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Dade | 8 | 295 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Scotland | 1 | 192 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Atchison | 3 | 214 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Holt | 3 | 270 | 1 | 4 | 4 |
| Missouri non-MSA | Missouri | Cedar | 7 | 447 | 1 | 3 | 6 |
| Missouri non-MSA | Missouri | Shannon | 9 | 340 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 75 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 134 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Lewis | 2 | 433 | 1 | 3 | 6 |
| Missouri non-MSA | Missouri | Mercer | 1 | 88 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 135 | 0 | 1 | 2 |
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
