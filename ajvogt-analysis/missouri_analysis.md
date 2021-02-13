# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/13/2021  
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
| St. Louis-Farmington | 4289 | 250461 | 561 | 650 | 902 |
| Kansas City | 2305 | 170935 | 367 | 429 | 661 |
| Missouri non-MSA | 1894 | 108470 | 148 | 190 | 272 |
| Springfield | 571 | 35680 | 76 | 79 | 107 |
| Columbia-Jefferson City | 289 | 34029 | 48 | 64 | 79 |
| Joplin | 274 | 16025 | 29 | 39 | 47 |
| Cape Girardeau-Sikeston | 210 | 12665 | 25 | 24 | 28 |
| St. Joseph | 189 | 9981 | 9 | 14 | 23 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1831 | 86196 | 190 | 221 | 319 |
| Kansas City | Kansas | Johnson | 702 | 51871 | 135 | 159 | 250 |
| St. Louis-Farmington | Illinois | Madison | 440 | 27192 | 75 | 88 | 124 |
| St. Louis-Farmington | Illinois | St. Clair | 445 | 24657 | 73 | 80 | 107 |
| Kansas City | Missouri | Jackson | 348 | 29388 | 72 | 80 | 113 |
| St. Louis-Farmington | Missouri | St. Charles | 395 | 32326 | 68 | 68 | 89 |
| Springfield | Missouri | Greene | 402 | 23000 | 52 | 53 | 70 |
| St. Louis-Farmington | Missouri | St. Louis City | 387 | 20909 | 45 | 54 | 62 |
| Kansas City | Missouri | Kansas City | 478 | 36213 | 41 | 55 | 106 |
| Kansas City | Kansas | Wyandotte | 252 | 18649 | 33 | 38 | 53 |
| St. Louis-Farmington | Missouri | Jefferson | 195 | 18692 | 29 | 41 | 61 |
| Kansas City | Kansas | Leavenworth | 71 | 6555 | 25 | 26 | 32 |
| Columbia-Jefferson City | Missouri | Boone | 71 | 15686 | 25 | 32 | 42 |
| Joplin | Missouri | Jasper | 211 | 12005 | 22 | 32 | 38 |
| Kansas City | Missouri | Cass | 78 | 7081 | 16 | 17 | 28 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 116 | 7437 | 16 | 16 | 18 |
| Kansas City | Missouri | Clay | 137 | 7714 | 15 | 18 | 25 |
| St. Louis-Farmington | Missouri | Franklin | 149 | 8253 | 15 | 18 | 29 |
| St. Louis-Farmington | Illinois | Clinton | 88 | 5515 | 12 | 16 | 21 |
| Springfield | Missouri | Christian | 71 | 6766 | 12 | 14 | 21 |
| St. Louis-Farmington | Illinois | Monroe | 78 | 3967 | 10 | 12 | 16 |
| Columbia-Jefferson City | Missouri | Cole | 111 | 8506 | 10 | 13 | 14 |
| Missouri non-MSA | Missouri | Johnson | 40 | 3791 | 10 | 9 | 10 |
| Missouri non-MSA | Missouri | Butler | 30 | 3346 | 9 | 9 | 10 |
| St. Louis-Farmington | Illinois | Macoupin | 73 | 4259 | 9 | 10 | 18 |
| St. Louis-Farmington | Missouri | St. Francois | 96 | 7488 | 8 | 11 | 14 |
| Kansas City | Missouri | Platte | 38 | 3035 | 7 | 9 | 10 |
| Missouri non-MSA | Missouri | Pettis | 75 | 4728 | 7 | 8 | 10 |
| St. Louis-Farmington | Missouri | Lincoln | 30 | 4188 | 7 | 9 | 11 |
| Columbia-Jefferson City | Missouri | Callaway | 39 | 4400 | 7 | 11 | 10 |
| St. Joseph | Missouri | Buchanan | 127 | 6881 | 6 | 9 | 15 |
| Cape Girardeau-Sikeston | Missouri | Scott | 74 | 3745 | 6 | 5 | 7 |
| St. Louis-Farmington | Illinois | Jersey | 44 | 2442 | 6 | 6 | 10 |
| Joplin | Missouri | Newton | 63 | 4020 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Taney | 77 | 4509 | 6 | 8 | 12 |
| Missouri non-MSA | Missouri | Lawrence | 68 | 2720 | 5 | 5 | 6 |
| Kansas City | Missouri | Lafayette | 48 | 2495 | 5 | 7 | 8 |
| Springfield | Missouri | Polk | 28 | 2127 | 5 | 4 | 4 |
| Kansas City | Kansas | Miami | 33 | 2551 | 4 | 4 | 12 |
| Missouri non-MSA | Missouri | Phelps | 117 | 2949 | 4 | 5 | 8 |
| St. Louis-Farmington | Illinois | Bond | 23 | 1857 | 4 | 3 | 5 |
| St. Louis-Farmington | Missouri | Warren | 13 | 2051 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Stone | 35 | 1994 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Adair | 13 | 2040 | 4 | 4 | 7 |
| Springfield | Missouri | Webster | 48 | 2975 | 3 | 4 | 8 |
| Missouri non-MSA | Missouri | Barry | 43 | 2160 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Howell | 42 | 2778 | 3 | 3 | 7 |
| Missouri non-MSA | Missouri | Saline | 34 | 2398 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Camden | 79 | 3686 | 3 | 6 | 8 |
| Missouri non-MSA | Missouri | Ripley | 13 | 842 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2392 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Henry | 33 | 1701 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Marion | 39 | 2626 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Washington | 45 | 2105 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 40 | 2953 | 2 | 3 | 4 |
| Kansas City | Missouri | Clinton | 61 | 1507 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Vernon | 34 | 1364 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Wayne | 10 | 811 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2281 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | McDonald | 25 | 1900 | 2 | 2 | 3 |
| Kansas City | Missouri | Ray | 22 | 1449 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Wright | 26 | 1361 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Livingston | 34 | 1309 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Benton | 23 | 1424 | 2 | 3 | 3 |
| Kansas City | Kansas | Linn | 7 | 735 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Carroll | 21 | 825 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Audrain | 54 | 2055 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Laclede | 64 | 2898 | 2 | 5 | 6 |
| Missouri non-MSA | Missouri | Macon | 12 | 1192 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | Gasconade | 36 | 864 | 1 | 1 | 3 |
| Springfield | Missouri | Dallas | 22 | 812 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Crawford | 29 | 2021 | 1 | 2 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 5 | 708 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 24 | 1245 | 1 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Osage | 12 | 1385 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 13 | 1596 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Harrison | 14 | 823 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Morgan | 39 | 1613 | 1 | 1 | 2 |
| St. Joseph | Kansas | Doniphan | 19 | 923 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Ralls | 12 | 752 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 560 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 11 | 942 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Scotland | 3 | 249 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 13 | 663 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Pike | 21 | 1475 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Perry | 23 | 2019 | 1 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 435 | 1 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 28 | 1672 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Oregon | 3 | 670 | 1 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 469 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Miller | 48 | 2301 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Mercer | 2 | 174 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 20 | 732 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Grundy | 34 | 818 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Nodaway | 24 | 2532 | 1 | 2 | 2 |
| Kansas City | Missouri | Caldwell | 10 | 632 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 11 | 543 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Texas | 21 | 1526 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 23 | 761 | 1 | 1 | 2 |
| Kansas City | Missouri | Bates | 20 | 1060 | 1 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 23 | 1672 | 1 | 2 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1048 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | New Madrid | 43 | 1765 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Carter | 8 | 418 | 0 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 17 | 1268 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Linn | 11 | 538 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Iron | 4 | 461 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 6 | 458 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 26 | 1400 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 12 | 465 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Randolph | 27 | 1800 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Madison | 16 | 1342 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Daviess | 11 | 581 | 0 | 1 | 2 |
| St. Joseph | Missouri | DeKalb | 26 | 909 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Monroe | 10 | 585 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 572 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Putnam | 2 | 222 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 139 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 364 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 744 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 5 | 410 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 528 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dent | 15 | 811 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Lewis | 4 | 625 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 475 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 175 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 6 | 349 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 258 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 3 | 263 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 13 | 415 | 0 | 0 | 0 |
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
