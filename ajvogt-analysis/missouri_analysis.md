# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/18/2020  
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
| St. Louis-Farmington | 1526 | 58127 | 604 | 576 | 577 |
| Missouri non-MSA | 216 | 20599 | 398 | 360 | 305 |
| Kansas City | 545 | 40135 | 342 | 324 | 357 |
| Springfield | 26 | 7266 | 176 | 169 | 143 |
| Columbia-Jefferson City | 24 | 7030 | 148 | 149 | 137 |
| Joplin | 56 | 4622 | 75 | 72 | 55 |
| Cape Girardeau-Sikeston | 26 | 2552 | 65 | 50 | 38 |
| St. Joseph | 16 | 2016 | 33 | 28 | 22 |
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
| St. Louis-Farmington | Missouri | St. Louis | 776 | 22386 | 171 | 167 | 180 |
| Springfield | Missouri | Greene | 19 | 5068 | 109 | 114 | 102 |
| Kansas City | Kansas | Johnson | 140 | 9814 | 99 | 93 | 105 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 4288 | 84 | 92 | 88 |
| Kansas City | Missouri | Jackson | 90 | 6796 | 80 | 73 | 69 |
| St. Louis-Farmington | Missouri | St. Charles | 108 | 6940 | 79 | 71 | 71 |
| St. Louis-Farmington | Missouri | St. Francois | 7 | 1847 | 67 | 50 | 41 |
| St. Louis-Farmington | Illinois | Madison | 130 | 5154 | 65 | 66 | 63 |
| St. Louis-Farmington | Missouri | Jefferson | 49 | 3659 | 64 | 57 | 54 |
| Joplin | Missouri | Jasper | 42 | 3348 | 60 | 61 | 45 |
| Kansas City | Missouri | Kansas City | 101 | 10271 | 48 | 53 | 80 |
| St. Louis-Farmington | Illinois | St. Clair | 180 | 6144 | 41 | 49 | 53 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 9 | 1413 | 37 | 29 | 21 |
| Springfield | Missouri | Christian | 3 | 1132 | 34 | 27 | 22 |
| St. Louis-Farmington | Missouri | St. Louis City | 192 | 6722 | 31 | 29 | 34 |
| Kansas City | Kansas | Wyandotte | 133 | 6569 | 29 | 30 | 37 |
| St. Louis-Farmington | Missouri | Franklin | 23 | 1426 | 29 | 23 | 21 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1289 | 28 | 26 | 22 |
| Missouri non-MSA | Missouri | Johnson | 4 | 966 | 28 | 25 | 14 |
| St. Joseph | Missouri | Buchanan | 13 | 1623 | 24 | 20 | 16 |
| Springfield | Missouri | Webster | 2 | 468 | 19 | 15 | 10 |
| Kansas City | Missouri | Clay | 40 | 1672 | 18 | 16 | 16 |
| Kansas City | Missouri | Cass | 16 | 1333 | 18 | 16 | 14 |
| Missouri non-MSA | Missouri | Laclede | 3 | 472 | 17 | 11 | 7 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 287 | 15 | 10 | 6 |
| Joplin | Missouri | Newton | 14 | 1274 | 15 | 11 | 10 |
| Missouri non-MSA | Missouri | Crawford | 2 | 330 | 15 | 8 | 7 |
| St. Louis-Farmington | Illinois | Clinton | 20 | 1004 | 14 | 16 | 16 |
| Missouri non-MSA | Missouri | Camden | 10 | 747 | 14 | 13 | 11 |
| Missouri non-MSA | Missouri | Howell | 3 | 467 | 13 | 12 | 9 |
| Kansas City | Kansas | Leavenworth | 10 | 1839 | 13 | 11 | 9 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 553 | 13 | 13 | 11 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 693 | 13 | 10 | 9 |
| Missouri non-MSA | Missouri | Perry | 4 | 554 | 12 | 9 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 418 | 12 | 8 | 5 |
| Missouri non-MSA | Missouri | Taney | 22 | 1091 | 11 | 11 | 10 |
| Kansas City | Missouri | Lafayette | 2 | 368 | 11 | 7 | 5 |
| Missouri non-MSA | Missouri | Phelps | 1 | 376 | 11 | 9 | 8 |
| Missouri non-MSA | Missouri | Wright | 0 | 197 | 11 | 7 | 4 |
| Missouri non-MSA | Missouri | Butler | 4 | 519 | 11 | 9 | 6 |
| Missouri non-MSA | Missouri | Miller | 1 | 405 | 10 | 9 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 15 | 788 | 10 | 9 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 5 | 509 | 10 | 7 | 7 |
| Springfield | Missouri | Polk | 1 | 434 | 9 | 8 | 6 |
| Missouri non-MSA | Missouri | Texas | 2 | 231 | 8 | 8 | 5 |
| Missouri non-MSA | Missouri | Pettis | 8 | 927 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | Morgan | 1 | 235 | 8 | 7 | 4 |
| Missouri non-MSA | Missouri | Grundy | 2 | 158 | 8 | 6 | 4 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 694 | 8 | 6 | 8 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 475 | 8 | 7 | 6 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 362 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Audrain | 2 | 386 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Stone | 4 | 375 | 7 | 5 | 5 |
| St. Louis-Farmington | Illinois | Bond | 4 | 266 | 7 | 7 | 5 |
| St. Louis-Farmington | Missouri | Warren | 0 | 424 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Wayne | 0 | 157 | 7 | 4 | 2 |
| Missouri non-MSA | Missouri | Marion | 7 | 620 | 6 | 8 | 11 |
| Missouri non-MSA | Missouri | Dent | 0 | 106 | 6 | 4 | 2 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 603 | 6 | 9 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 258 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Pike | 3 | 215 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 443 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 8 | 698 | 6 | 7 | 15 |
| St. Louis-Farmington | Illinois | Macoupin | 6 | 461 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Saline | 9 | 635 | 5 | 5 | 5 |
| Kansas City | Missouri | Platte | 10 | 592 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Randolph | 2 | 196 | 5 | 4 | 3 |
| St. Joseph | Missouri | Andrew | 1 | 194 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Barton | 0 | 161 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Washington | 3 | 314 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Benton | 2 | 200 | 5 | 3 | 2 |
| Kansas City | Kansas | Miami | 1 | 314 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Madison | 0 | 255 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Barry | 6 | 420 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 12 | 493 | 4 | 4 | 6 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 161 | 4 | 2 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 313 | 4 | 4 | 4 |
| St. Louis-Farmington | Illinois | Jersey | 13 | 362 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Ozark | 0 | 99 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Macon | 0 | 119 | 4 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 164 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Livingston | 1 | 367 | 3 | 20 | 10 |
| Missouri non-MSA | Missouri | Vernon | 0 | 141 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 165 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | McDonald | 10 | 1031 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 15 | 148 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 277 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Douglas | 3 | 149 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Daviess | 0 | 73 | 3 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 119 | 2 | 2 | 1 |
| Kansas City | Missouri | Clinton | 0 | 190 | 2 | 3 | 2 |
| St. Joseph | Missouri | DeKalb | 2 | 104 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 88 | 2 | 2 | 2 |
| Kansas City | Missouri | Ray | 0 | 153 | 2 | 1 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 66 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 59 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 1 | 73 | 1 | 1 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 64 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 77 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 4 | 151 | 1 | 2 | 1 |
| Kansas City | Missouri | Bates | 1 | 92 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 133 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 66 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 138 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Carroll | 1 | 131 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 75 | 1 | 1 | 0 |
| Kansas City | Kansas | Linn | 0 | 66 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 99 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 58 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 2 | 78 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 59 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 44 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 110 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 84 | 0 | 0 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 95 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 42 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 43 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 71 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 57 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 28 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 184 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 46 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 72 | 0 | 0 | 0 |
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
