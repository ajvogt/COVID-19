# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/24/2020  
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
| St. Louis-Farmington | 1573 | 61232 | 527 | 558 | 565 |
| Missouri non-MSA | 273 | 23205 | 446 | 407 | 347 |
| Kansas City | 584 | 42332 | 368 | 351 | 352 |
| Springfield | 36 | 8293 | 173 | 172 | 159 |
| Columbia-Jefferson City | 31 | 7536 | 88 | 119 | 136 |
| Joplin | 62 | 5041 | 74 | 75 | 63 |
| Cape Girardeau-Sikeston | 30 | 2820 | 51 | 54 | 42 |
| St. Joseph | 19 | 2303 | 46 | 37 | 29 |
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
| St. Louis-Farmington | Missouri | St. Louis | 788 | 23297 | 150 | 164 | 177 |
| Springfield | Missouri | Greene | 24 | 5701 | 106 | 107 | 108 |
| Kansas City | Kansas | Johnson | 145 | 10411 | 103 | 99 | 100 |
| Kansas City | Missouri | Kansas City | 122 | 10823 | 84 | 69 | 77 |
| St. Louis-Farmington | Missouri | St. Charles | 115 | 7399 | 76 | 75 | 70 |
| St. Louis-Farmington | Missouri | Jefferson | 57 | 4021 | 63 | 59 | 56 |
| St. Louis-Farmington | Illinois | Madison | 131 | 5463 | 53 | 59 | 61 |
| Kansas City | Missouri | Jackson | 92 | 7064 | 52 | 64 | 66 |
| Joplin | Missouri | Jasper | 48 | 3634 | 51 | 57 | 50 |
| St. Louis-Farmington | Illinois | St. Clair | 187 | 6386 | 41 | 43 | 47 |
| Columbia-Jefferson City | Missouri | Boone | 8 | 4504 | 39 | 62 | 85 |
| St. Louis-Farmington | Missouri | St. Louis City | 195 | 6934 | 35 | 32 | 32 |
| St. Joseph | Missouri | Buchanan | 15 | 1834 | 34 | 27 | 21 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 12 | 1588 | 32 | 33 | 24 |
| Kansas City | Kansas | Wyandotte | 134 | 6757 | 32 | 31 | 34 |
| Springfield | Missouri | Christian | 5 | 1314 | 31 | 31 | 25 |
| St. Louis-Farmington | Missouri | Franklin | 28 | 1610 | 31 | 29 | 24 |
| Columbia-Jefferson City | Missouri | Cole | 11 | 1434 | 24 | 27 | 23 |
| Joplin | Missouri | Newton | 14 | 1407 | 23 | 18 | 12 |
| St. Louis-Farmington | Missouri | St. Francois | 9 | 1959 | 23 | 42 | 37 |
| Springfield | Missouri | Webster | 3 | 593 | 21 | 19 | 13 |
| Missouri non-MSA | Missouri | Pettis | 10 | 1065 | 20 | 14 | 10 |
| Missouri non-MSA | Missouri | Camden | 10 | 884 | 20 | 18 | 14 |
| Missouri non-MSA | Missouri | Johnson | 4 | 1046 | 19 | 19 | 16 |
| Kansas City | Missouri | Cass | 23 | 1434 | 18 | 17 | 15 |
| Missouri non-MSA | Missouri | Laclede | 4 | 584 | 18 | 17 | 10 |
| Kansas City | Kansas | Leavenworth | 11 | 1965 | 18 | 15 | 11 |
| Kansas City | Missouri | Lafayette | 2 | 486 | 17 | 14 | 9 |
| Missouri non-MSA | Missouri | Howell | 3 | 556 | 16 | 15 | 11 |
| Missouri non-MSA | Missouri | Pulaski | 5 | 612 | 16 | 12 | 9 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 571 | 15 | 11 | 8 |
| Missouri non-MSA | Missouri | Butler | 6 | 610 | 15 | 12 | 8 |
| Kansas City | Missouri | Clay | 41 | 1760 | 14 | 16 | 16 |
| Missouri non-MSA | Missouri | Wright | 0 | 278 | 14 | 11 | 6 |
| St. Louis-Farmington | Illinois | Clinton | 20 | 1088 | 14 | 14 | 16 |
| Missouri non-MSA | Missouri | Morgan | 1 | 315 | 13 | 10 | 6 |
| Missouri non-MSA | Missouri | Texas | 2 | 298 | 13 | 9 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 7 | 764 | 12 | 12 | 10 |
| Missouri non-MSA | Missouri | Benton | 3 | 275 | 12 | 7 | 4 |
| Missouri non-MSA | Missouri | Taney | 31 | 1157 | 11 | 11 | 9 |
| Missouri non-MSA | Missouri | Phelps | 7 | 440 | 10 | 11 | 9 |
| Missouri non-MSA | Missouri | Miller | 1 | 463 | 10 | 10 | 8 |
| Springfield | Missouri | Polk | 3 | 503 | 10 | 10 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 16 | 837 | 10 | 9 | 9 |
| Kansas City | Missouri | Platte | 10 | 656 | 10 | 8 | 7 |
| Missouri non-MSA | Missouri | Stoddard | 12 | 478 | 10 | 10 | 6 |
| Missouri non-MSA | Missouri | Saline | 9 | 693 | 9 | 7 | 5 |
| St. Louis-Farmington | Illinois | Macoupin | 7 | 515 | 9 | 7 | 7 |
| Missouri non-MSA | Missouri | Perry | 4 | 610 | 9 | 11 | 10 |
| Missouri non-MSA | Missouri | Washington | 10 | 367 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Crawford | 4 | 369 | 8 | 10 | 7 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 602 | 8 | 11 | 11 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 497 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Stone | 4 | 418 | 7 | 6 | 5 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 322 | 7 | 10 | 7 |
| St. Joseph | Missouri | Andrew | 2 | 238 | 7 | 5 | 4 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 733 | 6 | 7 | 7 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 639 | 6 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 404 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Wayne | 0 | 200 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Barry | 6 | 460 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 9 | 729 | 6 | 5 | 14 |
| Kansas City | Kansas | Miami | 1 | 357 | 6 | 5 | 6 |
| St. Louis-Farmington | Missouri | Warren | 0 | 460 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Dent | 1 | 132 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Grundy | 3 | 181 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Randolph | 3 | 227 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Audrain | 2 | 413 | 5 | 5 | 5 |
| St. Louis-Farmington | Illinois | Bond | 4 | 296 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Madison | 0 | 285 | 4 | 4 | 6 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 289 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Vernon | 1 | 167 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Douglas | 3 | 174 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1052 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Macon | 0 | 149 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Carter | 1 | 87 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Marion | 14 | 643 | 4 | 5 | 9 |
| Missouri non-MSA | Missouri | Livingston | 1 | 391 | 4 | 3 | 10 |
| Missouri non-MSA | Missouri | Henry | 4 | 178 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Daviess | 1 | 98 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 187 | 3 | 3 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 14 | 385 | 3 | 4 | 5 |
| Kansas City | Missouri | Clinton | 0 | 210 | 3 | 3 | 3 |
| St. Joseph | Missouri | DeKalb | 2 | 126 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 57 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 0 | 117 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Cedar | 0 | 95 | 3 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 182 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 16 | 511 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Pike | 3 | 233 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Barton | 0 | 178 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Shannon | 1 | 89 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 102 | 2 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Osage | 2 | 136 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 326 | 2 | 3 | 4 |
| Kansas City | Missouri | Caldwell | 1 | 79 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 291 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ripley | 1 | 153 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 18 | 158 | 2 | 2 | 3 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 47 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 82 | 1 | 1 | 1 |
| Kansas City | Missouri | Bates | 2 | 101 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 67 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 121 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 38 | 1 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 73 | 1 | 1 | 1 |
| Kansas City | Missouri | Ray | 0 | 159 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 74 | 1 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 105 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 54 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 167 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Lewis | 2 | 81 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 2 | 88 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 57 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 50 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Carroll | 1 | 137 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 145 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 31 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 70 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 86 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 61 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 61 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 103 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 49 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 1 | 75 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 185 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 44 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 28 | 0 | 0 | 0 |
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
