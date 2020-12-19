# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/19/2020  
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
| St. Louis-Farmington | 2967 | 183252 | 1934 | 1904 | 2021 |
| Kansas City | 1408 | 122595 | 1279 | 1276 | 1285 |
| Missouri non-MSA | 1176 | 84761 | 906 | 836 | 846 |
| Springfield | 338 | 26547 | 323 | 276 | 255 |
| Columbia-Jefferson City | 168 | 27337 | 228 | 208 | 244 |
| Cape Girardeau-Sikeston | 156 | 10376 | 80 | 81 | 100 |
| Joplin | 183 | 12560 | 72 | 67 | 86 |
| St. Joseph | 119 | 8039 | 69 | 71 | 85 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1223 | 63160 | 605 | 627 | 652 |
| Kansas City | Kansas | Johnson | 383 | 35086 | 417 | 415 | 408 |
| St. Louis-Farmington | Missouri | St. Charles | 252 | 24839 | 290 | 252 | 272 |
| Kansas City | Missouri | Kansas City | 326 | 27650 | 238 | 228 | 253 |
| St. Louis-Farmington | Illinois | Madison | 350 | 18933 | 237 | 235 | 236 |
| Springfield | Missouri | Greene | 238 | 17106 | 208 | 177 | 163 |
| Kansas City | Missouri | Jackson | 207 | 21257 | 190 | 206 | 218 |
| St. Louis-Farmington | Illinois | St. Clair | 321 | 17212 | 177 | 197 | 206 |
| St. Louis-Farmington | Missouri | Jefferson | 121 | 13760 | 156 | 140 | 159 |
| Kansas City | Kansas | Wyandotte | 189 | 14105 | 135 | 143 | 129 |
| St. Louis-Farmington | Missouri | St. Louis City | 279 | 15471 | 124 | 133 | 144 |
| Columbia-Jefferson City | Missouri | Boone | 36 | 12287 | 119 | 103 | 108 |
| Springfield | Missouri | Christian | 35 | 4898 | 72 | 60 | 53 |
| Missouri non-MSA | Missouri | Pettis | 50 | 3773 | 71 | 70 | 42 |
| Kansas City | Missouri | Cass | 46 | 4935 | 67 | 62 | 59 |
| St. Louis-Farmington | Missouri | St. Francois | 58 | 5996 | 66 | 51 | 55 |
| St. Louis-Farmington | Missouri | Franklin | 102 | 5919 | 65 | 58 | 61 |
| Kansas City | Missouri | Clay | 87 | 5677 | 60 | 56 | 57 |
| Missouri non-MSA | Missouri | Howell | 35 | 2116 | 59 | 34 | 21 |
| Joplin | Missouri | Jasper | 143 | 9330 | 57 | 54 | 68 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 91 | 5995 | 53 | 48 | 59 |
| Kansas City | Kansas | Leavenworth | 36 | 4698 | 50 | 49 | 46 |
| St. Louis-Farmington | Missouri | Lincoln | 17 | 3202 | 48 | 40 | 41 |
| St. Joseph | Missouri | Buchanan | 84 | 5693 | 45 | 49 | 57 |
| Columbia-Jefferson City | Missouri | Cole | 77 | 7150 | 45 | 44 | 64 |
| St. Louis-Farmington | Illinois | Clinton | 77 | 4117 | 37 | 40 | 46 |
| St. Louis-Farmington | Illinois | Monroe | 56 | 2729 | 36 | 34 | 35 |
| Missouri non-MSA | Missouri | Taney | 47 | 3525 | 34 | 34 | 36 |
| St. Louis-Farmington | Illinois | Macoupin | 56 | 2952 | 32 | 34 | 44 |
| Columbia-Jefferson City | Missouri | Callaway | 17 | 3437 | 29 | 29 | 34 |
| Missouri non-MSA | Missouri | Laclede | 38 | 2291 | 26 | 24 | 23 |
| Missouri non-MSA | Missouri | Johnson | 25 | 2988 | 26 | 25 | 27 |
| Kansas City | Kansas | Miami | 7 | 1514 | 25 | 26 | 23 |
| Kansas City | Missouri | Platte | 19 | 2103 | 24 | 22 | 23 |
| Missouri non-MSA | Missouri | Pulaski | 26 | 2217 | 24 | 32 | 28 |
| Springfield | Missouri | Webster | 35 | 2193 | 23 | 20 | 19 |
| Missouri non-MSA | Missouri | Butler | 12 | 2631 | 23 | 23 | 27 |
| Missouri non-MSA | Missouri | Adair | 4 | 1400 | 22 | 18 | 15 |
| Missouri non-MSA | Missouri | Miller | 42 | 1864 | 21 | 18 | 18 |
| Missouri non-MSA | Missouri | Phelps | 76 | 2215 | 21 | 21 | 28 |
| Missouri non-MSA | Missouri | Audrain | 23 | 1451 | 21 | 20 | 18 |
| St. Louis-Farmington | Illinois | Jersey | 33 | 1740 | 21 | 23 | 24 |
| Missouri non-MSA | Missouri | Camden | 58 | 2874 | 20 | 21 | 24 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1970 | 20 | 16 | 14 |
| Cape Girardeau-Sikeston | Missouri | Scott | 49 | 3141 | 19 | 23 | 31 |
| Missouri non-MSA | Missouri | Texas | 13 | 1218 | 18 | 15 | 11 |
| Missouri non-MSA | Missouri | Benton | 15 | 1114 | 18 | 21 | 13 |
| Kansas City | Missouri | Ray | 7 | 960 | 17 | 14 | 12 |
| Missouri non-MSA | Missouri | Crawford | 15 | 1470 | 17 | 14 | 15 |
| St. Louis-Farmington | Missouri | Warren | 6 | 1471 | 17 | 13 | 16 |
| Missouri non-MSA | Missouri | Saline | 16 | 1845 | 17 | 15 | 15 |
| Kansas City | Missouri | Lafayette | 36 | 1839 | 16 | 15 | 18 |
| Missouri non-MSA | Missouri | Stone | 23 | 1470 | 16 | 14 | 14 |
| Missouri non-MSA | Missouri | Stoddard | 29 | 1941 | 15 | 16 | 19 |
| St. Louis-Farmington | Illinois | Bond | 15 | 1402 | 15 | 16 | 17 |
| Missouri non-MSA | Missouri | Morgan | 16 | 1350 | 15 | 15 | 13 |
| Missouri non-MSA | Missouri | Randolph | 15 | 1484 | 15 | 14 | 14 |
| Joplin | Missouri | Newton | 40 | 3230 | 14 | 13 | 18 |
| Missouri non-MSA | Missouri | Henry | 18 | 1333 | 14 | 12 | 15 |
| Springfield | Missouri | Polk | 16 | 1688 | 14 | 15 | 13 |
| Missouri non-MSA | Missouri | Marion | 23 | 2164 | 14 | 19 | 22 |
| Kansas City | Missouri | Clinton | 49 | 1138 | 14 | 13 | 11 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2169 | 14 | 12 | 16 |
| Missouri non-MSA | Missouri | Perry | 15 | 1758 | 13 | 10 | 14 |
| Missouri non-MSA | Missouri | Wright | 19 | 946 | 13 | 10 | 8 |
| Columbia-Jefferson City | Missouri | Cooper | 14 | 1379 | 13 | 10 | 11 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1296 | 12 | 11 | 13 |
| Missouri non-MSA | Missouri | Barry | 35 | 1676 | 12 | 11 | 13 |
| Missouri non-MSA | Missouri | Vernon | 13 | 869 | 11 | 10 | 9 |
| Missouri non-MSA | Missouri | Pike | 11 | 1159 | 11 | 11 | 14 |
| Missouri non-MSA | Missouri | Madison | 10 | 1084 | 11 | 10 | 12 |
| Missouri non-MSA | Missouri | Mississippi | 9 | 1080 | 11 | 11 | 13 |
| Missouri non-MSA | Missouri | Macon | 5 | 838 | 11 | 9 | 11 |
| Missouri non-MSA | Missouri | Livingston | 19 | 935 | 11 | 9 | 8 |
| Missouri non-MSA | Missouri | Oregon | 3 | 491 | 10 | 6 | 5 |
| St. Joseph | Missouri | Andrew | 13 | 998 | 10 | 9 | 11 |
| Missouri non-MSA | Missouri | Douglas | 19 | 551 | 9 | 6 | 6 |
| Missouri non-MSA | Missouri | Harrison | 7 | 563 | 9 | 9 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 26 | 1518 | 9 | 8 | 11 |
| Missouri non-MSA | Missouri | Carroll | 8 | 585 | 9 | 8 | 8 |
| Columbia-Jefferson City | Missouri | Moniteau | 16 | 1411 | 9 | 8 | 11 |
| Missouri non-MSA | Missouri | Washington | 34 | 1652 | 9 | 9 | 15 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2224 | 9 | 10 | 15 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1548 | 8 | 8 | 7 |
| Kansas City | Missouri | Bates | 10 | 708 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | Gentry | 15 | 556 | 8 | 7 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1093 | 7 | 7 | 9 |
| Missouri non-MSA | Missouri | Gasconade | 28 | 605 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Iron | 1 | 322 | 7 | 5 | 4 |
| St. Joseph | Missouri | DeKalb | 17 | 716 | 7 | 6 | 7 |
| Kansas City | Kansas | Linn | 3 | 438 | 6 | 7 | 6 |
| St. Joseph | Kansas | Doniphan | 5 | 632 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 436 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Wayne | 4 | 607 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Grundy | 18 | 620 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Dent | 6 | 638 | 6 | 6 | 7 |
| Kansas City | Missouri | Caldwell | 3 | 487 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Ripley | 8 | 627 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Daviess | 9 | 424 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Barton | 7 | 718 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 20 | 1220 | 5 | 6 | 8 |
| Missouri non-MSA | Missouri | Monroe | 5 | 468 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 177 | 4 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 11 | 921 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Ralls | 4 | 588 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 616 | 4 | 3 | 3 |
| Springfield | Missouri | Dallas | 14 | 662 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Ozark | 4 | 346 | 3 | 2 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 349 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Shannon | 9 | 391 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 11 | 389 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 4 | 410 | 3 | 3 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 580 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Lewis | 2 | 496 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Cedar | 8 | 481 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Maries | 6 | 429 | 3 | 3 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 5 | 319 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Carter | 6 | 352 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Mercer | 1 | 116 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 8 | 335 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 213 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Holt | 7 | 316 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Shelby | 1 | 272 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Chariton | 2 | 289 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Hickory | 6 | 408 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Scotland | 3 | 217 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Atchison | 4 | 255 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Putnam | 1 | 187 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 106 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 4 | 342 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Knox | 1 | 143 | 0 | 0 | 0 |
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
