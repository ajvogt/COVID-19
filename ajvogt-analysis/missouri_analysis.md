# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/19/2020  
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
| St. Louis-Farmington | 1540 | 58718 | 603 | 559 | 577 |
| Missouri non-MSA | 227 | 21158 | 424 | 367 | 314 |
| Kansas City | 549 | 40680 | 361 | 338 | 364 |
| Springfield | 26 | 7474 | 184 | 169 | 146 |
| Columbia-Jefferson City | 24 | 7142 | 143 | 141 | 137 |
| Joplin | 57 | 4737 | 77 | 73 | 58 |
| Cape Girardeau-Sikeston | 27 | 2588 | 54 | 50 | 38 |
| St. Joseph | 16 | 2084 | 38 | 30 | 24 |
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
| St. Louis-Farmington | Missouri | St. Louis | 780 | 22556 | 173 | 170 | 182 |
| Springfield | Missouri | Greene | 19 | 5197 | 112 | 111 | 103 |
| Kansas City | Kansas | Johnson | 141 | 9957 | 104 | 95 | 107 |
| Kansas City | Missouri | Jackson | 92 | 6912 | 85 | 78 | 71 |
| St. Louis-Farmington | Missouri | St. Charles | 108 | 7019 | 78 | 72 | 69 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 4328 | 78 | 82 | 87 |
| St. Louis-Farmington | Missouri | St. Francois | 8 | 1868 | 67 | 47 | 40 |
| St. Louis-Farmington | Missouri | Jefferson | 50 | 3740 | 64 | 59 | 55 |
| St. Louis-Farmington | Illinois | Madison | 130 | 5231 | 64 | 60 | 64 |
| Joplin | Missouri | Jasper | 43 | 3432 | 61 | 60 | 47 |
| Kansas City | Missouri | Kansas City | 101 | 10374 | 49 | 56 | 80 |
| Springfield | Missouri | Christian | 3 | 1178 | 37 | 30 | 22 |
| St. Louis-Farmington | Illinois | St. Clair | 182 | 6184 | 37 | 43 | 51 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 9 | 1431 | 34 | 28 | 21 |
| St. Louis-Farmington | Missouri | Franklin | 26 | 1461 | 32 | 25 | 22 |
| St. Louis-Farmington | Missouri | St. Louis City | 195 | 6750 | 31 | 29 | 34 |
| Kansas City | Kansas | Wyandotte | 133 | 6612 | 31 | 30 | 37 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1328 | 29 | 28 | 23 |
| Missouri non-MSA | Missouri | Johnson | 4 | 969 | 27 | 24 | 14 |
| St. Joseph | Missouri | Buchanan | 13 | 1664 | 26 | 21 | 16 |
| Springfield | Missouri | Webster | 2 | 486 | 20 | 15 | 10 |
| Kansas City | Missouri | Cass | 17 | 1360 | 20 | 17 | 15 |
| Kansas City | Missouri | Clay | 40 | 1700 | 19 | 17 | 17 |
| Joplin | Missouri | Newton | 14 | 1305 | 16 | 12 | 11 |
| Missouri non-MSA | Missouri | Laclede | 3 | 489 | 16 | 12 | 8 |
| Missouri non-MSA | Missouri | Camden | 10 | 767 | 16 | 13 | 11 |
| Missouri non-MSA | Missouri | Crawford | 2 | 339 | 15 | 8 | 7 |
| Missouri non-MSA | Missouri | Howell | 3 | 484 | 15 | 13 | 10 |
| Kansas City | Kansas | Leavenworth | 10 | 1877 | 15 | 12 | 10 |
| Missouri non-MSA | Missouri | Pettis | 8 | 974 | 14 | 10 | 9 |
| St. Louis-Farmington | Illinois | Clinton | 20 | 1022 | 14 | 15 | 16 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 709 | 13 | 11 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 434 | 13 | 9 | 6 |
| Missouri non-MSA | Missouri | Wright | 0 | 217 | 12 | 8 | 4 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 562 | 12 | 12 | 11 |
| Kansas City | Missouri | Lafayette | 2 | 377 | 12 | 8 | 5 |
| Missouri non-MSA | Missouri | Texas | 2 | 261 | 12 | 10 | 6 |
| Missouri non-MSA | Missouri | Pulaski | 5 | 530 | 12 | 8 | 7 |
| Missouri non-MSA | Missouri | Miller | 1 | 420 | 11 | 10 | 8 |
| Missouri non-MSA | Missouri | Taney | 24 | 1102 | 11 | 11 | 10 |
| Missouri non-MSA | Missouri | Perry | 4 | 558 | 11 | 9 | 9 |
| Missouri non-MSA | Missouri | Phelps | 1 | 384 | 10 | 10 | 8 |
| Missouri non-MSA | Missouri | Morgan | 1 | 256 | 10 | 8 | 5 |
| Missouri non-MSA | Missouri | Butler | 4 | 531 | 10 | 9 | 6 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 494 | 10 | 8 | 6 |
| Cape Girardeau-Sikeston | Missouri | Scott | 16 | 797 | 10 | 9 | 9 |
| Springfield | Missouri | Polk | 1 | 446 | 10 | 8 | 6 |
| Missouri non-MSA | Missouri | Audrain | 2 | 398 | 9 | 6 | 5 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 295 | 8 | 10 | 6 |
| Missouri non-MSA | Missouri | Benton | 2 | 226 | 8 | 4 | 3 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 700 | 8 | 7 | 7 |
| Kansas City | Missouri | Platte | 10 | 619 | 8 | 7 | 6 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 368 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Grundy | 2 | 164 | 7 | 6 | 4 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 271 | 7 | 5 | 3 |
| St. Louis-Farmington | Illinois | Bond | 4 | 276 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Stone | 4 | 383 | 7 | 5 | 5 |
| St. Louis-Farmington | Missouri | Warren | 0 | 429 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Marion | 11 | 625 | 7 | 8 | 11 |
| Missouri non-MSA | Missouri | Dent | 0 | 116 | 6 | 5 | 3 |
| St. Louis-Farmington | Illinois | Macoupin | 6 | 470 | 6 | 5 | 7 |
| Missouri non-MSA | Missouri | Pike | 3 | 219 | 6 | 5 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 455 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Wayne | 0 | 165 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Nodaway | 8 | 707 | 6 | 7 | 15 |
| Missouri non-MSA | Missouri | Saline | 9 | 643 | 6 | 5 | 4 |
| St. Joseph | Missouri | Andrew | 1 | 206 | 6 | 4 | 3 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 605 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Randolph | 2 | 201 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Macon | 0 | 130 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Madison | 0 | 263 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Adair | 0 | 317 | 4 | 4 | 4 |
| Kansas City | Kansas | Miami | 1 | 314 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Barry | 6 | 429 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Barton | 0 | 162 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Ozark | 0 | 105 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Livingston | 1 | 375 | 4 | 7 | 10 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 169 | 4 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 163 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Vernon | 1 | 147 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Washington | 4 | 319 | 3 | 4 | 5 |
| Springfield | Missouri | Dallas | 1 | 167 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1036 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 281 | 3 | 2 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 13 | 373 | 3 | 4 | 6 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 122 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Douglas | 3 | 155 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 93 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 14 | 495 | 3 | 4 | 5 |
| St. Joseph | Missouri | DeKalb | 2 | 109 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 15 | 152 | 2 | 3 | 3 |
| Kansas City | Missouri | Ray | 0 | 156 | 2 | 2 | 1 |
| Kansas City | Missouri | Clinton | 0 | 193 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Carter | 1 | 65 | 2 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 105 | 2 | 1 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 69 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 4 | 155 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Hickory | 2 | 85 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Daviess | 0 | 76 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 81 | 2 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 94 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 1 | 75 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carroll | 1 | 132 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 116 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 136 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 67 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 138 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 75 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 59 | 1 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 66 | 1 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 65 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 99 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 59 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 39 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 46 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 85 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 43 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 71 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 184 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 73 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 34 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 56 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 18 | 0 | 0 | 0 |
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
