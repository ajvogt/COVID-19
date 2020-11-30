# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/30/2020  
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
| St. Louis-Farmington | 2329 | 146713 | 2122 | 2266 | 2043 |
| Kansas City | 1172 | 97579 | 1236 | 1358 | 1211 |
| Missouri non-MSA | 839 | 69064 | 761 | 904 | 924 |
| Columbia-Jefferson City | 107 | 23114 | 247 | 295 | 337 |
| Springfield | 241 | 21377 | 208 | 239 | 229 |
| Cape Girardeau-Sikeston | 113 | 8742 | 103 | 130 | 126 |
| St. Joseph | 78 | 6534 | 93 | 95 | 83 |
| Joplin | 144 | 11196 | 79 | 115 | 120 |
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
| St. Louis-Farmington | Missouri | St. Louis | 976 | 51324 | 709 | 738 | 665 |
| Kansas City | Kansas | Johnson | 285 | 26731 | 405 | 413 | 363 |
| St. Louis-Farmington | Missouri | St. Charles | 213 | 19964 | 270 | 316 | 289 |
| Kansas City | Missouri | Kansas City | 281 | 23210 | 255 | 294 | 274 |
| St. Louis-Farmington | Illinois | Madison | 255 | 14379 | 216 | 242 | 227 |
| St. Louis-Farmington | Illinois | St. Clair | 259 | 13410 | 213 | 212 | 172 |
| Kansas City | Missouri | Jackson | 180 | 17136 | 205 | 242 | 225 |
| St. Louis-Farmington | Missouri | Jefferson | 103 | 10976 | 177 | 196 | 171 |
| St. Louis-Farmington | Missouri | St. Louis City | 238 | 12960 | 173 | 160 | 144 |
| Springfield | Missouri | Greene | 173 | 13825 | 139 | 155 | 146 |
| Kansas City | Kansas | Wyandotte | 178 | 11412 | 125 | 123 | 90 |
| Columbia-Jefferson City | Missouri | Boone | 23 | 10311 | 94 | 118 | 135 |
| Columbia-Jefferson City | Missouri | Cole | 49 | 6151 | 75 | 87 | 97 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 65 | 5033 | 62 | 76 | 74 |
| Joplin | Missouri | Jasper | 106 | 8223 | 60 | 87 | 92 |
| St. Louis-Farmington | Missouri | Franklin | 72 | 4800 | 60 | 68 | 66 |
| St. Joseph | Missouri | Buchanan | 57 | 4641 | 56 | 59 | 53 |
| St. Louis-Farmington | Missouri | St. Francois | 44 | 5065 | 55 | 69 | 69 |
| Kansas City | Missouri | Cass | 39 | 3765 | 53 | 61 | 54 |
| St. Louis-Farmington | Illinois | Clinton | 61 | 3308 | 52 | 54 | 47 |
| St. Louis-Farmington | Illinois | Macoupin | 18 | 2232 | 48 | 53 | 45 |
| Kansas City | Kansas | Leavenworth | 31 | 3729 | 45 | 45 | 34 |
| St. Louis-Farmington | Missouri | Lincoln | 9 | 2438 | 39 | 44 | 38 |
| St. Louis-Farmington | Illinois | Monroe | 45 | 2075 | 39 | 36 | 35 |
| Kansas City | Missouri | Clay | 69 | 4583 | 38 | 66 | 64 |
| Springfield | Missouri | Christian | 23 | 3757 | 38 | 45 | 44 |
| Columbia-Jefferson City | Missouri | Callaway | 8 | 2820 | 36 | 40 | 47 |
| Cape Girardeau-Sikeston | Missouri | Scott | 38 | 2651 | 33 | 43 | 38 |
| Missouri non-MSA | Missouri | Taney | 40 | 2845 | 32 | 38 | 33 |
| Missouri non-MSA | Missouri | Phelps | 42 | 1771 | 31 | 34 | 28 |
| Missouri non-MSA | Missouri | Johnson | 15 | 2530 | 30 | 32 | 32 |
| Missouri non-MSA | Missouri | Butler | 9 | 2139 | 26 | 29 | 28 |
| St. Louis-Farmington | Illinois | Jersey | 24 | 1272 | 23 | 26 | 26 |
| Missouri non-MSA | Missouri | Marion | 16 | 1774 | 23 | 27 | 26 |
| Missouri non-MSA | Missouri | Mississippi | 7 | 868 | 23 | 20 | 13 |
| Kansas City | Missouri | Lafayette | 29 | 1528 | 22 | 21 | 21 |
| Missouri non-MSA | Missouri | Stoddard | 20 | 1628 | 21 | 28 | 23 |
| Missouri non-MSA | Missouri | Camden | 45 | 2449 | 21 | 26 | 26 |
| Kansas City | Kansas | Miami | 2 | 1013 | 21 | 19 | 14 |
| Missouri non-MSA | Missouri | Nodaway | 13 | 1989 | 20 | 22 | 25 |
| Missouri non-MSA | Missouri | Pulaski | 18 | 1614 | 20 | 22 | 18 |
| Missouri non-MSA | Missouri | Audrain | 13 | 1089 | 19 | 17 | 15 |
| St. Louis-Farmington | Illinois | Bond | 10 | 1048 | 19 | 17 | 17 |
| Joplin | Missouri | Newton | 38 | 2973 | 19 | 27 | 28 |
| Kansas City | Missouri | Platte | 17 | 1654 | 19 | 23 | 20 |
| St. Louis-Farmington | Missouri | Warren | 2 | 1215 | 19 | 22 | 18 |
| Missouri non-MSA | Missouri | Laclede | 30 | 1801 | 18 | 19 | 18 |
| Springfield | Missouri | Webster | 24 | 1820 | 16 | 22 | 20 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 1360 | 16 | 17 | 18 |
| Missouri non-MSA | Missouri | Lawrence | 37 | 1902 | 16 | 22 | 24 |
| St. Joseph | Kansas | Doniphan | 2 | 503 | 16 | 12 | 9 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1058 | 15 | 16 | 20 |
| Missouri non-MSA | Missouri | Pettis | 32 | 2679 | 15 | 16 | 32 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1691 | 15 | 16 | 16 |
| Missouri non-MSA | Missouri | Saline | 12 | 1583 | 14 | 17 | 19 |
| Missouri non-MSA | Missouri | Henry | 10 | 1085 | 14 | 21 | 22 |
| Missouri non-MSA | Missouri | Pike | 8 | 912 | 14 | 18 | 18 |
| Missouri non-MSA | Missouri | Perry | 12 | 1535 | 14 | 19 | 22 |
| Missouri non-MSA | Missouri | Madison | 7 | 887 | 13 | 13 | 11 |
| Missouri non-MSA | Missouri | Crawford | 12 | 1191 | 13 | 16 | 17 |
| Missouri non-MSA | Missouri | Washington | 23 | 1417 | 13 | 20 | 23 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1225 | 12 | 15 | 18 |
| Missouri non-MSA | Missouri | Miller | 24 | 1488 | 12 | 16 | 18 |
| Missouri non-MSA | Missouri | Macon | 3 | 677 | 12 | 16 | 14 |
| Missouri non-MSA | Missouri | Randolph | 5 | 1195 | 11 | 14 | 17 |
| St. Joseph | Missouri | DeKalb | 10 | 591 | 11 | 9 | 9 |
| Kansas City | Missouri | Bates | 9 | 552 | 11 | 12 | 9 |
| Missouri non-MSA | Missouri | Morgan | 12 | 1068 | 10 | 11 | 12 |
| St. Joseph | Missouri | Andrew | 9 | 799 | 10 | 13 | 11 |
| Missouri non-MSA | Missouri | Barry | 25 | 1439 | 10 | 17 | 18 |
| Kansas City | Missouri | Ray | 4 | 694 | 10 | 11 | 13 |
| Springfield | Missouri | Polk | 12 | 1377 | 10 | 10 | 10 |
| Missouri non-MSA | Missouri | Stone | 16 | 1174 | 10 | 15 | 14 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 936 | 9 | 12 | 13 |
| Missouri non-MSA | Missouri | Howell | 28 | 1582 | 9 | 10 | 11 |
| Columbia-Jefferson City | Missouri | Cooper | 7 | 1165 | 9 | 12 | 17 |
| Missouri non-MSA | Missouri | Adair | 3 | 1074 | 9 | 14 | 17 |
| Missouri non-MSA | Missouri | Ralls | 1 | 471 | 9 | 9 | 8 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 473 | 9 | 7 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 16 | 1081 | 9 | 9 | 11 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 506 | 8 | 8 | 8 |
| Kansas City | Missouri | Clinton | 45 | 884 | 8 | 10 | 11 |
| Missouri non-MSA | Missouri | Dent | 4 | 514 | 8 | 9 | 8 |
| Missouri non-MSA | Missouri | Carroll | 6 | 432 | 8 | 8 | 7 |
| Missouri non-MSA | Missouri | Ripley | 8 | 511 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Texas | 8 | 959 | 7 | 9 | 11 |
| Missouri non-MSA | Missouri | Douglas | 15 | 434 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | McDonald | 16 | 1405 | 6 | 6 | 5 |
| Kansas City | Kansas | Linn | 1 | 295 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Monroe | 3 | 389 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Vernon | 7 | 666 | 6 | 9 | 10 |
| Missouri non-MSA | Missouri | Montgomery | 5 | 346 | 6 | 6 | 5 |
| Kansas City | Missouri | Caldwell | 2 | 393 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Benton | 8 | 772 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Livingston | 14 | 783 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Putnam | 1 | 157 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Wayne | 3 | 492 | 5 | 6 | 5 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 8 | 802 | 5 | 7 | 9 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 334 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Wright | 14 | 766 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Harrison | 2 | 395 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Linn | 9 | 320 | 4 | 5 | 4 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 247 | 4 | 6 | 5 |
| Springfield | Missouri | Dallas | 9 | 598 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Gentry | 11 | 415 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Barton | 4 | 630 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Clark | 3 | 298 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Sullivan | 6 | 564 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Grundy | 14 | 507 | 3 | 7 | 7 |
| Missouri non-MSA | Missouri | Maries | 3 | 363 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Oregon | 0 | 374 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Holt | 3 | 265 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 179 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 8 | 333 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Shelby | 1 | 205 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Atchison | 3 | 211 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Cedar | 6 | 441 | 2 | 5 | 6 |
| Missouri non-MSA | Missouri | Ozark | 2 | 295 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 6 | 366 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Chariton | 0 | 238 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Carter | 5 | 294 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Shannon | 9 | 339 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 233 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Lewis | 2 | 429 | 2 | 5 | 7 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 256 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Dade | 6 | 287 | 1 | 3 | 4 |
| Missouri non-MSA | Missouri | Scotland | 1 | 183 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 131 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 72 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 133 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 85 | 1 | 1 | 1 |
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
