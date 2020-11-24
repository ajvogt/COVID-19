# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/24/2020  
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
| St. Louis-Farmington | 2182 | 133859 | 2332 | 2359 | 1798 |
| Kansas City | 1103 | 91179 | 1491 | 1450 | 1144 |
| Missouri non-MSA | 765 | 64548 | 1045 | 1063 | 893 |
| Columbia-Jefferson City | 88 | 21614 | 337 | 373 | 327 |
| Springfield | 230 | 20132 | 260 | 259 | 225 |
| Cape Girardeau-Sikeston | 104 | 8101 | 157 | 153 | 118 |
| Joplin | 141 | 10694 | 144 | 152 | 120 |
| St. Joseph | 73 | 6016 | 107 | 96 | 72 |
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
| St. Louis-Farmington | Missouri | St. Louis | 944 | 46954 | 701 | 770 | 585 |
| Kansas City | Kansas | Johnson | 271 | 25025 | 434 | 445 | 362 |
| St. Louis-Farmington | Missouri | St. Charles | 186 | 18327 | 358 | 334 | 264 |
| Kansas City | Missouri | Kansas City | 255 | 21608 | 321 | 313 | 249 |
| Kansas City | Missouri | Jackson | 171 | 15920 | 279 | 267 | 205 |
| St. Louis-Farmington | Illinois | Madison | 217 | 13074 | 257 | 265 | 199 |
| St. Louis-Farmington | Missouri | Jefferson | 96 | 9929 | 211 | 200 | 150 |
| St. Louis-Farmington | Illinois | St. Clair | 254 | 12087 | 199 | 191 | 140 |
| Springfield | Missouri | Greene | 169 | 12997 | 167 | 165 | 140 |
| St. Louis-Farmington | Missouri | St. Louis City | 230 | 11958 | 166 | 167 | 124 |
| Columbia-Jefferson City | Missouri | Boone | 17 | 9720 | 139 | 155 | 127 |
| Kansas City | Kansas | Wyandotte | 178 | 10924 | 137 | 117 | 90 |
| Joplin | Missouri | Jasper | 104 | 7842 | 109 | 117 | 91 |
| Columbia-Jefferson City | Missouri | Cole | 38 | 5711 | 97 | 105 | 95 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 59 | 4642 | 90 | 89 | 68 |
| Kansas City | Missouri | Clay | 62 | 4340 | 84 | 80 | 62 |
| St. Louis-Farmington | Missouri | St. Francois | 36 | 4716 | 80 | 81 | 64 |
| St. Louis-Farmington | Missouri | Franklin | 59 | 4468 | 78 | 77 | 64 |
| Kansas City | Missouri | Cass | 36 | 3446 | 70 | 65 | 48 |
| St. Joseph | Missouri | Buchanan | 53 | 4308 | 66 | 61 | 46 |
| St. Louis-Farmington | Illinois | Clinton | 56 | 2984 | 57 | 55 | 41 |
| St. Louis-Farmington | Illinois | Macoupin | 17 | 1918 | 57 | 55 | 37 |
| Cape Girardeau-Sikeston | Missouri | Scott | 36 | 2449 | 53 | 48 | 35 |
| St. Louis-Farmington | Missouri | Lincoln | 8 | 2217 | 51 | 47 | 36 |
| Springfield | Missouri | Christian | 22 | 3526 | 50 | 50 | 43 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 2597 | 45 | 46 | 48 |
| Missouri non-MSA | Missouri | Taney | 37 | 2660 | 44 | 38 | 33 |
| Kansas City | Kansas | Leavenworth | 29 | 3503 | 42 | 42 | 30 |
| St. Louis-Farmington | Illinois | Monroe | 44 | 1875 | 39 | 40 | 32 |
| Missouri non-MSA | Missouri | Phelps | 38 | 1586 | 39 | 35 | 25 |
| Missouri non-MSA | Missouri | Stoddard | 19 | 1490 | 35 | 30 | 21 |
| Joplin | Missouri | Newton | 37 | 2852 | 35 | 35 | 28 |
| Missouri non-MSA | Missouri | Johnson | 12 | 2335 | 33 | 34 | 29 |
| Missouri non-MSA | Missouri | Butler | 8 | 1967 | 32 | 30 | 28 |
| Missouri non-MSA | Missouri | Camden | 44 | 2329 | 32 | 33 | 26 |
| Missouri non-MSA | Missouri | Marion | 15 | 1625 | 28 | 28 | 24 |
| Springfield | Missouri | Webster | 23 | 1727 | 28 | 24 | 20 |
| Kansas City | Missouri | Platte | 14 | 1528 | 28 | 24 | 18 |
| Missouri non-MSA | Missouri | Lawrence | 33 | 1813 | 27 | 28 | 25 |
| Missouri non-MSA | Missouri | Perry | 8 | 1455 | 26 | 28 | 22 |
| Missouri non-MSA | Missouri | Pulaski | 15 | 1496 | 26 | 21 | 18 |
| St. Louis-Farmington | Missouri | Warren | 2 | 1103 | 26 | 24 | 16 |
| Missouri non-MSA | Missouri | Washington | 22 | 1334 | 25 | 28 | 23 |
| St. Louis-Farmington | Illinois | Jersey | 23 | 1118 | 25 | 25 | 21 |
| Missouri non-MSA | Missouri | Henry | 9 | 998 | 24 | 27 | 20 |
| Missouri non-MSA | Missouri | Saline | 12 | 1496 | 22 | 23 | 18 |
| Missouri non-MSA | Missouri | Macon | 2 | 609 | 22 | 18 | 13 |
| Kansas City | Missouri | Lafayette | 29 | 1389 | 22 | 21 | 19 |
| Missouri non-MSA | Missouri | Barry | 22 | 1377 | 22 | 21 | 19 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 775 | 21 | 18 | 11 |
| Missouri non-MSA | Missouri | Laclede | 29 | 1693 | 21 | 19 | 17 |
| Missouri non-MSA | Missouri | Miller | 23 | 1417 | 20 | 20 | 19 |
| Missouri non-MSA | Missouri | Adair | 1 | 1017 | 20 | 22 | 17 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1858 | 19 | 26 | 25 |
| Missouri non-MSA | Missouri | Pike | 8 | 819 | 19 | 21 | 15 |
| Kansas City | Kansas | Miami | 2 | 923 | 19 | 17 | 13 |
| Missouri non-MSA | Missouri | Stone | 15 | 1125 | 19 | 18 | 15 |
| Missouri non-MSA | Missouri | Crawford | 11 | 1112 | 18 | 19 | 16 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 1256 | 18 | 21 | 16 |
| Missouri non-MSA | Missouri | Randolph | 5 | 1122 | 17 | 22 | 17 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 962 | 17 | 21 | 20 |
| Missouri non-MSA | Missouri | Pettis | 29 | 2583 | 16 | 24 | 34 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1595 | 16 | 17 | 16 |
| Missouri non-MSA | Missouri | Audrain | 11 | 982 | 16 | 16 | 13 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1152 | 16 | 22 | 18 |
| St. Joseph | Missouri | Andrew | 9 | 735 | 16 | 14 | 10 |
| Columbia-Jefferson City | Missouri | Cooper | 6 | 1109 | 15 | 18 | 16 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 876 | 14 | 14 | 13 |
| Missouri non-MSA | Missouri | Madison | 7 | 800 | 14 | 13 | 10 |
| Kansas City | Missouri | Bates | 8 | 495 | 14 | 13 | 8 |
| St. Louis-Farmington | Illinois | Bond | 10 | 914 | 13 | 16 | 14 |
| Missouri non-MSA | Missouri | Dent | 4 | 471 | 13 | 10 | 7 |
| St. Joseph | Kansas | Doniphan | 2 | 434 | 12 | 11 | 7 |
| Missouri non-MSA | Missouri | Morgan | 9 | 1012 | 12 | 12 | 12 |
| St. Joseph | Missouri | DeKalb | 9 | 539 | 12 | 9 | 8 |
| Kansas City | Missouri | Clinton | 42 | 829 | 12 | 13 | 11 |
| Missouri non-MSA | Missouri | Vernon | 5 | 630 | 12 | 11 | 10 |
| Missouri non-MSA | Missouri | Ralls | 1 | 419 | 11 | 10 | 7 |
| Kansas City | Missouri | Ray | 4 | 633 | 10 | 13 | 12 |
| Missouri non-MSA | Missouri | Pemiscot | 16 | 1021 | 10 | 12 | 10 |
| Missouri non-MSA | Missouri | Carroll | 5 | 391 | 10 | 8 | 7 |
| Missouri non-MSA | Missouri | Texas | 7 | 911 | 10 | 11 | 11 |
| Missouri non-MSA | Missouri | Harrison | 1 | 373 | 10 | 9 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 7 | 766 | 10 | 11 | 10 |
| Missouri non-MSA | Missouri | Howell | 26 | 1518 | 9 | 11 | 13 |
| Missouri non-MSA | Missouri | Grundy | 13 | 479 | 9 | 10 | 7 |
| Missouri non-MSA | Missouri | Livingston | 11 | 743 | 9 | 8 | 6 |
| Missouri non-MSA | Missouri | Gentry | 11 | 389 | 9 | 9 | 6 |
| Kansas City | Missouri | Caldwell | 1 | 358 | 9 | 8 | 6 |
| Springfield | Missouri | Polk | 11 | 1310 | 9 | 10 | 12 |
| Missouri non-MSA | Missouri | Cedar | 4 | 428 | 8 | 9 | 6 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 449 | 8 | 8 | 6 |
| Missouri non-MSA | Missouri | Wayne | 3 | 462 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Clark | 2 | 282 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | Holt | 3 | 246 | 7 | 5 | 4 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 217 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Benton | 8 | 731 | 7 | 10 | 8 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 299 | 7 | 9 | 6 |
| Missouri non-MSA | Missouri | Sullivan | 6 | 536 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Monroe | 3 | 343 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Lewis | 2 | 416 | 6 | 7 | 7 |
| Springfield | Missouri | Dallas | 5 | 572 | 6 | 8 | 7 |
| Missouri non-MSA | Missouri | Iron | 0 | 219 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Ripley | 5 | 470 | 6 | 8 | 7 |
| Missouri non-MSA | Missouri | McDonald | 15 | 1365 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Maries | 3 | 342 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 421 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Wright | 13 | 733 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Carter | 4 | 276 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Scotland | 1 | 176 | 5 | 5 | 3 |
| Kansas City | Kansas | Linn | 1 | 258 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Atchison | 1 | 194 | 5 | 6 | 3 |
| Missouri non-MSA | Missouri | Barton | 4 | 601 | 5 | 7 | 6 |
| Missouri non-MSA | Missouri | Chariton | 0 | 221 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Montgomery | 5 | 304 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Linn | 10 | 292 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Dade | 5 | 277 | 4 | 6 | 4 |
| Missouri non-MSA | Missouri | Oregon | 0 | 352 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Douglas | 15 | 388 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Putnam | 1 | 125 | 4 | 4 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 244 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Daviess | 8 | 315 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Knox | 1 | 130 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 184 | 3 | 4 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 158 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Hickory | 4 | 350 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Mercer | 0 | 79 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Ozark | 2 | 277 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 66 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 326 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 121 | 1 | 2 | 2 |
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
