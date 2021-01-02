# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/02/2021  
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
| St. Louis-Farmington | 3347 | 201914 | 1307 | 1466 | 1718 |
| Kansas City | 1597 | 135329 | 956 | 1069 | 1178 |
| Missouri non-MSA | 1373 | 92189 | 509 | 587 | 722 |
| Springfield | 404 | 29087 | 169 | 200 | 239 |
| Columbia-Jefferson City | 197 | 29525 | 153 | 173 | 203 |
| Joplin | 204 | 13462 | 68 | 70 | 72 |
| Cape Girardeau-Sikeston | 178 | 11080 | 53 | 56 | 71 |
| St. Joseph | 136 | 8608 | 44 | 47 | 61 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1391 | 69480 | 456 | 496 | 568 |
| Kansas City | Kansas | Johnson | 452 | 38865 | 305 | 350 | 381 |
| Kansas City | Missouri | Kansas City | 352 | 30039 | 177 | 185 | 210 |
| Kansas City | Missouri | Jackson | 243 | 23425 | 151 | 167 | 192 |
| St. Louis-Farmington | Missouri | St. Charles | 287 | 27135 | 146 | 189 | 220 |
| St. Louis-Farmington | Illinois | St. Clair | 353 | 19050 | 143 | 140 | 176 |
| St. Louis-Farmington | Illinois | Madison | 389 | 21054 | 141 | 167 | 207 |
| Springfield | Missouri | Greene | 278 | 18725 | 109 | 128 | 151 |
| Kansas City | Kansas | Wyandotte | 198 | 15576 | 102 | 124 | 134 |
| St. Louis-Farmington | Missouri | Jefferson | 134 | 15097 | 97 | 106 | 125 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17028 | 92 | 111 | 128 |
| Columbia-Jefferson City | Missouri | Boone | 44 | 13356 | 69 | 84 | 98 |
| Joplin | Missouri | Jasper | 158 | 9995 | 51 | 52 | 56 |
| St. Louis-Farmington | Missouri | Franklin | 113 | 6556 | 46 | 50 | 54 |
| Kansas City | Missouri | Clay | 98 | 6271 | 45 | 46 | 51 |
| Kansas City | Missouri | Cass | 54 | 5553 | 42 | 48 | 56 |
| St. Louis-Farmington | Missouri | St. Francois | 69 | 6539 | 42 | 44 | 46 |
| Columbia-Jefferson City | Missouri | Cole | 86 | 7605 | 36 | 36 | 44 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 99 | 6455 | 35 | 37 | 43 |
| Springfield | Missouri | Christian | 49 | 5450 | 34 | 43 | 52 |
| Missouri non-MSA | Missouri | Audrain | 32 | 1794 | 34 | 27 | 22 |
| Kansas City | Kansas | Leavenworth | 38 | 5044 | 31 | 35 | 40 |
| St. Louis-Farmington | Illinois | Monroe | 59 | 3135 | 29 | 31 | 33 |
| Missouri non-MSA | Missouri | Pettis | 61 | 4063 | 27 | 24 | 45 |
| Kansas City | Missouri | Platte | 23 | 2420 | 27 | 25 | 23 |
| Columbia-Jefferson City | Missouri | Callaway | 20 | 3778 | 26 | 26 | 30 |
| St. Louis-Farmington | Illinois | Clinton | 80 | 4485 | 25 | 29 | 36 |
| St. Louis-Farmington | Illinois | Macoupin | 79 | 3273 | 24 | 25 | 31 |
| Kansas City | Kansas | Miami | 15 | 1818 | 24 | 25 | 24 |
| St. Joseph | Missouri | Buchanan | 96 | 6014 | 23 | 26 | 40 |
| Missouri non-MSA | Missouri | Vernon | 19 | 1082 | 21 | 16 | 13 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3536 | 21 | 27 | 34 |
| Missouri non-MSA | Missouri | Camden | 63 | 3143 | 19 | 20 | 21 |
| Missouri non-MSA | Missouri | Phelps | 85 | 2480 | 17 | 20 | 22 |
| Missouri non-MSA | Missouri | Crawford | 19 | 1706 | 16 | 17 | 16 |
| Springfield | Missouri | Webster | 38 | 2423 | 16 | 18 | 19 |
| Joplin | Missouri | Newton | 46 | 3467 | 16 | 18 | 15 |
| St. Louis-Farmington | Illinois | Jersey | 42 | 1972 | 15 | 17 | 21 |
| Missouri non-MSA | Missouri | Taney | 52 | 3752 | 15 | 18 | 27 |
| Cape Girardeau-Sikeston | Missouri | Scott | 60 | 3328 | 14 | 15 | 20 |
| Missouri non-MSA | Missouri | Johnson | 29 | 3214 | 13 | 18 | 21 |
| Kansas City | Missouri | Lafayette | 40 | 2058 | 12 | 16 | 16 |
| Missouri non-MSA | Missouri | Howell | 37 | 2313 | 12 | 15 | 23 |
| Missouri non-MSA | Missouri | Butler | 15 | 2805 | 12 | 13 | 19 |
| Missouri non-MSA | Missouri | Adair | 4 | 1594 | 11 | 15 | 16 |
| Missouri non-MSA | Missouri | Marion | 24 | 2329 | 11 | 12 | 17 |
| Missouri non-MSA | Missouri | Laclede | 46 | 2491 | 10 | 15 | 21 |
| St. Louis-Farmington | Illinois | Bond | 16 | 1554 | 10 | 11 | 15 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1639 | 10 | 13 | 13 |
| Missouri non-MSA | Missouri | Wright | 23 | 1068 | 10 | 9 | 9 |
| Missouri non-MSA | Missouri | Madison | 10 | 1200 | 10 | 9 | 9 |
| Kansas City | Missouri | Bates | 12 | 834 | 10 | 9 | 9 |
| Kansas City | Missouri | Ray | 8 | 1115 | 9 | 13 | 13 |
| Missouri non-MSA | Missouri | Stone | 24 | 1612 | 9 | 11 | 13 |
| Missouri non-MSA | Missouri | Washington | 39 | 1780 | 9 | 10 | 10 |
| Missouri non-MSA | Missouri | Pulaski | 27 | 2546 | 9 | 24 | 29 |
| Missouri non-MSA | Missouri | Miller | 41 | 2024 | 9 | 12 | 16 |
| Missouri non-MSA | Missouri | Dunklin | 15 | 2083 | 8 | 8 | 12 |
| Missouri non-MSA | Missouri | Texas | 17 | 1339 | 8 | 11 | 12 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1188 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Saline | 23 | 1994 | 7 | 11 | 13 |
| Missouri non-MSA | Missouri | Randolph | 17 | 1599 | 7 | 9 | 12 |
| Missouri non-MSA | Missouri | New Madrid | 31 | 1615 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Livingston | 23 | 1036 | 7 | 7 | 8 |
| Kansas City | Missouri | Clinton | 56 | 1248 | 7 | 9 | 11 |
| Missouri non-MSA | Missouri | Perry | 19 | 1852 | 7 | 7 | 9 |
| Missouri non-MSA | Missouri | Lawrence | 52 | 2293 | 7 | 10 | 11 |
| St. Joseph | Kansas | Doniphan | 7 | 723 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | Pike | 14 | 1275 | 7 | 9 | 11 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 5 | 1412 | 7 | 9 | 10 |
| St. Joseph | Missouri | Andrew | 14 | 1091 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1652 | 6 | 8 | 8 |
| St. Joseph | Missouri | DeKalb | 19 | 780 | 6 | 5 | 5 |
| Springfield | Missouri | Polk | 21 | 1792 | 6 | 8 | 13 |
| Missouri non-MSA | Missouri | Morgan | 24 | 1444 | 6 | 7 | 11 |
| Missouri non-MSA | Missouri | Henry | 22 | 1432 | 6 | 10 | 10 |
| Missouri non-MSA | Missouri | Stoddard | 33 | 2015 | 6 | 6 | 11 |
| Kansas City | Kansas | Linn | 3 | 518 | 6 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1493 | 6 | 8 | 10 |
| Columbia-Jefferson City | Missouri | Moniteau | 17 | 1488 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Barry | 36 | 1781 | 5 | 8 | 10 |
| Missouri non-MSA | Missouri | Harrison | 10 | 633 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Benton | 16 | 1189 | 5 | 6 | 13 |
| Missouri non-MSA | Missouri | Macon | 10 | 916 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Mississippi | 15 | 1137 | 4 | 5 | 8 |
| Missouri non-MSA | Missouri | Iron | 1 | 408 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Ralls | 7 | 660 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Ripley | 8 | 673 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Dent | 8 | 701 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Grundy | 23 | 679 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 458 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 29 | 675 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 498 | 4 | 4 | 4 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 381 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Douglas | 19 | 617 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Barton | 8 | 764 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Lewis | 3 | 539 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Cedar | 8 | 516 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Monroe | 5 | 516 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Gentry | 16 | 604 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Wayne | 6 | 663 | 3 | 4 | 5 |
| Kansas City | Missouri | Caldwell | 5 | 545 | 3 | 4 | 4 |
| Springfield | Missouri | Dallas | 18 | 697 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Carroll | 18 | 650 | 2 | 5 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 21 | 1273 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Oregon | 3 | 532 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 10 | 656 | 2 | 3 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 956 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Chariton | 3 | 332 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Maries | 6 | 463 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Ozark | 4 | 378 | 2 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 617 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Linn | 11 | 417 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Daviess | 9 | 468 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Dade | 9 | 368 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 199 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shelby | 4 | 293 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 4 | 371 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 9 | 425 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 341 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Carter | 6 | 373 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Worth | 1 | 119 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 1 | 131 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 9 | 408 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Putnam | 1 | 199 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 324 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 223 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Atchison | 5 | 260 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 150 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 227 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2286 | 0 | 4 | 9 |
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
