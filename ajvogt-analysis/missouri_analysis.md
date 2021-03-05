# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 03/04/2021  
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
| St. Louis-Farmington | 4663 | 257361 | 335 | 354 | 471 |
| Kansas City | 2531 | 176591 | 192 | 296 | 347 |
| Missouri non-MSA | 2058 | 110170 | 80 | 89 | 125 |
| Springfield | 624 | 36365 | 36 | 37 | 52 |
| Columbia-Jefferson City | 324 | 34506 | 19 | 23 | 37 |
| Joplin | 289 | 16326 | 11 | 15 | 24 |
| Cape Girardeau-Sikeston | 225 | 12867 | 9 | 10 | 16 |
| St. Joseph | 203 | 10105 | 4 | 6 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 2007 | 88778 | 121 | 138 | 171 |
| Kansas City | Kansas | Johnson | 752 | 54533 | 75 | 139 | 150 |
| St. Louis-Farmington | Illinois | St. Clair | 468 | 25568 | 49 | 48 | 59 |
| St. Louis-Farmington | Illinois | Madison | 458 | 28108 | 47 | 46 | 61 |
| St. Louis-Farmington | Missouri | St. Louis City | 425 | 21544 | 37 | 32 | 42 |
| St. Louis-Farmington | Missouri | St. Charles | 428 | 33001 | 31 | 30 | 47 |
| Kansas City | Missouri | Jackson | 388 | 30193 | 26 | 41 | 57 |
| Springfield | Missouri | Greene | 436 | 23482 | 25 | 26 | 35 |
| Kansas City | Kansas | Wyandotte | 268 | 19280 | 24 | 34 | 35 |
| Kansas City | Missouri | Kansas City | 525 | 36729 | 17 | 24 | 34 |
| St. Louis-Farmington | Missouri | Jefferson | 223 | 19026 | 15 | 16 | 25 |
| Kansas City | Kansas | Leavenworth | 83 | 6810 | 10 | 12 | 18 |
| Kansas City | Missouri | Cass | 91 | 7267 | 10 | 9 | 12 |
| Kansas City | Missouri | Clay | 151 | 7919 | 9 | 12 | 13 |
| Missouri non-MSA | Missouri | Butler | 35 | 3517 | 9 | 8 | 9 |
| Joplin | Missouri | Jasper | 220 | 12242 | 8 | 12 | 19 |
| Columbia-Jefferson City | Missouri | Boone | 84 | 15911 | 7 | 11 | 18 |
| St. Louis-Farmington | Missouri | Franklin | 164 | 8435 | 6 | 9 | 12 |
| Springfield | Missouri | Christian | 80 | 6890 | 6 | 7 | 9 |
| Kansas City | Missouri | Lafayette | 56 | 2573 | 5 | 4 | 5 |
| St. Louis-Farmington | Illinois | Macoupin | 80 | 4364 | 5 | 5 | 7 |
| Kansas City | Missouri | Platte | 43 | 3121 | 4 | 5 | 6 |
| Cape Girardeau-Sikeston | Missouri | Scott | 77 | 3840 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Cedar | 19 | 703 | 4 | 2 | 1 |
| St. Louis-Farmington | Illinois | Monroe | 83 | 4071 | 4 | 5 | 8 |
| Columbia-Jefferson City | Missouri | Cole | 118 | 8593 | 4 | 4 | 7 |
| Columbia-Jefferson City | Missouri | Callaway | 45 | 4501 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Phelps | 121 | 3022 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Taney | 90 | 4591 | 4 | 3 | 5 |
| St. Louis-Farmington | Missouri | Lincoln | 39 | 4303 | 4 | 4 | 6 |
| Kansas City | Kansas | Miami | 42 | 2645 | 3 | 4 | 4 |
| St. Louis-Farmington | Missouri | St. Francois | 107 | 7591 | 3 | 3 | 7 |
| St. Louis-Farmington | Illinois | Clinton | 89 | 5578 | 3 | 3 | 8 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 127 | 7523 | 3 | 4 | 9 |
| Springfield | Missouri | Polk | 31 | 2171 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Nodaway | 25 | 2580 | 3 | 2 | 1 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1917 | 2 | 3 | 3 |
| St. Joseph | Missouri | Buchanan | 136 | 6958 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 76 | 2763 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Pettis | 75 | 4790 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Camden | 81 | 3731 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2314 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Johnson | 45 | 3871 | 2 | 3 | 6 |
| Missouri non-MSA | Missouri | Barry | 45 | 2195 | 2 | 2 | 2 |
| Joplin | Missouri | Newton | 69 | 4084 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Howell | 42 | 2824 | 2 | 2 | 2 |
| St. Louis-Farmington | Illinois | Jersey | 47 | 2496 | 1 | 2 | 4 |
| St. Louis-Farmington | Missouri | Warren | 19 | 2099 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 24 | 1272 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Stone | 38 | 2030 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Henry | 37 | 1749 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 588 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Saline | 38 | 2430 | 1 | 1 | 2 |
| Kansas City | Missouri | Ray | 25 | 1517 | 1 | 4 | 3 |
| Missouri non-MSA | Missouri | Crawford | 32 | 2056 | 1 | 1 | 2 |
| Kansas City | Missouri | Bates | 23 | 1086 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Adair | 18 | 2080 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 5 | 275 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Cooper | 28 | 1694 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Perry | 27 | 2049 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 12 | 970 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Laclede | 66 | 2926 | 1 | 1 | 3 |
| Kansas City | Kansas | Linn | 8 | 752 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Vernon | 38 | 1395 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | McDonald | 26 | 1926 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 48 | 2990 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Randolph | 30 | 1815 | 1 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 9 | 451 | 1 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 6 | 722 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Audrain | 57 | 2077 | 1 | 0 | 2 |
| Columbia-Jefferson City | Missouri | Osage | 14 | 1404 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Livingston | 37 | 1331 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Macon | 15 | 1213 | 0 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 22 | 942 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Miller | 49 | 2319 | 0 | 0 | 1 |
| Springfield | Missouri | Webster | 53 | 2995 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Morgan | 42 | 1626 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dunklin | 19 | 2412 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Douglas | 26 | 771 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 41 | 879 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Benton | 27 | 1453 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Linn | 12 | 545 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Texas | 22 | 1544 | 0 | 0 | 1 |
| Springfield | Missouri | Dallas | 24 | 827 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Oregon | 3 | 677 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 7 | 355 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Pike | 22 | 1488 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 15 | 1618 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 482 | 0 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 18 | 1284 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Washington | 48 | 2121 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Marion | 42 | 2646 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Monroe | 10 | 597 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 29 | 1681 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 10 | 631 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 16 | 1346 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 11 | 821 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dent | 17 | 821 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 27 | 921 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 7 | 536 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 12 | 758 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 14 | 420 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 34 | 829 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1053 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 23 | 835 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 9 | 424 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 6 | 423 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 568 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | New Madrid | 45 | 1769 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 367 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 16 | 550 | 0 | 0 | 1 |
| Kansas City | Missouri | Caldwell | 11 | 641 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 263 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 12 | 482 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 5 | 465 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Pemiscot | 29 | 1413 | 0 | 0 | 0 |
| Kansas City | Missouri | Clinton | 65 | 1525 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ripley | 14 | 855 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Worth | 1 | 143 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 3 | 225 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 14 | 747 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 179 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 6 | 472 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 260 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 11 | 587 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 21 | 734 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 178 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 13 | 467 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 29 | 1365 | 0 | 0 | 1 |
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
