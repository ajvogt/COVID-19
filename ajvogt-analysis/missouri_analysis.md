# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/14/2020  
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
| St. Louis-Farmington | 2060 | 110212 | 2111 | 1771 | 1258 |
| Kansas City | 1014 | 76687 | 1296 | 1103 | 811 |
| Missouri non-MSA | 708 | 53753 | 1019 | 887 | 712 |
| Columbia-Jefferson City | 83 | 17972 | 388 | 355 | 266 |
| Springfield | 215 | 17566 | 254 | 218 | 188 |
| Cape Girardeau-Sikeston | 99 | 6623 | 148 | 119 | 87 |
| Joplin | 124 | 9222 | 148 | 118 | 95 |
| St. Joseph | 66 | 5016 | 87 | 70 | 57 |
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
| St. Louis-Farmington | Missouri | St. Louis | 912 | 39554 | 708 | 585 | 422 |
| Kansas City | Kansas | Johnson | 243 | 20946 | 441 | 366 | 259 |
| St. Louis-Farmington | Missouri | St. Charles | 167 | 14839 | 304 | 255 | 191 |
| Kansas City | Missouri | Kansas City | 244 | 18367 | 279 | 241 | 181 |
| St. Louis-Farmington | Illinois | Madison | 177 | 10504 | 248 | 210 | 133 |
| Kansas City | Missouri | Jackson | 153 | 13120 | 232 | 196 | 140 |
| St. Louis-Farmington | Illinois | St. Clair | 245 | 10135 | 173 | 134 | 93 |
| St. Louis-Farmington | Missouri | Jefferson | 94 | 7857 | 173 | 145 | 97 |
| Columbia-Jefferson City | Missouri | Boone | 15 | 8227 | 163 | 140 | 94 |
| Springfield | Missouri | Greene | 158 | 11373 | 160 | 139 | 114 |
| Joplin | Missouri | Jasper | 98 | 6713 | 117 | 90 | 71 |
| St. Louis-Farmington | Missouri | St. Louis City | 230 | 10117 | 106 | 107 | 80 |
| Columbia-Jefferson City | Missouri | Cole | 36 | 4647 | 104 | 102 | 81 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 58 | 3798 | 94 | 71 | 49 |
| Kansas City | Kansas | Wyandotte | 167 | 9690 | 80 | 71 | 62 |
| St. Louis-Farmington | Missouri | St. Francois | 36 | 3884 | 75 | 65 | 45 |
| St. Louis-Farmington | Missouri | Franklin | 57 | 3665 | 70 | 60 | 50 |
| Kansas City | Missouri | Clay | 54 | 3490 | 64 | 60 | 43 |
| St. Joseph | Missouri | Buchanan | 47 | 3683 | 60 | 45 | 36 |
| St. Louis-Farmington | Illinois | Macoupin | 14 | 1406 | 55 | 39 | 24 |
| Kansas City | Missouri | Cass | 35 | 2765 | 54 | 44 | 32 |
| Springfield | Missouri | Christian | 20 | 3042 | 53 | 45 | 36 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 2119 | 52 | 51 | 39 |
| St. Louis-Farmington | Illinois | Clinton | 47 | 2453 | 50 | 41 | 33 |
| Missouri non-MSA | Missouri | Pettis | 28 | 2392 | 49 | 48 | 36 |
| St. Louis-Farmington | Missouri | Lincoln | 7 | 1716 | 41 | 31 | 24 |
| Cape Girardeau-Sikeston | Missouri | Scott | 33 | 1959 | 38 | 33 | 26 |
| Kansas City | Kansas | Leavenworth | 25 | 3095 | 37 | 29 | 21 |
| St. Louis-Farmington | Illinois | Monroe | 40 | 1442 | 37 | 30 | 21 |
| Missouri non-MSA | Missouri | Johnson | 11 | 2013 | 35 | 32 | 22 |
| Missouri non-MSA | Missouri | Taney | 36 | 2248 | 35 | 30 | 25 |
| Missouri non-MSA | Missouri | Camden | 41 | 2024 | 33 | 27 | 22 |
| Joplin | Missouri | Newton | 26 | 2509 | 30 | 28 | 23 |
| Missouri non-MSA | Missouri | Henry | 8 | 740 | 30 | 23 | 14 |
| Missouri non-MSA | Missouri | Marion | 15 | 1326 | 29 | 25 | 18 |
| Missouri non-MSA | Missouri | Phelps | 34 | 1214 | 28 | 22 | 17 |
| Missouri non-MSA | Missouri | Washington | 21 | 1022 | 28 | 22 | 15 |
| Missouri non-MSA | Missouri | Lawrence | 32 | 1517 | 27 | 25 | 21 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1603 | 26 | 28 | 21 |
| Missouri non-MSA | Missouri | Saline | 11 | 1280 | 26 | 20 | 14 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 754 | 24 | 22 | 16 |
| Columbia-Jefferson City | Missouri | Moniteau | 14 | 951 | 24 | 19 | 17 |
| Missouri non-MSA | Missouri | Adair | 0 | 817 | 23 | 18 | 13 |
| St. Louis-Farmington | Illinois | Jersey | 23 | 874 | 23 | 27 | 14 |
| Missouri non-MSA | Missouri | Butler | 8 | 1630 | 22 | 24 | 24 |
| Kansas City | Missouri | Lafayette | 27 | 1181 | 22 | 20 | 15 |
| Missouri non-MSA | Missouri | Barry | 19 | 1151 | 22 | 19 | 17 |
| Missouri non-MSA | Missouri | Stoddard | 17 | 1158 | 21 | 16 | 15 |
| Missouri non-MSA | Missouri | Pike | 8 | 594 | 21 | 15 | 10 |
| Columbia-Jefferson City | Missouri | Cooper | 6 | 935 | 21 | 20 | 14 |
| St. Louis-Farmington | Illinois | Bond | 9 | 774 | 21 | 17 | 12 |
| Missouri non-MSA | Missouri | Miller | 20 | 1213 | 20 | 20 | 18 |
| Missouri non-MSA | Missouri | Laclede | 28 | 1493 | 20 | 18 | 16 |
| Missouri non-MSA | Missouri | Perry | 8 | 1132 | 20 | 20 | 13 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 1035 | 19 | 16 | 12 |
| Missouri non-MSA | Missouri | Randolph | 4 | 895 | 19 | 17 | 15 |
| Missouri non-MSA | Missouri | Crawford | 10 | 907 | 19 | 16 | 13 |
| Springfield | Missouri | Webster | 23 | 1456 | 19 | 17 | 16 |
| St. Louis-Farmington | Missouri | Warren | 2 | 847 | 17 | 14 | 10 |
| Kansas City | Missouri | Ray | 2 | 502 | 17 | 14 | 9 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1413 | 17 | 16 | 16 |
| Kansas City | Missouri | Platte | 14 | 1271 | 16 | 17 | 13 |
| Missouri non-MSA | Missouri | Pulaski | 13 | 1249 | 15 | 14 | 13 |
| Missouri non-MSA | Missouri | Benton | 7 | 653 | 15 | 11 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 734 | 15 | 14 | 14 |
| Missouri non-MSA | Missouri | Audrain | 11 | 812 | 14 | 13 | 9 |
| Missouri non-MSA | Missouri | Pemiscot | 15 | 910 | 14 | 11 | 9 |
| Missouri non-MSA | Missouri | Vernon | 4 | 515 | 14 | 11 | 8 |
| Kansas City | Kansas | Miami | 2 | 747 | 14 | 11 | 8 |
| Missouri non-MSA | Missouri | Stone | 13 | 927 | 14 | 13 | 11 |
| Missouri non-MSA | Missouri | Macon | 1 | 399 | 13 | 11 | 7 |
| Missouri non-MSA | Missouri | Texas | 6 | 801 | 13 | 12 | 10 |
| Kansas City | Missouri | Clinton | 38 | 701 | 13 | 12 | 11 |
| Springfield | Missouri | Polk | 11 | 1199 | 11 | 9 | 12 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 6 | 664 | 11 | 9 | 8 |
| Missouri non-MSA | Missouri | Madison | 7 | 648 | 11 | 8 | 8 |
| Missouri non-MSA | Missouri | Morgan | 8 | 880 | 11 | 12 | 11 |
| St. Joseph | Kansas | Doniphan | 2 | 322 | 11 | 7 | 5 |
| Missouri non-MSA | Missouri | Lewis | 2 | 336 | 10 | 8 | 6 |
| Missouri non-MSA | Missouri | Howell | 22 | 1404 | 10 | 11 | 15 |
| Missouri non-MSA | Missouri | Ripley | 5 | 389 | 10 | 7 | 6 |
| Missouri non-MSA | Missouri | Cedar | 4 | 347 | 10 | 7 | 5 |
| Springfield | Missouri | Dallas | 3 | 496 | 9 | 7 | 8 |
| St. Joseph | Missouri | Andrew | 8 | 579 | 9 | 8 | 7 |
| Kansas City | Missouri | Bates | 8 | 353 | 9 | 6 | 4 |
| Missouri non-MSA | Missouri | Ralls | 1 | 310 | 9 | 6 | 4 |
| Missouri non-MSA | Missouri | Gentry | 11 | 292 | 9 | 7 | 4 |
| Missouri non-MSA | Missouri | Monroe | 3 | 277 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | Harrison | 1 | 269 | 8 | 5 | 3 |
| Missouri non-MSA | Missouri | Barton | 4 | 536 | 8 | 6 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 359 | 7 | 7 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 206 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Dade | 5 | 222 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Dent | 4 | 350 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Clark | 2 | 208 | 7 | 6 | 3 |
| Missouri non-MSA | Missouri | Chariton | 0 | 155 | 7 | 6 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 555 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Sullivan | 5 | 465 | 6 | 7 | 6 |
| St. Joseph | Missouri | DeKalb | 9 | 432 | 6 | 8 | 7 |
| Missouri non-MSA | Missouri | Carroll | 4 | 291 | 6 | 5 | 4 |
| Kansas City | Missouri | Caldwell | 1 | 259 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Livingston | 10 | 647 | 6 | 4 | 4 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 361 | 6 | 6 | 5 |
| Kansas City | Kansas | Linn | 1 | 200 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Grundy | 12 | 362 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Hickory | 4 | 311 | 6 | 4 | 5 |
| Missouri non-MSA | Missouri | Maries | 1 | 281 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Wayne | 3 | 392 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Wright | 11 | 676 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Linn | 10 | 231 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Holt | 2 | 181 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Atchison | 1 | 132 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Daviess | 5 | 278 | 4 | 3 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 202 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Shelby | 1 | 151 | 4 | 2 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 145 | 4 | 5 | 2 |
| Missouri non-MSA | Missouri | Douglas | 14 | 350 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | McDonald | 15 | 1304 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 101 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Montgomery | 5 | 248 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Scotland | 1 | 120 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 302 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Iron | 0 | 159 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Putnam | 1 | 88 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Shannon | 7 | 308 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Carter | 4 | 222 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 127 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Knox | 1 | 96 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Mercer | 0 | 56 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Ozark | 1 | 248 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 44 | 0 | 0 | 0 |
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
