# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/08/2020  
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
| St. Louis-Farmington | 2584 | 162806 | 2055 | 2067 | 2176 |
| Kansas City | 1253 | 108487 | 1307 | 1236 | 1340 |
| Missouri non-MSA | 942 | 75853 | 841 | 807 | 934 |
| Columbia-Jefferson City | 126 | 25122 | 255 | 250 | 311 |
| Springfield | 288 | 23521 | 250 | 242 | 248 |
| Cape Girardeau-Sikeston | 122 | 9576 | 103 | 105 | 128 |
| St. Joseph | 97 | 7316 | 89 | 92 | 94 |
| Joplin | 162 | 11767 | 73 | 76 | 113 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1098 | 56500 | 668 | 681 | 709 |
| Kansas City | Kansas | Johnson | 309 | 30199 | 397 | 369 | 411 |
| St. Louis-Farmington | Missouri | St. Charles | 219 | 22127 | 271 | 271 | 301 |
| Kansas City | Missouri | Kansas City | 304 | 25335 | 258 | 266 | 290 |
| Kansas City | Missouri | Jackson | 190 | 19126 | 249 | 229 | 245 |
| St. Louis-Farmington | Illinois | Madison | 287 | 16348 | 248 | 233 | 245 |
| St. Louis-Farmington | Illinois | St. Clair | 280 | 15140 | 223 | 218 | 201 |
| St. Louis-Farmington | Missouri | Jefferson | 108 | 12289 | 162 | 168 | 182 |
| Springfield | Missouri | Greene | 212 | 15179 | 158 | 155 | 158 |
| St. Louis-Farmington | Missouri | St. Louis City | 260 | 14082 | 150 | 151 | 153 |
| Kansas City | Kansas | Wyandotte | 184 | 12407 | 125 | 105 | 109 |
| Columbia-Jefferson City | Missouri | Boone | 25 | 11143 | 113 | 101 | 128 |
| Columbia-Jefferson City | Missouri | Cole | 60 | 6709 | 64 | 71 | 88 |
| Kansas City | Missouri | Cass | 40 | 4249 | 62 | 57 | 60 |
| Joplin | Missouri | Jasper | 124 | 8695 | 61 | 60 | 88 |
| St. Joseph | Missouri | Buchanan | 66 | 5183 | 60 | 62 | 62 |
| Kansas City | Missouri | Clay | 76 | 5080 | 58 | 52 | 66 |
| St. Louis-Farmington | Missouri | Franklin | 91 | 5288 | 57 | 58 | 67 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 66 | 5494 | 56 | 60 | 75 |
| Springfield | Missouri | Christian | 24 | 4224 | 53 | 49 | 49 |
| Missouri non-MSA | Missouri | Pulaski | 24 | 1978 | 47 | 34 | 27 |
| Kansas City | Kansas | Leavenworth | 34 | 4138 | 45 | 45 | 43 |
| St. Louis-Farmington | Illinois | Clinton | 65 | 3649 | 44 | 47 | 50 |
| St. Louis-Farmington | Missouri | St. Francois | 47 | 5413 | 43 | 49 | 65 |
| Missouri non-MSA | Missouri | Pettis | 36 | 2980 | 41 | 28 | 28 |
| St. Louis-Farmington | Missouri | Lincoln | 13 | 2763 | 41 | 39 | 42 |
| Columbia-Jefferson City | Missouri | Callaway | 11 | 3137 | 40 | 38 | 43 |
| Missouri non-MSA | Missouri | Taney | 39 | 3182 | 39 | 37 | 37 |
| St. Louis-Farmington | Illinois | Macoupin | 27 | 2547 | 38 | 44 | 49 |
| St. Louis-Farmington | Illinois | Monroe | 48 | 2353 | 38 | 34 | 37 |
| Cape Girardeau-Sikeston | Missouri | Scott | 42 | 2936 | 35 | 34 | 40 |
| Missouri non-MSA | Missouri | Laclede | 33 | 2039 | 31 | 24 | 22 |
| Missouri non-MSA | Missouri | Butler | 9 | 2382 | 29 | 29 | 29 |
| St. Louis-Farmington | Illinois | Jersey | 25 | 1496 | 28 | 27 | 25 |
| Missouri non-MSA | Missouri | Phelps | 50 | 1995 | 28 | 29 | 32 |
| Kansas City | Missouri | Platte | 17 | 1870 | 25 | 24 | 23 |
| Missouri non-MSA | Missouri | Johnson | 16 | 2720 | 24 | 27 | 30 |
| Missouri non-MSA | Missouri | Marion | 18 | 1970 | 24 | 24 | 27 |
| Missouri non-MSA | Missouri | Camden | 49 | 2634 | 23 | 21 | 27 |
| Kansas City | Kansas | Miami | 3 | 1229 | 22 | 21 | 19 |
| St. Louis-Farmington | Illinois | Bond | 12 | 1205 | 22 | 20 | 18 |
| Missouri non-MSA | Missouri | Miller | 26 | 1663 | 22 | 17 | 18 |
| Missouri non-MSA | Missouri | Stoddard | 24 | 1792 | 19 | 21 | 25 |
| Springfield | Missouri | Polk | 15 | 1522 | 19 | 15 | 12 |
| Missouri non-MSA | Missouri | Audrain | 15 | 1236 | 19 | 18 | 17 |
| Missouri non-MSA | Missouri | Randolph | 9 | 1345 | 18 | 15 | 18 |
| Missouri non-MSA | Missouri | Stone | 19 | 1318 | 17 | 13 | 15 |
| Springfield | Missouri | Webster | 27 | 1968 | 16 | 17 | 20 |
| Kansas City | Missouri | Lafayette | 30 | 1667 | 16 | 19 | 20 |
| Missouri non-MSA | Missouri | Benton | 11 | 890 | 16 | 11 | 11 |
| Missouri non-MSA | Missouri | Nodaway | 14 | 2116 | 15 | 18 | 22 |
| Missouri non-MSA | Missouri | Crawford | 14 | 1312 | 15 | 14 | 17 |
| Missouri non-MSA | Missouri | Washington | 27 | 1555 | 15 | 15 | 22 |
| Missouri non-MSA | Missouri | Morgan | 13 | 1181 | 14 | 12 | 12 |
| Kansas City | Missouri | Clinton | 47 | 996 | 14 | 11 | 12 |
| Missouri non-MSA | Missouri | Lawrence | 39 | 2033 | 14 | 15 | 22 |
| Missouri non-MSA | Missouri | Pike | 10 | 1035 | 14 | 15 | 18 |
| Missouri non-MSA | Missouri | Mississippi | 7 | 979 | 13 | 14 | 15 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1173 | 13 | 15 | 18 |
| Missouri non-MSA | Missouri | Henry | 12 | 1193 | 13 | 13 | 21 |
| Missouri non-MSA | Missouri | Texas | 10 | 1056 | 12 | 10 | 11 |
| Missouri non-MSA | Missouri | Saline | 12 | 1683 | 12 | 13 | 18 |
| Joplin | Missouri | Newton | 38 | 3072 | 12 | 15 | 24 |
| Columbia-Jefferson City | Missouri | Cooper | 9 | 1256 | 12 | 10 | 14 |
| Missouri non-MSA | Missouri | Adair | 3 | 1173 | 12 | 11 | 17 |
| Missouri non-MSA | Missouri | Barry | 29 | 1546 | 12 | 12 | 17 |
| Kansas City | Missouri | Ray | 6 | 791 | 11 | 11 | 13 |
| St. Louis-Farmington | Missouri | Warren | 3 | 1312 | 11 | 14 | 19 |
| Missouri non-MSA | Missouri | Vernon | 10 | 762 | 11 | 9 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1787 | 11 | 13 | 15 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1320 | 11 | 12 | 17 |
| Missouri non-MSA | Missouri | Madison | 9 | 974 | 11 | 12 | 13 |
| St. Joseph | Missouri | Andrew | 11 | 898 | 11 | 11 | 12 |
| Missouri non-MSA | Missouri | Perry | 12 | 1638 | 11 | 13 | 20 |
| Missouri non-MSA | Missouri | Howell | 31 | 1669 | 10 | 10 | 11 |
| St. Joseph | Kansas | Doniphan | 5 | 587 | 10 | 10 | 11 |
| Columbia-Jefferson City | Missouri | Osage | 4 | 1017 | 10 | 10 | 12 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 10 | 870 | 9 | 7 | 9 |
| Missouri non-MSA | Missouri | Gentry | 13 | 482 | 8 | 6 | 8 |
| Missouri non-MSA | Missouri | Dent | 4 | 583 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Harrison | 3 | 457 | 8 | 6 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 19 | 1154 | 8 | 9 | 10 |
| Kansas City | Missouri | Bates | 9 | 611 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | Wright | 15 | 834 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Carroll | 7 | 496 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Livingston | 16 | 839 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Ralls | 2 | 532 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | McDonald | 16 | 1457 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Macon | 3 | 737 | 7 | 9 | 13 |
| Missouri non-MSA | Missouri | New Madrid | 24 | 1420 | 7 | 11 | 16 |
| St. Joseph | Missouri | DeKalb | 15 | 648 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Ripley | 8 | 572 | 6 | 7 | 8 |
| Kansas City | Kansas | Linn | 1 | 353 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 25 | 531 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Grundy | 14 | 553 | 6 | 5 | 7 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 294 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Daviess | 8 | 374 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 374 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Shelby | 1 | 246 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Wayne | 3 | 540 | 5 | 5 | 6 |
| Kansas City | Missouri | Caldwell | 3 | 436 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Lewis | 2 | 467 | 5 | 3 | 6 |
| Missouri non-MSA | Missouri | Douglas | 15 | 474 | 4 | 6 | 4 |
| Missouri non-MSA | Missouri | Barton | 5 | 663 | 4 | 4 | 6 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 540 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Maries | 4 | 399 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Linn | 11 | 350 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 376 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Iron | 1 | 261 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Carter | 6 | 322 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Chariton | 0 | 267 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Clark | 4 | 325 | 3 | 3 | 5 |
| Springfield | Missouri | Dallas | 10 | 628 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Monroe | 5 | 418 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Holt | 4 | 291 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Oregon | 2 | 405 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 197 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Atchison | 3 | 232 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 358 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 6 | 384 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dade | 8 | 306 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 6 | 583 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Ozark | 3 | 312 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 89 | 2 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 4 | 276 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Putnam | 1 | 175 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Cedar | 7 | 457 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | Scotland | 1 | 201 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 142 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 92 | 0 | 0 | 1 |
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
