# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/30/2020  
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
| St. Louis-Farmington | 3286 | 198115 | 1246 | 1445 | 1713 |
| Kansas City | 1559 | 132483 | 946 | 1033 | 1163 |
| Missouri non-MSA | 1343 | 90553 | 498 | 595 | 716 |
| Springfield | 377 | 28599 | 172 | 214 | 240 |
| Columbia-Jefferson City | 196 | 29048 | 154 | 177 | 197 |
| Joplin | 202 | 13180 | 58 | 62 | 66 |
| Cape Girardeau-Sikeston | 178 | 10929 | 47 | 56 | 72 |
| St. Joseph | 132 | 8484 | 36 | 44 | 65 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1356 | 68226 | 422 | 480 | 563 |
| Kansas City | Kansas | Johnson | 435 | 37875 | 271 | 337 | 371 |
| Kansas City | Missouri | Kansas City | 350 | 29643 | 177 | 184 | 214 |
| Kansas City | Missouri | Jackson | 235 | 23016 | 162 | 159 | 196 |
| St. Louis-Farmington | Missouri | St. Charles | 288 | 26741 | 155 | 191 | 225 |
| St. Louis-Farmington | Illinois | Madison | 384 | 20555 | 141 | 170 | 205 |
| Kansas City | Kansas | Wyandotte | 194 | 15206 | 129 | 117 | 126 |
| St. Louis-Farmington | Illinois | St. Clair | 343 | 18628 | 123 | 137 | 173 |
| Springfield | Missouri | Greene | 252 | 18419 | 114 | 136 | 153 |
| St. Louis-Farmington | Missouri | St. Louis City | 297 | 16801 | 100 | 114 | 128 |
| St. Louis-Farmington | Missouri | Jefferson | 132 | 14783 | 88 | 102 | 126 |
| Columbia-Jefferson City | Missouri | Boone | 44 | 13137 | 78 | 89 | 94 |
| Joplin | Missouri | Jasper | 157 | 9791 | 44 | 46 | 52 |
| Kansas City | Missouri | Clay | 97 | 6147 | 44 | 44 | 52 |
| Kansas City | Missouri | Cass | 54 | 5443 | 43 | 50 | 55 |
| St. Louis-Farmington | Missouri | Franklin | 113 | 6408 | 39 | 48 | 53 |
| St. Louis-Farmington | Missouri | St. Francois | 69 | 6411 | 36 | 41 | 44 |
| Springfield | Missouri | Christian | 48 | 5359 | 36 | 48 | 53 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 99 | 6361 | 31 | 37 | 44 |
| Columbia-Jefferson City | Missouri | Cole | 85 | 7491 | 30 | 34 | 44 |
| St. Louis-Farmington | Illinois | Monroe | 59 | 3044 | 27 | 30 | 32 |
| Kansas City | Kansas | Leavenworth | 38 | 4939 | 25 | 36 | 40 |
| Columbia-Jefferson City | Missouri | Callaway | 20 | 3697 | 24 | 26 | 29 |
| St. Louis-Farmington | Illinois | Clinton | 80 | 4381 | 24 | 28 | 35 |
| Missouri non-MSA | Missouri | Pulaski | 27 | 2512 | 22 | 24 | 29 |
| Kansas City | Kansas | Miami | 11 | 1725 | 22 | 22 | 23 |
| St. Joseph | Missouri | Buchanan | 94 | 5955 | 22 | 26 | 43 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3478 | 22 | 28 | 34 |
| Missouri non-MSA | Missouri | Pettis | 61 | 3978 | 22 | 29 | 43 |
| St. Louis-Farmington | Illinois | Macoupin | 77 | 3199 | 20 | 25 | 32 |
| Kansas City | Missouri | Platte | 22 | 2324 | 20 | 22 | 22 |
| Missouri non-MSA | Missouri | Phelps | 85 | 2424 | 19 | 20 | 21 |
| Missouri non-MSA | Missouri | Camden | 62 | 3084 | 18 | 19 | 21 |
| Missouri non-MSA | Missouri | Johnson | 29 | 3193 | 18 | 18 | 22 |
| St. Louis-Farmington | Illinois | Jersey | 39 | 1951 | 18 | 19 | 22 |
| Missouri non-MSA | Missouri | Crawford | 19 | 1666 | 17 | 17 | 15 |
| Missouri non-MSA | Missouri | Adair | 4 | 1573 | 15 | 18 | 16 |
| Missouri non-MSA | Missouri | Audrain | 32 | 1626 | 15 | 18 | 17 |
| Missouri non-MSA | Missouri | Taney | 52 | 3696 | 15 | 18 | 28 |
| Missouri non-MSA | Missouri | Howell | 37 | 2266 | 13 | 13 | 22 |
| Kansas City | Missouri | Lafayette | 40 | 2034 | 13 | 16 | 16 |
| Joplin | Missouri | Newton | 45 | 3389 | 13 | 15 | 13 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1611 | 13 | 12 | 13 |
| Springfield | Missouri | Webster | 38 | 2360 | 12 | 17 | 18 |
| Missouri non-MSA | Missouri | Butler | 14 | 2770 | 12 | 13 | 21 |
| Cape Girardeau-Sikeston | Missouri | Scott | 60 | 3286 | 12 | 14 | 21 |
| Missouri non-MSA | Missouri | Marion | 24 | 2304 | 11 | 12 | 17 |
| Missouri non-MSA | Missouri | Laclede | 44 | 2455 | 11 | 15 | 21 |
| Kansas City | Missouri | Ray | 8 | 1089 | 11 | 13 | 13 |
| Missouri non-MSA | Missouri | Saline | 23 | 1971 | 10 | 13 | 12 |
| Missouri non-MSA | Missouri | Randolph | 16 | 1585 | 10 | 10 | 13 |
| St. Louis-Farmington | Illinois | Bond | 16 | 1528 | 9 | 12 | 16 |
| Missouri non-MSA | Missouri | Madison | 10 | 1175 | 9 | 9 | 9 |
| Missouri non-MSA | Missouri | Miller | 41 | 1988 | 9 | 14 | 16 |
| Missouri non-MSA | Missouri | Dunklin | 15 | 2060 | 8 | 13 | 12 |
| Missouri non-MSA | Missouri | Texas | 17 | 1316 | 8 | 11 | 11 |
| Missouri non-MSA | Missouri | Pike | 14 | 1257 | 8 | 9 | 11 |
| Missouri non-MSA | Missouri | Washington | 39 | 1749 | 8 | 8 | 11 |
| Missouri non-MSA | Missouri | Wright | 23 | 1030 | 8 | 9 | 8 |
| Missouri non-MSA | Missouri | New Madrid | 31 | 1601 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Vernon | 17 | 960 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | Stone | 24 | 1578 | 7 | 11 | 13 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 4 | 1391 | 7 | 8 | 11 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1172 | 7 | 7 | 7 |
| Kansas City | Missouri | Bates | 11 | 794 | 7 | 8 | 8 |
| Kansas City | Missouri | Clinton | 56 | 1223 | 7 | 9 | 11 |
| Missouri non-MSA | Missouri | Lawrence | 47 | 2265 | 7 | 10 | 12 |
| Springfield | Missouri | Polk | 21 | 1775 | 7 | 9 | 13 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1638 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Perry | 19 | 1838 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Iron | 1 | 398 | 6 | 6 | 5 |
| St. Joseph | Missouri | Andrew | 14 | 1075 | 6 | 7 | 9 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1471 | 6 | 9 | 10 |
| Missouri non-MSA | Missouri | Livingston | 22 | 1005 | 6 | 8 | 7 |
| Missouri non-MSA | Missouri | Henry | 21 | 1407 | 6 | 9 | 10 |
| Missouri non-MSA | Missouri | Barry | 36 | 1767 | 5 | 9 | 10 |
| Missouri non-MSA | Missouri | Dent | 7 | 693 | 5 | 5 | 5 |
| Kansas City | Kansas | Linn | 3 | 487 | 5 | 5 | 6 |
| Columbia-Jefferson City | Missouri | Moniteau | 17 | 1469 | 5 | 6 | 8 |
| Missouri non-MSA | Missouri | Macon | 8 | 895 | 5 | 8 | 7 |
| Missouri non-MSA | Missouri | Morgan | 23 | 1423 | 5 | 8 | 11 |
| Missouri non-MSA | Missouri | Ralls | 7 | 646 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Gasconade | 29 | 660 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Stoddard | 33 | 1999 | 4 | 6 | 12 |
| St. Joseph | Missouri | DeKalb | 19 | 757 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Carroll | 15 | 642 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Grundy | 23 | 663 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Wayne | 6 | 657 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Monroe | 5 | 506 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 486 | 4 | 4 | 4 |
| Kansas City | Missouri | Caldwell | 5 | 538 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Douglas | 19 | 604 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Benton | 16 | 1165 | 3 | 7 | 13 |
| Missouri non-MSA | Missouri | Gentry | 16 | 595 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Ripley | 8 | 661 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Barton | 9 | 758 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2286 | 3 | 7 | 9 |
| Missouri non-MSA | Missouri | Daviess | 9 | 465 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Oregon | 3 | 526 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Harrison | 7 | 608 | 3 | 5 | 7 |
| St. Joseph | Kansas | Doniphan | 5 | 697 | 3 | 6 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 21 | 1262 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Mississippi | 11 | 1119 | 3 | 4 | 8 |
| Missouri non-MSA | Missouri | Clark | 4 | 366 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 4 | 372 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 442 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Lewis | 3 | 526 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Chariton | 3 | 320 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 8 | 502 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 653 | 2 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 611 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Maries | 6 | 453 | 2 | 2 | 3 |
| Springfield | Missouri | Dallas | 18 | 686 | 2 | 2 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 370 | 2 | 1 | 4 |
| Missouri non-MSA | Missouri | Hickory | 9 | 425 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 11 | 408 | 1 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 336 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Dade | 8 | 362 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 196 | 1 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 946 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Carter | 6 | 368 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shelby | 4 | 289 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shannon | 9 | 407 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Putnam | 1 | 198 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 1 | 126 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 116 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 323 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 223 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 5 | 259 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 225 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 149 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
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
