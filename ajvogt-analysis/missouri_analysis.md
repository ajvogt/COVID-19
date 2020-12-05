# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/05/2020  
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
| St. Louis-Farmington | 2532 | 156592 | 1940 | 2095 | 2176 |
| Kansas City | 1235 | 104729 | 1181 | 1252 | 1320 |
| Missouri non-MSA | 932 | 73049 | 733 | 814 | 951 |
| Columbia-Jefferson City | 125 | 24418 | 227 | 263 | 339 |
| Springfield | 262 | 22677 | 220 | 234 | 243 |
| Cape Girardeau-Sikeston | 119 | 9241 | 99 | 109 | 129 |
| St. Joseph | 94 | 7036 | 89 | 98 | 91 |
| Joplin | 159 | 11611 | 71 | 92 | 121 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1084 | 54376 | 620 | 677 | 700 |
| Kansas City | Kansas | Johnson | 299 | 29272 | 363 | 384 | 407 |
| St. Louis-Farmington | Missouri | St. Charles | 219 | 21310 | 259 | 284 | 303 |
| Kansas City | Missouri | Kansas City | 302 | 24453 | 244 | 271 | 285 |
| St. Louis-Farmington | Illinois | Madison | 271 | 15643 | 232 | 232 | 251 |
| Kansas City | Missouri | Jackson | 186 | 18369 | 222 | 225 | 245 |
| St. Louis-Farmington | Illinois | St. Clair | 274 | 14442 | 212 | 213 | 194 |
| St. Louis-Farmington | Missouri | Jefferson | 108 | 11788 | 150 | 173 | 181 |
| St. Louis-Farmington | Missouri | St. Louis City | 255 | 13600 | 137 | 157 | 149 |
| Springfield | Missouri | Greene | 190 | 14628 | 137 | 149 | 155 |
| Kansas City | Kansas | Wyandotte | 184 | 12096 | 97 | 111 | 105 |
| Columbia-Jefferson City | Missouri | Boone | 25 | 10834 | 92 | 103 | 140 |
| Columbia-Jefferson City | Missouri | Cole | 60 | 6529 | 64 | 78 | 95 |
| St. Joseph | Missouri | Buchanan | 66 | 4995 | 63 | 64 | 60 |
| Joplin | Missouri | Jasper | 121 | 8569 | 60 | 72 | 94 |
| Kansas City | Missouri | Cass | 40 | 4060 | 57 | 55 | 58 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 65 | 5311 | 56 | 64 | 77 |
| Kansas City | Missouri | Clay | 76 | 4886 | 53 | 55 | 66 |
| St. Louis-Farmington | Missouri | Franklin | 86 | 5102 | 52 | 61 | 68 |
| Springfield | Missouri | Christian | 24 | 4053 | 50 | 48 | 48 |
| St. Louis-Farmington | Illinois | Macoupin | 25 | 2467 | 50 | 45 | 51 |
| St. Louis-Farmington | Illinois | Clinton | 63 | 3557 | 44 | 48 | 52 |
| St. Louis-Farmington | Missouri | St. Francois | 47 | 5282 | 42 | 55 | 69 |
| Kansas City | Kansas | Leavenworth | 32 | 4001 | 38 | 42 | 40 |
| St. Louis-Farmington | Missouri | Lincoln | 13 | 2634 | 34 | 40 | 42 |
| Missouri non-MSA | Missouri | Taney | 39 | 3042 | 34 | 37 | 36 |
| Columbia-Jefferson City | Missouri | Callaway | 11 | 3019 | 34 | 37 | 47 |
| Cape Girardeau-Sikeston | Missouri | Scott | 42 | 2816 | 32 | 35 | 39 |
| St. Louis-Farmington | Illinois | Monroe | 48 | 2241 | 31 | 37 | 37 |
| Missouri non-MSA | Missouri | Phelps | 51 | 1919 | 30 | 33 | 32 |
| St. Louis-Farmington | Illinois | Jersey | 24 | 1410 | 28 | 24 | 29 |
| Missouri non-MSA | Missouri | Pulaski | 24 | 1768 | 27 | 25 | 22 |
| Missouri non-MSA | Missouri | Butler | 9 | 2299 | 27 | 29 | 28 |
| Missouri non-MSA | Missouri | Laclede | 32 | 1952 | 25 | 22 | 21 |
| Kansas City | Missouri | Platte | 17 | 1788 | 24 | 23 | 23 |
| Missouri non-MSA | Missouri | Johnson | 16 | 2635 | 23 | 26 | 32 |
| Missouri non-MSA | Missouri | Camden | 49 | 2579 | 23 | 23 | 27 |
| Missouri non-MSA | Missouri | Marion | 18 | 1894 | 22 | 24 | 27 |
| St. Louis-Farmington | Illinois | Bond | 11 | 1175 | 22 | 19 | 19 |
| Missouri non-MSA | Missouri | Miller | 26 | 1602 | 18 | 16 | 19 |
| Missouri non-MSA | Missouri | Pettis | 36 | 2782 | 18 | 18 | 30 |
| Kansas City | Kansas | Miami | 3 | 1143 | 18 | 19 | 17 |
| Missouri non-MSA | Missouri | Nodaway | 13 | 2076 | 18 | 19 | 24 |
| Kansas City | Missouri | Lafayette | 30 | 1617 | 18 | 20 | 21 |
| Missouri non-MSA | Missouri | Pike | 10 | 1004 | 17 | 16 | 19 |
| Missouri non-MSA | Missouri | Stoddard | 24 | 1712 | 16 | 21 | 24 |
| Missouri non-MSA | Missouri | Lawrence | 39 | 1997 | 16 | 18 | 24 |
| Missouri non-MSA | Missouri | Washington | 22 | 1522 | 16 | 19 | 25 |
| Springfield | Missouri | Webster | 26 | 1912 | 15 | 19 | 20 |
| Missouri non-MSA | Missouri | Audrain | 15 | 1164 | 14 | 17 | 16 |
| St. Louis-Farmington | Missouri | Warren | 3 | 1285 | 14 | 18 | 19 |
| Missouri non-MSA | Missouri | Stone | 19 | 1265 | 14 | 14 | 15 |
| Springfield | Missouri | Polk | 12 | 1466 | 14 | 12 | 12 |
| Missouri non-MSA | Missouri | Randolph | 9 | 1278 | 13 | 14 | 18 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1137 | 13 | 16 | 20 |
| Missouri non-MSA | Missouri | Crawford | 14 | 1262 | 13 | 14 | 17 |
| Kansas City | Missouri | Clinton | 47 | 951 | 12 | 10 | 12 |
| Missouri non-MSA | Missouri | Barry | 29 | 1519 | 12 | 13 | 18 |
| Missouri non-MSA | Missouri | Perry | 12 | 1608 | 12 | 16 | 23 |
| Kansas City | Missouri | Ray | 6 | 758 | 12 | 11 | 13 |
| St. Joseph | Missouri | Andrew | 11 | 870 | 12 | 13 | 12 |
| Missouri non-MSA | Missouri | Henry | 12 | 1153 | 12 | 15 | 22 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1295 | 12 | 13 | 18 |
| Missouri non-MSA | Missouri | Madison | 9 | 936 | 11 | 14 | 12 |
| Joplin | Missouri | Newton | 38 | 3042 | 11 | 19 | 26 |
| Missouri non-MSA | Missouri | Mississippi | 7 | 924 | 11 | 17 | 14 |
| Missouri non-MSA | Missouri | New Madrid | 24 | 1399 | 11 | 13 | 17 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1745 | 11 | 13 | 16 |
| Missouri non-MSA | Missouri | Morgan | 13 | 1129 | 11 | 11 | 11 |
| Missouri non-MSA | Missouri | Adair | 3 | 1140 | 11 | 11 | 17 |
| Columbia-Jefferson City | Missouri | Cooper | 8 | 1227 | 10 | 11 | 17 |
| Missouri non-MSA | Missouri | Vernon | 10 | 725 | 9 | 9 | 11 |
| Missouri non-MSA | Missouri | Saline | 12 | 1628 | 9 | 13 | 19 |
| Missouri non-MSA | Missouri | Howell | 31 | 1635 | 9 | 9 | 10 |
| Missouri non-MSA | Missouri | Pemiscot | 19 | 1132 | 9 | 9 | 11 |
| Missouri non-MSA | Missouri | Ripley | 8 | 565 | 9 | 8 | 8 |
| Columbia-Jefferson City | Missouri | Osage | 4 | 985 | 8 | 10 | 13 |
| Missouri non-MSA | Missouri | Texas | 10 | 1001 | 8 | 8 | 11 |
| Missouri non-MSA | Missouri | Benton | 11 | 812 | 8 | 7 | 9 |
| Missouri non-MSA | Missouri | Ralls | 2 | 514 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | Gasconade | 25 | 510 | 7 | 7 | 6 |
| St. Joseph | Missouri | DeKalb | 15 | 624 | 7 | 9 | 8 |
| Missouri non-MSA | Missouri | Gentry | 13 | 454 | 7 | 7 | 8 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 8 | 844 | 7 | 7 | 9 |
| Missouri non-MSA | Missouri | Macon | 3 | 709 | 7 | 11 | 14 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 280 | 7 | 5 | 6 |
| Missouri non-MSA | Missouri | Wright | 15 | 806 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Dent | 4 | 547 | 6 | 8 | 8 |
| Missouri non-MSA | Missouri | Carroll | 6 | 460 | 6 | 7 | 7 |
| Kansas City | Missouri | Bates | 9 | 581 | 6 | 9 | 10 |
| St. Joseph | Kansas | Doniphan | 2 | 547 | 6 | 11 | 10 |
| Kansas City | Kansas | Linn | 1 | 337 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Harrison | 3 | 431 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 366 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Grundy | 14 | 537 | 5 | 5 | 8 |
| Missouri non-MSA | Missouri | Wayne | 3 | 520 | 5 | 5 | 5 |
| Kansas City | Missouri | Caldwell | 3 | 417 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Livingston | 16 | 809 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | McDonald | 16 | 1430 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Daviess | 8 | 362 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Douglas | 15 | 455 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Monroe | 3 | 410 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Shelby | 1 | 229 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Oregon | 1 | 396 | 4 | 3 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 529 | 4 | 7 | 8 |
| Missouri non-MSA | Missouri | Maries | 4 | 386 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Linn | 11 | 338 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Barton | 5 | 650 | 3 | 4 | 6 |
| Springfield | Missouri | Dallas | 10 | 618 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Iron | 1 | 250 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Ozark | 3 | 306 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 6 | 312 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Chariton | 0 | 258 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Putnam | 1 | 167 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 360 | 2 | 5 | 5 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 4 | 270 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Holt | 4 | 278 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 6 | 574 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Atchison | 3 | 224 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Clark | 4 | 312 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Hickory | 6 | 380 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dade | 8 | 299 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 351 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 7 | 452 | 1 | 2 | 6 |
| Missouri non-MSA | Missouri | Lewis | 2 | 441 | 1 | 2 | 6 |
| Missouri non-MSA | Missouri | Scotland | 1 | 195 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 185 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 80 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 140 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 90 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 136 | 0 | 1 | 2 |
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
