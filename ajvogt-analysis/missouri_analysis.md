# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/13/2020  
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
| St. Louis-Farmington | 2776 | 172191 | 1863 | 1951 | 2139 |
| Kansas City | 1320 | 114927 | 1330 | 1282 | 1348 |
| Missouri non-MSA | 1043 | 80626 | 884 | 880 | 933 |
| Springfield | 315 | 24968 | 280 | 269 | 256 |
| Columbia-Jefferson City | 140 | 26164 | 207 | 234 | 285 |
| St. Joseph | 106 | 7696 | 82 | 89 | 92 |
| Cape Girardeau-Sikeston | 149 | 9961 | 81 | 91 | 118 |
| Joplin | 174 | 12189 | 71 | 76 | 104 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1152 | 59470 | 598 | 624 | 695 |
| Kansas City | Kansas | Johnson | 339 | 32163 | 413 | 388 | 411 |
| Kansas City | Missouri | Kansas City | 316 | 26470 | 242 | 250 | 280 |
| St. Louis-Farmington | Missouri | St. Charles | 234 | 23340 | 238 | 257 | 291 |
| Kansas City | Missouri | Jackson | 197 | 20291 | 233 | 239 | 246 |
| St. Louis-Farmington | Illinois | Madison | 325 | 17482 | 226 | 233 | 243 |
| St. Louis-Farmington | Illinois | St. Clair | 306 | 16142 | 208 | 211 | 207 |
| Springfield | Missouri | Greene | 229 | 16101 | 179 | 170 | 163 |
| Kansas City | Kansas | Wyandotte | 184 | 13156 | 151 | 124 | 121 |
| St. Louis-Farmington | Missouri | St. Louis City | 270 | 14797 | 140 | 144 | 156 |
| St. Louis-Farmington | Missouri | Jefferson | 113 | 12942 | 134 | 150 | 172 |
| Columbia-Jefferson City | Missouri | Boone | 29 | 11683 | 105 | 106 | 121 |
| Missouri non-MSA | Missouri | Pettis | 38 | 3513 | 79 | 61 | 40 |
| Kansas City | Missouri | Cass | 41 | 4599 | 64 | 62 | 63 |
| Springfield | Missouri | Christian | 29 | 4542 | 61 | 59 | 52 |
| Kansas City | Missouri | Clay | 81 | 5401 | 61 | 60 | 65 |
| St. Louis-Farmington | Missouri | Franklin | 96 | 5584 | 60 | 59 | 65 |
| St. Joseph | Missouri | Buchanan | 72 | 5480 | 60 | 65 | 61 |
| Joplin | Missouri | Jasper | 135 | 9038 | 58 | 63 | 81 |
| Missouri non-MSA | Missouri | Howell | 34 | 2043 | 55 | 33 | 21 |
| Kansas City | Kansas | Leavenworth | 35 | 4347 | 49 | 44 | 44 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 89 | 5713 | 47 | 50 | 67 |
| St. Louis-Farmington | Missouri | St. Francois | 51 | 5675 | 45 | 45 | 61 |
| Columbia-Jefferson City | Missouri | Cole | 65 | 6913 | 42 | 58 | 78 |
| St. Louis-Farmington | Illinois | Clinton | 72 | 3878 | 42 | 42 | 49 |
| Missouri non-MSA | Missouri | Taney | 46 | 3380 | 39 | 39 | 39 |
| St. Louis-Farmington | Missouri | Lincoln | 13 | 2961 | 38 | 39 | 43 |
| St. Louis-Farmington | Illinois | Macoupin | 43 | 2758 | 37 | 41 | 47 |
| Missouri non-MSA | Missouri | Pulaski | 24 | 2136 | 35 | 39 | 30 |
| St. Louis-Farmington | Illinois | Monroe | 54 | 2545 | 35 | 34 | 37 |
| Missouri non-MSA | Missouri | Laclede | 38 | 2193 | 29 | 29 | 23 |
| Columbia-Jefferson City | Missouri | Callaway | 13 | 3279 | 29 | 35 | 39 |
| Missouri non-MSA | Missouri | Butler | 10 | 2527 | 28 | 29 | 31 |
| Kansas City | Kansas | Miami | 7 | 1339 | 28 | 23 | 20 |
| Missouri non-MSA | Missouri | Johnson | 22 | 2859 | 26 | 27 | 30 |
| St. Louis-Farmington | Illinois | Jersey | 28 | 1612 | 25 | 27 | 25 |
| Cape Girardeau-Sikeston | Missouri | Scott | 45 | 3045 | 24 | 30 | 38 |
| Missouri non-MSA | Missouri | Marion | 20 | 2088 | 23 | 23 | 26 |
| Missouri non-MSA | Missouri | Phelps | 59 | 2106 | 22 | 26 | 31 |
| Missouri non-MSA | Missouri | Camden | 51 | 2765 | 22 | 24 | 26 |
| Missouri non-MSA | Missouri | Benton | 11 | 1036 | 21 | 20 | 13 |
| Kansas City | Missouri | Platte | 17 | 1972 | 21 | 24 | 23 |
| Missouri non-MSA | Missouri | Audrain | 16 | 1338 | 20 | 18 | 18 |
| Springfield | Missouri | Webster | 29 | 2070 | 19 | 18 | 20 |
| Missouri non-MSA | Missouri | Morgan | 14 | 1280 | 17 | 16 | 13 |
| Missouri non-MSA | Missouri | Adair | 3 | 1281 | 17 | 15 | 16 |
| Kansas City | Missouri | Lafayette | 35 | 1752 | 16 | 18 | 19 |
| Missouri non-MSA | Missouri | Miller | 31 | 1749 | 16 | 19 | 18 |
| Missouri non-MSA | Missouri | Stoddard | 25 | 1864 | 16 | 17 | 24 |
| St. Louis-Farmington | Illinois | Bond | 15 | 1295 | 15 | 18 | 17 |
| Missouri non-MSA | Missouri | Randolph | 11 | 1423 | 15 | 16 | 19 |
| Missouri non-MSA | Missouri | Crawford | 14 | 1387 | 15 | 15 | 16 |
| Springfield | Missouri | Polk | 15 | 1611 | 15 | 16 | 14 |
| Missouri non-MSA | Missouri | Saline | 14 | 1759 | 15 | 13 | 17 |
| Missouri non-MSA | Missouri | Texas | 10 | 1130 | 14 | 13 | 11 |
| Kansas City | Missouri | Clinton | 48 | 1069 | 14 | 14 | 12 |
| Missouri non-MSA | Missouri | Stone | 20 | 1382 | 14 | 15 | 15 |
| Joplin | Missouri | Newton | 39 | 3151 | 12 | 13 | 22 |
| Missouri non-MSA | Missouri | Pike | 11 | 1104 | 12 | 15 | 17 |
| Kansas City | Missouri | Ray | 6 | 860 | 12 | 12 | 12 |
| Missouri non-MSA | Missouri | Harrison | 7 | 520 | 11 | 9 | 8 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2093 | 11 | 14 | 20 |
| Missouri non-MSA | Missouri | Henry | 16 | 1263 | 11 | 13 | 18 |
| Missouri non-MSA | Missouri | Washington | 27 | 1609 | 11 | 14 | 20 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1842 | 11 | 11 | 15 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1231 | 11 | 13 | 16 |
| Missouri non-MSA | Missouri | Barry | 33 | 1606 | 11 | 12 | 16 |
| Missouri non-MSA | Missouri | Nodaway | 17 | 2166 | 10 | 14 | 18 |
| Columbia-Jefferson City | Missouri | Cooper | 10 | 1314 | 10 | 11 | 13 |
| St. Louis-Farmington | Missouri | Warren | 3 | 1375 | 10 | 12 | 18 |
| Missouri non-MSA | Missouri | Carroll | 8 | 541 | 10 | 8 | 8 |
| Missouri non-MSA | Missouri | Mississippi | 8 | 1029 | 10 | 12 | 16 |
| Missouri non-MSA | Missouri | Madison | 10 | 1021 | 9 | 10 | 12 |
| St. Joseph | Missouri | Andrew | 13 | 950 | 9 | 11 | 12 |
| Missouri non-MSA | Missouri | Oregon | 2 | 468 | 9 | 7 | 5 |
| Kansas City | Missouri | Bates | 9 | 659 | 9 | 8 | 10 |
| Missouri non-MSA | Missouri | Wright | 16 | 888 | 9 | 9 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 26 | 1470 | 8 | 9 | 15 |
| Missouri non-MSA | Missouri | Perry | 15 | 1681 | 8 | 11 | 18 |
| Missouri non-MSA | Missouri | Livingston | 18 | 871 | 8 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1365 | 8 | 10 | 14 |
| Missouri non-MSA | Missouri | McDonald | 17 | 1502 | 7 | 7 | 6 |
| Kansas City | Kansas | Linn | 2 | 391 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Vernon | 13 | 799 | 7 | 9 | 9 |
| Missouri non-MSA | Missouri | Gasconade | 27 | 566 | 7 | 7 | 7 |
| St. Joseph | Missouri | DeKalb | 16 | 679 | 7 | 7 | 8 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 335 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Wayne | 3 | 574 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Grundy | 14 | 587 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 19 | 1194 | 6 | 8 | 9 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1049 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Gentry | 14 | 511 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Douglas | 18 | 506 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Ralls | 2 | 562 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | Macon | 4 | 767 | 6 | 7 | 12 |
| St. Joseph | Kansas | Doniphan | 5 | 587 | 5 | 6 | 10 |
| Missouri non-MSA | Missouri | Dent | 5 | 605 | 5 | 7 | 8 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 10 | 899 | 5 | 7 | 8 |
| Missouri non-MSA | Missouri | Lewis | 2 | 478 | 5 | 3 | 5 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 401 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Barton | 6 | 691 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Daviess | 8 | 401 | 4 | 4 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 5 | 304 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Linn | 11 | 373 | 4 | 4 | 5 |
| Kansas City | Missouri | Caldwell | 3 | 458 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Iron | 1 | 287 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Monroe | 5 | 442 | 4 | 4 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 561 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Ripley | 8 | 597 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Ozark | 4 | 336 | 3 | 3 | 2 |
| Springfield | Missouri | Dallas | 13 | 644 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Shannon | 9 | 376 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Atchison | 4 | 249 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 3 | 391 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Carter | 6 | 342 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Maries | 4 | 412 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Worth | 0 | 103 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 259 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Holt | 5 | 305 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Dade | 8 | 320 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Clark | 4 | 336 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Chariton | 0 | 277 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Hickory | 6 | 399 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 8 | 592 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 203 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 103 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Cedar | 8 | 465 | 1 | 1 | 4 |
| Missouri non-MSA | Missouri | Scotland | 2 | 206 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 151 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 140 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 176 | 0 | 2 | 3 |
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
