# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/05/2020  
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
| St. Louis-Farmington | 1952 | 91284 | 1145 | 986 | 793 |
| Kansas City | 939 | 63321 | 737 | 614 | 529 |
| Missouri non-MSA | 616 | 44509 | 684 | 621 | 553 |
| Columbia-Jefferson City | 69 | 14242 | 269 | 221 | 189 |
| Springfield | 191 | 15371 | 208 | 177 | 166 |
| Joplin | 101 | 7969 | 85 | 82 | 75 |
| Cape Girardeau-Sikeston | 87 | 5350 | 81 | 70 | 64 |
| St. Joseph | 56 | 4274 | 46 | 44 | 48 |
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
| St. Louis-Farmington | Missouri | St. Louis | 895 | 33375 | 401 | 339 | 269 |
| Kansas City | Kansas | Johnson | 222 | 15668 | 209 | 169 | 133 |
| Kansas City | Missouri | Kansas City | 222 | 15892 | 187 | 144 | 115 |
| St. Louis-Farmington | Missouri | St. Charles | 157 | 12202 | 179 | 160 | 136 |
| Springfield | Missouri | Greene | 142 | 9974 | 125 | 105 | 99 |
| Kansas City | Missouri | Jackson | 144 | 11002 | 122 | 115 | 107 |
| St. Louis-Farmington | Illinois | Madison | 163 | 8108 | 105 | 86 | 69 |
| St. Louis-Farmington | Missouri | Jefferson | 90 | 6333 | 98 | 78 | 52 |
| Columbia-Jefferson City | Missouri | Cole | 26 | 3663 | 93 | 75 | 62 |
| St. Louis-Farmington | Missouri | St. Louis City | 225 | 9102 | 89 | 74 | 59 |
| Columbia-Jefferson City | Missouri | Boone | 15 | 6634 | 77 | 64 | 61 |
| St. Louis-Farmington | Illinois | St. Clair | 228 | 8618 | 74 | 67 | 56 |
| Joplin | Missouri | Jasper | 79 | 5730 | 57 | 59 | 48 |
| Kansas City | Kansas | Wyandotte | 165 | 8666 | 56 | 46 | 45 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 1607 | 50 | 38 | 28 |
| St. Louis-Farmington | Missouri | Franklin | 50 | 3060 | 48 | 47 | 37 |
| St. Louis-Farmington | Missouri | St. Francois | 30 | 3206 | 45 | 37 | 32 |
| Kansas City | Missouri | Clay | 50 | 2882 | 44 | 38 | 34 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 55 | 2998 | 43 | 35 | 33 |
| Springfield | Missouri | Christian | 17 | 2584 | 38 | 32 | 30 |
| Missouri non-MSA | Missouri | Pettis | 24 | 1870 | 34 | 27 | 21 |
| Kansas City | Missouri | Cass | 33 | 2311 | 31 | 27 | 24 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1349 | 29 | 22 | 17 |
| St. Joseph | Missouri | Buchanan | 44 | 3182 | 28 | 27 | 31 |
| Joplin | Missouri | Newton | 22 | 2239 | 27 | 23 | 26 |
| Missouri non-MSA | Missouri | Taney | 35 | 1944 | 27 | 25 | 17 |
| Missouri non-MSA | Missouri | Butler | 8 | 1441 | 27 | 27 | 23 |
| Cape Girardeau-Sikeston | Missouri | Scott | 27 | 1624 | 27 | 22 | 21 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1675 | 24 | 20 | 21 |
| St. Louis-Farmington | Illinois | Clinton | 32 | 1988 | 22 | 23 | 22 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1373 | 21 | 21 | 16 |
| St. Louis-Farmington | Illinois | Monroe | 34 | 1112 | 20 | 17 | 12 |
| Missouri non-MSA | Missouri | Marion | 14 | 1078 | 20 | 16 | 12 |
| Springfield | Missouri | Polk | 11 | 1106 | 19 | 15 | 12 |
| Missouri non-MSA | Missouri | Lawrence | 24 | 1256 | 18 | 17 | 17 |
| Missouri non-MSA | Missouri | Camden | 37 | 1741 | 18 | 17 | 20 |
| Missouri non-MSA | Missouri | Miller | 18 | 1014 | 18 | 15 | 14 |
| Kansas City | Kansas | Leavenworth | 21 | 2695 | 18 | 14 | 14 |
| Springfield | Missouri | Webster | 19 | 1290 | 18 | 16 | 16 |
| Missouri non-MSA | Missouri | Howell | 14 | 1310 | 17 | 19 | 17 |
| Kansas City | Missouri | Lafayette | 26 | 973 | 17 | 15 | 12 |
| Missouri non-MSA | Missouri | Barry | 10 | 963 | 17 | 16 | 14 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 521 | 16 | 14 | 9 |
| Columbia-Jefferson City | Missouri | Moniteau | 12 | 750 | 16 | 17 | 13 |
| Missouri non-MSA | Missouri | Phelps | 30 | 959 | 15 | 13 | 14 |
| Missouri non-MSA | Missouri | Saline | 11 | 1055 | 14 | 10 | 8 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 594 | 14 | 11 | 12 |
| Missouri non-MSA | Missouri | Audrain | 11 | 681 | 13 | 10 | 7 |
| Missouri non-MSA | Missouri | Washington | 20 | 766 | 13 | 11 | 9 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1240 | 13 | 15 | 11 |
| Missouri non-MSA | Missouri | Randolph | 3 | 720 | 13 | 12 | 12 |
| Missouri non-MSA | Missouri | Perry | 8 | 906 | 13 | 10 | 8 |
| Missouri non-MSA | Missouri | Morgan | 8 | 774 | 13 | 12 | 11 |
| Missouri non-MSA | Missouri | Henry | 8 | 477 | 13 | 9 | 7 |
| St. Louis-Farmington | Illinois | Macoupin | 11 | 919 | 12 | 12 | 10 |
| Missouri non-MSA | Missouri | Laclede | 23 | 1303 | 12 | 15 | 16 |
| Missouri non-MSA | Missouri | Pulaski | 11 | 1107 | 12 | 14 | 12 |
| Kansas City | Missouri | Platte | 13 | 1097 | 12 | 12 | 11 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 979 | 12 | 13 | 13 |
| Missouri non-MSA | Missouri | Crawford | 9 | 730 | 12 | 11 | 10 |
| Columbia-Jefferson City | Missouri | Cooper | 4 | 708 | 11 | 9 | 7 |
| Kansas City | Missouri | Clinton | 29 | 588 | 11 | 10 | 10 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 861 | 11 | 10 | 8 |
| Missouri non-MSA | Missouri | Stone | 11 | 791 | 11 | 10 | 9 |
| Missouri non-MSA | Missouri | Sullivan | 3 | 397 | 11 | 8 | 5 |
| Missouri non-MSA | Missouri | Adair | 0 | 603 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Texas | 3 | 665 | 10 | 9 | 9 |
| St. Joseph | Missouri | DeKalb | 3 | 373 | 10 | 8 | 6 |
| Kansas City | Missouri | Ray | 2 | 349 | 9 | 6 | 5 |
| Missouri non-MSA | Missouri | Pike | 8 | 417 | 9 | 7 | 5 |
| St. Louis-Farmington | Missouri | Warren | 2 | 697 | 8 | 8 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 3 | 571 | 8 | 9 | 6 |
| St. Louis-Farmington | Illinois | Bond | 9 | 576 | 8 | 6 | 7 |
| Kansas City | Kansas | Miami | 2 | 580 | 7 | 5 | 5 |
| Springfield | Missouri | Dallas | 2 | 417 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | Hickory | 4 | 264 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Macon | 1 | 273 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 14 | 784 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 495 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Madison | 3 | 555 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | McDonald | 13 | 1269 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Vernon | 3 | 388 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 205 | 6 | 6 | 3 |
| St. Joseph | Missouri | Andrew | 8 | 492 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Lewis | 2 | 245 | 5 | 5 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 521 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Wright | 9 | 629 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Maries | 1 | 230 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 303 | 5 | 5 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 286 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Wayne | 3 | 345 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Shannon | 6 | 279 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Cedar | 4 | 272 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Benton | 7 | 518 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Carroll | 4 | 232 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Ripley | 4 | 306 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Grundy | 11 | 296 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Livingston | 9 | 592 | 4 | 3 | 4 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 94 | 4 | 1 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 262 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Dent | 4 | 286 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Gentry | 10 | 213 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Monroe | 2 | 197 | 4 | 4 | 3 |
| Kansas City | Missouri | Bates | 8 | 280 | 3 | 3 | 4 |
| Kansas City | Missouri | Caldwell | 1 | 200 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 13 | 314 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Barton | 4 | 461 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Clark | 2 | 137 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 124 | 3 | 2 | 2 |
| Kansas City | Kansas | Linn | 1 | 138 | 3 | 2 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 157 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Daviess | 4 | 241 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 3 | 198 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Chariton | 0 | 80 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Dade | 3 | 160 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 1 | 231 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Linn | 7 | 181 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 227 | 2 | 2 | 2 |
| St. Joseph | Kansas | Doniphan | 1 | 227 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Harrison | 1 | 206 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 1 | 98 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 57 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Atchison | 1 | 91 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 1 | 133 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 134 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 84 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 65 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 0 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 70 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 112 | 0 | 1 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
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
