# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/21/2020  
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
| St. Louis-Farmington | 1544 | 59757 | 536 | 546 | 572 |
| Missouri non-MSA | 237 | 21952 | 417 | 364 | 325 |
| Kansas City | 551 | 41443 | 374 | 340 | 363 |
| Springfield | 27 | 7772 | 167 | 164 | 150 |
| Columbia-Jefferson City | 24 | 7300 | 101 | 119 | 135 |
| Joplin | 57 | 4868 | 77 | 75 | 60 |
| Cape Girardeau-Sikeston | 28 | 2697 | 52 | 53 | 39 |
| St. Joseph | 16 | 2188 | 39 | 33 | 26 |
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
| St. Louis-Farmington | Missouri | St. Louis | 782 | 22833 | 143 | 161 | 177 |
| Kansas City | Kansas | Johnson | 141 | 10180 | 107 | 95 | 105 |
| Springfield | Missouri | Greene | 19 | 5386 | 103 | 105 | 104 |
| Kansas City | Missouri | Jackson | 92 | 7064 | 84 | 75 | 73 |
| St. Louis-Farmington | Missouri | St. Charles | 108 | 7150 | 70 | 72 | 68 |
| St. Louis-Farmington | Illinois | Madison | 130 | 5341 | 61 | 60 | 63 |
| St. Louis-Farmington | Missouri | Jefferson | 50 | 3840 | 59 | 55 | 55 |
| Joplin | Missouri | Jasper | 43 | 3521 | 58 | 60 | 48 |
| Kansas City | Missouri | Kansas City | 103 | 10545 | 57 | 58 | 77 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 4403 | 47 | 66 | 86 |
| St. Louis-Farmington | Missouri | St. Francois | 8 | 1913 | 43 | 43 | 39 |
| St. Louis-Farmington | Illinois | St. Clair | 183 | 6278 | 42 | 43 | 51 |
| Kansas City | Kansas | Wyandotte | 133 | 6684 | 33 | 30 | 37 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 10 | 1501 | 32 | 31 | 22 |
| St. Louis-Farmington | Missouri | St. Louis City | 195 | 6830 | 31 | 30 | 33 |
| Springfield | Missouri | Christian | 3 | 1235 | 30 | 29 | 24 |
| St. Joseph | Missouri | Buchanan | 13 | 1750 | 29 | 24 | 19 |
| St. Louis-Farmington | Missouri | Franklin | 26 | 1529 | 28 | 26 | 23 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1374 | 25 | 26 | 22 |
| Springfield | Missouri | Webster | 2 | 521 | 20 | 16 | 11 |
| Kansas City | Missouri | Cass | 17 | 1389 | 19 | 17 | 15 |
| Joplin | Missouri | Newton | 14 | 1347 | 19 | 15 | 11 |
| Missouri non-MSA | Missouri | Johnson | 4 | 984 | 18 | 20 | 14 |
| Missouri non-MSA | Missouri | Camden | 10 | 809 | 18 | 15 | 12 |
| Kansas City | Missouri | Lafayette | 2 | 440 | 17 | 12 | 7 |
| Kansas City | Missouri | Clay | 40 | 1724 | 16 | 16 | 17 |
| St. Louis-Farmington | Illinois | Clinton | 20 | 1064 | 16 | 15 | 17 |
| Missouri non-MSA | Missouri | Laclede | 3 | 513 | 15 | 13 | 8 |
| Missouri non-MSA | Missouri | Pettis | 9 | 1004 | 15 | 11 | 9 |
| Missouri non-MSA | Missouri | Howell | 3 | 505 | 15 | 12 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 744 | 15 | 12 | 10 |
| Kansas City | Kansas | Leavenworth | 10 | 1877 | 15 | 12 | 10 |
| Missouri non-MSA | Missouri | Wright | 0 | 248 | 14 | 10 | 5 |
| Missouri non-MSA | Missouri | Crawford | 2 | 349 | 14 | 9 | 7 |
| Missouri non-MSA | Missouri | Morgan | 1 | 299 | 14 | 10 | 6 |
| Missouri non-MSA | Missouri | Pulaski | 5 | 556 | 13 | 9 | 7 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 445 | 12 | 9 | 6 |
| Missouri non-MSA | Missouri | Miller | 1 | 442 | 12 | 10 | 8 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 524 | 11 | 9 | 7 |
| Missouri non-MSA | Missouri | Texas | 2 | 278 | 11 | 8 | 6 |
| Missouri non-MSA | Missouri | Taney | 28 | 1127 | 11 | 11 | 9 |
| Missouri non-MSA | Missouri | Butler | 4 | 559 | 10 | 10 | 7 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 580 | 10 | 10 | 11 |
| Springfield | Missouri | Polk | 2 | 463 | 10 | 8 | 6 |
| Missouri non-MSA | Missouri | Phelps | 1 | 411 | 10 | 10 | 9 |
| Cape Girardeau-Sikeston | Missouri | Scott | 16 | 814 | 9 | 9 | 9 |
| Missouri non-MSA | Missouri | Benton | 2 | 245 | 9 | 5 | 3 |
| St. Louis-Farmington | Illinois | Macoupin | 7 | 495 | 9 | 7 | 7 |
| Missouri non-MSA | Missouri | Audrain | 2 | 405 | 8 | 6 | 5 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 311 | 8 | 11 | 7 |
| Kansas City | Missouri | Platte | 10 | 631 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Perry | 4 | 575 | 8 | 9 | 9 |
| St. Louis-Farmington | Illinois | Bond | 4 | 288 | 8 | 5 | 6 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 277 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Saline | 9 | 665 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Stone | 4 | 395 | 6 | 6 | 5 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 627 | 6 | 7 | 8 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 711 | 6 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 377 | 6 | 6 | 6 |
| St. Joseph | Missouri | Andrew | 1 | 221 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Washington | 5 | 339 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 9 | 718 | 5 | 5 | 15 |
| Missouri non-MSA | Missouri | Grundy | 2 | 170 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 466 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Macon | 0 | 144 | 5 | 4 | 2 |
| St. Louis-Farmington | Missouri | Warren | 0 | 441 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Pike | 3 | 226 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Dent | 0 | 120 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Randolph | 2 | 217 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Wayne | 0 | 180 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Madison | 0 | 271 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Marion | 14 | 628 | 4 | 5 | 10 |
| Kansas City | Kansas | Miami | 1 | 314 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Ozark | 0 | 112 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Livingston | 1 | 380 | 4 | 3 | 10 |
| Missouri non-MSA | Missouri | New Madrid | 14 | 507 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 179 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1043 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Vernon | 1 | 154 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Carter | 1 | 77 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Douglas | 3 | 164 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 319 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Barry | 6 | 434 | 3 | 4 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 13 | 380 | 3 | 4 | 5 |
| Kansas City | Missouri | Caldwell | 1 | 78 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 284 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Barton | 0 | 166 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 0 | 86 | 2 | 3 | 2 |
| Springfield | Missouri | Dallas | 1 | 167 | 2 | 3 | 2 |
| St. Joseph | Missouri | DeKalb | 2 | 112 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 15 | 154 | 2 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 127 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Shannon | 1 | 84 | 2 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 99 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 97 | 2 | 2 | 2 |
| Kansas City | Missouri | Clinton | 0 | 196 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 0 | 87 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 4 | 162 | 2 | 2 | 2 |
| Kansas City | Missouri | Ray | 0 | 156 | 2 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 105 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 2 | 87 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 62 | 2 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 162 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Gentry | 9 | 120 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 79 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 71 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 69 | 1 | 1 | 1 |
| Kansas City | Kansas | Linn | 0 | 66 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 42 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 1 | 134 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 139 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Dade | 0 | 48 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 100 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 140 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 0 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 73 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 86 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 59 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 75 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 48 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 185 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 22 | 0 | 0 | 0 |
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
