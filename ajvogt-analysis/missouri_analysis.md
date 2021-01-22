# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/22/2021  
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
| St. Louis-Farmington | 3907 | 231194 | 1135 | 1323 | 1393 |
| Kansas City | 1995 | 157912 | 892 | 1052 | 1068 |
| Missouri non-MSA | 1641 | 103416 | 347 | 487 | 545 |
| Springfield | 488 | 33574 | 119 | 186 | 206 |
| Columbia-Jefferson City | 255 | 32445 | 90 | 121 | 149 |
| Joplin | 242 | 15035 | 52 | 67 | 75 |
| Cape Girardeau-Sikeston | 195 | 12083 | 32 | 40 | 49 |
| St. Joseph | 167 | 9528 | 31 | 39 | 43 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1619 | 79875 | 402 | 470 | 486 |
| Kansas City | Kansas | Johnson | 618 | 47051 | 386 | 406 | 369 |
| St. Louis-Farmington | Illinois | Madison | 471 | 24822 | 165 | 183 | 175 |
| St. Louis-Farmington | Illinois | St. Clair | 433 | 22624 | 146 | 162 | 162 |
| Kansas City | Missouri | Kansas City | 421 | 34147 | 131 | 174 | 191 |
| Kansas City | Missouri | Jackson | 292 | 27046 | 125 | 166 | 172 |
| St. Louis-Farmington | Missouri | St. Charles | 332 | 30679 | 123 | 158 | 167 |
| St. Louis-Farmington | Missouri | Jefferson | 165 | 17562 | 84 | 106 | 113 |
| Springfield | Missouri | Greene | 337 | 21606 | 78 | 120 | 132 |
| Kansas City | Kansas | Wyandotte | 222 | 17568 | 75 | 91 | 109 |
| Columbia-Jefferson City | Missouri | Boone | 58 | 14839 | 51 | 64 | 75 |
| Joplin | Missouri | Jasper | 182 | 11205 | 42 | 52 | 57 |
| Kansas City | Kansas | Leavenworth | 51 | 5866 | 41 | 41 | 36 |
| St. Louis-Farmington | Missouri | Franklin | 127 | 7754 | 41 | 53 | 54 |
| Kansas City | Missouri | Cass | 68 | 6538 | 33 | 47 | 46 |
| St. Louis-Farmington | Missouri | St. Louis City | 303 | 17679 | 31 | 19 | 52 |
| Kansas City | Missouri | Clay | 120 | 7190 | 29 | 41 | 45 |
| St. Louis-Farmington | Illinois | Clinton | 86 | 5107 | 28 | 29 | 29 |
| St. Louis-Farmington | Illinois | Macoupin | 96 | 3913 | 24 | 32 | 28 |
| Springfield | Missouri | Christian | 61 | 6355 | 24 | 37 | 41 |
| Kansas City | Kansas | Miami | 22 | 2343 | 23 | 24 | 25 |
| St. Louis-Farmington | Missouri | St. Francois | 81 | 7226 | 20 | 28 | 35 |
| St. Joseph | Missouri | Buchanan | 117 | 6593 | 20 | 25 | 26 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 108 | 7065 | 19 | 24 | 30 |
| St. Louis-Farmington | Illinois | Monroe | 71 | 3628 | 19 | 22 | 25 |
| Columbia-Jefferson City | Missouri | Cole | 104 | 8200 | 14 | 23 | 30 |
| St. Louis-Farmington | Illinois | Jersey | 59 | 2258 | 14 | 13 | 14 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 3952 | 14 | 17 | 21 |
| Missouri non-MSA | Missouri | Butler | 22 | 3133 | 14 | 15 | 15 |
| Missouri non-MSA | Missouri | Taney | 68 | 4265 | 13 | 24 | 22 |
| Springfield | Missouri | Webster | 45 | 2827 | 12 | 18 | 18 |
| Missouri non-MSA | Missouri | Pettis | 68 | 4505 | 12 | 20 | 22 |
| Missouri non-MSA | Missouri | Phelps | 107 | 2828 | 11 | 15 | 18 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3578 | 11 | 17 | 17 |
| Kansas City | Missouri | Platte | 33 | 2815 | 11 | 16 | 21 |
| Missouri non-MSA | Missouri | Barry | 40 | 2051 | 11 | 12 | 10 |
| Missouri non-MSA | Missouri | Adair | 7 | 1913 | 11 | 13 | 15 |
| Missouri non-MSA | Missouri | Camden | 69 | 3535 | 10 | 16 | 19 |
| St. Louis-Farmington | Missouri | Warren | 12 | 1907 | 10 | 11 | 12 |
| Joplin | Missouri | Newton | 60 | 3830 | 9 | 15 | 17 |
| Kansas City | Missouri | Lafayette | 45 | 2326 | 9 | 11 | 12 |
| Missouri non-MSA | Missouri | Saline | 28 | 2270 | 8 | 11 | 12 |
| Cape Girardeau-Sikeston | Missouri | Scott | 68 | 3608 | 8 | 11 | 13 |
| Columbia-Jefferson City | Missouri | Callaway | 32 | 4162 | 8 | 14 | 21 |
| Missouri non-MSA | Missouri | Washington | 41 | 2012 | 8 | 10 | 10 |
| Missouri non-MSA | Missouri | Howell | 41 | 2668 | 8 | 14 | 16 |
| Kansas City | Missouri | Ray | 15 | 1336 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | Macon | 10 | 1093 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Laclede | 54 | 2760 | 7 | 10 | 12 |
| Missouri non-MSA | Missouri | Stone | 29 | 1859 | 7 | 10 | 11 |
| Missouri non-MSA | Missouri | McDonald | 23 | 1839 | 7 | 9 | 8 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1762 | 6 | 9 | 10 |
| Missouri non-MSA | Missouri | Wright | 24 | 1281 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Ozark | 5 | 494 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2291 | 6 | 9 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 33 | 2871 | 6 | 17 | 17 |
| Missouri non-MSA | Missouri | Livingston | 25 | 1209 | 6 | 8 | 8 |
| Missouri non-MSA | Missouri | Crawford | 23 | 1928 | 5 | 9 | 12 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1617 | 5 | 6 | 6 |
| Kansas City | Missouri | Clinton | 60 | 1432 | 5 | 7 | 8 |
| Missouri non-MSA | Missouri | Vernon | 31 | 1297 | 5 | 9 | 13 |
| Missouri non-MSA | Missouri | Randolph | 20 | 1778 | 5 | 8 | 8 |
| Missouri non-MSA | Missouri | Gasconade | 32 | 808 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Marion | 34 | 2532 | 5 | 7 | 10 |
| Missouri non-MSA | Missouri | Pike | 17 | 1409 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2170 | 5 | 7 | 6 |
| Missouri non-MSA | Missouri | Miller | 45 | 2232 | 5 | 7 | 10 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2492 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Benton | 19 | 1355 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Harrison | 10 | 744 | 4 | 6 | 5 |
| Kansas City | Missouri | Bates | 15 | 986 | 4 | 6 | 8 |
| Columbia-Jefferson City | Missouri | Osage | 9 | 1316 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Lawrence | 61 | 2578 | 4 | 10 | 12 |
| Kansas City | Kansas | Linn | 5 | 666 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Wayne | 9 | 766 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Perry | 22 | 1969 | 4 | 4 | 5 |
| St. Joseph | Kansas | Doniphan | 11 | 849 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Audrain | 47 | 1958 | 4 | 7 | 14 |
| Missouri non-MSA | Missouri | Henry | 26 | 1594 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Douglas | 21 | 724 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 40 | 1721 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Sullivan | 12 | 731 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Texas | 20 | 1477 | 3 | 5 | 7 |
| St. Joseph | Missouri | DeKalb | 23 | 867 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Clark | 5 | 426 | 3 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1630 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Grundy | 30 | 784 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Dent | 10 | 774 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Cedar | 9 | 617 | 3 | 4 | 4 |
| St. Joseph | Missouri | Andrew | 16 | 1219 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Madison | 13 | 1305 | 2 | 3 | 6 |
| Missouri non-MSA | Missouri | Barton | 9 | 887 | 2 | 6 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1360 | 2 | 3 | 4 |
| Springfield | Missouri | Polk | 25 | 2024 | 2 | 8 | 9 |
| Missouri non-MSA | Missouri | Carroll | 18 | 745 | 2 | 4 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 395 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 10 | 492 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Chariton | 3 | 393 | 2 | 2 | 3 |
| Springfield | Missouri | Dallas | 20 | 762 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Lewis | 3 | 609 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Gentry | 18 | 687 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Morgan | 31 | 1571 | 2 | 5 | 6 |
| Missouri non-MSA | Missouri | Oregon | 3 | 642 | 2 | 3 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 681 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 12 | 1524 | 2 | 3 | 6 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 446 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 20 | 1191 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Maries | 7 | 509 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ripley | 10 | 754 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 250 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 10 | 538 | 1 | 3 | 3 |
| Kansas City | Missouri | Caldwell | 8 | 602 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 6 | 519 | 1 | 2 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1015 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 5 | 332 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 548 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 256 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 9 | 721 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Carter | 7 | 406 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 450 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 12 | 399 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 213 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 1 | 453 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Hickory | 10 | 455 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Holt | 10 | 349 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 7 | 565 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 2 | 165 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 156 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 132 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 235 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 286 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
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
