# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/13/2020  
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
| St. Louis-Farmington | 2051 | 108007 | 2163 | 1726 | 1221 |
| Kansas City | 1005 | 74477 | 1082 | 1007 | 767 |
| Missouri non-MSA | 706 | 52618 | 1024 | 918 | 718 |
| Columbia-Jefferson City | 81 | 17593 | 410 | 374 | 267 |
| Springfield | 212 | 17263 | 241 | 239 | 191 |
| Joplin | 121 | 9059 | 141 | 120 | 96 |
| Cape Girardeau-Sikeston | 98 | 6421 | 139 | 116 | 85 |
| St. Joseph | 64 | 4933 | 83 | 70 | 59 |
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
| St. Louis-Farmington | Missouri | St. Louis | 911 | 38620 | 671 | 554 | 398 |
| St. Louis-Farmington | Missouri | St. Charles | 165 | 14596 | 309 | 260 | 197 |
| Kansas City | Kansas | Johnson | 239 | 19808 | 278 | 285 | 221 |
| St. Louis-Farmington | Illinois | Madison | 173 | 10169 | 273 | 194 | 124 |
| Kansas City | Missouri | Kansas City | 241 | 18068 | 272 | 248 | 166 |
| Kansas City | Missouri | Jackson | 152 | 12890 | 238 | 196 | 152 |
| St. Louis-Farmington | Missouri | Jefferson | 94 | 7764 | 183 | 151 | 97 |
| St. Louis-Farmington | Illinois | St. Clair | 244 | 9923 | 174 | 125 | 87 |
| Columbia-Jefferson City | Missouri | Boone | 15 | 8040 | 170 | 139 | 93 |
| Springfield | Missouri | Greene | 155 | 11190 | 154 | 149 | 115 |
| St. Louis-Farmington | Missouri | St. Louis City | 230 | 10117 | 130 | 112 | 82 |
| Columbia-Jefferson City | Missouri | Cole | 34 | 4558 | 113 | 110 | 82 |
| Joplin | Missouri | Jasper | 95 | 6585 | 110 | 89 | 64 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 58 | 3699 | 90 | 71 | 48 |
| St. Louis-Farmington | Missouri | St. Francois | 36 | 3819 | 76 | 66 | 45 |
| St. Louis-Farmington | Missouri | Franklin | 57 | 3631 | 70 | 64 | 51 |
| Kansas City | Missouri | Clay | 54 | 3424 | 63 | 61 | 47 |
| St. Joseph | Missouri | Buchanan | 46 | 3649 | 61 | 47 | 39 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 2083 | 59 | 59 | 40 |
| St. Louis-Farmington | Illinois | Macoupin | 14 | 1344 | 56 | 35 | 23 |
| Kansas City | Kansas | Wyandotte | 167 | 9498 | 53 | 58 | 56 |
| St. Louis-Farmington | Illinois | Clinton | 47 | 2392 | 51 | 38 | 31 |
| Missouri non-MSA | Missouri | Pettis | 28 | 2302 | 50 | 48 | 33 |
| Kansas City | Missouri | Cass | 35 | 2703 | 50 | 43 | 32 |
| Springfield | Missouri | Christian | 20 | 2964 | 49 | 46 | 37 |
| St. Louis-Farmington | Illinois | Jersey | 22 | 837 | 43 | 25 | 13 |
| St. Louis-Farmington | Illinois | Monroe | 40 | 1406 | 37 | 29 | 19 |
| St. Louis-Farmington | Missouri | Lincoln | 7 | 1667 | 37 | 31 | 23 |
| Missouri non-MSA | Missouri | Johnson | 11 | 1953 | 37 | 32 | 22 |
| Cape Girardeau-Sikeston | Missouri | Scott | 33 | 1889 | 34 | 32 | 25 |
| Missouri non-MSA | Missouri | Camden | 41 | 1985 | 31 | 26 | 22 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1603 | 31 | 30 | 23 |
| Missouri non-MSA | Missouri | Taney | 36 | 2194 | 31 | 31 | 23 |
| Joplin | Missouri | Newton | 26 | 2474 | 31 | 30 | 31 |
| Missouri non-MSA | Missouri | Lawrence | 32 | 1489 | 29 | 25 | 22 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 750 | 29 | 24 | 16 |
| Missouri non-MSA | Missouri | Washington | 21 | 997 | 28 | 23 | 15 |
| Missouri non-MSA | Missouri | Marion | 15 | 1298 | 28 | 25 | 17 |
| Missouri non-MSA | Missouri | Henry | 8 | 701 | 27 | 22 | 13 |
| Missouri non-MSA | Missouri | Perry | 8 | 1123 | 27 | 22 | 13 |
| Missouri non-MSA | Missouri | Phelps | 33 | 1175 | 26 | 23 | 19 |
| Kansas City | Kansas | Leavenworth | 25 | 3010 | 25 | 23 | 18 |
| St. Louis-Farmington | Illinois | Bond | 9 | 757 | 24 | 16 | 12 |
| Columbia-Jefferson City | Missouri | Moniteau | 14 | 936 | 23 | 21 | 17 |
| Missouri non-MSA | Missouri | Adair | 0 | 798 | 23 | 19 | 13 |
| Kansas City | Missouri | Lafayette | 27 | 1153 | 23 | 21 | 16 |
| Missouri non-MSA | Missouri | Miller | 20 | 1193 | 23 | 21 | 18 |
| Missouri non-MSA | Missouri | Laclede | 28 | 1478 | 22 | 18 | 18 |
| Columbia-Jefferson City | Missouri | Cooper | 6 | 906 | 21 | 20 | 13 |
| Missouri non-MSA | Missouri | Saline | 11 | 1233 | 21 | 19 | 12 |
| Missouri non-MSA | Missouri | Barry | 19 | 1126 | 21 | 20 | 18 |
| Missouri non-MSA | Missouri | Stoddard | 17 | 1139 | 20 | 17 | 15 |
| Missouri non-MSA | Missouri | Pike | 8 | 577 | 20 | 15 | 10 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 1016 | 20 | 16 | 12 |
| Missouri non-MSA | Missouri | Crawford | 10 | 892 | 20 | 17 | 13 |
| Missouri non-MSA | Missouri | Butler | 8 | 1596 | 20 | 24 | 25 |
| Springfield | Missouri | Webster | 23 | 1441 | 19 | 19 | 17 |
| Kansas City | Missouri | Platte | 13 | 1260 | 18 | 17 | 15 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1386 | 18 | 17 | 14 |
| Kansas City | Missouri | Ray | 2 | 488 | 17 | 14 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 13 | 1235 | 16 | 15 | 13 |
| Missouri non-MSA | Missouri | Texas | 6 | 793 | 16 | 14 | 11 |
| St. Louis-Farmington | Missouri | Warren | 2 | 825 | 16 | 13 | 10 |
| Missouri non-MSA | Missouri | Randolph | 4 | 852 | 16 | 16 | 14 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 724 | 15 | 16 | 15 |
| Missouri non-MSA | Missouri | Vernon | 4 | 509 | 15 | 11 | 8 |
| Missouri non-MSA | Missouri | Stone | 13 | 909 | 15 | 14 | 11 |
| Missouri non-MSA | Missouri | Pemiscot | 15 | 899 | 14 | 11 | 9 |
| Missouri non-MSA | Missouri | Macon | 1 | 383 | 14 | 11 | 6 |
| Missouri non-MSA | Missouri | Audrain | 11 | 791 | 13 | 14 | 10 |
| Missouri non-MSA | Missouri | Benton | 7 | 622 | 13 | 9 | 6 |
| Kansas City | Missouri | Clinton | 38 | 683 | 12 | 12 | 11 |
| Missouri non-MSA | Missouri | Morgan | 8 | 875 | 12 | 13 | 12 |
| Missouri non-MSA | Missouri | Howell | 22 | 1399 | 11 | 15 | 17 |
| Missouri non-MSA | Missouri | Madison | 7 | 638 | 11 | 9 | 9 |
| Missouri non-MSA | Missouri | Ripley | 5 | 388 | 11 | 8 | 7 |
| Springfield | Missouri | Polk | 11 | 1185 | 10 | 15 | 13 |
| Missouri non-MSA | Missouri | Lewis | 2 | 325 | 10 | 8 | 5 |
| Missouri non-MSA | Missouri | Ralls | 1 | 303 | 9 | 6 | 4 |
| St. Joseph | Missouri | Andrew | 8 | 569 | 9 | 8 | 7 |
| Kansas City | Kansas | Miami | 2 | 712 | 9 | 9 | 7 |
| Missouri non-MSA | Missouri | Cedar | 4 | 338 | 9 | 7 | 5 |
| Kansas City | Missouri | Bates | 8 | 347 | 9 | 6 | 5 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 5 | 637 | 8 | 9 | 8 |
| Missouri non-MSA | Missouri | Monroe | 3 | 267 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | Gentry | 11 | 277 | 8 | 6 | 4 |
| Springfield | Missouri | Dallas | 3 | 483 | 7 | 8 | 8 |
| Missouri non-MSA | Missouri | Clark | 2 | 206 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Dade | 5 | 215 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Chariton | 0 | 145 | 7 | 6 | 3 |
| Kansas City | Missouri | Caldwell | 1 | 253 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Dent | 4 | 341 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Barton | 4 | 520 | 6 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 346 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 4 | 453 | 6 | 9 | 6 |
| St. Joseph | Missouri | DeKalb | 8 | 428 | 6 | 9 | 7 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 140 | 6 | 5 | 2 |
| Missouri non-MSA | Missouri | Grundy | 12 | 351 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 546 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 355 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Carroll | 4 | 285 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Harrison | 1 | 253 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Wayne | 3 | 390 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 194 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Livingston | 10 | 637 | 6 | 5 | 3 |
| St. Joseph | Kansas | Doniphan | 2 | 287 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Holt | 2 | 179 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Wright | 11 | 674 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Maries | 1 | 275 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Linn | 10 | 223 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Montgomery | 5 | 246 | 5 | 5 | 5 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 196 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Hickory | 4 | 300 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Oregon | 0 | 299 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Daviess | 5 | 277 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 97 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 158 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Atchison | 1 | 125 | 4 | 3 | 1 |
| Missouri non-MSA | Missouri | Douglas | 14 | 345 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Shelby | 1 | 146 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Scotland | 1 | 117 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | McDonald | 15 | 1299 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 124 | 3 | 2 | 2 |
| Kansas City | Kansas | Linn | 1 | 180 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Shannon | 7 | 304 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Knox | 1 | 94 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 83 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 1 | 248 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Carter | 4 | 215 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Mercer | 0 | 52 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 40 | 0 | 0 | 0 |
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
