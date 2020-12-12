# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/12/2020  
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
| St. Louis-Farmington | 2746 | 169710 | 1874 | 1907 | 2139 |
| Kansas City | 1310 | 113636 | 1272 | 1226 | 1325 |
| Missouri non-MSA | 1023 | 78413 | 766 | 750 | 901 |
| Springfield | 313 | 24283 | 229 | 225 | 242 |
| Columbia-Jefferson City | 139 | 25741 | 189 | 208 | 288 |
| Cape Girardeau-Sikeston | 148 | 9813 | 81 | 90 | 118 |
| St. Joseph | 104 | 7553 | 73 | 81 | 89 |
| Joplin | 169 | 12055 | 63 | 67 | 106 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1147 | 58921 | 649 | 634 | 708 |
| Kansas City | Kansas | Johnson | 338 | 32163 | 413 | 388 | 411 |
| St. Louis-Farmington | Illinois | Madison | 316 | 17273 | 232 | 232 | 244 |
| Kansas City | Missouri | Jackson | 196 | 19924 | 222 | 222 | 240 |
| St. Louis-Farmington | Illinois | St. Clair | 304 | 15973 | 218 | 215 | 205 |
| Kansas City | Missouri | Kansas City | 313 | 25983 | 218 | 231 | 271 |
| St. Louis-Farmington | Missouri | St. Charles | 229 | 22809 | 214 | 236 | 286 |
| Kansas City | Kansas | Wyandotte | 184 | 13156 | 151 | 124 | 121 |
| Springfield | Missouri | Greene | 228 | 15647 | 145 | 141 | 154 |
| St. Louis-Farmington | Missouri | St. Louis City | 270 | 14602 | 143 | 140 | 156 |
| St. Louis-Farmington | Missouri | Jefferson | 113 | 12667 | 125 | 137 | 170 |
| Columbia-Jefferson City | Missouri | Boone | 28 | 11450 | 88 | 90 | 121 |
| Missouri non-MSA | Missouri | Pettis | 38 | 3275 | 70 | 44 | 33 |
| Kansas City | Missouri | Cass | 41 | 4460 | 57 | 57 | 60 |
| St. Joseph | Missouri | Buchanan | 70 | 5374 | 54 | 58 | 59 |
| Kansas City | Missouri | Clay | 80 | 5254 | 52 | 53 | 63 |
| Joplin | Missouri | Jasper | 130 | 8929 | 51 | 55 | 83 |
| St. Louis-Farmington | Missouri | Franklin | 95 | 5458 | 50 | 51 | 63 |
| Kansas City | Kansas | Leavenworth | 35 | 4347 | 49 | 44 | 44 |
| Springfield | Missouri | Christian | 28 | 4388 | 47 | 49 | 49 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 89 | 5620 | 44 | 50 | 67 |
| Columbia-Jefferson City | Missouri | Cole | 65 | 6833 | 43 | 53 | 80 |
| St. Louis-Farmington | Illinois | Clinton | 67 | 3854 | 42 | 43 | 49 |
| Missouri non-MSA | Missouri | Pulaski | 24 | 2048 | 40 | 33 | 27 |
| St. Louis-Farmington | Illinois | Macoupin | 41 | 2725 | 36 | 43 | 47 |
| St. Louis-Farmington | Missouri | St. Francois | 51 | 5533 | 35 | 39 | 60 |
| Missouri non-MSA | Missouri | Taney | 46 | 3284 | 34 | 34 | 37 |
| St. Louis-Farmington | Illinois | Monroe | 54 | 2477 | 33 | 32 | 36 |
| St. Louis-Farmington | Missouri | Lincoln | 13 | 2860 | 32 | 33 | 41 |
| Columbia-Jefferson City | Missouri | Callaway | 13 | 3229 | 30 | 32 | 40 |
| Kansas City | Kansas | Miami | 7 | 1339 | 28 | 23 | 20 |
| Cape Girardeau-Sikeston | Missouri | Scott | 44 | 3004 | 26 | 29 | 38 |
| St. Louis-Farmington | Illinois | Jersey | 28 | 1591 | 25 | 27 | 26 |
| Missouri non-MSA | Missouri | Benton | 11 | 987 | 25 | 16 | 13 |
| Missouri non-MSA | Missouri | Johnson | 21 | 2806 | 24 | 23 | 29 |
| Missouri non-MSA | Missouri | Butler | 10 | 2468 | 24 | 25 | 29 |
| Missouri non-MSA | Missouri | Marion | 20 | 2063 | 24 | 23 | 26 |
| Missouri non-MSA | Missouri | Laclede | 37 | 2104 | 21 | 23 | 21 |
| Missouri non-MSA | Missouri | Camden | 51 | 2730 | 21 | 22 | 26 |
| Kansas City | Missouri | Platte | 17 | 1931 | 20 | 22 | 23 |
| Missouri non-MSA | Missouri | Phelps | 54 | 2062 | 20 | 25 | 31 |
| Missouri non-MSA | Missouri | Audrain | 16 | 1300 | 19 | 17 | 17 |
| Springfield | Missouri | Polk | 15 | 1586 | 17 | 15 | 13 |
| St. Louis-Farmington | Illinois | Bond | 14 | 1293 | 16 | 19 | 18 |
| Missouri non-MSA | Missouri | Stoddard | 25 | 1830 | 16 | 16 | 23 |
| Springfield | Missouri | Webster | 29 | 2027 | 16 | 16 | 20 |
| Missouri non-MSA | Missouri | Morgan | 13 | 1242 | 16 | 13 | 12 |
| Missouri non-MSA | Missouri | Miller | 28 | 1711 | 15 | 17 | 18 |
| Kansas City | Missouri | Lafayette | 31 | 1723 | 15 | 16 | 19 |
| Missouri non-MSA | Missouri | Adair | 3 | 1242 | 14 | 12 | 16 |
| Missouri non-MSA | Missouri | Randolph | 10 | 1376 | 14 | 13 | 18 |
| Missouri non-MSA | Missouri | Saline | 14 | 1726 | 14 | 11 | 17 |
| Missouri non-MSA | Missouri | Stone | 20 | 1358 | 13 | 13 | 15 |
| Missouri non-MSA | Missouri | Crawford | 14 | 1348 | 12 | 12 | 16 |
| Kansas City | Missouri | Clinton | 48 | 1037 | 12 | 12 | 12 |
| Missouri non-MSA | Missouri | Texas | 10 | 1086 | 12 | 10 | 10 |
| Missouri non-MSA | Missouri | Nodaway | 17 | 2161 | 12 | 15 | 21 |
| Joplin | Missouri | Newton | 39 | 3126 | 12 | 11 | 23 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1827 | 11 | 11 | 15 |
| Kansas City | Missouri | Ray | 6 | 837 | 11 | 11 | 12 |
| Missouri non-MSA | Missouri | Henry | 16 | 1230 | 11 | 11 | 19 |
| Missouri non-MSA | Missouri | Mississippi | 7 | 1001 | 11 | 11 | 15 |
| Missouri non-MSA | Missouri | Pike | 11 | 1078 | 10 | 13 | 17 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2069 | 10 | 13 | 20 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1207 | 10 | 11 | 17 |
| Missouri non-MSA | Missouri | Barry | 32 | 1588 | 9 | 11 | 16 |
| Missouri non-MSA | Missouri | Madison | 10 | 1004 | 9 | 10 | 12 |
| Missouri non-MSA | Missouri | Howell | 33 | 1702 | 9 | 9 | 10 |
| Kansas City | Missouri | Bates | 9 | 646 | 9 | 7 | 10 |
| Missouri non-MSA | Missouri | Washington | 27 | 1587 | 9 | 12 | 20 |
| St. Louis-Farmington | Missouri | Warren | 3 | 1350 | 9 | 11 | 18 |
| Missouri non-MSA | Missouri | Harrison | 7 | 495 | 9 | 7 | 8 |
| Missouri non-MSA | Missouri | Vernon | 13 | 786 | 8 | 9 | 9 |
| Columbia-Jefferson City | Missouri | Cooper | 10 | 1288 | 8 | 9 | 13 |
| Missouri non-MSA | Missouri | Carroll | 8 | 518 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | McDonald | 16 | 1486 | 8 | 6 | 6 |
| St. Joseph | Missouri | Andrew | 13 | 926 | 8 | 10 | 12 |
| Kansas City | Kansas | Linn | 2 | 391 | 7 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1039 | 7 | 8 | 11 |
| Missouri non-MSA | Missouri | Perry | 15 | 1661 | 7 | 10 | 18 |
| Missouri non-MSA | Missouri | New Madrid | 25 | 1450 | 7 | 9 | 15 |
| Missouri non-MSA | Missouri | Pemiscot | 19 | 1183 | 7 | 8 | 10 |
| Missouri non-MSA | Missouri | Macon | 4 | 759 | 7 | 7 | 13 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1344 | 7 | 9 | 14 |
| Missouri non-MSA | Missouri | Dent | 5 | 596 | 7 | 6 | 9 |
| Missouri non-MSA | Missouri | Livingston | 17 | 857 | 6 | 5 | 7 |
| Missouri non-MSA | Missouri | Wright | 16 | 853 | 6 | 6 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 10 | 890 | 6 | 6 | 8 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 324 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 27 | 553 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Ralls | 2 | 557 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Wayne | 3 | 562 | 6 | 5 | 5 |
| St. Joseph | Missouri | DeKalb | 16 | 666 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | Gentry | 14 | 495 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Grundy | 14 | 577 | 5 | 5 | 7 |
| St. Joseph | Kansas | Doniphan | 5 | 587 | 5 | 6 | 10 |
| Missouri non-MSA | Missouri | Lewis | 2 | 475 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 391 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Barton | 6 | 679 | 4 | 3 | 5 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 5 | 299 | 4 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 558 | 4 | 4 | 7 |
| Kansas City | Missouri | Caldwell | 3 | 445 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Shelby | 1 | 256 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Douglas | 17 | 482 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Monroe | 5 | 436 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Linn | 11 | 364 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Clark | 4 | 335 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Daviess | 8 | 385 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Oregon | 2 | 418 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Maries | 4 | 408 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Carter | 6 | 334 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Holt | 5 | 299 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Atchison | 4 | 245 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Ripley | 8 | 586 | 3 | 6 | 7 |
| Missouri non-MSA | Missouri | Iron | 1 | 271 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 3 | 386 | 2 | 4 | 6 |
| Missouri non-MSA | Missouri | Dade | 8 | 317 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Worth | 0 | 97 | 2 | 2 | 1 |
| Springfield | Missouri | Dallas | 13 | 635 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Hickory | 6 | 395 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Chariton | 0 | 273 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 366 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 4 | 320 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 8 | 585 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 196 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Putnam | 1 | 177 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Scotland | 1 | 205 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Cedar | 8 | 460 | 1 | 1 | 4 |
| Missouri non-MSA | Missouri | Mercer | 1 | 98 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 145 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 141 | 0 | 0 | 1 |
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
