# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/12/2020  
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
| St. Louis-Farmington | 2034 | 105528 | 2034 | 1590 | 1149 |
| Kansas City | 998 | 73879 | 1253 | 1019 | 759 |
| Missouri non-MSA | 702 | 51357 | 978 | 831 | 676 |
| Columbia-Jefferson City | 81 | 17077 | 405 | 337 | 250 |
| Springfield | 212 | 17011 | 234 | 221 | 182 |
| Cape Girardeau-Sikeston | 98 | 6264 | 130 | 106 | 80 |
| Joplin | 117 | 8861 | 127 | 106 | 89 |
| St. Joseph | 64 | 4861 | 82 | 65 | 57 |
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
| St. Louis-Farmington | Missouri | St. Louis | 904 | 37658 | 611 | 506 | 371 |
| Kansas City | Kansas | Johnson | 238 | 19808 | 395 | 320 | 229 |
| St. Louis-Farmington | Missouri | St. Charles | 164 | 14210 | 286 | 232 | 184 |
| Kansas City | Missouri | Kansas City | 241 | 17845 | 279 | 233 | 158 |
| St. Louis-Farmington | Illinois | Madison | 173 | 9951 | 263 | 184 | 118 |
| Kansas City | Missouri | Jackson | 151 | 12717 | 245 | 183 | 146 |
| St. Louis-Farmington | Missouri | Jefferson | 94 | 7549 | 173 | 136 | 90 |
| Columbia-Jefferson City | Missouri | Boone | 15 | 7819 | 169 | 123 | 85 |
| St. Louis-Farmington | Illinois | St. Clair | 243 | 9796 | 168 | 121 | 84 |
| Springfield | Missouri | Greene | 155 | 11020 | 149 | 137 | 109 |
| St. Louis-Farmington | Missouri | St. Louis City | 230 | 9917 | 116 | 102 | 77 |
| Columbia-Jefferson City | Missouri | Cole | 34 | 4412 | 107 | 100 | 77 |
| Joplin | Missouri | Jasper | 91 | 6437 | 101 | 79 | 59 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 58 | 3594 | 85 | 64 | 45 |
| Kansas City | Kansas | Wyandotte | 167 | 9498 | 79 | 72 | 59 |
| St. Louis-Farmington | Missouri | St. Francois | 36 | 3722 | 73 | 59 | 41 |
| St. Louis-Farmington | Missouri | Franklin | 57 | 3553 | 70 | 59 | 49 |
| Kansas City | Missouri | Clay | 54 | 3351 | 67 | 55 | 45 |
| St. Joseph | Missouri | Buchanan | 46 | 3598 | 59 | 43 | 38 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 2018 | 58 | 54 | 38 |
| Missouri non-MSA | Missouri | Pettis | 28 | 2274 | 57 | 46 | 32 |
| St. Louis-Farmington | Illinois | Macoupin | 14 | 1300 | 54 | 33 | 21 |
| St. Louis-Farmington | Illinois | Clinton | 39 | 2368 | 54 | 38 | 31 |
| Kansas City | Missouri | Cass | 35 | 2655 | 49 | 40 | 30 |
| Springfield | Missouri | Christian | 20 | 2911 | 46 | 42 | 35 |
| St. Louis-Farmington | Illinois | Jersey | 22 | 809 | 41 | 23 | 12 |
| St. Louis-Farmington | Illinois | Monroe | 40 | 1381 | 38 | 29 | 19 |
| St. Louis-Farmington | Missouri | Lincoln | 7 | 1629 | 36 | 28 | 22 |
| Missouri non-MSA | Missouri | Johnson | 11 | 1927 | 36 | 30 | 21 |
| Cape Girardeau-Sikeston | Missouri | Scott | 33 | 1855 | 33 | 30 | 24 |
| Kansas City | Kansas | Leavenworth | 25 | 3010 | 33 | 25 | 19 |
| Missouri non-MSA | Missouri | Taney | 36 | 2172 | 32 | 30 | 23 |
| Missouri non-MSA | Missouri | Washington | 20 | 977 | 30 | 21 | 14 |
| Missouri non-MSA | Missouri | Lawrence | 32 | 1459 | 29 | 23 | 21 |
| Missouri non-MSA | Missouri | Perry | 8 | 1108 | 28 | 21 | 13 |
| Missouri non-MSA | Missouri | Camden | 41 | 1942 | 28 | 23 | 21 |
| Missouri non-MSA | Missouri | Marion | 15 | 1270 | 27 | 23 | 16 |
| Joplin | Missouri | Newton | 26 | 2424 | 26 | 27 | 30 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 697 | 25 | 20 | 14 |
| Columbia-Jefferson City | Missouri | Cooper | 6 | 881 | 24 | 18 | 12 |
| St. Louis-Farmington | Illinois | Bond | 9 | 748 | 24 | 16 | 12 |
| Missouri non-MSA | Missouri | Henry | 8 | 645 | 24 | 18 | 11 |
| Columbia-Jefferson City | Missouri | Moniteau | 14 | 918 | 24 | 20 | 17 |
| Kansas City | Missouri | Lafayette | 27 | 1140 | 23 | 20 | 15 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1513 | 23 | 26 | 20 |
| Missouri non-MSA | Missouri | Phelps | 33 | 1114 | 22 | 18 | 17 |
| Missouri non-MSA | Missouri | Miller | 20 | 1165 | 21 | 19 | 17 |
| Missouri non-MSA | Missouri | Butler | 8 | 1591 | 21 | 24 | 25 |
| Missouri non-MSA | Missouri | Saline | 11 | 1203 | 21 | 17 | 11 |
| Missouri non-MSA | Missouri | Adair | 0 | 751 | 21 | 15 | 11 |
| Missouri non-MSA | Missouri | Stoddard | 17 | 1125 | 20 | 16 | 15 |
| Missouri non-MSA | Missouri | Laclede | 28 | 1449 | 20 | 16 | 17 |
| Kansas City | Missouri | Platte | 13 | 1240 | 20 | 16 | 14 |
| Missouri non-MSA | Missouri | Barry | 19 | 1102 | 19 | 18 | 17 |
| Springfield | Missouri | Webster | 23 | 1427 | 19 | 18 | 16 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1371 | 18 | 16 | 14 |
| Missouri non-MSA | Missouri | Pike | 8 | 544 | 18 | 13 | 8 |
| Kansas City | Missouri | Ray | 2 | 474 | 17 | 13 | 8 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 985 | 17 | 14 | 11 |
| Missouri non-MSA | Missouri | Crawford | 10 | 852 | 17 | 14 | 12 |
| Missouri non-MSA | Missouri | Randolph | 4 | 829 | 15 | 14 | 13 |
| Missouri non-MSA | Missouri | Vernon | 3 | 494 | 15 | 10 | 7 |
| St. Louis-Farmington | Missouri | Warren | 2 | 802 | 15 | 11 | 9 |
| Missouri non-MSA | Missouri | Stone | 13 | 896 | 15 | 13 | 10 |
| Missouri non-MSA | Missouri | Texas | 6 | 770 | 15 | 12 | 10 |
| Missouri non-MSA | Missouri | Pulaski | 13 | 1211 | 14 | 13 | 13 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 693 | 14 | 14 | 14 |
| Missouri non-MSA | Missouri | Audrain | 11 | 777 | 13 | 13 | 9 |
| Missouri non-MSA | Missouri | Pemiscot | 15 | 879 | 13 | 10 | 8 |
| Missouri non-MSA | Missouri | Macon | 1 | 368 | 13 | 10 | 6 |
| Kansas City | Kansas | Miami | 2 | 712 | 13 | 10 | 8 |
| Missouri non-MSA | Missouri | Morgan | 8 | 858 | 12 | 12 | 12 |
| Missouri non-MSA | Missouri | Benton | 7 | 597 | 11 | 8 | 5 |
| Kansas City | Missouri | Clinton | 33 | 667 | 11 | 11 | 11 |
| Missouri non-MSA | Missouri | Madison | 7 | 633 | 11 | 8 | 8 |
| Springfield | Missouri | Polk | 11 | 1182 | 10 | 14 | 13 |
| Missouri non-MSA | Missouri | Howell | 21 | 1385 | 10 | 14 | 16 |
| Missouri non-MSA | Missouri | Lewis | 2 | 320 | 10 | 8 | 5 |
| St. Joseph | Missouri | Andrew | 8 | 557 | 9 | 7 | 7 |
| Missouri non-MSA | Missouri | Ripley | 5 | 369 | 9 | 6 | 6 |
| Missouri non-MSA | Missouri | Monroe | 3 | 260 | 9 | 6 | 5 |
| Missouri non-MSA | Missouri | Chariton | 0 | 142 | 8 | 5 | 2 |
| Missouri non-MSA | Missouri | Ralls | 1 | 288 | 8 | 5 | 4 |
| Missouri non-MSA | Missouri | Gentry | 11 | 272 | 8 | 6 | 4 |
| Missouri non-MSA | Missouri | Clark | 2 | 192 | 7 | 5 | 3 |
| Kansas City | Missouri | Bates | 8 | 335 | 7 | 5 | 4 |
| Springfield | Missouri | Dallas | 3 | 471 | 7 | 7 | 7 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 5 | 624 | 7 | 8 | 7 |
| St. Joseph | Kansas | Doniphan | 2 | 287 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Carroll | 4 | 284 | 7 | 6 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 336 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 4 | 447 | 7 | 9 | 6 |
| Missouri non-MSA | Missouri | Barton | 4 | 510 | 7 | 5 | 6 |
| Missouri non-MSA | Missouri | Grundy | 12 | 345 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Cedar | 4 | 321 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 182 | 6 | 4 | 3 |
| Kansas City | Missouri | Caldwell | 1 | 247 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 349 | 6 | 6 | 5 |
| St. Joseph | Missouri | DeKalb | 8 | 419 | 6 | 8 | 7 |
| Missouri non-MSA | Missouri | Dade | 5 | 206 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 540 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Wayne | 3 | 388 | 6 | 5 | 4 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 135 | 5 | 5 | 2 |
| Missouri non-MSA | Missouri | Holt | 2 | 172 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Dent | 4 | 325 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Linn | 10 | 219 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Maries | 1 | 267 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Hickory | 4 | 300 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Oregon | 0 | 298 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Harrison | 1 | 242 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 92 | 5 | 3 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 191 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Livingston | 9 | 626 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Wright | 11 | 663 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Montgomery | 5 | 238 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Scotland | 1 | 115 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Douglas | 14 | 345 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Shelby | 1 | 142 | 4 | 2 | 1 |
| Kansas City | Kansas | Linn | 1 | 180 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Daviess | 5 | 268 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | McDonald | 15 | 1296 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Iron | 0 | 150 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Atchison | 1 | 115 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 122 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Shannon | 7 | 300 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Knox | 1 | 90 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 4 | 213 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 1 | 245 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Mercer | 0 | 50 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 78 | 1 | 1 | 1 |
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
