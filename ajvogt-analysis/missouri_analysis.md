# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/03/2021  
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
| St. Louis-Farmington | 4048 | 244014 | 833 | 956 | 1236 |
| Kansas City | 2154 | 166383 | 674 | 761 | 924 |
| Missouri non-MSA | 1802 | 106576 | 245 | 282 | 407 |
| Springfield | 551 | 34885 | 105 | 111 | 164 |
| Columbia-Jefferson City | 277 | 33443 | 85 | 87 | 112 |
| Joplin | 263 | 15650 | 53 | 53 | 63 |
| Cape Girardeau-Sikeston | 207 | 12388 | 26 | 25 | 38 |
| St. Joseph | 178 | 9860 | 24 | 26 | 35 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1705 | 84001 | 320 | 355 | 433 |
| Kansas City | Kansas | Johnson | 662 | 50030 | 245 | 287 | 344 |
| Kansas City | Missouri | Kansas City | 454 | 35760 | 124 | 133 | 162 |
| Kansas City | Missouri | Jackson | 320 | 28573 | 117 | 128 | 152 |
| St. Louis-Farmington | Illinois | Madison | 437 | 26351 | 115 | 139 | 159 |
| St. Louis-Farmington | Illinois | St. Clair | 429 | 23811 | 85 | 104 | 140 |
| Springfield | Missouri | Greene | 388 | 22471 | 71 | 73 | 106 |
| St. Louis-Farmington | Missouri | St. Charles | 375 | 31623 | 68 | 88 | 130 |
| St. Louis-Farmington | Missouri | St. Louis City | 353 | 20390 | 63 | 58 | 88 |
| St. Louis-Farmington | Missouri | Jefferson | 181 | 18300 | 56 | 65 | 93 |
| Kansas City | Kansas | Wyandotte | 232 | 18216 | 50 | 56 | 77 |
| Joplin | Missouri | Jasper | 201 | 11709 | 44 | 42 | 50 |
| Columbia-Jefferson City | Missouri | Boone | 69 | 15362 | 42 | 47 | 58 |
| Kansas City | Kansas | Leavenworth | 60 | 6247 | 33 | 33 | 37 |
| Kansas City | Missouri | Clay | 128 | 7522 | 25 | 29 | 36 |
| Kansas City | Missouri | Cass | 72 | 6901 | 24 | 31 | 39 |
| St. Louis-Farmington | Missouri | Franklin | 138 | 8063 | 23 | 28 | 42 |
| St. Louis-Farmington | Illinois | Clinton | 85 | 5349 | 20 | 22 | 26 |
| Springfield | Missouri | Christian | 69 | 6610 | 18 | 22 | 32 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 116 | 7260 | 17 | 16 | 23 |
| St. Louis-Farmington | Illinois | Monroe | 74 | 3839 | 17 | 18 | 21 |
| Columbia-Jefferson City | Missouri | Cole | 107 | 8389 | 16 | 15 | 21 |
| St. Louis-Farmington | Missouri | St. Francois | 92 | 7395 | 16 | 15 | 24 |
| Columbia-Jefferson City | Missouri | Callaway | 37 | 4323 | 15 | 12 | 15 |
| St. Louis-Farmington | Illinois | Macoupin | 72 | 4162 | 15 | 22 | 27 |
| St. Joseph | Missouri | Buchanan | 125 | 6794 | 14 | 16 | 21 |
| Missouri non-MSA | Missouri | Taney | 73 | 4427 | 13 | 13 | 19 |
| St. Louis-Farmington | Missouri | Lincoln | 27 | 4098 | 12 | 12 | 16 |
| Missouri non-MSA | Missouri | Pettis | 72 | 4644 | 12 | 12 | 17 |
| Kansas City | Missouri | Platte | 37 | 2937 | 11 | 10 | 14 |
| Kansas City | Kansas | Miami | 28 | 2502 | 11 | 20 | 20 |
| Missouri non-MSA | Missouri | Butler | 27 | 3249 | 10 | 10 | 12 |
| Joplin | Missouri | Newton | 62 | 3941 | 9 | 10 | 13 |
| Missouri non-MSA | Missouri | Johnson | 38 | 3685 | 9 | 9 | 13 |
| Kansas City | Missouri | Lafayette | 48 | 2424 | 8 | 9 | 10 |
| Missouri non-MSA | Missouri | Stone | 33 | 1946 | 8 | 6 | 9 |
| Missouri non-MSA | Missouri | Camden | 75 | 3633 | 8 | 8 | 14 |
| Springfield | Missouri | Webster | 46 | 2935 | 8 | 9 | 15 |
| St. Louis-Farmington | Illinois | Jersey | 44 | 2373 | 8 | 10 | 11 |
| St. Louis-Farmington | Missouri | Warren | 13 | 1995 | 7 | 8 | 10 |
| Missouri non-MSA | Missouri | Adair | 11 | 1995 | 7 | 8 | 11 |
| Missouri non-MSA | Missouri | Saline | 33 | 2348 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Laclede | 60 | 2838 | 6 | 6 | 9 |
| Missouri non-MSA | Missouri | Lawrence | 63 | 2653 | 6 | 7 | 9 |
| Cape Girardeau-Sikeston | Missouri | Scott | 71 | 3674 | 5 | 6 | 10 |
| Springfield | Missouri | Polk | 26 | 2077 | 5 | 4 | 7 |
| Missouri non-MSA | Missouri | Livingston | 32 | 1275 | 5 | 5 | 7 |
| Kansas City | Missouri | Ray | 20 | 1416 | 5 | 7 | 8 |
| Missouri non-MSA | Missouri | Howell | 41 | 2739 | 5 | 7 | 11 |
| Missouri non-MSA | Missouri | Henry | 30 | 1657 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Crawford | 28 | 1996 | 5 | 5 | 7 |
| Kansas City | Missouri | Bates | 19 | 1042 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 37 | 2924 | 4 | 4 | 11 |
| Missouri non-MSA | Missouri | Barry | 44 | 2114 | 4 | 5 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2234 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Wright | 26 | 1331 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Harrison | 13 | 803 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2349 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Phelps | 114 | 2891 | 4 | 5 | 10 |
| Columbia-Jefferson City | Missouri | Osage | 12 | 1368 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Macon | 12 | 1169 | 4 | 7 | 7 |
| Missouri non-MSA | Missouri | Pike | 20 | 1455 | 4 | 4 | 5 |
| Kansas City | Missouri | Clinton | 60 | 1478 | 4 | 4 | 6 |
| Kansas City | Kansas | Linn | 4 | 716 | 4 | 4 | 6 |
| St. Joseph | Kansas | Doniphan | 12 | 901 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 13 | 1575 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Washington | 42 | 2073 | 3 | 5 | 8 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1649 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 564 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Carroll | 21 | 798 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Texas | 21 | 1514 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 23 | 2525 | 3 | 3 | 7 |
| Missouri non-MSA | Missouri | Ripley | 10 | 793 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 33 | 846 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Benton | 23 | 1393 | 3 | 3 | 5 |
| St. Joseph | Missouri | Andrew | 17 | 1260 | 3 | 3 | 4 |
| St. Louis-Farmington | Illinois | Bond | 21 | 1811 | 3 | 5 | 8 |
| St. Joseph | Missouri | DeKalb | 24 | 905 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 22 | 1225 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Miller | 45 | 2283 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | Marion | 39 | 2589 | 2 | 4 | 6 |
| Missouri non-MSA | Missouri | Barton | 10 | 922 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 25 | 1389 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | McDonald | 25 | 1874 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 43 | 1746 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Cedar | 10 | 648 | 2 | 2 | 3 |
| Springfield | Missouri | Dallas | 22 | 792 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Vernon | 33 | 1334 | 2 | 3 | 6 |
| Missouri non-MSA | Missouri | Daviess | 11 | 568 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Madison | 15 | 1333 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dent | 14 | 804 | 2 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1036 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Perry | 22 | 1997 | 2 | 3 | 4 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1658 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Audrain | 50 | 2018 | 2 | 4 | 6 |
| Missouri non-MSA | Missouri | Randolph | 27 | 1793 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Gentry | 19 | 719 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Morgan | 36 | 1597 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Shannon | 10 | 464 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 23 | 749 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Grundy | 31 | 803 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Wayne | 9 | 792 | 1 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 418 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Clark | 6 | 443 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Linn | 10 | 526 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Oregon | 3 | 659 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Maries | 7 | 522 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 8 | 580 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 12 | 740 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 262 | 1 | 1 | 1 |
| Kansas City | Missouri | Caldwell | 10 | 619 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 694 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Ozark | 10 | 519 | 0 | 2 | 4 |
| Missouri non-MSA | Missouri | Shelby | 6 | 346 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 10 | 360 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 11 | 461 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 164 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 3 | 404 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Scotland | 3 | 240 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 3 | 461 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 173 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 3 | 621 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 740 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Putnam | 2 | 219 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 13 | 410 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 6 | 289 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 257 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 8 | 410 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 550 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 453 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Worth | 1 | 137 | 0 | 0 | 0 |
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
