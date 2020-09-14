# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/14/2020  
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
| St. Louis-Farmington | 1497 | 56002 | 556 | 580 | 590 |
| Missouri non-MSA | 191 | 19030 | 311 | 328 | 278 |
| Kansas City | 520 | 38819 | 306 | 332 | 366 |
| Springfield | 26 | 6601 | 162 | 164 | 132 |
| Columbia-Jefferson City | 24 | 6593 | 137 | 165 | 132 |
| Joplin | 53 | 4324 | 73 | 65 | 50 |
| Cape Girardeau-Sikeston | 26 | 2332 | 54 | 41 | 34 |
| St. Joseph | 16 | 1909 | 26 | 25 | 20 |
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
| St. Louis-Farmington | Missouri | St. Louis | 768 | 21831 | 179 | 182 | 189 |
| Springfield | Missouri | Greene | 19 | 4660 | 108 | 115 | 96 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 4071 | 85 | 111 | 84 |
| Kansas City | Kansas | Johnson | 134 | 9428 | 82 | 93 | 106 |
| St. Louis-Farmington | Missouri | St. Charles | 105 | 6660 | 74 | 69 | 71 |
| Kansas City | Missouri | Jackson | 87 | 6473 | 67 | 72 | 67 |
| Joplin | Missouri | Jasper | 40 | 3110 | 62 | 55 | 40 |
| Kansas City | Missouri | Kansas City | 96 | 10146 | 60 | 68 | 90 |
| St. Louis-Farmington | Illinois | Madison | 119 | 4908 | 58 | 66 | 64 |
| St. Louis-Farmington | Missouri | Jefferson | 47 | 3425 | 51 | 54 | 53 |
| St. Louis-Farmington | Illinois | St. Clair | 178 | 5983 | 44 | 52 | 56 |
| St. Louis-Farmington | Missouri | St. Francois | 7 | 1606 | 44 | 40 | 37 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 9 | 1276 | 30 | 22 | 18 |
| Springfield | Missouri | Christian | 3 | 1025 | 29 | 26 | 20 |
| St. Louis-Farmington | Missouri | St. Louis City | 192 | 6608 | 29 | 32 | 37 |
| Kansas City | Kansas | Wyandotte | 124 | 6451 | 28 | 31 | 43 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1198 | 26 | 26 | 23 |
| St. Louis-Farmington | Missouri | Franklin | 23 | 1329 | 24 | 22 | 20 |
| Missouri non-MSA | Missouri | Johnson | 4 | 853 | 22 | 18 | 11 |
| St. Joseph | Missouri | Buchanan | 13 | 1547 | 19 | 17 | 14 |
| Kansas City | Missouri | Cass | 16 | 1255 | 16 | 13 | 14 |
| Kansas City | Missouri | Clay | 39 | 1608 | 16 | 17 | 16 |
| St. Louis-Farmington | Illinois | Clinton | 19 | 950 | 15 | 18 | 16 |
| Springfield | Missouri | Webster | 2 | 379 | 13 | 11 | 7 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 250 | 13 | 8 | 5 |
| Missouri non-MSA | Missouri | Taney | 22 | 1050 | 12 | 10 | 12 |
| Missouri non-MSA | Missouri | Camden | 9 | 683 | 12 | 11 | 9 |
| Joplin | Missouri | Newton | 13 | 1214 | 11 | 9 | 9 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 506 | 11 | 12 | 11 |
| Missouri non-MSA | Missouri | Laclede | 1 | 402 | 10 | 8 | 6 |
| Missouri non-MSA | Missouri | Perry | 4 | 516 | 10 | 9 | 8 |
| Missouri non-MSA | Missouri | Phelps | 1 | 338 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 636 | 9 | 10 | 8 |
| Kansas City | Kansas | Leavenworth | 9 | 1771 | 9 | 9 | 8 |
| Missouri non-MSA | Missouri | Howell | 3 | 396 | 9 | 10 | 7 |
| Missouri non-MSA | Missouri | Butler | 4 | 484 | 9 | 7 | 6 |
| Cape Girardeau-Sikeston | Missouri | Scott | 15 | 746 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | Miller | 1 | 355 | 8 | 7 | 7 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 581 | 8 | 9 | 8 |
| Springfield | Missouri | Polk | 1 | 390 | 7 | 7 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 426 | 7 | 7 | 5 |
| Missouri non-MSA | Missouri | Marion | 7 | 595 | 7 | 9 | 11 |
| Kansas City | Missouri | Lafayette | 2 | 320 | 7 | 6 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 335 | 7 | 8 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 441 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Morgan | 1 | 199 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Pettis | 8 | 894 | 6 | 7 | 9 |
| St. Louis-Farmington | Missouri | Lincoln | 2 | 666 | 6 | 7 | 8 |
| Kansas City | Missouri | Platte | 10 | 571 | 6 | 6 | 5 |
| St. Louis-Farmington | Missouri | Warren | 0 | 402 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Wayne | 0 | 145 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Texas | 2 | 197 | 6 | 7 | 4 |
| Kansas City | Kansas | Miami | 1 | 282 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Grundy | 1 | 130 | 5 | 6 | 3 |
| Missouri non-MSA | Missouri | Madison | 0 | 238 | 5 | 7 | 6 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 358 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Nodaway | 7 | 677 | 5 | 20 | 15 |
| Missouri non-MSA | Missouri | Wright | 0 | 147 | 5 | 4 | 2 |
| St. Louis-Farmington | Illinois | Macoupin | 6 | 432 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Stone | 2 | 348 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Pulaski | 3 | 460 | 5 | 5 | 6 |
| St. Louis-Farmington | Illinois | Jersey | 12 | 356 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 6 | 135 | 5 | 2 | 3 |
| Missouri non-MSA | Missouri | Pike | 2 | 189 | 4 | 3 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 182 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 12 | 479 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Crawford | 2 | 249 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Saline | 9 | 617 | 4 | 5 | 4 |
| St. Joseph | Missouri | Andrew | 1 | 180 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Barry | 5 | 409 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Audrain | 2 | 344 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Barton | 0 | 145 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Washington | 1 | 298 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Dent | 0 | 84 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Ripley | 0 | 132 | 4 | 3 | 2 |
| St. Louis-Farmington | Illinois | Bond | 4 | 231 | 3 | 6 | 5 |
| Springfield | Missouri | Dallas | 1 | 147 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 292 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Daviess | 0 | 66 | 3 | 3 | 1 |
| Kansas City | Missouri | Clinton | 0 | 179 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Vernon | 0 | 127 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 151 | 2 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 225 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 0 | 82 | 2 | 4 | 2 |
| Missouri non-MSA | Missouri | Douglas | 3 | 137 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 104 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | McDonald | 10 | 1016 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 263 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Benton | 1 | 180 | 2 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 109 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Henry | 4 | 145 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 80 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 134 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Livingston | 1 | 351 | 1 | 19 | 9 |
| St. Joseph | Missouri | DeKalb | 2 | 93 | 1 | 2 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 89 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 70 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 149 | 1 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 60 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 94 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 1 | 67 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 50 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 59 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Carroll | 1 | 126 | 1 | 1 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 56 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 108 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 41 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 67 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 82 | 0 | 1 | 1 |
| Kansas City | Missouri | Ray | 0 | 140 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 2 | 72 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 42 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 33 | 0 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 82 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 54 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 56 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 69 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 184 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Mercer | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 72 | 0 | 0 | 1 |
| Kansas City | Kansas | Linn | 0 | 57 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 34 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 28 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 43 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 48 | 0 | 0 | 0 |
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
