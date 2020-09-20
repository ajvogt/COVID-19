# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/20/2020  
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
| St. Louis-Farmington | 1544 | 59298 | 579 | 554 | 577 |
| Missouri non-MSA | 236 | 21581 | 418 | 359 | 321 |
| Kansas City | 551 | 41111 | 364 | 339 | 365 |
| Springfield | 27 | 7620 | 160 | 163 | 148 |
| Columbia-Jefferson City | 24 | 7223 | 122 | 126 | 136 |
| Joplin | 57 | 4816 | 77 | 74 | 60 |
| Cape Girardeau-Sikeston | 28 | 2638 | 52 | 50 | 39 |
| St. Joseph | 16 | 2141 | 38 | 32 | 25 |
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
| St. Louis-Farmington | Missouri | St. Louis | 782 | 22729 | 163 | 169 | 181 |
| Kansas City | Kansas | Johnson | 141 | 10083 | 104 | 96 | 107 |
| Springfield | Missouri | Greene | 19 | 5286 | 100 | 105 | 103 |
| Kansas City | Missouri | Jackson | 92 | 6987 | 82 | 74 | 71 |
| St. Louis-Farmington | Missouri | St. Charles | 108 | 7066 | 72 | 70 | 68 |
| St. Louis-Farmington | Missouri | St. Francois | 8 | 1895 | 65 | 45 | 40 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 4365 | 63 | 71 | 86 |
| Joplin | Missouri | Jasper | 43 | 3492 | 60 | 60 | 48 |
| St. Louis-Farmington | Illinois | Madison | 130 | 5291 | 59 | 60 | 64 |
| St. Louis-Farmington | Missouri | Jefferson | 50 | 3783 | 59 | 55 | 54 |
| Kansas City | Missouri | Kansas City | 103 | 10470 | 54 | 58 | 79 |
| St. Louis-Farmington | Illinois | St. Clair | 183 | 6239 | 39 | 42 | 52 |
| St. Louis-Farmington | Missouri | St. Louis City | 195 | 6797 | 32 | 30 | 34 |
| Kansas City | Kansas | Wyandotte | 133 | 6659 | 32 | 30 | 36 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 10 | 1461 | 31 | 29 | 21 |
| St. Louis-Farmington | Missouri | Franklin | 26 | 1496 | 30 | 25 | 23 |
| Springfield | Missouri | Christian | 3 | 1204 | 28 | 29 | 23 |
| St. Joseph | Missouri | Buchanan | 13 | 1712 | 27 | 23 | 18 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1354 | 26 | 26 | 23 |
| Missouri non-MSA | Missouri | Johnson | 4 | 975 | 25 | 23 | 14 |
| Kansas City | Missouri | Cass | 17 | 1380 | 19 | 17 | 15 |
| Springfield | Missouri | Webster | 2 | 500 | 18 | 16 | 11 |
| Kansas City | Missouri | Clay | 40 | 1714 | 17 | 16 | 17 |
| Joplin | Missouri | Newton | 14 | 1324 | 16 | 13 | 11 |
| St. Louis-Farmington | Illinois | Clinton | 20 | 1051 | 16 | 15 | 16 |
| Missouri non-MSA | Missouri | Howell | 3 | 498 | 16 | 12 | 10 |
| Missouri non-MSA | Missouri | Pettis | 8 | 992 | 15 | 11 | 9 |
| Missouri non-MSA | Missouri | Camden | 10 | 780 | 15 | 13 | 11 |
| Missouri non-MSA | Missouri | Laclede | 3 | 498 | 15 | 12 | 8 |
| Kansas City | Kansas | Leavenworth | 10 | 1877 | 15 | 12 | 10 |
| Missouri non-MSA | Missouri | Crawford | 2 | 345 | 14 | 9 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 730 | 14 | 12 | 10 |
| Missouri non-MSA | Missouri | Wright | 0 | 231 | 14 | 9 | 5 |
| Kansas City | Missouri | Lafayette | 2 | 408 | 13 | 10 | 6 |
| Missouri non-MSA | Missouri | Morgan | 1 | 280 | 13 | 9 | 5 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 439 | 12 | 8 | 6 |
| Missouri non-MSA | Missouri | Pulaski | 5 | 537 | 12 | 8 | 7 |
| Missouri non-MSA | Missouri | Texas | 2 | 270 | 12 | 9 | 6 |
| Missouri non-MSA | Missouri | Taney | 28 | 1116 | 11 | 11 | 10 |
| Missouri non-MSA | Missouri | Miller | 1 | 429 | 11 | 9 | 8 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 569 | 11 | 11 | 11 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 507 | 10 | 8 | 7 |
| Missouri non-MSA | Missouri | Phelps | 1 | 401 | 10 | 10 | 8 |
| Springfield | Missouri | Polk | 2 | 463 | 10 | 9 | 7 |
| Cape Girardeau-Sikeston | Missouri | Scott | 16 | 802 | 10 | 8 | 9 |
| Missouri non-MSA | Missouri | Butler | 4 | 541 | 9 | 9 | 7 |
| Missouri non-MSA | Missouri | Perry | 4 | 570 | 9 | 9 | 9 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 306 | 9 | 11 | 7 |
| Missouri non-MSA | Missouri | Benton | 2 | 239 | 9 | 5 | 3 |
| Missouri non-MSA | Missouri | Audrain | 2 | 402 | 8 | 6 | 5 |
| St. Louis-Farmington | Illinois | Bond | 4 | 286 | 8 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 373 | 8 | 6 | 6 |
| Kansas City | Missouri | Platte | 10 | 625 | 8 | 7 | 6 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 275 | 7 | 5 | 3 |
| St. Louis-Farmington | Illinois | Macoupin | 7 | 486 | 7 | 6 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 704 | 7 | 6 | 7 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 625 | 7 | 8 | 8 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 463 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Saline | 9 | 660 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Stone | 4 | 387 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 9 | 713 | 6 | 7 | 15 |
| Missouri non-MSA | Missouri | Marion | 14 | 626 | 6 | 6 | 10 |
| St. Joseph | Missouri | Andrew | 1 | 213 | 5 | 4 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 437 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Dent | 0 | 120 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Pike | 3 | 225 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Macon | 0 | 139 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 168 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Grundy | 2 | 163 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Randolph | 2 | 207 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Washington | 5 | 329 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Livingston | 1 | 377 | 4 | 2 | 10 |
| Kansas City | Kansas | Miami | 1 | 314 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Madison | 0 | 269 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 175 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Ozark | 0 | 110 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 318 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Douglas | 3 | 162 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1042 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 14 | 503 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Vernon | 1 | 151 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Barry | 6 | 431 | 3 | 4 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 13 | 378 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Oregon | 0 | 99 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 1 | 71 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 165 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 282 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 15 | 154 | 3 | 3 | 3 |
| Kansas City | Missouri | Clinton | 0 | 197 | 3 | 3 | 2 |
| Kansas City | Missouri | Caldwell | 1 | 76 | 3 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 125 | 3 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 167 | 3 | 3 | 2 |
| St. Joseph | Missouri | DeKalb | 2 | 111 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 0 | 87 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Daviess | 0 | 83 | 2 | 2 | 2 |
| Kansas City | Missouri | Ray | 0 | 157 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 162 | 2 | 1 | 2 |
| Kansas City | Missouri | Bates | 1 | 98 | 2 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 105 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 4 | 161 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shannon | 1 | 81 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 2 | 86 | 2 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 69 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 138 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 78 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 59 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 1 | 133 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 67 | 1 | 1 | 1 |
| Kansas City | Kansas | Linn | 0 | 66 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 41 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 116 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 100 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 139 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Dade | 0 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 59 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 86 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Lewis | 2 | 71 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 48 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 59 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 75 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 185 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Mercer | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 22 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 47 | 0 | 0 | 0 |
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
