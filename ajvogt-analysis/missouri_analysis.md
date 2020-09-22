# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/22/2020  
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
| St. Louis-Farmington | 1549 | 60287 | 555 | 550 | 566 |
| Missouri non-MSA | 239 | 22353 | 420 | 382 | 329 |
| Kansas City | 555 | 41771 | 368 | 342 | 352 |
| Springfield | 27 | 7917 | 165 | 166 | 152 |
| Columbia-Jefferson City | 24 | 7375 | 93 | 119 | 134 |
| Joplin | 59 | 4892 | 77 | 76 | 59 |
| Cape Girardeau-Sikeston | 28 | 2743 | 50 | 54 | 40 |
| St. Joseph | 16 | 2224 | 42 | 35 | 27 |
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
| St. Louis-Farmington | Missouri | St. Louis | 782 | 22992 | 154 | 161 | 175 |
| Kansas City | Kansas | Johnson | 141 | 10236 | 103 | 93 | 99 |
| Springfield | Missouri | Greene | 19 | 5473 | 102 | 105 | 105 |
| St. Louis-Farmington | Missouri | St. Charles | 108 | 7274 | 79 | 74 | 70 |
| Kansas City | Missouri | Jackson | 92 | 7064 | 76 | 73 | 68 |
| Kansas City | Missouri | Kansas City | 106 | 10675 | 65 | 61 | 78 |
| St. Louis-Farmington | Illinois | Madison | 130 | 5379 | 61 | 60 | 62 |
| St. Louis-Farmington | Missouri | Jefferson | 52 | 3895 | 61 | 56 | 55 |
| Joplin | Missouri | Jasper | 45 | 3540 | 57 | 61 | 48 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 4453 | 46 | 66 | 85 |
| St. Louis-Farmington | Illinois | St. Clair | 183 | 6317 | 44 | 43 | 50 |
| St. Louis-Farmington | Missouri | St. Francois | 9 | 1948 | 37 | 44 | 38 |
| St. Louis-Farmington | Missouri | St. Louis City | 195 | 6858 | 33 | 29 | 33 |
| Kansas City | Kansas | Wyandotte | 133 | 6693 | 32 | 30 | 34 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 10 | 1532 | 30 | 32 | 22 |
| St. Joseph | Missouri | Buchanan | 13 | 1772 | 30 | 25 | 19 |
| Springfield | Missouri | Christian | 3 | 1255 | 30 | 30 | 24 |
| St. Louis-Farmington | Missouri | Franklin | 28 | 1553 | 29 | 27 | 23 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1386 | 24 | 26 | 22 |
| Missouri non-MSA | Missouri | Laclede | 3 | 560 | 20 | 16 | 9 |
| Kansas City | Missouri | Cass | 17 | 1405 | 19 | 18 | 15 |
| Joplin | Missouri | Newton | 14 | 1352 | 19 | 15 | 11 |
| Springfield | Missouri | Webster | 2 | 529 | 18 | 17 | 11 |
| Missouri non-MSA | Missouri | Camden | 10 | 837 | 17 | 16 | 13 |
| Missouri non-MSA | Missouri | Pettis | 9 | 1026 | 17 | 12 | 9 |
| Kansas City | Missouri | Lafayette | 2 | 464 | 16 | 13 | 8 |
| Missouri non-MSA | Missouri | Howell | 3 | 528 | 16 | 13 | 10 |
| Kansas City | Missouri | Clay | 40 | 1736 | 16 | 16 | 16 |
| St. Louis-Farmington | Illinois | Clinton | 20 | 1071 | 15 | 15 | 16 |
| Missouri non-MSA | Missouri | Johnson | 4 | 995 | 15 | 19 | 15 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 746 | 15 | 12 | 10 |
| Missouri non-MSA | Missouri | Pulaski | 5 | 578 | 14 | 11 | 8 |
| Kansas City | Kansas | Leavenworth | 11 | 1923 | 14 | 13 | 11 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 458 | 13 | 9 | 6 |
| Missouri non-MSA | Missouri | Wright | 0 | 252 | 13 | 10 | 5 |
| Missouri non-MSA | Missouri | Morgan | 1 | 302 | 13 | 10 | 6 |
| Missouri non-MSA | Missouri | Butler | 4 | 576 | 12 | 10 | 7 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 532 | 12 | 9 | 7 |
| Missouri non-MSA | Missouri | Taney | 28 | 1135 | 11 | 12 | 9 |
| Missouri non-MSA | Missouri | Crawford | 2 | 361 | 11 | 10 | 7 |
| Missouri non-MSA | Missouri | Texas | 2 | 279 | 11 | 8 | 6 |
| Missouri non-MSA | Missouri | Miller | 1 | 443 | 11 | 10 | 8 |
| Springfield | Missouri | Polk | 2 | 487 | 11 | 10 | 7 |
| Cape Girardeau-Sikeston | Missouri | Scott | 16 | 824 | 10 | 9 | 9 |
| Missouri non-MSA | Missouri | Perry | 4 | 599 | 10 | 10 | 10 |
| Missouri non-MSA | Missouri | Benton | 2 | 248 | 9 | 6 | 3 |
| Kansas City | Missouri | Platte | 10 | 640 | 9 | 7 | 6 |
| Missouri non-MSA | Missouri | Phelps | 1 | 415 | 8 | 10 | 9 |
| St. Louis-Farmington | Illinois | Macoupin | 7 | 496 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 485 | 8 | 7 | 6 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 584 | 8 | 10 | 11 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 316 | 7 | 11 | 7 |
| Missouri non-MSA | Missouri | Saline | 9 | 672 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Stone | 4 | 400 | 7 | 6 | 5 |
| St. Louis-Farmington | Illinois | Bond | 4 | 290 | 7 | 5 | 6 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 627 | 6 | 7 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 719 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Nodaway | 9 | 719 | 6 | 5 | 15 |
| St. Louis-Farmington | Missouri | Warren | 0 | 447 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Audrain | 2 | 411 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Madison | 0 | 281 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Pike | 3 | 228 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Dent | 0 | 126 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Macon | 0 | 144 | 5 | 4 | 2 |
| St. Joseph | Missouri | Andrew | 1 | 225 | 5 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 381 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Washington | 6 | 340 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Grundy | 2 | 172 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Randolph | 2 | 219 | 4 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 280 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Wayne | 0 | 181 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Carter | 1 | 82 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1048 | 4 | 3 | 2 |
| Kansas City | Kansas | Miami | 1 | 328 | 4 | 4 | 5 |
| St. Joseph | Missouri | DeKalb | 2 | 122 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Livingston | 1 | 385 | 4 | 3 | 10 |
| Missouri non-MSA | Missouri | Douglas | 3 | 165 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Vernon | 1 | 158 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Marion | 14 | 631 | 3 | 5 | 10 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 182 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 319 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Ozark | 0 | 114 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 0 | 91 | 3 | 3 | 2 |
| Kansas City | Missouri | Clinton | 0 | 202 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 14 | 508 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Barry | 6 | 433 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 289 | 3 | 3 | 2 |
| St. Louis-Farmington | Illinois | Jersey | 13 | 381 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Cedar | 0 | 91 | 3 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 173 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 16 | 155 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Henry | 4 | 167 | 2 | 2 | 2 |
| Kansas City | Missouri | Caldwell | 1 | 78 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 99 | 2 | 2 | 2 |
| Kansas City | Missouri | Bates | 1 | 101 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 169 | 2 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 164 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Shannon | 1 | 86 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 127 | 2 | 2 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 105 | 2 | 1 | 1 |
| Kansas City | Missouri | Ray | 0 | 158 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 2 | 88 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 81 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 46 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 144 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 1 | 62 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 54 | 1 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 71 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 71 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 35 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 144 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Gentry | 9 | 117 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 50 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Carroll | 1 | 136 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 75 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 40 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 28 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 68 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 86 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 101 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 59 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 75 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 48 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 43 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 185 | 0 | 0 | 0 |
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
