# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/12/2021  
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
| St. Louis-Farmington | 3578 | 219165 | 1655 | 1626 | 1565 |
| Kansas City | 1743 | 148845 | 1288 | 1206 | 1130 |
| Missouri non-MSA | 1514 | 99456 | 705 | 677 | 627 |
| Springfield | 448 | 32088 | 288 | 263 | 237 |
| Columbia-Jefferson City | 218 | 31434 | 185 | 182 | 175 |
| Joplin | 232 | 14413 | 90 | 91 | 74 |
| Cape Girardeau-Sikeston | 188 | 11741 | 69 | 59 | 59 |
| St. Joseph | 142 | 9224 | 57 | 56 | 50 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1476 | 75623 | 596 | 583 | 538 |
| Kansas City | Kansas | Johnson | 517 | 43450 | 438 | 398 | 376 |
| Kansas City | Missouri | Kansas City | 369 | 32799 | 255 | 238 | 210 |
| St. Louis-Farmington | Missouri | St. Charles | 300 | 29317 | 213 | 196 | 199 |
| Kansas City | Missouri | Jackson | 264 | 25548 | 211 | 193 | 175 |
| St. Louis-Farmington | Illinois | Madison | 433 | 23063 | 196 | 187 | 186 |
| St. Louis-Farmington | Illinois | St. Clair | 392 | 21117 | 195 | 183 | 165 |
| Springfield | Missouri | Greene | 306 | 20641 | 186 | 168 | 151 |
| St. Louis-Farmington | Missouri | Jefferson | 149 | 16635 | 151 | 139 | 123 |
| Kansas City | Kansas | Wyandotte | 201 | 16794 | 109 | 113 | 121 |
| Columbia-Jefferson City | Missouri | Boone | 50 | 14285 | 92 | 86 | 86 |
| St. Louis-Farmington | Missouri | Franklin | 116 | 7305 | 69 | 67 | 57 |
| Joplin | Missouri | Jasper | 172 | 10723 | 69 | 69 | 56 |
| Kansas City | Missouri | Cass | 58 | 6122 | 58 | 51 | 50 |
| Springfield | Missouri | Christian | 55 | 6077 | 58 | 53 | 51 |
| Kansas City | Missouri | Clay | 113 | 6823 | 56 | 51 | 47 |
| St. Louis-Farmington | Missouri | St. Francois | 76 | 7020 | 48 | 46 | 44 |
| Kansas City | Kansas | Leavenworth | 46 | 5512 | 47 | 40 | 38 |
| Columbia-Jefferson City | Missouri | Cole | 93 | 8039 | 42 | 41 | 37 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 103 | 6863 | 41 | 38 | 38 |
| St. Louis-Farmington | Illinois | Macoupin | 91 | 3606 | 35 | 32 | 28 |
| St. Joseph | Missouri | Buchanan | 99 | 6399 | 35 | 33 | 30 |
| St. Louis-Farmington | Illinois | Clinton | 81 | 4813 | 34 | 32 | 31 |
| Missouri non-MSA | Missouri | Taney | 57 | 4089 | 34 | 28 | 23 |
| Missouri non-MSA | Missouri | Pettis | 67 | 4336 | 31 | 32 | 27 |
| Missouri non-MSA | Missouri | Pulaski | 29 | 2801 | 30 | 21 | 22 |
| St. Louis-Farmington | Illinois | Monroe | 62 | 3430 | 28 | 29 | 29 |
| Missouri non-MSA | Missouri | Camden | 65 | 3414 | 28 | 24 | 21 |
| Kansas City | Kansas | Miami | 15 | 2133 | 27 | 29 | 26 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3803 | 27 | 24 | 28 |
| Springfield | Missouri | Webster | 44 | 2678 | 26 | 23 | 20 |
| Kansas City | Missouri | Platte | 25 | 2678 | 25 | 26 | 23 |
| Columbia-Jefferson City | Missouri | Callaway | 25 | 4042 | 24 | 27 | 25 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3443 | 21 | 18 | 19 |
| Missouri non-MSA | Missouri | Lawrence | 57 | 2521 | 21 | 18 | 14 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2436 | 21 | 10 | 9 |
| Joplin | Missouri | Newton | 60 | 3690 | 21 | 22 | 17 |
| Cape Girardeau-Sikeston | Missouri | Scott | 66 | 3513 | 20 | 15 | 15 |
| Missouri non-MSA | Missouri | Howell | 39 | 2534 | 20 | 20 | 16 |
| Missouri non-MSA | Missouri | Butler | 16 | 3001 | 17 | 17 | 15 |
| Missouri non-MSA | Missouri | Adair | 5 | 1786 | 16 | 16 | 16 |
| Missouri non-MSA | Missouri | Phelps | 93 | 2691 | 16 | 20 | 19 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1803 | 16 | 14 | 14 |
| Missouri non-MSA | Missouri | Saline | 26 | 2177 | 15 | 15 | 13 |
| Missouri non-MSA | Missouri | Laclede | 51 | 2665 | 15 | 15 | 15 |
| Missouri non-MSA | Missouri | Washington | 41 | 1930 | 15 | 13 | 10 |
| Missouri non-MSA | Missouri | Stone | 27 | 1767 | 14 | 13 | 12 |
| Missouri non-MSA | Missouri | Barry | 37 | 1932 | 14 | 11 | 10 |
| St. Louis-Farmington | Illinois | Bond | 20 | 1667 | 14 | 12 | 12 |
| Springfield | Missouri | Polk | 24 | 1958 | 14 | 13 | 11 |
| Kansas City | Missouri | Lafayette | 43 | 2223 | 14 | 14 | 15 |
| Missouri non-MSA | Missouri | Crawford | 20 | 1862 | 13 | 15 | 15 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2207 | 13 | 11 | 12 |
| Missouri non-MSA | Missouri | Miller | 43 | 2169 | 13 | 13 | 14 |
| Kansas City | Missouri | Ray | 10 | 1261 | 13 | 13 | 13 |
| Missouri non-MSA | Missouri | Wright | 24 | 1210 | 12 | 13 | 10 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17435 | 12 | 59 | 87 |
| Missouri non-MSA | Missouri | Benton | 18 | 1312 | 12 | 11 | 9 |
| Missouri non-MSA | Missouri | Livingston | 24 | 1140 | 12 | 10 | 8 |
| Missouri non-MSA | Missouri | Vernon | 24 | 1223 | 12 | 19 | 14 |
| St. Louis-Farmington | Illinois | Jersey | 47 | 2110 | 11 | 12 | 16 |
| Missouri non-MSA | Missouri | Marion | 30 | 2472 | 11 | 13 | 12 |
| Missouri non-MSA | Missouri | Audrain | 42 | 1911 | 11 | 22 | 19 |
| Kansas City | Missouri | Clinton | 59 | 1369 | 10 | 11 | 10 |
| Missouri non-MSA | Missouri | Henry | 24 | 1535 | 10 | 9 | 9 |
| Missouri non-MSA | Missouri | Macon | 10 | 1019 | 10 | 9 | 8 |
| Kansas City | Kansas | Linn | 3 | 617 | 9 | 9 | 7 |
| Missouri non-MSA | Missouri | Randolph | 19 | 1698 | 9 | 8 | 9 |
| Missouri non-MSA | Missouri | Barton | 8 | 842 | 9 | 6 | 5 |
| Missouri non-MSA | Missouri | McDonald | 22 | 1762 | 9 | 9 | 8 |
| St. Joseph | Kansas | Doniphan | 7 | 810 | 9 | 8 | 7 |
| Kansas City | Missouri | Bates | 13 | 934 | 8 | 10 | 9 |
| Missouri non-MSA | Missouri | Morgan | 30 | 1536 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2104 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | Oregon | 3 | 611 | 8 | 6 | 4 |
| Missouri non-MSA | Missouri | Gasconade | 30 | 754 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Texas | 19 | 1435 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | Perry | 20 | 1933 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | New Madrid | 38 | 1686 | 7 | 7 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 19 | 1584 | 7 | 8 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1270 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Grundy | 26 | 744 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Pike | 17 | 1350 | 7 | 7 | 8 |
| St. Joseph | Missouri | Andrew | 15 | 1184 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Ozark | 5 | 441 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Linn | 10 | 463 | 7 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 19 | 1553 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 11 | 1497 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Douglas | 20 | 682 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Madison | 11 | 1278 | 6 | 8 | 8 |
| Missouri non-MSA | Missouri | Pemiscot | 22 | 1331 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Wayne | 8 | 726 | 5 | 5 | 5 |
| St. Joseph | Missouri | DeKalb | 21 | 831 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Carroll | 18 | 715 | 5 | 5 | 5 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1000 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 9 | 516 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Cedar | 9 | 584 | 5 | 6 | 3 |
| Missouri non-MSA | Missouri | Gentry | 16 | 657 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Harrison | 10 | 684 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Ripley | 9 | 723 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 11 | 701 | 4 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 661 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Iron | 1 | 439 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Ralls | 7 | 708 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 502 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Lewis | 3 | 581 | 3 | 4 | 3 |
| Springfield | Missouri | Dallas | 19 | 734 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Atchison | 5 | 284 | 3 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 418 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 536 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Mississippi | 18 | 1168 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Dent | 9 | 741 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 436 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 230 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Monroe | 6 | 554 | 3 | 3 | 3 |
| Kansas City | Missouri | Caldwell | 7 | 582 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Chariton | 3 | 362 | 2 | 3 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 365 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 4 | 319 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Dade | 10 | 384 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Maries | 7 | 489 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 6 | 397 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 244 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 1 | 149 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 342 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 5 | 389 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 9 | 445 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 127 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 204 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 157 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 233 | 0 | 0 | 0 |
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
