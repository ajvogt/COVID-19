# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/09/2021  
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
| St. Louis-Farmington | 3550 | 214704 | 1724 | 1522 | 1619 |
| Kansas City | 1740 | 145555 | 1135 | 1168 | 1145 |
| Missouri non-MSA | 1497 | 97610 | 604 | 610 | 679 |
| Springfield | 439 | 31487 | 261 | 248 | 247 |
| Columbia-Jefferson City | 218 | 30980 | 165 | 166 | 183 |
| Joplin | 226 | 14220 | 84 | 85 | 74 |
| Cape Girardeau-Sikeston | 187 | 11586 | 62 | 58 | 63 |
| St. Joseph | 142 | 9064 | 52 | 52 | 52 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1466 | 73847 | 623 | 540 | 543 |
| Kansas City | Kansas | Johnson | 517 | 42456 | 394 | 409 | 376 |
| Kansas City | Missouri | Kansas City | 369 | 32048 | 225 | 217 | 210 |
| St. Louis-Farmington | Illinois | St. Clair | 386 | 20618 | 224 | 173 | 170 |
| St. Louis-Farmington | Illinois | Madison | 426 | 22561 | 215 | 170 | 193 |
| St. Louis-Farmington | Missouri | St. Charles | 299 | 28738 | 190 | 179 | 206 |
| Kansas City | Missouri | Jackson | 263 | 24938 | 179 | 171 | 180 |
| Springfield | Missouri | Greene | 298 | 20266 | 171 | 160 | 158 |
| St. Louis-Farmington | Missouri | Jefferson | 149 | 16257 | 134 | 125 | 125 |
| Kansas City | Kansas | Wyandotte | 201 | 16576 | 97 | 122 | 126 |
| Columbia-Jefferson City | Missouri | Boone | 50 | 14049 | 78 | 77 | 90 |
| St. Louis-Farmington | Missouri | Franklin | 116 | 7104 | 64 | 59 | 57 |
| Joplin | Missouri | Jasper | 167 | 10563 | 62 | 63 | 56 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17427 | 57 | 74 | 102 |
| Springfield | Missouri | Christian | 55 | 5947 | 52 | 50 | 53 |
| Kansas City | Missouri | Clay | 113 | 6661 | 46 | 46 | 49 |
| Kansas City | Missouri | Cass | 58 | 5929 | 42 | 43 | 51 |
| St. Louis-Farmington | Missouri | St. Francois | 75 | 6895 | 39 | 44 | 47 |
| Kansas City | Kansas | Leavenworth | 46 | 5395 | 39 | 40 | 37 |
| Columbia-Jefferson City | Missouri | Cole | 93 | 7938 | 38 | 39 | 39 |
| St. Louis-Farmington | Illinois | Clinton | 81 | 4754 | 38 | 30 | 33 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 103 | 6770 | 38 | 37 | 40 |
| St. Joseph | Missouri | Buchanan | 99 | 6286 | 31 | 29 | 32 |
| St. Louis-Farmington | Illinois | Monroe | 61 | 3353 | 31 | 28 | 31 |
| St. Louis-Farmington | Illinois | Macoupin | 90 | 3490 | 31 | 26 | 28 |
| Kansas City | Kansas | Miami | 15 | 2083 | 29 | 31 | 26 |
| Missouri non-MSA | Missouri | Pulaski | 29 | 2759 | 26 | 19 | 25 |
| Missouri non-MSA | Missouri | Pettis | 67 | 4283 | 26 | 29 | 37 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3742 | 25 | 23 | 31 |
| Columbia-Jefferson City | Missouri | Callaway | 25 | 3996 | 25 | 26 | 26 |
| Missouri non-MSA | Missouri | Howell | 39 | 2499 | 22 | 19 | 26 |
| Springfield | Missouri | Webster | 43 | 2617 | 22 | 21 | 20 |
| Joplin | Missouri | Newton | 59 | 3657 | 21 | 21 | 18 |
| Missouri non-MSA | Missouri | Taney | 56 | 3977 | 21 | 23 | 24 |
| Kansas City | Missouri | Platte | 24 | 2614 | 21 | 25 | 23 |
| Missouri non-MSA | Missouri | Camden | 65 | 3327 | 20 | 21 | 20 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2422 | 19 | 9 | 9 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3381 | 18 | 16 | 20 |
| Cape Girardeau-Sikeston | Missouri | Scott | 65 | 3472 | 18 | 15 | 16 |
| Missouri non-MSA | Missouri | Lawrence | 57 | 2470 | 17 | 15 | 13 |
| Missouri non-MSA | Missouri | Laclede | 51 | 2635 | 17 | 15 | 18 |
| St. Louis-Farmington | Illinois | Jersey | 47 | 2091 | 17 | 16 | 17 |
| Missouri non-MSA | Missouri | Phelps | 93 | 2641 | 16 | 18 | 20 |
| Missouri non-MSA | Missouri | Saline | 26 | 2139 | 15 | 13 | 14 |
| Missouri non-MSA | Missouri | Adair | 5 | 1735 | 15 | 14 | 17 |
| Kansas City | Missouri | Lafayette | 43 | 2191 | 14 | 14 | 16 |
| St. Louis-Farmington | Illinois | Bond | 19 | 1651 | 13 | 11 | 13 |
| Missouri non-MSA | Missouri | Washington | 41 | 1894 | 13 | 12 | 11 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1763 | 13 | 13 | 14 |
| Missouri non-MSA | Missouri | Vernon | 24 | 1194 | 13 | 18 | 13 |
| Springfield | Missouri | Polk | 24 | 1934 | 13 | 12 | 12 |
| Missouri non-MSA | Missouri | Crawford | 20 | 1823 | 13 | 15 | 16 |
| Missouri non-MSA | Missouri | Miller | 42 | 2133 | 12 | 11 | 14 |
| Missouri non-MSA | Missouri | Butler | 16 | 2939 | 12 | 14 | 17 |
| Missouri non-MSA | Missouri | Stone | 27 | 1732 | 12 | 12 | 13 |
| Missouri non-MSA | Missouri | Benton | 16 | 1289 | 12 | 9 | 11 |
| Missouri non-MSA | Missouri | Barry | 37 | 1903 | 12 | 10 | 11 |
| Kansas City | Missouri | Ray | 9 | 1224 | 12 | 11 | 13 |
| Missouri non-MSA | Missouri | Wright | 24 | 1176 | 11 | 12 | 10 |
| Kansas City | Missouri | Clinton | 59 | 1348 | 10 | 10 | 11 |
| Missouri non-MSA | Missouri | Marion | 30 | 2433 | 10 | 12 | 13 |
| Kansas City | Kansas | Linn | 3 | 607 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2163 | 9 | 9 | 12 |
| Kansas City | Missouri | Bates | 13 | 910 | 9 | 10 | 9 |
| St. Joseph | Missouri | Andrew | 15 | 1169 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Macon | 10 | 992 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | Audrain | 41 | 1880 | 8 | 21 | 20 |
| Missouri non-MSA | Missouri | Texas | 19 | 1419 | 8 | 9 | 11 |
| Missouri non-MSA | Missouri | Randolph | 19 | 1667 | 8 | 7 | 10 |
| Missouri non-MSA | Missouri | Morgan | 24 | 1513 | 7 | 7 | 9 |
| St. Joseph | Kansas | Doniphan | 7 | 792 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | Oregon | 3 | 595 | 7 | 5 | 6 |
| Columbia-Jefferson City | Missouri | Moniteau | 18 | 1563 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Livingston | 24 | 1102 | 7 | 8 | 8 |
| Missouri non-MSA | Missouri | Henry | 24 | 1503 | 7 | 7 | 9 |
| Missouri non-MSA | Missouri | Perry | 19 | 1911 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2076 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | McDonald | 21 | 1730 | 6 | 8 | 8 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1252 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Madison | 11 | 1259 | 6 | 8 | 8 |
| Missouri non-MSA | Missouri | New Madrid | 38 | 1668 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Barton | 8 | 819 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Cedar | 9 | 572 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 10 | 1473 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Gasconade | 30 | 732 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Pike | 17 | 1327 | 6 | 6 | 9 |
| Missouri non-MSA | Missouri | Wayne | 7 | 709 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Gentry | 16 | 650 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Grundy | 26 | 724 | 5 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1537 | 5 | 5 | 8 |
| Missouri non-MSA | Missouri | Carroll | 18 | 695 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Douglas | 20 | 665 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Ralls | 7 | 700 | 4 | 4 | 5 |
| St. Joseph | Missouri | DeKalb | 21 | 817 | 4 | 5 | 5 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 413 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 10 | 692 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 22 | 1316 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Linn | 10 | 439 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 4 | 410 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Monroe | 6 | 549 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Ripley | 9 | 703 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 9 | 494 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 18 | 1163 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Harrison | 10 | 661 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 527 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 488 | 3 | 4 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 984 | 3 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 645 | 3 | 2 | 3 |
| Kansas City | Missouri | Caldwell | 7 | 575 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Lewis | 3 | 570 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Dade | 10 | 382 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Dent | 9 | 730 | 2 | 3 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 360 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Shannon | 9 | 429 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 222 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Atchison | 5 | 279 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Chariton | 3 | 355 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 6 | 396 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Iron | 1 | 427 | 2 | 3 | 5 |
| Springfield | Missouri | Dallas | 19 | 723 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Shelby | 4 | 314 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 481 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 236 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 5 | 384 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 1 | 141 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 9 | 443 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 335 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 156 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 125 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 233 | 0 | 0 | 1 |
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
