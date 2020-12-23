# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/23/2020  
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
| St. Louis-Farmington | 3119 | 189390 | 1645 | 1769 | 1917 |
| Kansas City | 1465 | 125858 | 1120 | 1196 | 1231 |
| Missouri non-MSA | 1263 | 87064 | 691 | 747 | 777 |
| Springfield | 365 | 27394 | 257 | 255 | 249 |
| Columbia-Jefferson City | 185 | 27968 | 200 | 196 | 219 |
| Joplin | 194 | 12774 | 67 | 63 | 71 |
| Cape Girardeau-Sikeston | 166 | 10599 | 65 | 67 | 85 |
| St. Joseph | 125 | 8230 | 52 | 57 | 78 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1312 | 65266 | 538 | 583 | 630 |
| Kansas City | Kansas | Johnson | 401 | 35973 | 404 | 412 | 402 |
| St. Louis-Farmington | Missouri | St. Charles | 263 | 25650 | 227 | 233 | 252 |
| St. Louis-Farmington | Illinois | Madison | 362 | 19568 | 200 | 216 | 223 |
| Kansas City | Missouri | Kansas City | 338 | 28400 | 190 | 204 | 232 |
| Springfield | Missouri | Greene | 248 | 17620 | 159 | 160 | 159 |
| Kansas City | Missouri | Jackson | 218 | 21876 | 156 | 181 | 206 |
| St. Louis-Farmington | Illinois | St. Clair | 326 | 17761 | 150 | 173 | 194 |
| St. Louis-Farmington | Missouri | St. Louis City | 286 | 16101 | 128 | 131 | 145 |
| St. Louis-Farmington | Missouri | Jefferson | 125 | 14164 | 115 | 125 | 147 |
| Kansas City | Kansas | Wyandotte | 190 | 14297 | 104 | 135 | 125 |
| Columbia-Jefferson City | Missouri | Boone | 39 | 12586 | 101 | 99 | 97 |
| Springfield | Missouri | Christian | 41 | 5105 | 60 | 57 | 53 |
| St. Louis-Farmington | Missouri | Franklin | 109 | 6134 | 57 | 56 | 58 |
| Kansas City | Missouri | Cass | 50 | 5138 | 57 | 58 | 58 |
| Joplin | Missouri | Jasper | 151 | 9478 | 48 | 49 | 55 |
| Kansas City | Kansas | Leavenworth | 37 | 4761 | 46 | 44 | 45 |
| St. Louis-Farmington | Missouri | St. Francois | 64 | 6154 | 46 | 50 | 49 |
| Kansas City | Missouri | Clay | 91 | 5837 | 45 | 51 | 50 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 94 | 6142 | 43 | 43 | 51 |
| Columbia-Jefferson City | Missouri | Cole | 81 | 7278 | 38 | 39 | 55 |
| Missouri non-MSA | Missouri | Pettis | 57 | 3824 | 37 | 54 | 41 |
| St. Louis-Farmington | Missouri | Lincoln | 18 | 3321 | 34 | 38 | 38 |
| St. Louis-Farmington | Illinois | Clinton | 79 | 4209 | 32 | 37 | 42 |
| St. Louis-Farmington | Illinois | Monroe | 56 | 2852 | 32 | 33 | 35 |
| St. Joseph | Missouri | Buchanan | 89 | 5798 | 30 | 37 | 51 |
| St. Louis-Farmington | Illinois | Macoupin | 59 | 3053 | 30 | 32 | 38 |
| Columbia-Jefferson City | Missouri | Callaway | 19 | 3525 | 27 | 26 | 32 |
| Missouri non-MSA | Missouri | Pulaski | 27 | 2352 | 26 | 25 | 29 |
| Kansas City | Missouri | Platte | 20 | 2183 | 24 | 20 | 22 |
| Kansas City | Kansas | Miami | 7 | 1566 | 23 | 24 | 23 |
| Missouri non-MSA | Missouri | Adair | 4 | 1463 | 22 | 19 | 15 |
| Springfield | Missouri | Webster | 38 | 2272 | 22 | 20 | 18 |
| Missouri non-MSA | Missouri | Taney | 49 | 3591 | 21 | 26 | 32 |
| St. Louis-Farmington | Illinois | Jersey | 35 | 1823 | 21 | 21 | 23 |
| Missouri non-MSA | Missouri | Phelps | 79 | 2286 | 20 | 18 | 24 |
| Missouri non-MSA | Missouri | Audrain | 28 | 1518 | 20 | 19 | 18 |
| Missouri non-MSA | Missouri | Miller | 42 | 1925 | 20 | 17 | 17 |
| Kansas City | Missouri | Lafayette | 36 | 1940 | 20 | 17 | 19 |
| Missouri non-MSA | Missouri | Camden | 60 | 2954 | 20 | 20 | 21 |
| Missouri non-MSA | Missouri | Johnson | 27 | 3065 | 19 | 22 | 24 |
| Missouri non-MSA | Missouri | Laclede | 41 | 2374 | 19 | 22 | 23 |
| Joplin | Missouri | Newton | 43 | 3296 | 18 | 14 | 15 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1998 | 18 | 14 | 13 |
| Cape Girardeau-Sikeston | Missouri | Scott | 56 | 3200 | 16 | 17 | 26 |
| Missouri non-MSA | Missouri | Crawford | 18 | 1541 | 16 | 16 | 14 |
| Kansas City | Missouri | Ray | 7 | 1010 | 16 | 14 | 12 |
| Missouri non-MSA | Missouri | Saline | 21 | 1899 | 15 | 15 | 14 |
| Missouri non-MSA | Missouri | Stone | 23 | 1524 | 15 | 14 | 14 |
| St. Louis-Farmington | Illinois | Bond | 15 | 1459 | 15 | 16 | 18 |
| Missouri non-MSA | Missouri | Texas | 13 | 1257 | 15 | 14 | 11 |
| Missouri non-MSA | Missouri | Butler | 13 | 2683 | 13 | 19 | 24 |
| Missouri non-MSA | Missouri | Lawrence | 45 | 2215 | 13 | 12 | 14 |
| Missouri non-MSA | Missouri | Marion | 24 | 2223 | 13 | 16 | 20 |
| Missouri non-MSA | Missouri | Henry | 21 | 1365 | 13 | 11 | 12 |
| Missouri non-MSA | Missouri | Howell | 36 | 2172 | 13 | 35 | 21 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1428 | 13 | 12 | 11 |
| Springfield | Missouri | Polk | 21 | 1725 | 12 | 12 | 13 |
| Missouri non-MSA | Missouri | Barry | 35 | 1726 | 12 | 11 | 11 |
| Missouri non-MSA | Missouri | Morgan | 21 | 1388 | 11 | 13 | 13 |
| Missouri non-MSA | Missouri | Benton | 16 | 1138 | 11 | 16 | 13 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1519 | 11 | 13 | 14 |
| Missouri non-MSA | Missouri | Macon | 7 | 860 | 11 | 8 | 8 |
| Missouri non-MSA | Missouri | Vernon | 14 | 904 | 11 | 9 | 9 |
| Kansas City | Missouri | Clinton | 53 | 1173 | 11 | 11 | 11 |
| Missouri non-MSA | Missouri | Perry | 15 | 1790 | 10 | 10 | 11 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2261 | 10 | 10 | 13 |
| Missouri non-MSA | Missouri | Pike | 14 | 1199 | 10 | 11 | 13 |
| Missouri non-MSA | Missouri | Randolph | 15 | 1515 | 10 | 11 | 13 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 3 | 1339 | 10 | 11 | 13 |
| Missouri non-MSA | Missouri | Livingston | 20 | 963 | 10 | 8 | 7 |
| Missouri non-MSA | Missouri | Wright | 23 | 972 | 9 | 9 | 8 |
| St. Joseph | Kansas | Doniphan | 5 | 673 | 9 | 6 | 9 |
| Missouri non-MSA | Missouri | Washington | 35 | 1691 | 9 | 9 | 12 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1589 | 9 | 8 | 7 |
| Kansas City | Missouri | Bates | 10 | 744 | 9 | 8 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 31 | 1968 | 9 | 11 | 16 |
| Missouri non-MSA | Missouri | Madison | 10 | 1110 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | New Madrid | 27 | 1544 | 8 | 8 | 9 |
| St. Joseph | Missouri | Andrew | 13 | 1032 | 8 | 8 | 10 |
| Columbia-Jefferson City | Missouri | Moniteau | 16 | 1433 | 7 | 7 | 9 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1122 | 7 | 6 | 8 |
| Missouri non-MSA | Missouri | Iron | 1 | 354 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Carroll | 9 | 612 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Douglas | 19 | 576 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Harrison | 7 | 583 | 6 | 7 | 7 |
| Kansas City | Missouri | Caldwell | 4 | 510 | 6 | 4 | 5 |
| Kansas City | Kansas | Linn | 3 | 450 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Gentry | 15 | 569 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Mississippi | 11 | 1097 | 6 | 8 | 13 |
| Missouri non-MSA | Missouri | Gasconade | 29 | 628 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 20 | 1240 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 637 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Grundy | 20 | 633 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Montgomery | 8 | 457 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Ralls | 5 | 612 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Dent | 6 | 653 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Wayne | 6 | 627 | 4 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 596 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Daviess | 9 | 440 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 184 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Barton | 9 | 732 | 4 | 4 | 4 |
| St. Joseph | Missouri | DeKalb | 18 | 727 | 3 | 5 | 7 |
| Missouri non-MSA | Missouri | Lewis | 3 | 509 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Monroe | 5 | 477 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 4 | 423 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Dade | 8 | 350 | 3 | 3 | 2 |
| Springfield | Missouri | Dallas | 17 | 672 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Ripley | 8 | 635 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Chariton | 2 | 303 | 3 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 11 | 934 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Maries | 6 | 438 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Oregon | 3 | 501 | 2 | 6 | 5 |
| Missouri non-MSA | Missouri | Shannon | 9 | 399 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 11 | 395 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Shelby | 2 | 280 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Putnam | 1 | 191 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Cedar | 8 | 486 | 2 | 1 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 5 | 323 | 1 | 3 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 356 | 1 | 3 | 4 |
| Missouri non-MSA | Missouri | Carter | 6 | 359 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 218 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 120 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 222 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 9 | 412 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 4 | 344 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Holt | 9 | 318 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ozark | 4 | 352 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Knox | 1 | 147 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 5 | 255 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Worth | 1 | 110 | 0 | 1 | 1 |
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
