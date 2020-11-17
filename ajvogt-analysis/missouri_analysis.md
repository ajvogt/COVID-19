# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/17/2020  
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
| St. Louis-Farmington | 2086 | 117532 | 2386 | 2045 | 1428 |
| Kansas City | 1026 | 80742 | 1409 | 1222 | 898 |
| Missouri non-MSA | 715 | 57231 | 1081 | 987 | 769 |
| Columbia-Jefferson City | 83 | 19255 | 409 | 395 | 287 |
| Springfield | 215 | 18307 | 257 | 234 | 195 |
| Joplin | 133 | 9685 | 161 | 134 | 101 |
| Cape Girardeau-Sikeston | 99 | 6999 | 150 | 127 | 94 |
| St. Joseph | 66 | 5262 | 86 | 79 | 59 |
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
| St. Louis-Farmington | Missouri | St. Louis | 917 | 42043 | 838 | 681 | 481 |
| Kansas City | Kansas | Johnson | 248 | 21981 | 456 | 389 | 285 |
| St. Louis-Farmington | Missouri | St. Charles | 169 | 15818 | 311 | 284 | 211 |
| Kansas City | Missouri | Kansas City | 244 | 19360 | 304 | 269 | 195 |
| St. Louis-Farmington | Illinois | Madison | 184 | 11271 | 272 | 241 | 152 |
| Kansas City | Missouri | Jackson | 155 | 13966 | 256 | 227 | 162 |
| St. Louis-Farmington | Missouri | Jefferson | 94 | 8446 | 189 | 165 | 112 |
| St. Louis-Farmington | Illinois | St. Clair | 245 | 10692 | 183 | 159 | 107 |
| Columbia-Jefferson City | Missouri | Boone | 15 | 8743 | 171 | 162 | 105 |
| St. Louis-Farmington | Missouri | St. Louis City | 230 | 10792 | 168 | 135 | 97 |
| Springfield | Missouri | Greene | 158 | 11828 | 164 | 147 | 119 |
| Joplin | Missouri | Jasper | 98 | 7078 | 125 | 104 | 76 |
| Columbia-Jefferson City | Missouri | Cole | 36 | 5026 | 113 | 108 | 86 |
| Kansas City | Kansas | Wyandotte | 167 | 9964 | 97 | 79 | 68 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 58 | 4012 | 89 | 78 | 53 |
| St. Louis-Farmington | Missouri | St. Francois | 36 | 4156 | 83 | 73 | 52 |
| St. Louis-Farmington | Missouri | Franklin | 58 | 3917 | 76 | 65 | 54 |
| Kansas City | Missouri | Clay | 58 | 3746 | 75 | 67 | 48 |
| Kansas City | Missouri | Cass | 35 | 2956 | 60 | 51 | 36 |
| St. Joseph | Missouri | Buchanan | 47 | 3843 | 56 | 51 | 38 |
| St. Louis-Farmington | Illinois | Macoupin | 16 | 1518 | 53 | 45 | 26 |
| St. Louis-Farmington | Illinois | Clinton | 52 | 2579 | 53 | 45 | 34 |
| Springfield | Missouri | Christian | 20 | 3176 | 50 | 48 | 37 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 2280 | 48 | 55 | 42 |
| Cape Girardeau-Sikeston | Missouri | Scott | 33 | 2074 | 43 | 34 | 28 |
| St. Louis-Farmington | Missouri | Lincoln | 7 | 1858 | 42 | 37 | 27 |
| Kansas City | Kansas | Leavenworth | 26 | 3208 | 42 | 33 | 24 |
| St. Louis-Farmington | Illinois | Monroe | 43 | 1597 | 41 | 36 | 25 |
| Joplin | Missouri | Newton | 35 | 2607 | 35 | 29 | 24 |
| Missouri non-MSA | Missouri | Camden | 43 | 2104 | 34 | 29 | 22 |
| Missouri non-MSA | Missouri | Johnson | 11 | 2098 | 34 | 34 | 23 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1719 | 33 | 31 | 24 |
| Missouri non-MSA | Missouri | Pettis | 28 | 2465 | 32 | 44 | 36 |
| Missouri non-MSA | Missouri | Washington | 21 | 1157 | 32 | 29 | 19 |
| Missouri non-MSA | Missouri | Taney | 36 | 2349 | 32 | 30 | 27 |
| Missouri non-MSA | Missouri | Phelps | 34 | 1310 | 31 | 25 | 18 |
| Missouri non-MSA | Missouri | Perry | 8 | 1268 | 30 | 27 | 17 |
| Missouri non-MSA | Missouri | Lawrence | 32 | 1618 | 29 | 28 | 22 |
| Missouri non-MSA | Missouri | Henry | 8 | 824 | 29 | 25 | 16 |
| Columbia-Jefferson City | Missouri | Moniteau | 14 | 1038 | 29 | 22 | 18 |
| Missouri non-MSA | Missouri | Marion | 15 | 1424 | 28 | 28 | 20 |
| Missouri non-MSA | Missouri | Butler | 8 | 1740 | 27 | 24 | 24 |
| Missouri non-MSA | Missouri | Randolph | 4 | 997 | 26 | 22 | 17 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 841 | 26 | 24 | 18 |
| Missouri non-MSA | Missouri | Stoddard | 17 | 1242 | 26 | 19 | 16 |
| Missouri non-MSA | Missouri | Adair | 0 | 876 | 25 | 21 | 14 |
| St. Louis-Farmington | Illinois | Jersey | 23 | 943 | 25 | 31 | 16 |
| Missouri non-MSA | Missouri | Saline | 12 | 1340 | 25 | 22 | 15 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 1129 | 25 | 21 | 14 |
| Missouri non-MSA | Missouri | Pike | 8 | 681 | 24 | 19 | 13 |
| St. Louis-Farmington | Missouri | Warren | 2 | 921 | 22 | 17 | 11 |
| Columbia-Jefferson City | Missouri | Cooper | 6 | 1000 | 22 | 22 | 14 |
| Missouri non-MSA | Missouri | Barry | 19 | 1223 | 21 | 20 | 17 |
| Springfield | Missouri | Webster | 23 | 1531 | 21 | 19 | 17 |
| Kansas City | Missouri | Platte | 14 | 1332 | 20 | 18 | 14 |
| Missouri non-MSA | Missouri | Crawford | 10 | 983 | 20 | 18 | 15 |
| Kansas City | Missouri | Lafayette | 27 | 1234 | 20 | 21 | 16 |
| Missouri non-MSA | Missouri | Miller | 21 | 1271 | 19 | 20 | 17 |
| St. Louis-Farmington | Illinois | Bond | 10 | 818 | 18 | 19 | 12 |
| Missouri non-MSA | Missouri | Laclede | 28 | 1542 | 18 | 19 | 16 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1477 | 18 | 19 | 16 |
| Missouri non-MSA | Missouri | Audrain | 11 | 865 | 17 | 14 | 11 |
| Missouri non-MSA | Missouri | Stone | 13 | 988 | 17 | 15 | 12 |
| Kansas City | Missouri | Ray | 2 | 557 | 16 | 16 | 10 |
| Missouri non-MSA | Missouri | Pulaski | 14 | 1311 | 16 | 15 | 14 |
| Missouri non-MSA | Missouri | Macon | 1 | 454 | 15 | 14 | 8 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 623 | 15 | 11 | 8 |
| Kansas City | Kansas | Miami | 2 | 786 | 15 | 13 | 9 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 777 | 15 | 14 | 13 |
| Kansas City | Missouri | Clinton | 38 | 744 | 14 | 12 | 11 |
| Missouri non-MSA | Missouri | Pemiscot | 15 | 947 | 13 | 12 | 9 |
| Missouri non-MSA | Missouri | Texas | 6 | 839 | 13 | 13 | 10 |
| Missouri non-MSA | Missouri | Benton | 7 | 678 | 13 | 11 | 7 |
| Missouri non-MSA | Missouri | Howell | 22 | 1449 | 13 | 11 | 15 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 6 | 696 | 12 | 9 | 8 |
| Missouri non-MSA | Missouri | Madison | 7 | 702 | 12 | 10 | 9 |
| Kansas City | Missouri | Bates | 8 | 397 | 12 | 8 | 5 |
| Springfield | Missouri | Polk | 11 | 1247 | 12 | 11 | 12 |
| St. Joseph | Missouri | Andrew | 8 | 623 | 12 | 10 | 7 |
| Missouri non-MSA | Missouri | Morgan | 8 | 924 | 12 | 11 | 12 |
| Missouri non-MSA | Missouri | Grundy | 12 | 413 | 11 | 9 | 6 |
| Missouri non-MSA | Missouri | Vernon | 4 | 546 | 11 | 12 | 8 |
| Missouri non-MSA | Missouri | Ripley | 5 | 424 | 11 | 9 | 7 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 247 | 10 | 8 | 4 |
| St. Joseph | Kansas | Doniphan | 2 | 344 | 10 | 8 | 5 |
| Missouri non-MSA | Missouri | Cedar | 4 | 369 | 10 | 7 | 5 |
| Missouri non-MSA | Missouri | Ralls | 1 | 338 | 10 | 8 | 5 |
| Missouri non-MSA | Missouri | Barton | 4 | 561 | 9 | 7 | 5 |
| Missouri non-MSA | Missouri | Gentry | 11 | 324 | 9 | 8 | 5 |
| Springfield | Missouri | Dallas | 3 | 525 | 9 | 8 | 8 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 391 | 9 | 8 | 5 |
| Missouri non-MSA | Missouri | Harrison | 1 | 303 | 9 | 7 | 4 |
| Missouri non-MSA | Missouri | Lewis | 2 | 368 | 9 | 9 | 6 |
| Missouri non-MSA | Missouri | Dent | 4 | 377 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Monroe | 3 | 295 | 8 | 7 | 5 |
| Kansas City | Missouri | Caldwell | 1 | 294 | 8 | 7 | 4 |
| Missouri non-MSA | Missouri | Chariton | 0 | 181 | 8 | 7 | 4 |
| Missouri non-MSA | Missouri | Livingston | 10 | 678 | 8 | 6 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 5 | 484 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Dade | 5 | 244 | 7 | 6 | 3 |
| Kansas City | Kansas | Linn | 1 | 217 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Clark | 2 | 226 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Carroll | 4 | 318 | 6 | 6 | 5 |
| St. Joseph | Missouri | DeKalb | 9 | 452 | 6 | 9 | 7 |
| Missouri non-MSA | Missouri | Atchison | 1 | 153 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Linn | 10 | 254 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 378 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Wright | 11 | 691 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Maries | 1 | 296 | 5 | 5 | 5 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 163 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Wayne | 3 | 406 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Hickory | 4 | 329 | 5 | 5 | 5 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 217 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Scotland | 1 | 135 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 161 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 172 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | McDonald | 15 | 1319 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Oregon | 0 | 320 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 5 | 265 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Putnam | 1 | 96 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Carter | 4 | 234 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 5 | 288 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Holt | 2 | 192 | 3 | 4 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 110 | 3 | 4 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 136 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 14 | 358 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Knox | 1 | 104 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Shannon | 9 | 314 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Ozark | 1 | 257 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 50 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 59 | 1 | 1 | 0 |
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
