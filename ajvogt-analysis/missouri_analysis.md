# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/25/2020  
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
| St. Louis-Farmington | 1588 | 61657 | 504 | 554 | 561 |
| Missouri non-MSA | 276 | 23615 | 430 | 414 | 356 |
| Kansas City | 585 | 42681 | 363 | 352 | 356 |
| Springfield | 37 | 8480 | 173 | 174 | 162 |
| Columbia-Jefferson City | 31 | 7666 | 90 | 119 | 138 |
| Joplin | 63 | 5116 | 70 | 73 | 65 |
| St. Joseph | 19 | 2340 | 46 | 39 | 30 |
| Cape Girardeau-Sikeston | 30 | 2873 | 45 | 55 | 43 |
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
| St. Louis-Farmington | Missouri | St. Louis | 795 | 23427 | 148 | 160 | 173 |
| Kansas City | Kansas | Johnson | 146 | 10556 | 106 | 102 | 102 |
| Springfield | Missouri | Greene | 25 | 5807 | 105 | 107 | 109 |
| Kansas City | Missouri | Kansas City | 123 | 10909 | 91 | 69 | 79 |
| St. Louis-Farmington | Missouri | St. Charles | 115 | 7459 | 74 | 76 | 70 |
| St. Louis-Farmington | Missouri | Jefferson | 57 | 4054 | 56 | 60 | 56 |
| St. Louis-Farmington | Illinois | Madison | 136 | 5511 | 51 | 58 | 61 |
| Joplin | Missouri | Jasper | 49 | 3685 | 48 | 54 | 51 |
| St. Louis-Farmington | Illinois | St. Clair | 188 | 6421 | 39 | 40 | 47 |
| Kansas City | Missouri | Jackson | 92 | 7064 | 38 | 59 | 64 |
| Columbia-Jefferson City | Missouri | Boone | 8 | 4548 | 37 | 60 | 85 |
| St. Joseph | Missouri | Buchanan | 15 | 1867 | 34 | 29 | 22 |
| St. Louis-Farmington | Missouri | St. Louis City | 196 | 6964 | 34 | 32 | 32 |
| Kansas City | Kansas | Wyandotte | 134 | 6804 | 33 | 31 | 35 |
| St. Louis-Farmington | Missouri | Franklin | 28 | 1642 | 30 | 29 | 25 |
| Springfield | Missouri | Christian | 5 | 1344 | 30 | 32 | 26 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 12 | 1620 | 29 | 33 | 25 |
| Columbia-Jefferson City | Missouri | Cole | 11 | 1481 | 27 | 28 | 25 |
| Joplin | Missouri | Newton | 14 | 1431 | 22 | 18 | 13 |
| Missouri non-MSA | Missouri | Camden | 10 | 902 | 22 | 18 | 14 |
| Missouri non-MSA | Missouri | Pettis | 11 | 1077 | 21 | 15 | 11 |
| Springfield | Missouri | Webster | 3 | 607 | 19 | 19 | 14 |
| Kansas City | Kansas | Leavenworth | 11 | 1965 | 18 | 15 | 11 |
| St. Louis-Farmington | Missouri | St. Francois | 9 | 1973 | 18 | 42 | 37 |
| Kansas City | Missouri | Cass | 22 | 1457 | 17 | 18 | 16 |
| Missouri non-MSA | Missouri | Laclede | 4 | 595 | 17 | 17 | 10 |
| Missouri non-MSA | Missouri | Pulaski | 5 | 632 | 17 | 14 | 9 |
| Kansas City | Missouri | Lafayette | 2 | 489 | 17 | 14 | 9 |
| Missouri non-MSA | Missouri | Howell | 3 | 578 | 15 | 14 | 12 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 584 | 15 | 11 | 8 |
| Springfield | Missouri | Polk | 3 | 537 | 14 | 12 | 9 |
| Kansas City | Missouri | Clay | 41 | 1773 | 14 | 16 | 16 |
| Missouri non-MSA | Missouri | Johnson | 4 | 1065 | 14 | 21 | 17 |
| Missouri non-MSA | Missouri | Butler | 6 | 617 | 14 | 12 | 8 |
| St. Louis-Farmington | Illinois | Clinton | 20 | 1101 | 13 | 14 | 15 |
| Missouri non-MSA | Missouri | Wright | 0 | 293 | 13 | 12 | 7 |
| Missouri non-MSA | Missouri | Benton | 3 | 289 | 12 | 8 | 4 |
| Missouri non-MSA | Missouri | Morgan | 1 | 320 | 12 | 10 | 7 |
| Missouri non-MSA | Missouri | Taney | 31 | 1172 | 11 | 11 | 10 |
| Kansas City | Missouri | Platte | 10 | 669 | 11 | 8 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 7 | 769 | 10 | 12 | 10 |
| Missouri non-MSA | Missouri | Phelps | 8 | 451 | 10 | 11 | 9 |
| Missouri non-MSA | Missouri | Texas | 2 | 305 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Miller | 1 | 475 | 10 | 10 | 8 |
| Missouri non-MSA | Missouri | Saline | 9 | 704 | 9 | 7 | 5 |
| Missouri non-MSA | Missouri | Stoddard | 12 | 484 | 9 | 10 | 7 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 618 | 9 | 11 | 11 |
| St. Louis-Farmington | Illinois | Macoupin | 7 | 523 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Washington | 10 | 376 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Perry | 6 | 614 | 8 | 10 | 10 |
| Missouri non-MSA | Missouri | Crawford | 4 | 388 | 8 | 11 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 16 | 846 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 499 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Stone | 4 | 430 | 7 | 7 | 6 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 410 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Wayne | 0 | 205 | 6 | 6 | 4 |
| St. Joseph | Missouri | Andrew | 2 | 241 | 6 | 6 | 4 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 333 | 6 | 11 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 738 | 6 | 7 | 7 |
| Kansas City | Kansas | Miami | 1 | 357 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Barry | 6 | 461 | 5 | 5 | 4 |
| St. Louis-Farmington | Missouri | Warren | 0 | 464 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 9 | 738 | 5 | 5 | 14 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 642 | 5 | 6 | 7 |
| St. Louis-Farmington | Illinois | Bond | 5 | 304 | 5 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 295 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Randolph | 3 | 231 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Macon | 0 | 153 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Carter | 1 | 93 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Daviess | 1 | 106 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Henry | 4 | 184 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Dent | 1 | 139 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Madison | 0 | 288 | 4 | 4 | 7 |
| Kansas City | Missouri | Clinton | 0 | 221 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Audrain | 2 | 416 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Livingston | 1 | 396 | 4 | 3 | 10 |
| Missouri non-MSA | Missouri | Marion | 14 | 649 | 4 | 5 | 9 |
| Missouri non-MSA | Missouri | Douglas | 3 | 178 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 64 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Vernon | 1 | 169 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 192 | 3 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Osage | 2 | 145 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Cedar | 0 | 102 | 3 | 2 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 14 | 387 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Ripley | 0 | 157 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 16 | 516 | 3 | 3 | 5 |
| St. Joseph | Missouri | DeKalb | 2 | 127 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ozark | 0 | 121 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Oregon | 0 | 110 | 3 | 2 | 2 |
| Springfield | Missouri | Dallas | 1 | 185 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Grundy | 3 | 179 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | Shannon | 1 | 93 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1051 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Pike | 3 | 234 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Barton | 0 | 178 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 330 | 2 | 3 | 4 |
| Kansas City | Missouri | Caldwell | 1 | 82 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 292 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 1 | 72 | 2 | 1 | 0 |
| Kansas City | Missouri | Bates | 2 | 104 | 1 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 47 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 56 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 59 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 82 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 2 | 89 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 39 | 1 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 105 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 74 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 18 | 157 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Maries | 0 | 75 | 1 | 1 | 1 |
| Kansas City | Missouri | Ray | 0 | 161 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 0 | 51 | 1 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 169 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Gentry | 9 | 118 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 145 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 82 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 106 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carroll | 1 | 138 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 63 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 31 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 70 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 50 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 1 | 75 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 87 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 61 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 185 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 22 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
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
