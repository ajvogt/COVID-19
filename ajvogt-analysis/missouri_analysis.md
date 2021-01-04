# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/04/2021  
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
| St. Louis-Farmington | 3370 | 206476 | 1577 | 1420 | 1662 |
| Kansas City | 1607 | 138635 | 1246 | 1078 | 1130 |
| Missouri non-MSA | 1383 | 94344 | 663 | 608 | 709 |
| Springfield | 405 | 29960 | 238 | 216 | 242 |
| Columbia-Jefferson City | 198 | 30071 | 181 | 168 | 188 |
| Joplin | 222 | 13734 | 94 | 73 | 70 |
| St. Joseph | 138 | 8792 | 57 | 50 | 58 |
| Cape Girardeau-Sikeston | 178 | 11239 | 54 | 54 | 66 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1392 | 70999 | 554 | 473 | 554 |
| Kansas City | Kansas | Johnson | 455 | 39696 | 424 | 329 | 347 |
| Kansas City | Missouri | Kansas City | 356 | 30887 | 224 | 205 | 214 |
| Kansas City | Missouri | Jackson | 245 | 23992 | 179 | 176 | 187 |
| St. Louis-Farmington | Missouri | St. Charles | 290 | 27723 | 177 | 172 | 213 |
| St. Louis-Farmington | Illinois | Madison | 397 | 21557 | 174 | 163 | 197 |
| St. Louis-Farmington | Illinois | St. Clair | 359 | 19589 | 168 | 149 | 171 |
| Springfield | Missouri | Greene | 278 | 19262 | 150 | 139 | 154 |
| Kansas City | Kansas | Wyandotte | 198 | 15892 | 147 | 127 | 126 |
| St. Louis-Farmington | Missouri | Jefferson | 134 | 15501 | 127 | 110 | 123 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17293 | 108 | 102 | 123 |
| Columbia-Jefferson City | Missouri | Boone | 44 | 13600 | 80 | 79 | 92 |
| Joplin | Missouri | Jasper | 163 | 10201 | 70 | 54 | 54 |
| St. Louis-Farmington | Missouri | Franklin | 113 | 6800 | 65 | 57 | 56 |
| Kansas City | Missouri | Clay | 98 | 6428 | 51 | 48 | 51 |
| St. Louis-Farmington | Missouri | St. Francois | 69 | 6668 | 49 | 42 | 46 |
| Springfield | Missouri | Christian | 49 | 5647 | 48 | 45 | 53 |
| Kansas City | Missouri | Cass | 55 | 5706 | 47 | 46 | 54 |
| Columbia-Jefferson City | Missouri | Cole | 86 | 7737 | 42 | 38 | 40 |
| Kansas City | Kansas | Leavenworth | 38 | 5118 | 42 | 30 | 37 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 99 | 6563 | 36 | 36 | 41 |
| Missouri non-MSA | Missouri | Audrain | 32 | 1833 | 34 | 24 | 22 |
| Kansas City | Kansas | Miami | 15 | 1880 | 33 | 26 | 24 |
| Missouri non-MSA | Missouri | Pettis | 61 | 4106 | 32 | 21 | 44 |
| St. Joseph | Missouri | Buchanan | 98 | 6137 | 32 | 29 | 38 |
| St. Louis-Farmington | Illinois | Monroe | 61 | 3204 | 30 | 28 | 32 |
| Columbia-Jefferson City | Missouri | Callaway | 20 | 3858 | 30 | 25 | 27 |
| Kansas City | Missouri | Platte | 23 | 2497 | 29 | 25 | 23 |
| St. Louis-Farmington | Illinois | Clinton | 80 | 4547 | 29 | 27 | 33 |
| St. Louis-Farmington | Illinois | Macoupin | 81 | 3335 | 27 | 23 | 28 |
| Missouri non-MSA | Missouri | Vernon | 19 | 1139 | 27 | 18 | 13 |
| Missouri non-MSA | Missouri | Phelps | 86 | 2576 | 24 | 22 | 21 |
| Joplin | Missouri | Newton | 59 | 3533 | 23 | 19 | 16 |
| Missouri non-MSA | Missouri | Taney | 52 | 3846 | 23 | 20 | 26 |
| St. Louis-Farmington | Missouri | Lincoln | 19 | 3597 | 21 | 25 | 32 |
| Springfield | Missouri | Webster | 39 | 2484 | 21 | 17 | 19 |
| Missouri non-MSA | Missouri | Camden | 63 | 3208 | 21 | 20 | 20 |
| Missouri non-MSA | Missouri | Howell | 37 | 2390 | 21 | 17 | 25 |
| Missouri non-MSA | Missouri | Butler | 15 | 2873 | 18 | 16 | 19 |
| Missouri non-MSA | Missouri | Crawford | 19 | 1757 | 17 | 18 | 16 |
| Kansas City | Missouri | Lafayette | 40 | 2121 | 17 | 17 | 16 |
| Missouri non-MSA | Missouri | Marion | 24 | 2388 | 16 | 13 | 16 |
| Missouri non-MSA | Missouri | Johnson | 31 | 3280 | 15 | 17 | 21 |
| St. Louis-Farmington | Illinois | Jersey | 43 | 2021 | 15 | 18 | 20 |
| Missouri non-MSA | Missouri | Laclede | 46 | 2547 | 15 | 15 | 19 |
| Missouri non-MSA | Missouri | Lawrence | 52 | 2365 | 15 | 12 | 12 |
| Missouri non-MSA | Missouri | Saline | 23 | 2066 | 15 | 14 | 14 |
| Missouri non-MSA | Missouri | Wright | 24 | 1117 | 14 | 11 | 10 |
| Missouri non-MSA | Missouri | Adair | 4 | 1653 | 14 | 16 | 17 |
| Missouri non-MSA | Missouri | Washington | 39 | 1822 | 13 | 10 | 10 |
| Kansas City | Missouri | Ray | 8 | 1162 | 13 | 13 | 13 |
| Springfield | Missouri | Polk | 21 | 1857 | 13 | 10 | 13 |
| Missouri non-MSA | Missouri | Miller | 41 | 2069 | 13 | 11 | 15 |
| Cape Girardeau-Sikeston | Missouri | Scott | 60 | 3366 | 13 | 14 | 18 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1686 | 13 | 13 | 13 |
| Missouri non-MSA | Missouri | Pulaski | 28 | 2588 | 13 | 23 | 27 |
| Kansas City | Missouri | Bates | 12 | 869 | 12 | 10 | 9 |
| Missouri non-MSA | Missouri | Stone | 24 | 1656 | 12 | 10 | 13 |
| Missouri non-MSA | Missouri | Texas | 18 | 1378 | 11 | 9 | 12 |
| Missouri non-MSA | Missouri | Madison | 10 | 1232 | 11 | 9 | 9 |
| St. Louis-Farmington | Illinois | Bond | 17 | 1564 | 11 | 10 | 12 |
| Kansas City | Missouri | Clinton | 56 | 1290 | 10 | 9 | 11 |
| Missouri non-MSA | Missouri | Dunklin | 15 | 2112 | 10 | 9 | 12 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1697 | 10 | 9 | 8 |
| Columbia-Jefferson City | Missouri | Moniteau | 17 | 1528 | 10 | 7 | 7 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 5 | 1451 | 9 | 10 | 10 |
| St. Joseph | Missouri | Andrew | 14 | 1126 | 9 | 8 | 8 |
| St. Joseph | Kansas | Doniphan | 7 | 738 | 9 | 7 | 6 |
| Missouri non-MSA | Missouri | Barry | 36 | 1828 | 9 | 8 | 10 |
| Missouri non-MSA | Missouri | Henry | 22 | 1462 | 9 | 8 | 10 |
| Missouri non-MSA | Missouri | Morgan | 24 | 1473 | 9 | 7 | 11 |
| Missouri non-MSA | Missouri | New Madrid | 31 | 1631 | 8 | 7 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1214 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Benton | 16 | 1217 | 8 | 5 | 13 |
| Kansas City | Kansas | Linn | 3 | 534 | 8 | 6 | 6 |
| Missouri non-MSA | Missouri | Livingston | 24 | 1053 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2042 | 8 | 6 | 11 |
| Missouri non-MSA | Missouri | Macon | 10 | 942 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Perry | 19 | 1875 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Randolph | 17 | 1631 | 7 | 9 | 11 |
| Missouri non-MSA | Missouri | Cedar | 8 | 549 | 7 | 4 | 3 |
| Missouri non-MSA | Missouri | Pike | 14 | 1295 | 6 | 8 | 9 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1506 | 6 | 6 | 9 |
| St. Joseph | Missouri | DeKalb | 19 | 791 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Ralls | 7 | 679 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Harrison | 10 | 650 | 6 | 5 | 7 |
| Missouri non-MSA | Missouri | Douglas | 19 | 638 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 29 | 697 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Carroll | 18 | 676 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 476 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Dent | 8 | 717 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Mississippi | 17 | 1145 | 5 | 4 | 7 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 392 | 5 | 2 | 3 |
| Missouri non-MSA | Missouri | Grundy | 23 | 692 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 511 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Lewis | 3 | 556 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 21 | 1290 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Oregon | 3 | 554 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Gentry | 16 | 622 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Wayne | 6 | 684 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Monroe | 5 | 531 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Ripley | 8 | 686 | 4 | 4 | 4 |
| Springfield | Missouri | Dallas | 18 | 710 | 4 | 2 | 3 |
| Missouri non-MSA | Missouri | Barton | 8 | 778 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Iron | 1 | 411 | 3 | 5 | 5 |
| Kansas City | Missouri | Caldwell | 5 | 563 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Ozark | 4 | 392 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Daviess | 9 | 481 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Maries | 6 | 473 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Chariton | 3 | 340 | 3 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 3 | 628 | 2 | 2 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 964 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 10 | 666 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Hickory | 9 | 437 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 4 | 302 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Carter | 6 | 381 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 209 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Clark | 5 | 377 | 1 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 346 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 135 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 9 | 414 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 230 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 155 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 232 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 9 | 368 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Worth | 1 | 122 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 9 | 413 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Holt | 9 | 329 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 201 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Atchison | 5 | 261 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2286 | 0 | 4 | 7 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
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
