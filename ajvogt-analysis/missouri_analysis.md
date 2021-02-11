# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/11/2021  
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
| St. Louis-Farmington | 4169 | 249145 | 612 | 716 | 952 |
| Kansas City | 2243 | 170265 | 452 | 503 | 714 |
| Missouri non-MSA | 1829 | 108109 | 188 | 213 | 288 |
| Springfield | 553 | 35515 | 79 | 84 | 114 |
| Columbia-Jefferson City | 278 | 33923 | 53 | 70 | 82 |
| Joplin | 270 | 15963 | 34 | 44 | 51 |
| Cape Girardeau-Sikeston | 208 | 12619 | 29 | 27 | 29 |
| St. Joseph | 187 | 9965 | 13 | 18 | 24 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1776 | 85740 | 212 | 262 | 337 |
| Kansas City | Kansas | Johnson | 695 | 51608 | 173 | 168 | 271 |
| St. Louis-Farmington | Illinois | St. Clair | 443 | 24518 | 82 | 87 | 113 |
| St. Louis-Farmington | Illinois | Madison | 438 | 27038 | 81 | 95 | 132 |
| Kansas City | Missouri | Jackson | 328 | 29228 | 81 | 95 | 122 |
| St. Louis-Farmington | Missouri | St. Charles | 379 | 32140 | 63 | 66 | 94 |
| Kansas City | Missouri | Kansas City | 462 | 36177 | 54 | 87 | 112 |
| Springfield | Missouri | Greene | 388 | 22885 | 52 | 57 | 74 |
| St. Louis-Farmington | Missouri | St. Louis City | 376 | 20765 | 44 | 54 | 64 |
| Kansas City | Kansas | Wyandotte | 249 | 18609 | 42 | 40 | 60 |
| St. Louis-Farmington | Missouri | Jefferson | 183 | 18628 | 35 | 46 | 66 |
| Kansas City | Kansas | Leavenworth | 71 | 6516 | 30 | 28 | 33 |
| Columbia-Jefferson City | Missouri | Boone | 69 | 15623 | 27 | 34 | 44 |
| Joplin | Missouri | Jasper | 208 | 11954 | 26 | 35 | 41 |
| Kansas City | Missouri | Clay | 131 | 7685 | 20 | 23 | 28 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 116 | 7407 | 19 | 17 | 18 |
| St. Louis-Farmington | Illinois | Clinton | 86 | 5500 | 18 | 18 | 22 |
| St. Louis-Farmington | Missouri | Franklin | 138 | 8214 | 18 | 20 | 30 |
| Kansas City | Missouri | Cass | 72 | 7041 | 17 | 20 | 30 |
| Springfield | Missouri | Christian | 71 | 6748 | 17 | 16 | 22 |
| St. Louis-Farmington | Illinois | Monroe | 76 | 3949 | 13 | 15 | 17 |
| Columbia-Jefferson City | Missouri | Cole | 107 | 8486 | 12 | 14 | 14 |
| St. Joseph | Missouri | Buchanan | 126 | 6872 | 10 | 11 | 15 |
| Missouri non-MSA | Missouri | Johnson | 38 | 3766 | 10 | 9 | 10 |
| St. Louis-Farmington | Missouri | St. Francois | 92 | 7472 | 9 | 12 | 15 |
| Missouri non-MSA | Missouri | Pettis | 71 | 4717 | 9 | 10 | 12 |
| St. Louis-Farmington | Illinois | Macoupin | 73 | 4241 | 8 | 12 | 21 |
| Joplin | Missouri | Newton | 62 | 4009 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | Taney | 73 | 4495 | 8 | 10 | 13 |
| Kansas City | Missouri | Platte | 38 | 3012 | 8 | 10 | 11 |
| Missouri non-MSA | Missouri | Butler | 27 | 3314 | 7 | 9 | 10 |
| Kansas City | Missouri | Lafayette | 48 | 2482 | 7 | 8 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 72 | 3734 | 7 | 6 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 27 | 4165 | 7 | 9 | 12 |
| Missouri non-MSA | Missouri | Laclede | 64 | 2895 | 7 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Callaway | 37 | 4386 | 7 | 11 | 11 |
| St. Louis-Farmington | Illinois | Jersey | 44 | 2428 | 6 | 7 | 10 |
| Missouri non-MSA | Missouri | Lawrence | 66 | 2702 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Saline | 33 | 2388 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Ripley | 11 | 834 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2273 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Barry | 43 | 2155 | 5 | 4 | 7 |
| St. Louis-Farmington | Missouri | Warren | 13 | 2042 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Stone | 34 | 1986 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Camden | 75 | 3678 | 5 | 6 | 8 |
| Springfield | Missouri | Polk | 26 | 2111 | 4 | 3 | 5 |
| Kansas City | Kansas | Miami | 31 | 2542 | 4 | 6 | 13 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2382 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Phelps | 115 | 2936 | 4 | 5 | 8 |
| Missouri non-MSA | Missouri | Audrain | 51 | 2048 | 4 | 2 | 4 |
| Missouri non-MSA | Missouri | Adair | 11 | 2029 | 4 | 4 | 8 |
| Missouri non-MSA | Missouri | Howell | 42 | 2771 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Marion | 39 | 2617 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Vernon | 33 | 1361 | 3 | 3 | 4 |
| Kansas City | Missouri | Clinton | 60 | 1503 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Ozark | 11 | 543 | 3 | 2 | 3 |
| Springfield | Missouri | Webster | 46 | 2965 | 3 | 4 | 9 |
| Kansas City | Missouri | Ray | 22 | 1443 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Wright | 26 | 1356 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Carroll | 21 | 821 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Livingston | 32 | 1304 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Washington | 42 | 2098 | 3 | 3 | 5 |
| St. Louis-Farmington | Illinois | Bond | 23 | 1837 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Benton | 23 | 1420 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Crawford | 28 | 2017 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 37 | 2946 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Henry | 30 | 1686 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Harrison | 14 | 818 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 13 | 1592 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Pike | 21 | 1473 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Wayne | 9 | 807 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | McDonald | 25 | 1891 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Gasconade | 36 | 859 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 43 | 1765 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Miller | 48 | 2300 | 2 | 2 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 432 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Macon | 12 | 1187 | 2 | 2 | 5 |
| Kansas City | Missouri | Bates | 19 | 1058 | 2 | 3 | 4 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 468 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1670 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Perry | 22 | 2016 | 1 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Osage | 12 | 1382 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Morgan | 39 | 1609 | 1 | 1 | 2 |
| Springfield | Missouri | Dallas | 22 | 806 | 1 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 28 | 1671 | 1 | 1 | 2 |
| Kansas City | Kansas | Linn | 7 | 731 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 23 | 1239 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 11 | 660 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Daviess | 11 | 581 | 1 | 2 | 2 |
| St. Joseph | Kansas | Doniphan | 18 | 920 | 1 | 2 | 3 |
| Kansas City | Missouri | Caldwell | 10 | 630 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 6 | 458 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 25 | 1400 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Barton | 10 | 935 | 1 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 705 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 19 | 729 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Texas | 21 | 1523 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Grundy | 32 | 815 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 2 | 173 | 1 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1046 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 12 | 749 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 474 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 23 | 759 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Nodaway | 23 | 2532 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 558 | 1 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 17 | 1266 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Madison | 15 | 1341 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Linn | 10 | 537 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Carter | 8 | 416 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 3 | 409 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 245 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 569 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Oregon | 3 | 666 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dent | 14 | 811 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Maries | 7 | 528 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 27 | 1799 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Holt | 10 | 364 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 4 | 624 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dade | 13 | 415 | 0 | 0 | 1 |
| St. Joseph | Missouri | DeKalb | 26 | 907 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Putnam | 2 | 222 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 8 | 584 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 6 | 349 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 175 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 11 | 463 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 139 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 742 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 258 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 263 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 3 | 460 | 0 | 0 | 0 |
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
