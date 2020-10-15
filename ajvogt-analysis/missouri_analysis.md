# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/15/2020  
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
| St. Louis-Farmington | 1814 | 72454 | 615 | 549 | 535 |
| Missouri non-MSA | 417 | 32373 | 550 | 496 | 432 |
| Kansas City | 744 | 51551 | 497 | 469 | 412 |
| Springfield | 124 | 11926 | 185 | 180 | 172 |
| Columbia-Jefferson City | 54 | 9977 | 177 | 135 | 108 |
| Joplin | 77 | 6371 | 77 | 73 | 67 |
| Cape Girardeau-Sikeston | 52 | 3992 | 74 | 61 | 53 |
| St. Joseph | 42 | 3280 | 55 | 52 | 45 |
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
| St. Louis-Farmington | Missouri | St. Louis | 872 | 26881 | 187 | 164 | 165 |
| Kansas City | Missouri | Jackson | 120 | 8901 | 143 | 93 | 79 |
| Springfield | Missouri | Greene | 100 | 7941 | 114 | 110 | 106 |
| St. Louis-Farmington | Missouri | St. Charles | 135 | 9086 | 112 | 95 | 78 |
| Kansas City | Kansas | Johnson | 171 | 12562 | 106 | 96 | 101 |
| Columbia-Jefferson City | Missouri | Boone | 19 | 5398 | 80 | 47 | 42 |
| St. Louis-Farmington | Illinois | Madison | 150 | 6499 | 59 | 47 | 51 |
| Kansas City | Missouri | Kansas City | 173 | 12934 | 56 | 118 | 90 |
| Joplin | Missouri | Newton | 16 | 1813 | 50 | 21 | 19 |
| St. Louis-Farmington | Illinois | St. Clair | 207 | 7330 | 48 | 41 | 44 |
| Columbia-Jefferson City | Missouri | Cole | 18 | 2203 | 46 | 44 | 32 |
| St. Louis-Farmington | Missouri | St. Louis City | 232 | 7705 | 45 | 39 | 36 |
| St. Louis-Farmington | Missouri | Jefferson | 71 | 4930 | 45 | 46 | 48 |
| Kansas City | Missouri | Clay | 47 | 2198 | 45 | 26 | 19 |
| Missouri non-MSA | Missouri | Johnson | 12 | 1331 | 43 | 15 | 14 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 30 | 2327 | 43 | 37 | 33 |
| Kansas City | Kansas | Wyandotte | 143 | 7695 | 43 | 50 | 40 |
| St. Joseph | Missouri | Buchanan | 37 | 2577 | 40 | 39 | 33 |
| Springfield | Missouri | Christian | 8 | 1947 | 34 | 33 | 30 |
| St. Louis-Farmington | Missouri | St. Francois | 19 | 2505 | 31 | 26 | 27 |
| Joplin | Missouri | Jasper | 61 | 4558 | 27 | 52 | 47 |
| Missouri non-MSA | Missouri | Camden | 21 | 1359 | 26 | 24 | 21 |
| St. Louis-Farmington | Missouri | Franklin | 35 | 2155 | 26 | 28 | 26 |
| Kansas City | Missouri | Cass | 28 | 1795 | 25 | 19 | 17 |
| Cape Girardeau-Sikeston | Missouri | Scott | 18 | 1151 | 24 | 18 | 13 |
| Missouri non-MSA | Missouri | Phelps | 18 | 687 | 23 | 14 | 11 |
| Columbia-Jefferson City | Missouri | Callaway | 4 | 930 | 23 | 18 | 13 |
| Missouri non-MSA | Missouri | Laclede | 15 | 991 | 23 | 23 | 19 |
| Springfield | Missouri | Webster | 6 | 962 | 20 | 21 | 18 |
| Missouri non-MSA | Missouri | Howell | 4 | 943 | 19 | 22 | 17 |
| Missouri non-MSA | Missouri | Butler | 9 | 881 | 17 | 15 | 13 |
| Missouri non-MSA | Missouri | Lawrence | 14 | 880 | 17 | 17 | 14 |
| St. Louis-Farmington | Illinois | Clinton | 23 | 1452 | 16 | 16 | 16 |
| Missouri non-MSA | Missouri | Pulaski | 8 | 846 | 16 | 12 | 12 |
| Kansas City | Missouri | Platte | 12 | 859 | 15 | 10 | 9 |
| Kansas City | Missouri | Lafayette | 19 | 703 | 13 | 12 | 11 |
| Missouri non-MSA | Missouri | Texas | 2 | 489 | 13 | 11 | 9 |
| Missouri non-MSA | Missouri | Barton | 2 | 357 | 13 | 11 | 6 |
| Kansas City | Missouri | Clinton | 5 | 371 | 13 | 9 | 6 |
| Kansas City | Kansas | Leavenworth | 17 | 2386 | 12 | 13 | 18 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 693 | 12 | 12 | 10 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 985 | 12 | 14 | 10 |
| Springfield | Missouri | Polk | 9 | 823 | 12 | 11 | 13 |
| Missouri non-MSA | Missouri | Pettis | 13 | 1309 | 11 | 10 | 13 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 944 | 11 | 11 | 8 |
| Missouri non-MSA | Missouri | Madison | 1 | 398 | 11 | 6 | 5 |
| Missouri non-MSA | Missouri | Miller | 3 | 668 | 11 | 11 | 10 |
| Missouri non-MSA | Missouri | Wright | 0 | 521 | 11 | 11 | 12 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 293 | 10 | 9 | 6 |
| Missouri non-MSA | Missouri | Morgan | 5 | 526 | 10 | 10 | 10 |
| Columbia-Jefferson City | Missouri | Moniteau | 6 | 435 | 9 | 7 | 6 |
| Missouri non-MSA | Missouri | Barry | 8 | 615 | 9 | 8 | 6 |
| Missouri non-MSA | Missouri | Crawford | 6 | 500 | 9 | 6 | 7 |
| Missouri non-MSA | Missouri | Randolph | 2 | 443 | 9 | 12 | 8 |
| Missouri non-MSA | Missouri | Dent | 2 | 215 | 9 | 4 | 4 |
| Missouri non-MSA | Missouri | Stone | 7 | 597 | 9 | 9 | 8 |
| Missouri non-MSA | Missouri | New Madrid | 17 | 661 | 8 | 8 | 5 |
| St. Louis-Farmington | Illinois | Monroe | 27 | 810 | 8 | 8 | 7 |
| Missouri non-MSA | Missouri | Taney | 33 | 1479 | 8 | 18 | 14 |
| Missouri non-MSA | Missouri | Henry | 5 | 308 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | Livingston | 4 | 525 | 8 | 8 | 5 |
| St. Louis-Farmington | Illinois | Macoupin | 8 | 664 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Marion | 14 | 781 | 7 | 7 | 5 |
| St. Joseph | Missouri | Andrew | 3 | 357 | 7 | 7 | 5 |
| Missouri non-MSA | Missouri | Audrain | 5 | 514 | 6 | 4 | 4 |
| Missouri non-MSA | Missouri | Perry | 8 | 721 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Washington | 11 | 551 | 6 | 8 | 8 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 3 | 412 | 6 | 4 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 12 | 628 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | McDonald | 13 | 1167 | 6 | 3 | 4 |
| Kansas City | Missouri | Bates | 3 | 208 | 6 | 5 | 4 |
| St. Louis-Farmington | Missouri | Warren | 2 | 546 | 6 | 4 | 4 |
| Missouri non-MSA | Missouri | Adair | 0 | 424 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Saline | 9 | 857 | 6 | 9 | 7 |
| Missouri non-MSA | Missouri | Cedar | 3 | 196 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Ripley | 3 | 192 | 6 | 1 | 2 |
| Kansas City | Kansas | Miami | 2 | 474 | 5 | 4 | 5 |
| St. Louis-Farmington | Illinois | Bond | 9 | 405 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Dade | 0 | 121 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 189 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Vernon | 3 | 268 | 5 | 5 | 4 |
| St. Joseph | Missouri | DeKalb | 2 | 205 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Benton | 5 | 428 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Sullivan | 1 | 259 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 201 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 2 | 187 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Dunklin | 11 | 927 | 4 | 9 | 9 |
| Missouri non-MSA | Missouri | Carter | 3 | 141 | 4 | 2 | 3 |
| Missouri non-MSA | Missouri | Pike | 4 | 287 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Wayne | 1 | 269 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Hickory | 3 | 161 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Shannon | 2 | 179 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 258 | 3 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 507 | 3 | 5 | 5 |
| Springfield | Missouri | Dallas | 1 | 253 | 3 | 4 | 3 |
| Kansas City | Missouri | Ray | 2 | 215 | 3 | 3 | 2 |
| Kansas City | Kansas | Linn | 1 | 109 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 119 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Gentry | 10 | 164 | 3 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 211 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 4 | 348 | 3 | 3 | 2 |
| Kansas City | Missouri | Caldwell | 1 | 141 | 3 | 2 | 2 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 435 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 1 | 162 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Clark | 0 | 92 | 2 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 141 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Carroll | 2 | 159 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Lewis | 2 | 151 | 2 | 4 | 2 |
| Missouri non-MSA | Missouri | Macon | 0 | 187 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Harrison | 1 | 154 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 97 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Douglas | 3 | 251 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Monroe | 1 | 109 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 142 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Ralls | 0 | 172 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 88 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 1 | 78 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 45 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 50 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 1 | 95 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Grundy | 8 | 229 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Atchison | 1 | 70 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 96 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 102 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 45 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 57 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 1 | 54 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 66 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Mercer | 0 | 31 | 0 | 0 | 0 |
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
