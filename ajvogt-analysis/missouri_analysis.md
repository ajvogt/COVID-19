# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/23/2020  
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
| St. Louis-Farmington | 2181 | 131853 | 2410 | 2329 | 1766 |
| Kansas City | 1099 | 88925 | 1479 | 1340 | 1080 |
| Missouri non-MSA | 764 | 63731 | 1047 | 1066 | 891 |
| Columbia-Jefferson City | 88 | 21380 | 343 | 372 | 327 |
| Springfield | 230 | 19915 | 271 | 259 | 224 |
| Cape Girardeau-Sikeston | 104 | 8021 | 158 | 154 | 117 |
| Joplin | 141 | 10638 | 150 | 151 | 121 |
| St. Joseph | 73 | 5878 | 97 | 91 | 70 |
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
| St. Louis-Farmington | Missouri | St. Louis | 944 | 46357 | 767 | 766 | 573 |
| Kansas City | Kansas | Johnson | 271 | 23891 | 420 | 364 | 324 |
| St. Louis-Farmington | Missouri | St. Charles | 186 | 18073 | 363 | 333 | 264 |
| Kansas City | Missouri | Kansas City | 255 | 21420 | 333 | 321 | 247 |
| Kansas City | Missouri | Jackson | 171 | 15695 | 278 | 265 | 201 |
| St. Louis-Farmington | Illinois | Madison | 217 | 12865 | 268 | 265 | 194 |
| St. Louis-Farmington | Missouri | Jefferson | 96 | 9734 | 214 | 194 | 147 |
| St. Louis-Farmington | Illinois | St. Clair | 253 | 11915 | 210 | 189 | 136 |
| Springfield | Missouri | Greene | 169 | 12848 | 170 | 164 | 139 |
| St. Louis-Farmington | Missouri | St. Louis City | 230 | 11743 | 147 | 152 | 119 |
| Columbia-Jefferson City | Missouri | Boone | 17 | 9651 | 143 | 157 | 127 |
| Kansas City | Kansas | Wyandotte | 177 | 10535 | 120 | 89 | 77 |
| Joplin | Missouri | Jasper | 104 | 7800 | 115 | 117 | 92 |
| Columbia-Jefferson City | Missouri | Cole | 38 | 5620 | 99 | 103 | 95 |
| Kansas City | Missouri | Clay | 61 | 4314 | 94 | 84 | 62 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 59 | 4598 | 91 | 91 | 67 |
| St. Louis-Farmington | Missouri | St. Francois | 36 | 4677 | 84 | 83 | 65 |
| St. Louis-Farmington | Missouri | Franklin | 59 | 4379 | 77 | 73 | 63 |
| Kansas City | Missouri | Cass | 36 | 3391 | 68 | 65 | 47 |
| St. Joseph | Missouri | Buchanan | 53 | 4249 | 63 | 60 | 46 |
| St. Louis-Farmington | Illinois | Macoupin | 17 | 1895 | 58 | 56 | 37 |
| St. Louis-Farmington | Illinois | Clinton | 56 | 2943 | 57 | 55 | 41 |
| Springfield | Missouri | Christian | 22 | 3489 | 53 | 51 | 43 |
| Cape Girardeau-Sikeston | Missouri | Scott | 36 | 2419 | 53 | 47 | 35 |
| St. Louis-Farmington | Missouri | Lincoln | 8 | 2160 | 49 | 45 | 35 |
| Kansas City | Kansas | Leavenworth | 27 | 3408 | 44 | 35 | 27 |
| Missouri non-MSA | Missouri | Taney | 37 | 2618 | 44 | 38 | 32 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 2564 | 44 | 46 | 48 |
| Missouri non-MSA | Missouri | Phelps | 38 | 1548 | 37 | 34 | 25 |
| Missouri non-MSA | Missouri | Stoddard | 19 | 1475 | 35 | 30 | 21 |
| Joplin | Missouri | Newton | 37 | 2838 | 35 | 34 | 28 |
| Missouri non-MSA | Missouri | Johnson | 12 | 2320 | 35 | 34 | 29 |
| St. Louis-Farmington | Illinois | Monroe | 44 | 1797 | 34 | 38 | 29 |
| Missouri non-MSA | Missouri | Butler | 8 | 1956 | 33 | 30 | 28 |
| Missouri non-MSA | Missouri | Camden | 44 | 2301 | 32 | 33 | 26 |
| Missouri non-MSA | Missouri | Marion | 15 | 1608 | 31 | 30 | 24 |
| St. Louis-Farmington | Illinois | Jersey | 23 | 1105 | 29 | 25 | 21 |
| Missouri non-MSA | Missouri | Lawrence | 33 | 1787 | 28 | 29 | 25 |
| Springfield | Missouri | Webster | 23 | 1704 | 28 | 24 | 20 |
| Kansas City | Missouri | Platte | 14 | 1520 | 27 | 24 | 18 |
| Missouri non-MSA | Missouri | Henry | 9 | 981 | 27 | 28 | 20 |
| Missouri non-MSA | Missouri | Washington | 22 | 1323 | 26 | 29 | 23 |
| St. Louis-Farmington | Missouri | Warren | 2 | 1082 | 25 | 23 | 16 |
| Missouri non-MSA | Missouri | Perry | 8 | 1436 | 25 | 28 | 21 |
| Missouri non-MSA | Missouri | Pulaski | 15 | 1473 | 25 | 20 | 18 |
| Missouri non-MSA | Missouri | Barry | 22 | 1367 | 25 | 22 | 20 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1844 | 25 | 28 | 25 |
| Missouri non-MSA | Missouri | Pike | 8 | 809 | 22 | 22 | 16 |
| Missouri non-MSA | Missouri | Macon | 2 | 592 | 21 | 18 | 13 |
| Kansas City | Missouri | Lafayette | 29 | 1369 | 21 | 21 | 19 |
| Missouri non-MSA | Missouri | Miller | 23 | 1403 | 20 | 20 | 19 |
| Missouri non-MSA | Missouri | Saline | 12 | 1479 | 20 | 23 | 18 |
| Missouri non-MSA | Missouri | Stone | 15 | 1104 | 20 | 17 | 14 |
| Missouri non-MSA | Missouri | Laclede | 29 | 1670 | 20 | 19 | 18 |
| Missouri non-MSA | Missouri | Adair | 1 | 1007 | 20 | 23 | 17 |
| Missouri non-MSA | Missouri | Crawford | 11 | 1097 | 19 | 19 | 16 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 1245 | 19 | 21 | 16 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 706 | 18 | 13 | 9 |
| Missouri non-MSA | Missouri | Randolph | 5 | 1113 | 17 | 21 | 17 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1586 | 17 | 18 | 17 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1137 | 17 | 22 | 18 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 947 | 17 | 21 | 20 |
| Missouri non-MSA | Missouri | Pettis | 29 | 2571 | 17 | 29 | 34 |
| Kansas City | Kansas | Miami | 2 | 866 | 17 | 13 | 11 |
| St. Joseph | Missouri | Andrew | 9 | 727 | 15 | 14 | 10 |
| Columbia-Jefferson City | Missouri | Cooper | 6 | 1096 | 15 | 18 | 16 |
| St. Louis-Farmington | Illinois | Bond | 10 | 913 | 15 | 18 | 14 |
| Missouri non-MSA | Missouri | Audrain | 11 | 954 | 15 | 15 | 13 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 867 | 14 | 14 | 13 |
| Missouri non-MSA | Missouri | Madison | 7 | 792 | 14 | 14 | 10 |
| Kansas City | Missouri | Bates | 8 | 474 | 13 | 12 | 8 |
| Kansas City | Missouri | Clinton | 42 | 824 | 12 | 14 | 12 |
| Missouri non-MSA | Missouri | Morgan | 9 | 995 | 12 | 11 | 12 |
| Missouri non-MSA | Missouri | Vernon | 5 | 620 | 11 | 11 | 10 |
| Missouri non-MSA | Missouri | Dent | 4 | 458 | 11 | 10 | 7 |
| Kansas City | Missouri | Ray | 4 | 622 | 11 | 14 | 12 |
| Missouri non-MSA | Missouri | Texas | 7 | 908 | 11 | 12 | 11 |
| Missouri non-MSA | Missouri | Grundy | 13 | 480 | 10 | 11 | 7 |
| Missouri non-MSA | Missouri | Howell | 26 | 1513 | 10 | 11 | 14 |
| Springfield | Missouri | Polk | 11 | 1306 | 10 | 11 | 13 |
| Missouri non-MSA | Missouri | Pemiscot | 16 | 1018 | 10 | 13 | 10 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 7 | 762 | 10 | 11 | 10 |
| Missouri non-MSA | Missouri | Ralls | 1 | 407 | 10 | 10 | 6 |
| St. Joseph | Kansas | Doniphan | 2 | 391 | 9 | 8 | 6 |
| Missouri non-MSA | Missouri | Livingston | 11 | 740 | 9 | 8 | 6 |
| Missouri non-MSA | Missouri | Gentry | 11 | 385 | 8 | 9 | 6 |
| Kansas City | Missouri | Caldwell | 1 | 348 | 8 | 8 | 6 |
| Missouri non-MSA | Missouri | Cedar | 4 | 421 | 8 | 9 | 6 |
| Missouri non-MSA | Missouri | Carroll | 5 | 376 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 297 | 8 | 9 | 6 |
| Missouri non-MSA | Missouri | Harrison | 1 | 363 | 8 | 9 | 6 |
| St. Joseph | Missouri | DeKalb | 9 | 511 | 8 | 7 | 8 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 215 | 8 | 6 | 4 |
| Springfield | Missouri | Dallas | 5 | 568 | 8 | 8 | 7 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 445 | 8 | 8 | 6 |
| Missouri non-MSA | Missouri | Lewis | 2 | 415 | 8 | 8 | 7 |
| Missouri non-MSA | Missouri | Benton | 8 | 728 | 7 | 10 | 8 |
| Missouri non-MSA | Missouri | Sullivan | 6 | 536 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Holt | 3 | 240 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Iron | 0 | 218 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Monroe | 3 | 342 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Wayne | 3 | 452 | 6 | 6 | 5 |
| Kansas City | Kansas | Linn | 1 | 248 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Clark | 2 | 270 | 6 | 7 | 5 |
| Missouri non-MSA | Missouri | Barton | 4 | 601 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Carter | 4 | 276 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Atchison | 1 | 190 | 6 | 6 | 3 |
| Missouri non-MSA | Missouri | Maries | 2 | 337 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Wright | 13 | 729 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Chariton | 0 | 219 | 6 | 7 | 5 |
| Missouri non-MSA | Missouri | Montgomery | 5 | 301 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | McDonald | 15 | 1358 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Linn | 10 | 288 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Dade | 5 | 274 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 409 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Ripley | 5 | 457 | 5 | 8 | 7 |
| Missouri non-MSA | Missouri | Scotland | 1 | 172 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Oregon | 0 | 348 | 4 | 4 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 242 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Douglas | 15 | 383 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Shelby | 1 | 182 | 3 | 4 | 2 |
| Missouri non-MSA | Missouri | Knox | 1 | 125 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 155 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 8 | 309 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Putnam | 1 | 116 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Hickory | 4 | 347 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Mercer | 0 | 78 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Ozark | 2 | 275 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 63 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 324 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 121 | 1 | 2 | 2 |
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
