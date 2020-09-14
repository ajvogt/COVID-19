# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/13/2020  
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
| St. Louis-Farmington | 1496 | 55239 | 529 | 565 | 590 |
| Kansas City | 516 | 38558 | 313 | 334 | 373 |
| Missouri non-MSA | 191 | 18653 | 300 | 318 | 276 |
| Springfield | 26 | 6494 | 165 | 165 | 130 |
| Columbia-Jefferson City | 24 | 6365 | 129 | 162 | 126 |
| Joplin | 52 | 4274 | 70 | 65 | 49 |
| Cape Girardeau-Sikeston | 26 | 2269 | 48 | 39 | 34 |
| St. Joseph | 16 | 1873 | 26 | 24 | 19 |
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
| St. Louis-Farmington | Missouri | St. Louis | 768 | 21588 | 176 | 179 | 190 |
| Springfield | Missouri | Greene | 19 | 4585 | 111 | 117 | 94 |
| Kansas City | Kansas | Johnson | 134 | 9355 | 89 | 93 | 107 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 3918 | 79 | 111 | 80 |
| St. Louis-Farmington | Missouri | St. Charles | 105 | 6559 | 69 | 66 | 71 |
| Kansas City | Missouri | Jackson | 85 | 6407 | 66 | 72 | 68 |
| Kansas City | Missouri | Kansas City | 96 | 10088 | 63 | 69 | 93 |
| St. Louis-Farmington | Illinois | Madison | 118 | 4872 | 60 | 65 | 67 |
| Joplin | Missouri | Jasper | 39 | 3068 | 59 | 55 | 39 |
| St. Louis-Farmington | Missouri | Jefferson | 47 | 3369 | 52 | 56 | 53 |
| St. Louis-Farmington | Illinois | St. Clair | 178 | 5966 | 45 | 52 | 58 |
| Springfield | Missouri | Christian | 3 | 1003 | 29 | 26 | 20 |
| Kansas City | Kansas | Wyandotte | 122 | 6432 | 29 | 32 | 44 |
| St. Louis-Farmington | Missouri | St. Louis City | 192 | 6568 | 28 | 34 | 37 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1172 | 27 | 25 | 23 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 9 | 1239 | 26 | 21 | 17 |
| St. Louis-Farmington | Missouri | St. Francois | 7 | 1434 | 25 | 31 | 32 |
| Missouri non-MSA | Missouri | Johnson | 4 | 800 | 22 | 15 | 9 |
| St. Louis-Farmington | Missouri | Franklin | 23 | 1282 | 21 | 20 | 20 |
| St. Joseph | Missouri | Buchanan | 13 | 1521 | 19 | 17 | 13 |
| Kansas City | Missouri | Cass | 16 | 1243 | 16 | 13 | 14 |
| Kansas City | Missouri | Clay | 39 | 1589 | 15 | 16 | 16 |
| St. Louis-Farmington | Illinois | Clinton | 19 | 936 | 14 | 17 | 16 |
| Springfield | Missouri | Webster | 2 | 370 | 13 | 11 | 7 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 241 | 12 | 8 | 5 |
| Missouri non-MSA | Missouri | Camden | 9 | 672 | 12 | 11 | 9 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 492 | 12 | 12 | 10 |
| Missouri non-MSA | Missouri | Taney | 22 | 1034 | 11 | 9 | 11 |
| Joplin | Missouri | Newton | 13 | 1206 | 10 | 9 | 9 |
| Missouri non-MSA | Missouri | Phelps | 1 | 328 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Laclede | 1 | 392 | 10 | 7 | 6 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 628 | 10 | 11 | 9 |
| Missouri non-MSA | Missouri | Perry | 4 | 503 | 9 | 9 | 8 |
| Kansas City | Kansas | Leavenworth | 9 | 1771 | 9 | 9 | 8 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 574 | 9 | 9 | 8 |
| Missouri non-MSA | Missouri | Butler | 4 | 473 | 9 | 7 | 5 |
| Missouri non-MSA | Missouri | Howell | 3 | 386 | 8 | 10 | 7 |
| Missouri non-MSA | Missouri | Miller | 1 | 350 | 8 | 8 | 7 |
| Missouri non-MSA | Missouri | Nodaway | 7 | 670 | 7 | 20 | 15 |
| Springfield | Missouri | Polk | 1 | 390 | 7 | 7 | 5 |
| Cape Girardeau-Sikeston | Missouri | Scott | 15 | 732 | 7 | 9 | 10 |
| Missouri non-MSA | Missouri | Marion | 7 | 583 | 7 | 9 | 11 |
| Missouri non-MSA | Missouri | Pettis | 8 | 882 | 7 | 6 | 9 |
| Kansas City | Missouri | Lafayette | 2 | 314 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 415 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 434 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Morgan | 1 | 189 | 6 | 5 | 3 |
| Kansas City | Missouri | Platte | 10 | 568 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Texas | 2 | 185 | 6 | 6 | 4 |
| St. Louis-Farmington | Missouri | Warren | 0 | 397 | 6 | 5 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 6 | 432 | 5 | 6 | 7 |
| Kansas City | Kansas | Miami | 1 | 282 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Madison | 0 | 238 | 5 | 8 | 6 |
| Missouri non-MSA | Missouri | Grundy | 1 | 126 | 5 | 6 | 3 |
| St. Louis-Farmington | Missouri | Lincoln | 2 | 650 | 5 | 7 | 7 |
| St. Louis-Farmington | Illinois | Jersey | 12 | 353 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Stone | 2 | 342 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 353 | 4 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 314 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Saline | 9 | 614 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Washington | 1 | 295 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Pike | 2 | 186 | 4 | 3 | 1 |
| Missouri non-MSA | Missouri | New Madrid | 12 | 475 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 6 | 133 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Barry | 5 | 406 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Wayne | 0 | 131 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Pulaski | 3 | 451 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Audrain | 2 | 340 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Wright | 0 | 133 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Dent | 0 | 80 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Barton | 0 | 142 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 290 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Randolph | 1 | 171 | 3 | 4 | 3 |
| St. Joseph | Missouri | Andrew | 1 | 172 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ripley | 0 | 127 | 3 | 2 | 2 |
| Springfield | Missouri | Dallas | 1 | 146 | 3 | 2 | 2 |
| St. Louis-Farmington | Illinois | Bond | 4 | 226 | 3 | 6 | 5 |
| Kansas City | Missouri | Clinton | 0 | 176 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Crawford | 2 | 242 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Ozark | 0 | 81 | 3 | 4 | 2 |
| Missouri non-MSA | Missouri | Vernon | 0 | 125 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Daviess | 0 | 64 | 3 | 3 | 1 |
| Missouri non-MSA | Missouri | Henry | 4 | 145 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 101 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 146 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 3 | 134 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 220 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | McDonald | 10 | 1014 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 133 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Benton | 1 | 174 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 260 | 2 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 104 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 75 | 1 | 2 | 1 |
| St. Joseph | Missouri | DeKalb | 2 | 91 | 1 | 2 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 89 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 145 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 67 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 1 | 345 | 1 | 19 | 9 |
| Missouri non-MSA | Missouri | Harrison | 1 | 93 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 57 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 68 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 108 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 82 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 41 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 66 | 1 | 1 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 57 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 1 | 123 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 184 | 0 | 0 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 55 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 40 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 2 | 72 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 47 | 0 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 82 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 54 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 33 | 0 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 139 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 68 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 56 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 72 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 23 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 57 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 21 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 26 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 33 | 0 | 0 | 0 |
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
