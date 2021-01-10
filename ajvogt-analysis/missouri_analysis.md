# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/10/2021  
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
| St. Louis-Farmington | 3573 | 216790 | 1683 | 1589 | 1619 |
| Kansas City | 1743 | 146447 | 1188 | 1202 | 1149 |
| Missouri non-MSA | 1509 | 98437 | 660 | 645 | 667 |
| Springfield | 448 | 31763 | 280 | 260 | 249 |
| Columbia-Jefferson City | 218 | 31161 | 169 | 172 | 180 |
| Joplin | 231 | 14311 | 87 | 89 | 75 |
| Cape Girardeau-Sikeston | 188 | 11659 | 66 | 60 | 61 |
| St. Joseph | 142 | 9125 | 55 | 55 | 52 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1475 | 74745 | 620 | 564 | 551 |
| Kansas City | Kansas | Johnson | 517 | 42456 | 394 | 409 | 376 |
| Kansas City | Missouri | Kansas City | 369 | 32445 | 251 | 234 | 215 |
| St. Louis-Farmington | Missouri | St. Charles | 300 | 29003 | 207 | 186 | 206 |
| St. Louis-Farmington | Illinois | Madison | 429 | 22785 | 196 | 181 | 192 |
| Kansas City | Missouri | Jackson | 264 | 25179 | 193 | 180 | 179 |
| St. Louis-Farmington | Illinois | St. Clair | 393 | 20815 | 192 | 182 | 169 |
| Springfield | Missouri | Greene | 306 | 20430 | 181 | 166 | 159 |
| St. Louis-Farmington | Missouri | Jefferson | 149 | 16427 | 148 | 133 | 125 |
| Kansas City | Kansas | Wyandotte | 201 | 16576 | 97 | 122 | 126 |
| Columbia-Jefferson City | Missouri | Boone | 50 | 14160 | 81 | 81 | 90 |
| St. Louis-Farmington | Missouri | Franklin | 116 | 7195 | 69 | 63 | 57 |
| Joplin | Missouri | Jasper | 172 | 10638 | 65 | 67 | 56 |
| Springfield | Missouri | Christian | 55 | 6004 | 56 | 52 | 53 |
| Kansas City | Missouri | Cass | 58 | 6030 | 51 | 48 | 52 |
| Kansas City | Missouri | Clay | 113 | 6744 | 51 | 49 | 49 |
| St. Louis-Farmington | Missouri | St. Francois | 75 | 6963 | 45 | 46 | 47 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 103 | 6812 | 39 | 38 | 39 |
| Kansas City | Kansas | Leavenworth | 46 | 5395 | 39 | 40 | 37 |
| Columbia-Jefferson City | Missouri | Cole | 93 | 7975 | 39 | 39 | 38 |
| St. Louis-Farmington | Illinois | Clinton | 81 | 4777 | 35 | 32 | 32 |
| St. Joseph | Missouri | Buchanan | 99 | 6334 | 33 | 31 | 32 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17438 | 33 | 69 | 98 |
| St. Louis-Farmington | Illinois | Macoupin | 91 | 3546 | 33 | 29 | 28 |
| Missouri non-MSA | Missouri | Pettis | 67 | 4309 | 29 | 30 | 34 |
| Kansas City | Kansas | Miami | 15 | 2083 | 29 | 31 | 26 |
| St. Louis-Farmington | Illinois | Monroe | 62 | 3385 | 28 | 29 | 31 |
| Missouri non-MSA | Missouri | Pulaski | 29 | 2771 | 27 | 19 | 24 |
| Missouri non-MSA | Missouri | Taney | 56 | 4022 | 27 | 25 | 24 |
| Springfield | Missouri | Webster | 44 | 2653 | 25 | 23 | 20 |
| Missouri non-MSA | Missouri | Camden | 65 | 3373 | 25 | 23 | 21 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3758 | 25 | 22 | 29 |
| Columbia-Jefferson City | Missouri | Callaway | 25 | 4012 | 24 | 26 | 26 |
| Joplin | Missouri | Newton | 59 | 3673 | 21 | 21 | 18 |
| Kansas City | Missouri | Platte | 25 | 2628 | 21 | 24 | 23 |
| Missouri non-MSA | Missouri | Howell | 39 | 2514 | 20 | 20 | 27 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2422 | 19 | 9 | 8 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3405 | 19 | 17 | 19 |
| Missouri non-MSA | Missouri | Lawrence | 57 | 2490 | 19 | 17 | 14 |
| Cape Girardeau-Sikeston | Missouri | Scott | 66 | 3490 | 18 | 16 | 16 |
| Missouri non-MSA | Missouri | Adair | 5 | 1762 | 18 | 15 | 17 |
| Missouri non-MSA | Missouri | Laclede | 51 | 2651 | 17 | 15 | 18 |
| Missouri non-MSA | Missouri | Butler | 16 | 2977 | 16 | 16 | 16 |
| Missouri non-MSA | Missouri | Phelps | 93 | 2644 | 15 | 18 | 19 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1784 | 15 | 14 | 14 |
| St. Louis-Farmington | Illinois | Jersey | 47 | 2099 | 14 | 16 | 17 |
| Missouri non-MSA | Missouri | Saline | 26 | 2155 | 14 | 14 | 14 |
| Missouri non-MSA | Missouri | Crawford | 20 | 1841 | 14 | 15 | 16 |
| Springfield | Missouri | Polk | 24 | 1949 | 14 | 13 | 12 |
| Missouri non-MSA | Missouri | Barry | 37 | 1919 | 13 | 12 | 11 |
| St. Louis-Farmington | Illinois | Bond | 20 | 1654 | 13 | 12 | 12 |
| Missouri non-MSA | Missouri | Washington | 41 | 1906 | 13 | 13 | 10 |
| Missouri non-MSA | Missouri | Stone | 27 | 1745 | 13 | 13 | 12 |
| Missouri non-MSA | Missouri | Miller | 43 | 2146 | 13 | 12 | 14 |
| Kansas City | Missouri | Lafayette | 43 | 2204 | 12 | 14 | 16 |
| Missouri non-MSA | Missouri | Wright | 24 | 1194 | 12 | 13 | 11 |
| Missouri non-MSA | Missouri | Benton | 18 | 1300 | 12 | 10 | 10 |
| Missouri non-MSA | Missouri | Vernon | 24 | 1213 | 12 | 19 | 14 |
| Kansas City | Missouri | Ray | 10 | 1240 | 12 | 12 | 13 |
| Missouri non-MSA | Missouri | Marion | 30 | 2451 | 11 | 13 | 12 |
| Kansas City | Missouri | Clinton | 59 | 1360 | 11 | 10 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2184 | 11 | 11 | 11 |
| Kansas City | Kansas | Linn | 3 | 607 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Macon | 10 | 1005 | 10 | 8 | 8 |
| Missouri non-MSA | Missouri | Livingston | 24 | 1118 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2095 | 9 | 8 | 8 |
| Kansas City | Missouri | Bates | 13 | 920 | 9 | 10 | 9 |
| Missouri non-MSA | Missouri | Audrain | 41 | 1891 | 8 | 21 | 19 |
| Missouri non-MSA | Missouri | Randolph | 19 | 1685 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | Oregon | 3 | 606 | 8 | 6 | 6 |
| Missouri non-MSA | Missouri | McDonald | 22 | 1745 | 8 | 9 | 8 |
| Missouri non-MSA | Missouri | Henry | 24 | 1518 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Morgan | 30 | 1523 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Barton | 8 | 834 | 8 | 6 | 5 |
| St. Joseph | Missouri | Andrew | 15 | 1174 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Perry | 19 | 1922 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | Texas | 19 | 1426 | 8 | 9 | 11 |
| St. Joseph | Kansas | Doniphan | 7 | 792 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | New Madrid | 38 | 1678 | 7 | 7 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 19 | 1567 | 7 | 8 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1257 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Madison | 11 | 1266 | 6 | 8 | 8 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 11 | 1485 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Grundy | 26 | 735 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Gasconade | 30 | 735 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Pike | 17 | 1334 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | Pemiscot | 22 | 1327 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Douglas | 20 | 677 | 6 | 5 | 6 |
| St. Joseph | Missouri | DeKalb | 21 | 825 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Linn | 10 | 452 | 5 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 19 | 1540 | 5 | 5 | 8 |
| Missouri non-MSA | Missouri | Carroll | 18 | 704 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Cedar | 9 | 575 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Ralls | 7 | 707 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Wayne | 8 | 711 | 4 | 4 | 4 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 416 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 10 | 695 | 4 | 3 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 993 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Gentry | 16 | 651 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Ozark | 4 | 418 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 9 | 508 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Ripley | 9 | 710 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Harrison | 10 | 675 | 4 | 5 | 6 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 650 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Dent | 9 | 737 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Iron | 1 | 435 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Mississippi | 18 | 1165 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Monroe | 6 | 550 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 529 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 228 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 492 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Lewis | 3 | 576 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Shannon | 9 | 432 | 3 | 1 | 2 |
| Missouri non-MSA | Missouri | Atchison | 5 | 281 | 2 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 364 | 2 | 2 | 2 |
| Springfield | Missouri | Dallas | 19 | 727 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Chariton | 3 | 357 | 2 | 2 | 2 |
| Kansas City | Missouri | Caldwell | 7 | 580 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Dade | 10 | 381 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Shelby | 4 | 317 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 6 | 396 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 240 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 483 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 145 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 339 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 9 | 445 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 5 | 386 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 156 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 126 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 203 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 233 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
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
