# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 03/07/2021  
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
| St. Louis-Farmington | 4688 | 258340 | 311 | 331 | 421 |
| Kansas City | 2530 | 177094 | 179 | 202 | 322 |
| Missouri non-MSA | 2059 | 110427 | 63 | 83 | 109 |
| Springfield | 624 | 36473 | 32 | 36 | 46 |
| Columbia-Jefferson City | 324 | 34556 | 15 | 20 | 31 |
| Joplin | 293 | 16358 | 8 | 13 | 19 |
| Cape Girardeau-Sikeston | 226 | 12883 | 5 | 7 | 14 |
| St. Joseph | 203 | 10131 | 5 | 6 | 7 |
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
| St. Louis-Farmington | Missouri | St. Louis | 2019 | 89278 | 140 | 138 | 158 |
| Kansas City | Kansas | Johnson | 743 | 54730 | 72 | 77 | 144 |
| St. Louis-Farmington | Illinois | St. Clair | 471 | 25714 | 46 | 46 | 55 |
| St. Louis-Farmington | Illinois | Madison | 464 | 28231 | 40 | 43 | 55 |
| St. Louis-Farmington | Missouri | St. Charles | 428 | 33076 | 23 | 29 | 43 |
| Kansas City | Missouri | Kansas City | 530 | 36799 | 22 | 19 | 30 |
| Kansas City | Missouri | Jackson | 388 | 30275 | 22 | 30 | 49 |
| Springfield | Missouri | Greene | 436 | 23547 | 22 | 25 | 31 |
| St. Louis-Farmington | Missouri | St. Louis City | 425 | 21544 | 22 | 24 | 33 |
| Kansas City | Kansas | Wyandotte | 270 | 19307 | 20 | 26 | 33 |
| St. Louis-Farmington | Missouri | Jefferson | 223 | 19065 | 11 | 15 | 21 |
| Kansas City | Kansas | Leavenworth | 83 | 6833 | 9 | 10 | 17 |
| Kansas City | Missouri | Clay | 151 | 7950 | 8 | 10 | 12 |
| Kansas City | Missouri | Cass | 91 | 7293 | 7 | 9 | 11 |
| Joplin | Missouri | Jasper | 224 | 12267 | 6 | 11 | 15 |
| Missouri non-MSA | Missouri | Butler | 35 | 3545 | 6 | 9 | 9 |
| Columbia-Jefferson City | Missouri | Boone | 84 | 15937 | 6 | 9 | 16 |
| St. Louis-Farmington | Missouri | Franklin | 164 | 8455 | 5 | 7 | 11 |
| Columbia-Jefferson City | Missouri | Cole | 118 | 8605 | 4 | 4 | 6 |
| Kansas City | Missouri | Lafayette | 57 | 2585 | 4 | 4 | 4 |
| St. Louis-Farmington | Illinois | Macoupin | 80 | 4379 | 4 | 4 | 6 |
| Springfield | Missouri | Christian | 80 | 6905 | 4 | 6 | 8 |
| Springfield | Missouri | Polk | 31 | 2192 | 4 | 4 | 3 |
| St. Louis-Farmington | Missouri | Lincoln | 39 | 4320 | 3 | 4 | 6 |
| St. Louis-Farmington | Illinois | Monroe | 87 | 4090 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Pettis | 75 | 4811 | 3 | 4 | 4 |
| St. Joseph | Missouri | Buchanan | 136 | 6975 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 25 | 2580 | 3 | 1 | 1 |
| Kansas City | Missouri | Platte | 43 | 3136 | 3 | 4 | 5 |
| Kansas City | Kansas | Miami | 42 | 2650 | 3 | 4 | 4 |
| St. Louis-Farmington | Missouri | St. Francois | 107 | 7605 | 2 | 4 | 6 |
| Missouri non-MSA | Missouri | Taney | 90 | 4603 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Howell | 42 | 2834 | 2 | 3 | 2 |
| Cape Girardeau-Sikeston | Missouri | Scott | 77 | 3846 | 2 | 3 | 5 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 128 | 7530 | 2 | 3 | 7 |
| Missouri non-MSA | Missouri | Phelps | 121 | 3033 | 2 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Callaway | 45 | 4506 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Crawford | 32 | 2063 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2323 | 2 | 2 | 2 |
| Joplin | Missouri | Newton | 69 | 4091 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Schuyler | 5 | 280 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Saline | 38 | 2435 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | McDonald | 26 | 1932 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Camden | 81 | 3734 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 593 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Barton | 12 | 973 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 42 | 1632 | 1 | 0 | 1 |
| St. Louis-Farmington | Illinois | Clinton | 89 | 5581 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | Barry | 45 | 2200 | 1 | 1 | 2 |
| St. Louis-Farmington | Missouri | Warren | 19 | 2104 | 1 | 1 | 3 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1917 | 1 | 2 | 3 |
| Kansas City | Kansas | Linn | 8 | 756 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Laclede | 66 | 2929 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Johnson | 45 | 3885 | 1 | 3 | 5 |
| Missouri non-MSA | Missouri | Miller | 49 | 2324 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Marion | 42 | 2654 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 37 | 1750 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Adair | 18 | 2084 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Randolph | 30 | 1821 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 41 | 884 | 1 | 0 | 1 |
| Kansas City | Missouri | Ray | 25 | 1523 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 24 | 1275 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 12 | 548 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lawrence | 76 | 2766 | 0 | 1 | 3 |
| Columbia-Jefferson City | Missouri | Osage | 14 | 1407 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 22 | 1491 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 9 | 453 | 0 | 0 | 1 |
| St. Joseph | Kansas | Doniphan | 22 | 945 | 0 | 1 | 1 |
| Kansas City | Missouri | Bates | 23 | 1087 | 0 | 1 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 47 | 2499 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Texas | 22 | 1546 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Vernon | 38 | 1400 | 0 | 1 | 1 |
| Springfield | Missouri | Dallas | 24 | 830 | 0 | 0 | 1 |
| St. Joseph | Missouri | DeKalb | 27 | 925 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 14 | 859 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Douglas | 26 | 773 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Benton | 27 | 1455 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Perry | 27 | 2054 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 49 | 2995 | 0 | 1 | 2 |
| Springfield | Missouri | Webster | 53 | 2999 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Stone | 38 | 2033 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Audrain | 57 | 2078 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 482 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 7 | 726 | 0 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 18 | 1286 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 16 | 553 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 15 | 1620 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Cedar | 19 | 705 | 0 | 2 | 1 |
| Missouri non-MSA | Missouri | Shelby | 7 | 357 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 11 | 822 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 570 | 0 | 0 | 0 |
| Kansas City | Missouri | Clinton | 65 | 1528 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Madison | 16 | 1348 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1054 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 12 | 483 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 6 | 424 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 14 | 748 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 17 | 822 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 29 | 1681 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 179 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 34 | 830 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 7 | 538 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 15 | 1213 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Lewis | 10 | 632 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 23 | 837 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 143 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 11 | 642 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 29 | 1365 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 261 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 14 | 420 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 367 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 10 | 598 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | New Madrid | 45 | 1770 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 11 | 588 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 9 | 425 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Pemiscot | 29 | 1413 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 3 | 677 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Cooper | 27 | 1694 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Clark | 6 | 472 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 5 | 465 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 12 | 759 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 3 | 225 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dunklin | 19 | 2413 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 21 | 734 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 37 | 1331 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Washington | 48 | 2122 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Hickory | 13 | 467 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 263 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 179 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 14 | 824 | 0 | 0 | 0 |
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
