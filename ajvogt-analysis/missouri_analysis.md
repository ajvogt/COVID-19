# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/15/2021  
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
| St. Louis-Farmington | 3733 | 223243 | 1510 | 1523 | 1512 |
| Kansas City | 1873 | 151666 | 1213 | 1166 | 1121 |
| Missouri non-MSA | 1577 | 100985 | 628 | 628 | 625 |
| Springfield | 461 | 32735 | 253 | 260 | 238 |
| Columbia-Jefferson City | 242 | 31809 | 152 | 163 | 174 |
| Joplin | 237 | 14671 | 83 | 86 | 78 |
| Cape Girardeau-Sikeston | 193 | 11859 | 49 | 55 | 57 |
| St. Joseph | 156 | 9311 | 48 | 50 | 48 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1547 | 77057 | 537 | 541 | 518 |
| Kansas City | Kansas | Johnson | 587 | 44346 | 427 | 391 | 373 |
| Kansas City | Missouri | Kansas City | 380 | 33229 | 217 | 227 | 205 |
| Kansas City | Missouri | Jackson | 280 | 26171 | 207 | 196 | 179 |
| St. Louis-Farmington | Illinois | Madison | 449 | 23664 | 200 | 186 | 183 |
| St. Louis-Farmington | Missouri | St. Charles | 315 | 29812 | 192 | 191 | 191 |
| St. Louis-Farmington | Illinois | St. Clair | 410 | 21597 | 178 | 181 | 163 |
| Springfield | Missouri | Greene | 313 | 21059 | 162 | 166 | 151 |
| St. Louis-Farmington | Missouri | Jefferson | 153 | 16971 | 129 | 133 | 120 |
| Kansas City | Kansas | Wyandotte | 213 | 17039 | 107 | 104 | 115 |
| Columbia-Jefferson City | Missouri | Boone | 54 | 14481 | 77 | 80 | 86 |
| St. Louis-Farmington | Missouri | Franklin | 122 | 7463 | 66 | 64 | 57 |
| Joplin | Missouri | Jasper | 177 | 10906 | 62 | 65 | 58 |
| Kansas City | Missouri | Cass | 62 | 6302 | 61 | 53 | 52 |
| Kansas City | Missouri | Clay | 118 | 6982 | 54 | 50 | 48 |
| Springfield | Missouri | Christian | 60 | 6186 | 49 | 52 | 50 |
| Kansas City | Kansas | Leavenworth | 50 | 5574 | 42 | 37 | 37 |
| St. Louis-Farmington | Illinois | Macoupin | 92 | 3739 | 40 | 33 | 29 |
| St. Louis-Farmington | Missouri | St. Francois | 79 | 7086 | 37 | 39 | 41 |
| Missouri non-MSA | Missouri | Taney | 60 | 4168 | 34 | 29 | 24 |
| Columbia-Jefferson City | Missouri | Cole | 101 | 8098 | 32 | 35 | 36 |
| St. Louis-Farmington | Illinois | Clinton | 83 | 4910 | 30 | 30 | 31 |
| St. Joseph | Missouri | Buchanan | 110 | 6453 | 30 | 31 | 29 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 106 | 6930 | 29 | 33 | 36 |
| Missouri non-MSA | Missouri | Pulaski | 33 | 2828 | 28 | 20 | 22 |
| Missouri non-MSA | Missouri | Pettis | 68 | 4420 | 27 | 25 | 28 |
| St. Louis-Farmington | Illinois | Monroe | 67 | 3495 | 26 | 25 | 29 |
| Kansas City | Kansas | Miami | 17 | 2178 | 25 | 25 | 25 |
| Springfield | Missouri | Webster | 44 | 2741 | 24 | 22 | 20 |
| Missouri non-MSA | Missouri | Camden | 66 | 3461 | 22 | 22 | 21 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3496 | 22 | 20 | 18 |
| Kansas City | Missouri | Platte | 26 | 2737 | 21 | 22 | 24 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 3853 | 21 | 22 | 25 |
| Joplin | Missouri | Newton | 60 | 3765 | 21 | 21 | 19 |
| Missouri non-MSA | Missouri | Howell | 40 | 2611 | 20 | 21 | 17 |
| Columbia-Jefferson City | Missouri | Callaway | 29 | 4101 | 19 | 23 | 25 |
| Missouri non-MSA | Missouri | Phelps | 103 | 2745 | 18 | 18 | 20 |
| Missouri non-MSA | Missouri | Butler | 17 | 3034 | 17 | 16 | 14 |
| Missouri non-MSA | Missouri | Adair | 6 | 1836 | 16 | 17 | 17 |
| Missouri non-MSA | Missouri | Lawrence | 60 | 2546 | 16 | 18 | 14 |
| Missouri non-MSA | Missouri | Barry | 37 | 1974 | 14 | 13 | 11 |
| Cape Girardeau-Sikeston | Missouri | Scott | 68 | 3547 | 14 | 15 | 15 |
| Missouri non-MSA | Missouri | Stone | 28 | 1807 | 14 | 13 | 13 |
| Springfield | Missouri | Polk | 25 | 2005 | 13 | 15 | 12 |
| Missouri non-MSA | Missouri | Saline | 26 | 2209 | 13 | 15 | 14 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2247 | 13 | 11 | 12 |
| Kansas City | Missouri | Lafayette | 44 | 2261 | 13 | 14 | 15 |
| Missouri non-MSA | Missouri | Laclede | 54 | 2706 | 13 | 15 | 15 |
| Missouri non-MSA | Missouri | Crawford | 21 | 1887 | 13 | 12 | 15 |
| St. Louis-Farmington | Illinois | Jersey | 52 | 2158 | 12 | 13 | 16 |
| St. Louis-Farmington | Missouri | Warren | 11 | 1833 | 12 | 13 | 13 |
| Missouri non-MSA | Missouri | Vernon | 29 | 1257 | 12 | 12 | 14 |
| Missouri non-MSA | Missouri | Washington | 41 | 1955 | 12 | 12 | 11 |
| St. Louis-Farmington | Illinois | Bond | 23 | 1715 | 11 | 11 | 12 |
| Missouri non-MSA | Missouri | Randolph | 20 | 1738 | 11 | 9 | 9 |
| Missouri non-MSA | Missouri | Wright | 24 | 1235 | 11 | 11 | 11 |
| Missouri non-MSA | Missouri | McDonald | 23 | 1788 | 10 | 9 | 8 |
| Missouri non-MSA | Missouri | Miller | 44 | 2196 | 10 | 12 | 13 |
| Missouri non-MSA | Missouri | Livingston | 25 | 1167 | 10 | 9 | 9 |
| Missouri non-MSA | Missouri | Marion | 32 | 2494 | 10 | 11 | 12 |
| Kansas City | Missouri | Clinton | 60 | 1392 | 10 | 10 | 9 |
| Missouri non-MSA | Missouri | Audrain | 43 | 1928 | 10 | 9 | 18 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2133 | 10 | 8 | 7 |
| Missouri non-MSA | Missouri | Henry | 25 | 1565 | 9 | 9 | 9 |
| Kansas City | Missouri | Ray | 11 | 1279 | 9 | 11 | 12 |
| Missouri non-MSA | Missouri | Barton | 9 | 867 | 9 | 7 | 5 |
| Missouri non-MSA | Missouri | Macon | 10 | 1038 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Pike | 17 | 1372 | 8 | 6 | 8 |
| St. Joseph | Kansas | Doniphan | 10 | 819 | 8 | 6 | 7 |
| Kansas City | Kansas | Linn | 4 | 634 | 7 | 8 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 24 | 1605 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Harrison | 10 | 711 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Morgan | 31 | 1553 | 7 | 7 | 8 |
| Kansas City | Missouri | Bates | 14 | 953 | 7 | 8 | 9 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17460 | 6 | 30 | 75 |
| Missouri non-MSA | Missouri | Ozark | 5 | 450 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Texas | 20 | 1451 | 6 | 8 | 9 |
| Missouri non-MSA | Missouri | Grundy | 28 | 759 | 6 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Osage | 9 | 1284 | 6 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1576 | 6 | 5 | 7 |
| Missouri non-MSA | Missouri | Ripley | 9 | 740 | 6 | 4 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2457 | 6 | 12 | 8 |
| St. Joseph | Missouri | Andrew | 15 | 1198 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 31 | 769 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Douglas | 20 | 697 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Linn | 11 | 473 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Benton | 19 | 1321 | 5 | 9 | 8 |
| Missouri non-MSA | Missouri | Carroll | 18 | 726 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 11 | 1507 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Cedar | 9 | 595 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Perry | 21 | 1939 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Daviess | 9 | 525 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 39 | 1694 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Madison | 11 | 1285 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Wayne | 9 | 735 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1340 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Oregon | 3 | 624 | 4 | 6 | 4 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 430 | 4 | 3 | 2 |
| Springfield | Missouri | Dallas | 19 | 744 | 3 | 3 | 3 |
| St. Joseph | Missouri | DeKalb | 21 | 841 | 3 | 4 | 4 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1006 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Lewis | 3 | 591 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Dent | 9 | 751 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 11 | 705 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Gentry | 16 | 669 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Iron | 1 | 446 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 507 | 3 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 664 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Chariton | 3 | 375 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 20 | 1175 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 236 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ralls | 9 | 713 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Clark | 5 | 400 | 2 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 376 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 540 | 2 | 3 | 3 |
| Kansas City | Missouri | Caldwell | 7 | 589 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 443 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Monroe | 7 | 560 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Dade | 10 | 392 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Maries | 7 | 494 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Mercer | 2 | 152 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 248 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 4 | 323 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Carter | 7 | 399 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 343 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 9 | 449 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 6 | 285 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 130 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 160 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 206 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 234 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
* 1/4/2021: small fix for including 2021 data
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
