# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 03/10/2021  
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
| St. Louis-Farmington | 4734 | 259024 | 289 | 314 | 379 |
| Kansas City | 2552 | 177476 | 174 | 196 | 290 |
| Missouri non-MSA | 2088 | 110605 | 72 | 80 | 95 |
| Springfield | 633 | 36539 | 30 | 33 | 40 |
| Columbia-Jefferson City | 327 | 34602 | 16 | 19 | 25 |
| Joplin | 295 | 16384 | 10 | 11 | 16 |
| St. Joseph | 203 | 10143 | 5 | 5 | 6 |
| Cape Girardeau-Sikeston | 231 | 12892 | 4 | 7 | 10 |
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
| St. Louis-Farmington | Missouri | St. Louis | 2039 | 89599 | 136 | 132 | 147 |
| Kansas City | Kansas | Johnson | 747 | 54889 | 74 | 84 | 132 |
| St. Louis-Farmington | Illinois | St. Clair | 471 | 25816 | 41 | 45 | 49 |
| St. Louis-Farmington | Illinois | Madison | 467 | 28324 | 37 | 43 | 49 |
| Kansas City | Missouri | Kansas City | 541 | 36866 | 24 | 19 | 27 |
| St. Louis-Farmington | Missouri | St. Charles | 436 | 33137 | 23 | 27 | 39 |
| Kansas City | Missouri | Jackson | 391 | 30320 | 21 | 26 | 43 |
| Springfield | Missouri | Greene | 441 | 23589 | 18 | 22 | 28 |
| Kansas City | Kansas | Wyandotte | 270 | 19337 | 16 | 21 | 30 |
| St. Louis-Farmington | Missouri | Jefferson | 229 | 19098 | 12 | 13 | 18 |
| Kansas City | Kansas | Leavenworth | 83 | 6857 | 10 | 10 | 15 |
| St. Louis-Farmington | Missouri | St. Louis City | 425 | 21544 | 9 | 18 | 28 |
| Kansas City | Missouri | Cass | 92 | 7318 | 9 | 9 | 10 |
| Missouri non-MSA | Missouri | Butler | 37 | 3568 | 8 | 9 | 9 |
| Kansas City | Missouri | Clay | 153 | 7963 | 7 | 8 | 10 |
| Columbia-Jefferson City | Missouri | Boone | 84 | 15956 | 7 | 8 | 12 |
| Joplin | Missouri | Jasper | 226 | 12281 | 7 | 9 | 12 |
| St. Louis-Farmington | Missouri | Franklin | 168 | 8470 | 6 | 6 | 10 |
| Springfield | Missouri | Christian | 84 | 6918 | 5 | 5 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 80 | 4398 | 5 | 5 | 6 |
| St. Louis-Farmington | Missouri | Lincoln | 39 | 4332 | 4 | 4 | 6 |
| Springfield | Missouri | Polk | 31 | 2201 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Johnson | 47 | 3894 | 4 | 3 | 4 |
| Columbia-Jefferson City | Missouri | Cole | 120 | 8614 | 4 | 4 | 5 |
| St. Louis-Farmington | Missouri | St. Francois | 109 | 7616 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Pettis | 77 | 4815 | 4 | 3 | 4 |
| St. Joseph | Missouri | Buchanan | 136 | 6983 | 3 | 3 | 4 |
| Kansas City | Missouri | Lafayette | 57 | 2596 | 3 | 4 | 4 |
| Kansas City | Missouri | Platte | 44 | 3145 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Phelps | 123 | 3046 | 3 | 3 | 3 |
| St. Louis-Farmington | Illinois | Monroe | 89 | 4095 | 3 | 4 | 5 |
| Joplin | Missouri | Newton | 69 | 4103 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Crawford | 34 | 2070 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 8 | 602 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Callaway | 46 | 4515 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Taney | 91 | 4608 | 2 | 3 | 4 |
| Cape Girardeau-Sikeston | Missouri | Scott | 79 | 3853 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Stoddard | 37 | 2325 | 2 | 2 | 1 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 131 | 7532 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Vernon | 40 | 1405 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 30 | 1825 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Howell | 42 | 2835 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Marion | 42 | 2657 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Camden | 82 | 3739 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Adair | 18 | 2087 | 1 | 2 | 2 |
| St. Louis-Farmington | Missouri | Warren | 20 | 2108 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Lawrence | 77 | 2773 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Stone | 39 | 2040 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Miller | 51 | 2326 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Laclede | 66 | 2933 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | New Madrid | 45 | 1776 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | McDonald | 26 | 1933 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 42 | 888 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 38 | 1751 | 1 | 1 | 2 |
| St. Louis-Farmington | Illinois | Clinton | 89 | 5583 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Morgan | 42 | 1632 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Saline | 39 | 2436 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 5 | 282 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Perry | 27 | 2057 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Barry | 45 | 2202 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 49 | 2997 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Audrain | 57 | 2082 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 14 | 1411 | 1 | 1 | 1 |
| Kansas City | Missouri | Ray | 25 | 1525 | 1 | 1 | 2 |
| Kansas City | Kansas | Linn | 8 | 756 | 1 | 0 | 1 |
| St. Joseph | Kansas | Doniphan | 22 | 948 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 12 | 974 | 0 | 1 | 1 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1918 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Benton | 27 | 1459 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Macon | 15 | 1216 | 0 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 484 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 7 | 541 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 15 | 1623 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Pike | 23 | 1493 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 47 | 2502 | 0 | 1 | 3 |
| Kansas City | Kansas | Miami | 41 | 2642 | 0 | 3 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 7 | 726 | 0 | 0 | 0 |
| Kansas City | Missouri | Bates | 24 | 1090 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 27 | 774 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 14 | 859 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 25 | 1276 | 0 | 1 | 1 |
| Springfield | Missouri | Webster | 53 | 3000 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 572 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 29 | 1369 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 27 | 925 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dunklin | 19 | 2416 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carroll | 23 | 838 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 9 | 428 | 0 | 0 | 0 |
| Kansas City | Missouri | Clinton | 65 | 1529 | 0 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Cooper | 27 | 1698 | 0 | 0 | 1 |
| Springfield | Missouri | Dallas | 24 | 831 | 0 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 18 | 1287 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Texas | 22 | 1546 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 7 | 357 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 9 | 453 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 16 | 1348 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Nodaway | 25 | 2580 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Oregon | 3 | 679 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 16 | 553 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 10 | 633 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 17 | 823 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 180 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 11 | 822 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 11 | 643 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 19 | 706 | 0 | 2 | 1 |
| Missouri non-MSA | Missouri | Chariton | 6 | 425 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 12 | 547 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 11 | 599 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 369 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 29 | 1682 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 12 | 759 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 143 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1054 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 14 | 748 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 11 | 588 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 34 | 830 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 261 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 12 | 483 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 21 | 734 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 263 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 5 | 465 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Washington | 48 | 2122 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 14 | 467 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 6 | 472 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 37 | 1331 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 179 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 4 | 225 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Pemiscot | 29 | 1413 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 14 | 420 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 14 | 823 | 0 | 0 | 0 |
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
