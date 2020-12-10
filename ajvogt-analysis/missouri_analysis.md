# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/10/2020  
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
| St. Louis-Farmington | 2682 | 166126 | 1971 | 1947 | 2176 |
| Kansas City | 1289 | 111191 | 1402 | 1241 | 1343 |
| Missouri non-MSA | 1005 | 77232 | 880 | 784 | 919 |
| Springfield | 300 | 24060 | 279 | 247 | 251 |
| Columbia-Jefferson City | 139 | 25483 | 245 | 229 | 303 |
| Cape Girardeau-Sikeston | 128 | 9686 | 98 | 96 | 124 |
| St. Joseph | 101 | 7477 | 93 | 89 | 93 |
| Joplin | 169 | 11993 | 78 | 76 | 114 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1128 | 57538 | 649 | 625 | 712 |
| Kansas City | Kansas | Johnson | 321 | 31155 | 439 | 373 | 412 |
| Kansas City | Missouri | Kansas City | 313 | 25728 | 276 | 253 | 283 |
| St. Louis-Farmington | Missouri | St. Charles | 229 | 22553 | 258 | 256 | 297 |
| Kansas City | Missouri | Jackson | 193 | 19522 | 244 | 229 | 245 |
| St. Louis-Farmington | Illinois | Madison | 307 | 16760 | 233 | 228 | 246 |
| St. Louis-Farmington | Illinois | St. Clair | 290 | 15499 | 211 | 213 | 203 |
| Springfield | Missouri | Greene | 215 | 15524 | 172 | 157 | 161 |
| St. Louis-Farmington | Missouri | St. Louis City | 265 | 14365 | 154 | 148 | 158 |
| St. Louis-Farmington | Missouri | Jefferson | 112 | 12498 | 148 | 153 | 179 |
| Kansas City | Kansas | Wyandotte | 184 | 12778 | 142 | 114 | 116 |
| Columbia-Jefferson City | Missouri | Boone | 28 | 11348 | 110 | 97 | 126 |
| St. Joseph | Missouri | Buchanan | 68 | 5312 | 67 | 61 | 62 |
| Kansas City | Missouri | Cass | 41 | 4381 | 65 | 58 | 61 |
| Missouri non-MSA | Missouri | Pettis | 38 | 3148 | 64 | 36 | 30 |
| Joplin | Missouri | Jasper | 130 | 8879 | 63 | 63 | 89 |
| Columbia-Jefferson City | Missouri | Cole | 65 | 6766 | 61 | 60 | 84 |
| Springfield | Missouri | Christian | 28 | 4339 | 60 | 53 | 50 |
| Kansas City | Missouri | Clay | 80 | 5173 | 60 | 55 | 65 |
| St. Louis-Farmington | Missouri | Franklin | 95 | 5380 | 58 | 57 | 66 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 70 | 5553 | 53 | 55 | 72 |
| Kansas City | Kansas | Leavenworth | 34 | 4269 | 53 | 46 | 45 |
| Missouri non-MSA | Missouri | Pulaski | 24 | 2001 | 46 | 34 | 26 |
| Missouri non-MSA | Missouri | Taney | 42 | 3248 | 43 | 38 | 37 |
| St. Louis-Farmington | Illinois | Clinton | 66 | 3751 | 42 | 45 | 51 |
| St. Louis-Farmington | Missouri | St. Francois | 51 | 5477 | 40 | 43 | 63 |
| St. Louis-Farmington | Missouri | Lincoln | 13 | 2809 | 38 | 36 | 41 |
| Columbia-Jefferson City | Missouri | Callaway | 13 | 3189 | 37 | 35 | 41 |
| St. Louis-Farmington | Illinois | Macoupin | 32 | 2642 | 36 | 41 | 49 |
| St. Louis-Farmington | Illinois | Monroe | 50 | 2400 | 33 | 31 | 36 |
| Cape Girardeau-Sikeston | Missouri | Scott | 44 | 2969 | 32 | 31 | 39 |
| Missouri non-MSA | Missouri | Laclede | 35 | 2075 | 29 | 25 | 22 |
| Kansas City | Kansas | Miami | 7 | 1296 | 29 | 23 | 20 |
| Missouri non-MSA | Missouri | Butler | 10 | 2427 | 27 | 25 | 29 |
| St. Louis-Farmington | Illinois | Jersey | 26 | 1555 | 27 | 26 | 26 |
| Missouri non-MSA | Missouri | Phelps | 54 | 2021 | 26 | 27 | 31 |
| Missouri non-MSA | Missouri | Marion | 20 | 2017 | 26 | 24 | 26 |
| Missouri non-MSA | Missouri | Johnson | 20 | 2764 | 26 | 25 | 30 |
| Missouri non-MSA | Missouri | Camden | 51 | 2699 | 25 | 23 | 27 |
| Kansas City | Missouri | Platte | 17 | 1908 | 23 | 23 | 24 |
| Missouri non-MSA | Missouri | Benton | 11 | 944 | 22 | 14 | 11 |
| Springfield | Missouri | Webster | 29 | 2007 | 22 | 17 | 20 |
| Missouri non-MSA | Missouri | Audrain | 16 | 1271 | 20 | 18 | 17 |
| Springfield | Missouri | Polk | 15 | 1560 | 20 | 16 | 13 |
| Missouri non-MSA | Missouri | Miller | 28 | 1691 | 20 | 17 | 18 |
| St. Louis-Farmington | Illinois | Bond | 14 | 1252 | 20 | 19 | 18 |
| Missouri non-MSA | Missouri | Stoddard | 25 | 1820 | 20 | 18 | 25 |
| Missouri non-MSA | Missouri | Morgan | 13 | 1220 | 18 | 13 | 12 |
| Missouri non-MSA | Missouri | Randolph | 9 | 1363 | 17 | 15 | 18 |
| Kansas City | Missouri | Lafayette | 31 | 1704 | 17 | 18 | 20 |
| Missouri non-MSA | Missouri | Stone | 19 | 1342 | 16 | 14 | 15 |
| Joplin | Missouri | Newton | 39 | 3114 | 14 | 13 | 25 |
| Kansas City | Missouri | Clinton | 48 | 1015 | 14 | 12 | 12 |
| Missouri non-MSA | Missouri | Crawford | 14 | 1330 | 14 | 13 | 16 |
| Missouri non-MSA | Missouri | Adair | 3 | 1209 | 14 | 12 | 17 |
| Missouri non-MSA | Missouri | Texas | 10 | 1070 | 13 | 9 | 10 |
| Missouri non-MSA | Missouri | Nodaway | 16 | 2133 | 13 | 16 | 21 |
| Missouri non-MSA | Missouri | Henry | 15 | 1214 | 13 | 13 | 19 |
| Missouri non-MSA | Missouri | Pike | 11 | 1051 | 13 | 13 | 17 |
| Missouri non-MSA | Missouri | Barry | 32 | 1569 | 12 | 12 | 16 |
| Missouri non-MSA | Missouri | Mississippi | 7 | 992 | 12 | 12 | 15 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2052 | 12 | 15 | 21 |
| Missouri non-MSA | Missouri | Saline | 14 | 1698 | 12 | 12 | 17 |
| Kansas City | Missouri | Ray | 6 | 816 | 12 | 11 | 12 |
| Missouri non-MSA | Missouri | Vernon | 13 | 777 | 12 | 9 | 10 |
| Missouri non-MSA | Missouri | Howell | 32 | 1691 | 12 | 9 | 11 |
| Columbia-Jefferson City | Missouri | Cooper | 10 | 1271 | 12 | 10 | 14 |
| St. Joseph | Missouri | Andrew | 12 | 919 | 11 | 11 | 12 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1187 | 11 | 12 | 17 |
| Missouri non-MSA | Missouri | Madison | 10 | 993 | 11 | 11 | 12 |
| St. Louis-Farmington | Missouri | Warren | 3 | 1334 | 11 | 13 | 19 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1800 | 10 | 12 | 15 |
| Missouri non-MSA | Missouri | Washington | 27 | 1564 | 10 | 13 | 21 |
| Missouri non-MSA | Missouri | Perry | 15 | 1644 | 10 | 10 | 19 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1030 | 10 | 9 | 11 |
| Kansas City | Missouri | Bates | 9 | 628 | 10 | 8 | 10 |
| Missouri non-MSA | Missouri | Harrison | 5 | 478 | 10 | 7 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1333 | 9 | 10 | 16 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 10 | 880 | 9 | 7 | 9 |
| Missouri non-MSA | Missouri | Wright | 16 | 851 | 9 | 7 | 6 |
| Missouri non-MSA | Missouri | Carroll | 8 | 508 | 9 | 7 | 7 |
| Missouri non-MSA | Missouri | McDonald | 16 | 1480 | 9 | 6 | 6 |
| Missouri non-MSA | Missouri | Livingston | 16 | 854 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 19 | 1169 | 8 | 9 | 10 |
| Missouri non-MSA | Missouri | Gentry | 14 | 488 | 8 | 6 | 7 |
| Missouri non-MSA | Missouri | Dent | 5 | 586 | 7 | 7 | 8 |
| St. Joseph | Kansas | Doniphan | 5 | 587 | 7 | 9 | 10 |
| Missouri non-MSA | Missouri | Grundy | 14 | 567 | 7 | 5 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 25 | 1435 | 7 | 10 | 16 |
| Missouri non-MSA | Missouri | Macon | 4 | 748 | 7 | 8 | 13 |
| St. Joseph | Missouri | DeKalb | 16 | 659 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Ralls | 2 | 545 | 7 | 7 | 9 |
| Kansas City | Kansas | Linn | 2 | 371 | 6 | 7 | 6 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 313 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Wayne | 3 | 555 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 27 | 540 | 6 | 6 | 6 |
| Kansas City | Missouri | Caldwell | 3 | 447 | 6 | 5 | 7 |
| Missouri non-MSA | Missouri | Lewis | 2 | 474 | 5 | 3 | 5 |
| Missouri non-MSA | Missouri | Barton | 6 | 675 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Daviess | 8 | 383 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 2 | 381 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Shelby | 1 | 255 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Ripley | 8 | 584 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Monroe | 5 | 431 | 4 | 4 | 6 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 546 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Linn | 11 | 359 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 384 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Iron | 1 | 269 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Douglas | 17 | 477 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | Maries | 4 | 402 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Carter | 6 | 326 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Clark | 4 | 328 | 3 | 2 | 5 |
| Missouri non-MSA | Missouri | Holt | 5 | 293 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Oregon | 2 | 410 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 362 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Atchison | 4 | 236 | 3 | 2 | 4 |
| Springfield | Missouri | Dallas | 13 | 630 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Chariton | 0 | 269 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Worth | 0 | 93 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 3 | 316 | 2 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 4 | 284 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dade | 8 | 310 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 7 | 587 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Hickory | 6 | 390 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 196 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 8 | 459 | 1 | 1 | 5 |
| Missouri non-MSA | Missouri | Scotland | 1 | 202 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 144 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 175 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Mercer | 1 | 96 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 137 | 0 | 0 | 1 |
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
