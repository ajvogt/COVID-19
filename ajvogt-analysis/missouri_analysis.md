# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/17/2021  
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
County populations are pulled from this 
[JHU CSSE repository file](https://github.com/ajvogt/COVID-19/blob/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv).

## Missouri New Daily Confirmed Cases by Metropolitan Statistcal Areas
![](images/mo_daily_cases.png)

## Missouri New Daily Deaths by Metropolitan Statistcal Areas
![](images/mo_daily_deaths.png)

## Missouri Cumulative Deaths by Metropolitan Statistcal Areas
![](images/mo_cumulative_deaths.png)

## Missouri Metropolitan Statistical Area Totals
<!-- msa_table start -->
| MSA | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|
| St. Louis-Farmington | 3788 | 225785 | 1285 | 1484 | 1480 |
| Kansas City | 1905 | 153551 | 1014 | 1101 | 1106 |
| Missouri non-MSA | 1583 | 101886 | 492 | 576 | 597 |
| Springfield | 482 | 33004 | 177 | 229 | 224 |
| Columbia-Jefferson City | 244 | 32061 | 128 | 148 | 165 |
| Joplin | 242 | 14781 | 67 | 77 | 77 |
| Cape Girardeau-Sikeston | 193 | 11976 | 45 | 55 | 56 |
| St. Joseph | 160 | 9419 | 42 | 48 | 48 |
<!-- msa_table end -->

## STL-Farmington MSA New Daily Confirmed Cases by County
![](images/stl_daily_cases.png)

## STL-Farmington MSA New Daily Deaths by County
![](images/stl_daily_deaths.png)

## STL-Farmington MSA Cumulative Deaths by County
![](images/stl_cumulative_deaths.png)

<a name="msa-counties"></a>
## Metropolitan Statistical Area (MSA) Counties
<!-- county_table start -->
| MSA | State | County | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|---|---|
| St. Louis-Farmington | Missouri | St. Louis | 1563 | 78024 | 468 | 544 | 516 |
| Kansas City | Kansas | Johnson | 600 | 44973 | 359 | 376 | 366 |
| Kansas City | Missouri | Jackson | 283 | 26508 | 189 | 191 | 180 |
| St. Louis-Farmington | Illinois | Madison | 461 | 23998 | 173 | 184 | 176 |
| St. Louis-Farmington | Illinois | St. Clair | 424 | 21943 | 161 | 176 | 161 |
| Kansas City | Missouri | Kansas City | 382 | 33556 | 158 | 205 | 203 |
| St. Louis-Farmington | Missouri | St. Charles | 315 | 30094 | 155 | 181 | 187 |
| Springfield | Missouri | Greene | 333 | 21232 | 114 | 148 | 143 |
| St. Louis-Farmington | Missouri | Jefferson | 154 | 17175 | 106 | 127 | 119 |
| Kansas City | Kansas | Wyandotte | 220 | 17217 | 91 | 94 | 112 |
| Columbia-Jefferson City | Missouri | Boone | 54 | 14606 | 63 | 72 | 80 |
| Kansas City | Missouri | Cass | 62 | 6401 | 53 | 52 | 51 |
| St. Louis-Farmington | Missouri | Franklin | 122 | 7560 | 52 | 60 | 57 |
| Joplin | Missouri | Jasper | 182 | 10997 | 51 | 58 | 57 |
| Kansas City | Missouri | Clay | 118 | 7065 | 45 | 48 | 48 |
| Kansas City | Kansas | Leavenworth | 51 | 5666 | 38 | 39 | 37 |
| St. Louis-Farmington | Illinois | Macoupin | 94 | 3795 | 35 | 34 | 29 |
| Springfield | Missouri | Christian | 60 | 6236 | 33 | 44 | 46 |
| St. Louis-Farmington | Illinois | Clinton | 85 | 4979 | 28 | 32 | 30 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 106 | 7001 | 27 | 33 | 35 |
| St. Joseph | Missouri | Buchanan | 113 | 6523 | 27 | 30 | 29 |
| St. Louis-Farmington | Missouri | St. Francois | 79 | 7135 | 24 | 35 | 40 |
| Columbia-Jefferson City | Missouri | Cole | 101 | 8145 | 24 | 31 | 35 |
| Missouri non-MSA | Missouri | Taney | 60 | 4188 | 23 | 25 | 23 |
| St. Louis-Farmington | Illinois | Monroe | 70 | 3533 | 21 | 24 | 27 |
| Missouri non-MSA | Missouri | Pettis | 68 | 4454 | 20 | 24 | 24 |
| Kansas City | Missouri | Platte | 27 | 2771 | 20 | 21 | 23 |
| Missouri non-MSA | Missouri | Phelps | 103 | 2774 | 18 | 16 | 19 |
| Kansas City | Kansas | Miami | 19 | 2209 | 18 | 23 | 25 |
| Springfield | Missouri | Webster | 45 | 2778 | 17 | 21 | 20 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 3882 | 17 | 21 | 24 |
| Missouri non-MSA | Missouri | Howell | 41 | 2633 | 17 | 18 | 17 |
| Columbia-Jefferson City | Missouri | Callaway | 29 | 4128 | 16 | 20 | 24 |
| Missouri non-MSA | Missouri | Camden | 66 | 3487 | 16 | 20 | 20 |
| Joplin | Missouri | Newton | 60 | 3784 | 15 | 18 | 19 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3515 | 15 | 17 | 18 |
| Missouri non-MSA | Missouri | Adair | 6 | 1867 | 15 | 16 | 16 |
| Missouri non-MSA | Missouri | Barry | 38 | 2020 | 14 | 14 | 11 |
| Missouri non-MSA | Missouri | Butler | 18 | 3071 | 13 | 15 | 15 |
| Cape Girardeau-Sikeston | Missouri | Scott | 68 | 3579 | 12 | 15 | 15 |
| St. Louis-Farmington | Illinois | Jersey | 56 | 2184 | 12 | 13 | 15 |
| Missouri non-MSA | Missouri | Stone | 28 | 1828 | 11 | 12 | 12 |
| Missouri non-MSA | Missouri | Saline | 26 | 2231 | 10 | 12 | 13 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2259 | 10 | 11 | 9 |
| Missouri non-MSA | Missouri | Washington | 41 | 1979 | 10 | 12 | 11 |
| St. Louis-Farmington | Missouri | Warren | 11 | 1856 | 10 | 12 | 13 |
| Missouri non-MSA | Missouri | Laclede | 54 | 2723 | 10 | 13 | 14 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1726 | 10 | 11 | 11 |
| Missouri non-MSA | Missouri | Pulaski | 33 | 2841 | 10 | 18 | 21 |
| Kansas City | Missouri | Lafayette | 44 | 2272 | 9 | 11 | 15 |
| Missouri non-MSA | Missouri | Randolph | 20 | 1753 | 9 | 9 | 9 |
| Missouri non-MSA | Missouri | McDonald | 23 | 1812 | 9 | 9 | 9 |
| Missouri non-MSA | Missouri | Miller | 44 | 2212 | 9 | 11 | 12 |
| Missouri non-MSA | Missouri | Crawford | 21 | 1906 | 9 | 11 | 14 |
| Springfield | Missouri | Polk | 25 | 2012 | 9 | 11 | 11 |
| Missouri non-MSA | Missouri | Livingston | 25 | 1181 | 9 | 9 | 8 |
| Missouri non-MSA | Missouri | Ozark | 5 | 480 | 8 | 6 | 4 |
| Missouri non-MSA | Missouri | Wright | 24 | 1255 | 8 | 10 | 10 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1601 | 8 | 7 | 7 |
| Kansas City | Missouri | Ray | 13 | 1300 | 8 | 10 | 12 |
| Missouri non-MSA | Missouri | Vernon | 30 | 1272 | 8 | 10 | 13 |
| Missouri non-MSA | Missouri | Marion | 32 | 2509 | 8 | 9 | 11 |
| Missouri non-MSA | Missouri | Henry | 25 | 1575 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Pike | 17 | 1391 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2148 | 7 | 8 | 7 |
| Kansas City | Missouri | Clinton | 60 | 1412 | 7 | 9 | 9 |
| Missouri non-MSA | Missouri | Gasconade | 31 | 787 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Audrain | 44 | 1943 | 7 | 8 | 17 |
| Missouri non-MSA | Missouri | Macon | 10 | 1054 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Harrison | 10 | 721 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Barton | 9 | 878 | 6 | 7 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 60 | 2534 | 6 | 12 | 12 |
| Columbia-Jefferson City | Missouri | Moniteau | 26 | 1611 | 6 | 6 | 7 |
| St. Joseph | Kansas | Doniphan | 10 | 836 | 6 | 7 | 7 |
| Kansas City | Missouri | Bates | 14 | 963 | 6 | 7 | 8 |
| Columbia-Jefferson City | Missouri | Osage | 9 | 1299 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Morgan | 31 | 1564 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Texas | 20 | 1464 | 5 | 6 | 9 |
| Kansas City | Kansas | Linn | 5 | 642 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Grundy | 28 | 770 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Ripley | 9 | 745 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Benton | 19 | 1335 | 5 | 8 | 7 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2457 | 5 | 12 | 7 |
| Missouri non-MSA | Missouri | Wayne | 9 | 745 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Douglas | 20 | 709 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Cedar | 9 | 607 | 4 | 4 | 4 |
| St. Joseph | Missouri | Andrew | 16 | 1205 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Perry | 21 | 1952 | 4 | 6 | 6 |
| St. Joseph | Missouri | DeKalb | 21 | 855 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 11 | 1515 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Linn | 11 | 482 | 4 | 5 | 3 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17464 | 3 | 18 | 66 |
| Missouri non-MSA | Missouri | Carroll | 18 | 730 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Oregon | 3 | 631 | 3 | 6 | 4 |
| Missouri non-MSA | Missouri | Lewis | 3 | 601 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Clark | 5 | 410 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 39 | 1701 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Gentry | 16 | 674 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Dent | 9 | 759 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Chariton | 3 | 379 | 3 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 671 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1348 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Daviess | 10 | 529 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Madison | 11 | 1287 | 3 | 4 | 7 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 437 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 12 | 716 | 3 | 3 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 384 | 2 | 2 | 2 |
| Springfield | Missouri | Dallas | 19 | 746 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 511 | 2 | 2 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1012 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Maries | 7 | 501 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Iron | 1 | 452 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 449 | 2 | 2 | 2 |
| Kansas City | Missouri | Caldwell | 7 | 596 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 544 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dade | 10 | 394 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 252 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 20 | 1177 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Monroe | 7 | 562 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Ralls | 9 | 716 | 1 | 3 | 4 |
| Missouri non-MSA | Missouri | Mercer | 2 | 154 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 4 | 326 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 237 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 9 | 454 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 346 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 7 | 402 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 6 | 286 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 161 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 131 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 206 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 234 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
* 1/17/2021: including cumulative deaths plots
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

### To-Do (updated 1/17/2021)
- [ ] Verify county population data

#### Analysis Page
- [x] Update description to accurately reflect CSA vs. MSA
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
