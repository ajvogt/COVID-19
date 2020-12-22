# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/22/2020  
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
| St. Louis-Farmington | 3069 | 187981 | 1719 | 1798 | 1945 |
| Kansas City | 1420 | 125422 | 1139 | 1209 | 1244 |
| Missouri non-MSA | 1185 | 86554 | 700 | 764 | 788 |
| Springfield | 338 | 27216 | 260 | 263 | 251 |
| Columbia-Jefferson City | 172 | 27909 | 204 | 199 | 228 |
| Joplin | 185 | 12747 | 67 | 70 | 75 |
| Cape Girardeau-Sikeston | 160 | 10546 | 65 | 69 | 88 |
| St. Joseph | 121 | 8185 | 51 | 62 | 81 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1290 | 64879 | 577 | 598 | 641 |
| Kansas City | Kansas | Johnson | 390 | 35973 | 404 | 412 | 402 |
| St. Louis-Farmington | Missouri | St. Charles | 261 | 25469 | 236 | 238 | 258 |
| Kansas City | Missouri | Kansas City | 328 | 28263 | 204 | 209 | 240 |
| St. Louis-Farmington | Illinois | Madison | 360 | 19386 | 202 | 217 | 224 |
| Kansas City | Missouri | Jackson | 207 | 21757 | 167 | 187 | 209 |
| Springfield | Missouri | Greene | 238 | 17506 | 162 | 166 | 160 |
| St. Louis-Farmington | Illinois | St. Clair | 325 | 17609 | 157 | 176 | 197 |
| St. Louis-Farmington | Missouri | St. Louis City | 283 | 15985 | 130 | 135 | 147 |
| St. Louis-Farmington | Missouri | Jefferson | 121 | 14068 | 123 | 127 | 150 |
| Kansas City | Kansas | Wyandotte | 190 | 14297 | 104 | 135 | 125 |
| Columbia-Jefferson City | Missouri | Boone | 36 | 12562 | 103 | 101 | 101 |
| Springfield | Missouri | Christian | 35 | 5072 | 60 | 60 | 54 |
| Kansas City | Missouri | Cass | 46 | 5097 | 58 | 60 | 58 |
| St. Louis-Farmington | Missouri | Franklin | 106 | 6095 | 57 | 57 | 58 |
| Joplin | Missouri | Jasper | 145 | 9466 | 50 | 55 | 58 |
| Kansas City | Kansas | Leavenworth | 37 | 4761 | 46 | 44 | 45 |
| St. Louis-Farmington | Missouri | St. Francois | 58 | 6106 | 45 | 49 | 50 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 91 | 6109 | 44 | 43 | 52 |
| Kansas City | Missouri | Clay | 87 | 5794 | 43 | 51 | 52 |
| Missouri non-MSA | Missouri | Pettis | 50 | 3804 | 38 | 58 | 41 |
| Columbia-Jefferson City | Missouri | Cole | 77 | 7259 | 38 | 39 | 57 |
| St. Louis-Farmington | Missouri | Lincoln | 17 | 3298 | 37 | 38 | 39 |
| St. Louis-Farmington | Illinois | Clinton | 77 | 4175 | 35 | 37 | 42 |
| St. Louis-Farmington | Illinois | Monroe | 56 | 2821 | 34 | 33 | 35 |
| St. Louis-Farmington | Illinois | Macoupin | 57 | 3019 | 32 | 33 | 38 |
| St. Joseph | Missouri | Buchanan | 86 | 5763 | 30 | 41 | 53 |
| Columbia-Jefferson City | Missouri | Callaway | 18 | 3516 | 29 | 27 | 33 |
| Kansas City | Missouri | Platte | 19 | 2163 | 24 | 20 | 22 |
| Kansas City | Kansas | Miami | 7 | 1566 | 23 | 24 | 23 |
| Missouri non-MSA | Missouri | Johnson | 25 | 3055 | 22 | 23 | 25 |
| Springfield | Missouri | Webster | 35 | 2252 | 21 | 20 | 19 |
| Missouri non-MSA | Missouri | Taney | 47 | 3571 | 21 | 27 | 33 |
| Missouri non-MSA | Missouri | Miller | 42 | 1916 | 20 | 18 | 17 |
| Missouri non-MSA | Missouri | Phelps | 76 | 2278 | 20 | 20 | 25 |
| Missouri non-MSA | Missouri | Adair | 4 | 1435 | 19 | 18 | 14 |
| Missouri non-MSA | Missouri | Audrain | 23 | 1502 | 19 | 19 | 18 |
| Missouri non-MSA | Missouri | Laclede | 39 | 2359 | 19 | 22 | 23 |
| Missouri non-MSA | Missouri | Camden | 58 | 2937 | 19 | 21 | 21 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1989 | 18 | 14 | 13 |
| St. Louis-Farmington | Illinois | Jersey | 34 | 1784 | 18 | 20 | 23 |
| Kansas City | Missouri | Lafayette | 36 | 1904 | 17 | 16 | 18 |
| Missouri non-MSA | Missouri | Pulaski | 26 | 2280 | 17 | 21 | 27 |
| Missouri non-MSA | Missouri | Crawford | 15 | 1532 | 17 | 15 | 15 |
| Joplin | Missouri | Newton | 40 | 3281 | 17 | 14 | 16 |
| St. Louis-Farmington | Missouri | Warren | 8 | 1512 | 16 | 14 | 15 |
| Cape Girardeau-Sikeston | Missouri | Scott | 53 | 3184 | 16 | 17 | 26 |
| Missouri non-MSA | Missouri | Butler | 12 | 2672 | 15 | 20 | 24 |
| Missouri non-MSA | Missouri | Saline | 16 | 1888 | 15 | 14 | 14 |
| Kansas City | Missouri | Ray | 7 | 994 | 15 | 14 | 12 |
| Missouri non-MSA | Missouri | Texas | 13 | 1253 | 15 | 14 | 12 |
| Missouri non-MSA | Missouri | Stone | 23 | 1517 | 14 | 14 | 14 |
| Columbia-Jefferson City | Missouri | Cooper | 17 | 1427 | 14 | 12 | 11 |
| Missouri non-MSA | Missouri | Henry | 19 | 1360 | 13 | 11 | 13 |
| Missouri non-MSA | Missouri | Marion | 23 | 2207 | 12 | 16 | 20 |
| Missouri non-MSA | Missouri | Howell | 35 | 2162 | 12 | 35 | 21 |
| Missouri non-MSA | Missouri | Perry | 15 | 1783 | 12 | 10 | 12 |
| Missouri non-MSA | Missouri | Barry | 35 | 1717 | 12 | 12 | 12 |
| Missouri non-MSA | Missouri | Morgan | 16 | 1382 | 12 | 14 | 13 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2199 | 12 | 11 | 14 |
| Missouri non-MSA | Missouri | Vernon | 13 | 903 | 12 | 10 | 10 |
| Springfield | Missouri | Polk | 16 | 1714 | 12 | 13 | 13 |
| Missouri non-MSA | Missouri | Benton | 15 | 1137 | 12 | 17 | 13 |
| St. Louis-Farmington | Illinois | Bond | 15 | 1420 | 11 | 15 | 17 |
| Missouri non-MSA | Missouri | Livingston | 19 | 959 | 11 | 8 | 7 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2261 | 11 | 10 | 14 |
| Missouri non-MSA | Missouri | Stoddard | 31 | 1962 | 11 | 12 | 16 |
| Missouri non-MSA | Missouri | Macon | 5 | 855 | 11 | 8 | 9 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1336 | 11 | 11 | 13 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1583 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Randolph | 15 | 1510 | 10 | 11 | 13 |
| Missouri non-MSA | Missouri | Pike | 11 | 1190 | 10 | 11 | 13 |
| Kansas City | Missouri | Clinton | 50 | 1164 | 10 | 12 | 11 |
| Missouri non-MSA | Missouri | Wright | 19 | 968 | 9 | 9 | 8 |
| Missouri non-MSA | Missouri | Washington | 34 | 1682 | 9 | 9 | 12 |
| Missouri non-MSA | Missouri | Madison | 10 | 1101 | 9 | 9 | 10 |
| Kansas City | Missouri | Bates | 10 | 734 | 9 | 8 | 9 |
| St. Joseph | Kansas | Doniphan | 5 | 673 | 9 | 6 | 9 |
| St. Joseph | Missouri | Andrew | 13 | 1027 | 8 | 9 | 10 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1119 | 8 | 7 | 9 |
| Columbia-Jefferson City | Missouri | Moniteau | 16 | 1431 | 8 | 7 | 10 |
| Missouri non-MSA | Missouri | New Madrid | 26 | 1533 | 7 | 8 | 10 |
| Missouri non-MSA | Missouri | Mississippi | 10 | 1097 | 7 | 8 | 13 |
| Missouri non-MSA | Missouri | Douglas | 19 | 570 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Carroll | 9 | 609 | 7 | 8 | 8 |
| Missouri non-MSA | Missouri | Harrison | 7 | 579 | 6 | 8 | 7 |
| Missouri non-MSA | Missouri | Gentry | 15 | 568 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 29 | 626 | 6 | 6 | 7 |
| Kansas City | Kansas | Linn | 3 | 450 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 20 | 1240 | 6 | 6 | 7 |
| Kansas City | Missouri | Caldwell | 3 | 505 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Wayne | 4 | 623 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Iron | 1 | 337 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 455 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Ralls | 4 | 604 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 632 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Dent | 6 | 651 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Barton | 7 | 729 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Grundy | 19 | 629 | 4 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 595 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 181 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 9 | 433 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 4 | 423 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Monroe | 5 | 475 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Ripley | 8 | 632 | 3 | 4 | 5 |
| St. Joseph | Missouri | DeKalb | 17 | 722 | 3 | 5 | 7 |
| Missouri non-MSA | Missouri | Dade | 8 | 347 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Chariton | 2 | 303 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Maries | 6 | 436 | 3 | 2 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 11 | 930 | 3 | 4 | 5 |
| Springfield | Missouri | Dallas | 14 | 672 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Lewis | 2 | 503 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Oregon | 3 | 499 | 2 | 6 | 5 |
| Missouri non-MSA | Missouri | Shannon | 9 | 399 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 279 | 2 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 5 | 323 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Cedar | 8 | 486 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 11 | 394 | 2 | 3 | 3 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 355 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Scotland | 3 | 222 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 190 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 119 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 6 | 356 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 216 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ozark | 4 | 352 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Holt | 7 | 318 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 6 | 410 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 4 | 344 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Atchison | 4 | 255 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 1 | 146 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 109 | 0 | 1 | 1 |
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
