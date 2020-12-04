# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/04/2020  
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
| St. Louis-Farmington | 2466 | 154482 | 1851 | 2138 | 2152 |
| Kansas City | 1227 | 102205 | 1095 | 1241 | 1249 |
| Missouri non-MSA | 924 | 71983 | 669 | 817 | 933 |
| Springfield | 261 | 22331 | 212 | 228 | 238 |
| Columbia-Jefferson City | 125 | 24051 | 210 | 261 | 336 |
| Cape Girardeau-Sikeston | 119 | 9135 | 94 | 113 | 129 |
| St. Joseph | 90 | 6917 | 87 | 98 | 89 |
| Joplin | 157 | 11526 | 71 | 97 | 123 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1035 | 53688 | 588 | 678 | 696 |
| Kansas City | Kansas | Johnson | 294 | 28078 | 306 | 375 | 367 |
| St. Louis-Farmington | Missouri | St. Charles | 219 | 21069 | 258 | 294 | 302 |
| Kansas City | Missouri | Kansas City | 301 | 24115 | 242 | 269 | 279 |
| St. Louis-Farmington | Illinois | Madison | 270 | 15363 | 213 | 237 | 246 |
| Kansas City | Missouri | Jackson | 185 | 18081 | 211 | 223 | 239 |
| St. Louis-Farmington | Illinois | St. Clair | 269 | 14160 | 199 | 212 | 186 |
| St. Louis-Farmington | Missouri | Jefferson | 108 | 11667 | 153 | 180 | 180 |
| Springfield | Missouri | Greene | 190 | 14449 | 139 | 148 | 153 |
| St. Louis-Farmington | Missouri | St. Louis City | 246 | 13489 | 136 | 167 | 150 |
| Kansas City | Kansas | Wyandotte | 183 | 11781 | 86 | 110 | 94 |
| Columbia-Jefferson City | Missouri | Boone | 25 | 10692 | 84 | 105 | 139 |
| Joplin | Missouri | Jasper | 119 | 8499 | 59 | 75 | 95 |
| Columbia-Jefferson City | Missouri | Cole | 60 | 6420 | 58 | 77 | 94 |
| St. Joseph | Missouri | Buchanan | 63 | 4911 | 57 | 63 | 58 |
| Kansas City | Missouri | Clay | 76 | 4837 | 57 | 57 | 66 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 65 | 5253 | 55 | 66 | 77 |
| Kansas City | Missouri | Cass | 40 | 3989 | 52 | 55 | 56 |
| St. Louis-Farmington | Missouri | Franklin | 86 | 5040 | 52 | 63 | 67 |
| Springfield | Missouri | Christian | 24 | 3985 | 48 | 47 | 48 |
| St. Louis-Farmington | Missouri | St. Francois | 47 | 5248 | 44 | 60 | 69 |
| St. Louis-Farmington | Illinois | Macoupin | 23 | 2414 | 43 | 46 | 50 |
| Kansas City | Kansas | Leavenworth | 32 | 3895 | 40 | 42 | 37 |
| St. Louis-Farmington | Illinois | Clinton | 63 | 3491 | 36 | 50 | 50 |
| St. Louis-Farmington | Missouri | Lincoln | 13 | 2587 | 32 | 41 | 41 |
| Columbia-Jefferson City | Missouri | Callaway | 11 | 2960 | 31 | 36 | 46 |
| Missouri non-MSA | Missouri | Taney | 39 | 2970 | 30 | 35 | 34 |
| Missouri non-MSA | Missouri | Phelps | 50 | 1884 | 30 | 35 | 31 |
| Cape Girardeau-Sikeston | Missouri | Scott | 42 | 2780 | 30 | 37 | 39 |
| St. Louis-Farmington | Illinois | Monroe | 48 | 2191 | 27 | 36 | 36 |
| St. Louis-Farmington | Illinois | Jersey | 24 | 1384 | 25 | 26 | 28 |
| Kansas City | Missouri | Platte | 17 | 1771 | 24 | 24 | 22 |
| Missouri non-MSA | Missouri | Johnson | 16 | 2617 | 23 | 27 | 33 |
| Missouri non-MSA | Missouri | Pulaski | 23 | 1710 | 21 | 23 | 20 |
| Missouri non-MSA | Missouri | Laclede | 32 | 1903 | 21 | 20 | 20 |
| Missouri non-MSA | Missouri | Butler | 9 | 2247 | 21 | 29 | 27 |
| Missouri non-MSA | Missouri | Camden | 49 | 2547 | 20 | 22 | 27 |
| Missouri non-MSA | Missouri | Nodaway | 13 | 2076 | 19 | 19 | 25 |
| St. Louis-Farmington | Illinois | Bond | 11 | 1143 | 19 | 19 | 19 |
| Missouri non-MSA | Missouri | Marion | 18 | 1846 | 18 | 22 | 26 |
| Kansas City | Missouri | Lafayette | 30 | 1601 | 17 | 20 | 21 |
| Missouri non-MSA | Missouri | Washington | 22 | 1517 | 17 | 21 | 25 |
| Kansas City | Kansas | Miami | 3 | 1091 | 17 | 19 | 15 |
| Missouri non-MSA | Missouri | Lawrence | 39 | 1978 | 17 | 19 | 24 |
| Missouri non-MSA | Missouri | Miller | 26 | 1576 | 15 | 15 | 19 |
| Missouri non-MSA | Missouri | Stoddard | 23 | 1695 | 15 | 21 | 24 |
| Missouri non-MSA | Missouri | Audrain | 15 | 1144 | 15 | 17 | 15 |
| Missouri non-MSA | Missouri | Pike | 9 | 976 | 15 | 17 | 18 |
| St. Louis-Farmington | Missouri | Warren | 3 | 1270 | 14 | 18 | 19 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1126 | 13 | 16 | 20 |
| Missouri non-MSA | Missouri | Stone | 19 | 1239 | 12 | 14 | 15 |
| Missouri non-MSA | Missouri | Perry | 12 | 1596 | 12 | 17 | 23 |
| Missouri non-MSA | Missouri | Randolph | 9 | 1256 | 12 | 14 | 18 |
| Missouri non-MSA | Missouri | Crawford | 14 | 1239 | 12 | 15 | 17 |
| Missouri non-MSA | Missouri | Henry | 12 | 1138 | 11 | 15 | 22 |
| Joplin | Missouri | Newton | 38 | 3027 | 11 | 21 | 27 |
| Kansas City | Missouri | Clinton | 47 | 933 | 11 | 10 | 11 |
| Missouri non-MSA | Missouri | Mississippi | 7 | 915 | 11 | 17 | 14 |
| Missouri non-MSA | Missouri | Barry | 29 | 1500 | 11 | 14 | 18 |
| St. Joseph | Kansas | Doniphan | 2 | 534 | 11 | 12 | 9 |
| Kansas City | Missouri | Ray | 6 | 737 | 11 | 10 | 13 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1274 | 11 | 12 | 18 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1738 | 10 | 13 | 17 |
| Springfield | Missouri | Webster | 25 | 1855 | 10 | 17 | 19 |
| St. Joseph | Missouri | Andrew | 10 | 851 | 10 | 13 | 12 |
| Missouri non-MSA | Missouri | Adair | 3 | 1122 | 10 | 12 | 17 |
| Missouri non-MSA | Missouri | Madison | 9 | 925 | 10 | 14 | 12 |
| Missouri non-MSA | Missouri | New Madrid | 24 | 1388 | 10 | 14 | 17 |
| Springfield | Missouri | Polk | 12 | 1429 | 10 | 10 | 10 |
| Columbia-Jefferson City | Missouri | Cooper | 8 | 1208 | 10 | 11 | 17 |
| Missouri non-MSA | Missouri | Saline | 12 | 1618 | 9 | 14 | 18 |
| Missouri non-MSA | Missouri | Pemiscot | 19 | 1125 | 9 | 10 | 11 |
| Missouri non-MSA | Missouri | Morgan | 13 | 1104 | 8 | 10 | 11 |
| Missouri non-MSA | Missouri | Ripley | 8 | 558 | 8 | 8 | 8 |
| Columbia-Jefferson City | Missouri | Osage | 4 | 973 | 8 | 10 | 13 |
| Missouri non-MSA | Missouri | Vernon | 9 | 706 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | Pettis | 36 | 2705 | 8 | 13 | 28 |
| Missouri non-MSA | Missouri | Ralls | 2 | 506 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | Gasconade | 25 | 502 | 7 | 7 | 6 |
| St. Joseph | Missouri | DeKalb | 15 | 621 | 7 | 9 | 8 |
| Missouri non-MSA | Missouri | Texas | 9 | 993 | 7 | 8 | 11 |
| Kansas City | Kansas | Linn | 1 | 324 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Howell | 31 | 1616 | 7 | 8 | 10 |
| Missouri non-MSA | Missouri | Macon | 3 | 701 | 7 | 13 | 14 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 278 | 6 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 524 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Dent | 4 | 539 | 6 | 9 | 8 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 8 | 834 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Livingston | 16 | 804 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Gentry | 13 | 440 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 358 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Wright | 15 | 794 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Benton | 9 | 791 | 5 | 5 | 9 |
| Missouri non-MSA | Missouri | Carroll | 6 | 450 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Douglas | 15 | 452 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Grundy | 14 | 533 | 5 | 6 | 8 |
| Kansas City | Missouri | Caldwell | 3 | 409 | 5 | 6 | 7 |
| Kansas City | Missouri | Bates | 9 | 563 | 5 | 8 | 9 |
| Missouri non-MSA | Missouri | Monroe | 3 | 407 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | McDonald | 16 | 1426 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Wayne | 3 | 512 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Oregon | 1 | 394 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Harrison | 3 | 415 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Shelby | 1 | 224 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 8 | 353 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 358 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Maries | 4 | 379 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Linn | 11 | 334 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Putnam | 1 | 168 | 3 | 4 | 3 |
| Springfield | Missouri | Dallas | 10 | 613 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Chariton | 0 | 254 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Barton | 5 | 644 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Iron | 1 | 247 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Holt | 4 | 277 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Ozark | 3 | 303 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 6 | 379 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 6 | 573 | 2 | 4 | 6 |
| Missouri non-MSA | Missouri | Atchison | 3 | 220 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Carter | 6 | 303 | 2 | 3 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 4 | 268 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Clark | 4 | 309 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Scotland | 1 | 194 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Cedar | 7 | 450 | 1 | 3 | 6 |
| Missouri non-MSA | Missouri | Dade | 8 | 296 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 185 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 138 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Lewis | 2 | 436 | 1 | 3 | 6 |
| Missouri non-MSA | Missouri | Worth | 0 | 76 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 9 | 341 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 89 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 136 | 0 | 1 | 2 |
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
