# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/12/2020  
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
| St. Louis-Farmington | 1490 | 54493 | 515 | 562 | 593 |
| Kansas City | 508 | 38150 | 315 | 338 | 377 |
| Missouri non-MSA | 189 | 18185 | 310 | 306 | 269 |
| Springfield | 26 | 6182 | 154 | 156 | 122 |
| Columbia-Jefferson City | 24 | 6137 | 139 | 155 | 121 |
| Joplin | 52 | 4192 | 68 | 62 | 47 |
| Cape Girardeau-Sikeston | 25 | 2207 | 46 | 38 | 32 |
| St. Joseph | 16 | 1817 | 23 | 22 | 17 |
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
| St. Louis-Farmington | Missouri | St. Louis | 763 | 21343 | 167 | 183 | 195 |
| Springfield | Missouri | Greene | 19 | 4407 | 110 | 114 | 90 |
| Kansas City | Kansas | Johnson | 128 | 9228 | 87 | 97 | 107 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 3780 | 87 | 106 | 77 |
| Kansas City | Missouri | Jackson | 85 | 6313 | 70 | 70 | 68 |
| St. Louis-Farmington | Missouri | St. Charles | 105 | 6468 | 66 | 65 | 71 |
| Kansas City | Missouri | Kansas City | 96 | 10026 | 63 | 73 | 98 |
| Joplin | Missouri | Jasper | 39 | 3004 | 59 | 53 | 38 |
| St. Louis-Farmington | Illinois | Madison | 117 | 4780 | 57 | 65 | 66 |
| St. Louis-Farmington | Missouri | Jefferson | 47 | 3288 | 53 | 53 | 51 |
| St. Louis-Farmington | Illinois | St. Clair | 178 | 5924 | 49 | 54 | 58 |
| Kansas City | Kansas | Wyandotte | 120 | 6394 | 30 | 33 | 45 |
| St. Louis-Farmington | Missouri | St. Louis City | 192 | 6527 | 27 | 33 | 38 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1119 | 26 | 23 | 21 |
| St. Louis-Farmington | Missouri | St. Francois | 7 | 1395 | 26 | 31 | 32 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 8 | 1193 | 23 | 18 | 16 |
| Springfield | Missouri | Christian | 3 | 917 | 23 | 22 | 17 |
| Missouri non-MSA | Missouri | Johnson | 4 | 777 | 22 | 13 | 9 |
| St. Louis-Farmington | Missouri | Franklin | 23 | 1235 | 17 | 18 | 18 |
| St. Joseph | Missouri | Buchanan | 13 | 1476 | 16 | 16 | 12 |
| St. Louis-Farmington | Illinois | Clinton | 19 | 922 | 16 | 18 | 16 |
| Kansas City | Missouri | Clay | 39 | 1561 | 15 | 15 | 15 |
| Kansas City | Missouri | Cass | 16 | 1219 | 13 | 13 | 14 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 474 | 13 | 12 | 10 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 233 | 13 | 8 | 5 |
| Missouri non-MSA | Missouri | Howell | 3 | 377 | 12 | 10 | 7 |
| Missouri non-MSA | Missouri | Taney | 22 | 1021 | 11 | 9 | 12 |
| Missouri non-MSA | Missouri | Camden | 9 | 655 | 11 | 11 | 9 |
| Springfield | Missouri | Webster | 2 | 340 | 10 | 9 | 6 |
| Missouri non-MSA | Missouri | Livingston | 1 | 346 | 10 | 19 | 9 |
| Missouri non-MSA | Missouri | Marion | 7 | 575 | 10 | 10 | 11 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 612 | 9 | 9 | 9 |
| Kansas City | Kansas | Leavenworth | 9 | 1771 | 9 | 9 | 8 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 564 | 9 | 8 | 7 |
| Missouri non-MSA | Missouri | Phelps | 1 | 308 | 9 | 8 | 6 |
| Missouri non-MSA | Missouri | Laclede | 1 | 377 | 9 | 6 | 5 |
| Cape Girardeau-Sikeston | Missouri | Scott | 15 | 725 | 9 | 10 | 10 |
| Joplin | Missouri | Newton | 13 | 1188 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Nodaway | 7 | 663 | 8 | 20 | 15 |
| Missouri non-MSA | Missouri | Butler | 4 | 458 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Perry | 4 | 481 | 8 | 8 | 7 |
| Missouri non-MSA | Missouri | Miller | 1 | 338 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Texas | 2 | 177 | 8 | 6 | 3 |
| Kansas City | Missouri | Platte | 10 | 560 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 410 | 6 | 6 | 5 |
| Springfield | Missouri | Polk | 1 | 376 | 6 | 7 | 5 |
| Missouri non-MSA | Missouri | Madison | 0 | 229 | 6 | 8 | 6 |
| Missouri non-MSA | Missouri | Pettis | 8 | 871 | 6 | 6 | 9 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 311 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Morgan | 1 | 183 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 422 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | New Madrid | 11 | 473 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Washington | 1 | 294 | 5 | 4 | 6 |
| Kansas City | Kansas | Miami | 1 | 282 | 5 | 6 | 4 |
| St. Louis-Farmington | Missouri | Lincoln | 2 | 641 | 5 | 7 | 7 |
| St. Louis-Farmington | Illinois | Macoupin | 6 | 423 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Grundy | 1 | 109 | 5 | 5 | 2 |
| Missouri non-MSA | Missouri | Pulaski | 2 | 446 | 5 | 5 | 6 |
| St. Louis-Farmington | Illinois | Jersey | 12 | 349 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Ozark | 0 | 75 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 342 | 4 | 4 | 3 |
| Kansas City | Missouri | Lafayette | 2 | 292 | 4 | 4 | 3 |
| St. Louis-Farmington | Illinois | Bond | 4 | 223 | 4 | 7 | 5 |
| Missouri non-MSA | Missouri | Gasconade | 6 | 132 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Barry | 5 | 399 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Randolph | 1 | 166 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Wright | 0 | 127 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 284 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Audrain | 2 | 334 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Saline | 9 | 599 | 4 | 4 | 4 |
| St. Louis-Farmington | Missouri | Warren | 0 | 378 | 4 | 4 | 5 |
| Kansas City | Missouri | Clinton | 0 | 175 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Pike | 2 | 173 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Stone | 2 | 332 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Vernon | 0 | 121 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 120 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 125 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 0 | 61 | 3 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 142 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Dent | 0 | 69 | 3 | 2 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 164 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Barton | 0 | 132 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 217 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 141 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Henry | 4 | 139 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Crawford | 2 | 231 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 257 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | McDonald | 10 | 1011 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 3 | 132 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 96 | 2 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 2 | 88 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 128 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 71 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 99 | 1 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 89 | 1 | 1 | 1 |
| Kansas City | Missouri | Ray | 0 | 138 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 91 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 65 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 57 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 56 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 47 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 67 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 56 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 68 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 39 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Benton | 1 | 165 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 1 | 63 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 1 | 121 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 53 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 137 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 39 | 0 | 1 | 0 |
| Kansas City | Missouri | Bates | 1 | 81 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 52 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 78 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Gentry | 9 | 105 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 182 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 2 | 70 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 38 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 72 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 22 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 50 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 57 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 21 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 42 | 0 | 0 | 0 |
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
