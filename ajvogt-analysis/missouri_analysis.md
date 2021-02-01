# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/01/2021  
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
| St. Louis-Farmington | 4136 | 242752 | 878 | 1005 | 1319 |
| Kansas City | 2102 | 165409 | 681 | 827 | 926 |
| Missouri non-MSA | 1708 | 106232 | 253 | 289 | 428 |
| Springfield | 534 | 34728 | 106 | 118 | 169 |
| Columbia-Jefferson City | 261 | 33302 | 76 | 82 | 115 |
| Joplin | 255 | 15562 | 52 | 52 | 64 |
| Cape Girardeau-Sikeston | 201 | 12357 | 26 | 25 | 40 |
| St. Joseph | 175 | 9810 | 23 | 25 | 37 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1686 | 83508 | 337 | 362 | 467 |
| Kansas City | Kansas | Johnson | 655 | 49641 | 249 | 333 | 331 |
| Kansas City | Missouri | Kansas City | 440 | 35622 | 125 | 139 | 171 |
| St. Louis-Farmington | Illinois | Madison | 502 | 26173 | 124 | 144 | 170 |
| Kansas City | Missouri | Jackson | 308 | 28420 | 119 | 129 | 158 |
| St. Louis-Farmington | Illinois | St. Clair | 472 | 23677 | 100 | 115 | 154 |
| St. Louis-Farmington | Missouri | St. Charles | 344 | 31548 | 75 | 96 | 138 |
| Springfield | Missouri | Greene | 380 | 22354 | 69 | 77 | 109 |
| St. Louis-Farmington | Missouri | Jefferson | 170 | 18231 | 61 | 71 | 97 |
| Kansas City | Kansas | Wyandotte | 230 | 18114 | 51 | 64 | 74 |
| St. Louis-Farmington | Missouri | St. Louis City | 351 | 20260 | 47 | 60 | 90 |
| Columbia-Jefferson City | Missouri | Boone | 61 | 15328 | 43 | 48 | 61 |
| Joplin | Missouri | Jasper | 195 | 11630 | 42 | 42 | 50 |
| Kansas City | Kansas | Leavenworth | 59 | 6186 | 31 | 37 | 35 |
| Kansas City | Missouri | Clay | 124 | 7490 | 25 | 29 | 38 |
| St. Louis-Farmington | Missouri | Franklin | 131 | 8032 | 25 | 32 | 45 |
| Kansas City | Missouri | Cass | 69 | 6874 | 25 | 32 | 41 |
| Springfield | Missouri | Christian | 63 | 6584 | 20 | 23 | 33 |
| St. Louis-Farmington | Illinois | Clinton | 92 | 5318 | 20 | 23 | 27 |
| St. Louis-Farmington | Illinois | Monroe | 73 | 3812 | 19 | 19 | 22 |
| St. Louis-Farmington | Illinois | Macoupin | 101 | 4136 | 18 | 23 | 28 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 110 | 7240 | 17 | 15 | 24 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 4088 | 14 | 14 | 17 |
| Columbia-Jefferson City | Missouri | Cole | 104 | 8355 | 14 | 13 | 22 |
| Missouri non-MSA | Missouri | Taney | 68 | 4413 | 14 | 14 | 19 |
| Kansas City | Kansas | Miami | 28 | 2482 | 14 | 19 | 20 |
| St. Louis-Farmington | Missouri | St. Francois | 83 | 7364 | 13 | 15 | 24 |
| St. Joseph | Missouri | Buchanan | 122 | 6766 | 13 | 15 | 23 |
| Kansas City | Missouri | Platte | 36 | 2927 | 11 | 10 | 15 |
| Missouri non-MSA | Missouri | Pettis | 69 | 4624 | 11 | 11 | 17 |
| Joplin | Missouri | Newton | 60 | 3932 | 10 | 10 | 14 |
| Missouri non-MSA | Missouri | Butler | 24 | 3230 | 9 | 11 | 12 |
| Missouri non-MSA | Missouri | Johnson | 35 | 3674 | 9 | 10 | 14 |
| Columbia-Jefferson City | Missouri | Callaway | 34 | 4268 | 9 | 9 | 15 |
| Springfield | Missouri | Webster | 46 | 2929 | 8 | 10 | 15 |
| Missouri non-MSA | Missouri | Stone | 32 | 1931 | 8 | 6 | 9 |
| St. Louis-Farmington | Illinois | Jersey | 63 | 2356 | 7 | 11 | 12 |
| Missouri non-MSA | Missouri | Adair | 7 | 1992 | 7 | 8 | 12 |
| St. Louis-Farmington | Missouri | Warren | 12 | 1988 | 7 | 9 | 10 |
| Kansas City | Missouri | Lafayette | 46 | 2410 | 7 | 9 | 10 |
| Missouri non-MSA | Missouri | Camden | 74 | 3616 | 7 | 8 | 14 |
| Missouri non-MSA | Missouri | Laclede | 58 | 2829 | 7 | 7 | 10 |
| Missouri non-MSA | Missouri | Howell | 41 | 2737 | 6 | 7 | 13 |
| Missouri non-MSA | Missouri | Saline | 30 | 2334 | 6 | 7 | 10 |
| Kansas City | Missouri | Ray | 19 | 1408 | 5 | 7 | 8 |
| Missouri non-MSA | Missouri | Harrison | 12 | 797 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Henry | 28 | 1653 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Lawrence | 61 | 2641 | 5 | 7 | 9 |
| Missouri non-MSA | Missouri | Audrain | 50 | 2017 | 5 | 4 | 6 |
| Cape Girardeau-Sikeston | Missouri | Scott | 71 | 3671 | 5 | 6 | 10 |
| Missouri non-MSA | Missouri | Washington | 41 | 2069 | 5 | 6 | 9 |
| St. Joseph | Kansas | Doniphan | 12 | 894 | 5 | 4 | 5 |
| Springfield | Missouri | Polk | 25 | 2071 | 5 | 4 | 7 |
| Missouri non-MSA | Missouri | Livingston | 32 | 1271 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Crawford | 24 | 1990 | 5 | 5 | 8 |
| Missouri non-MSA | Missouri | Barry | 41 | 2109 | 5 | 5 | 9 |
| Missouri non-MSA | Missouri | Wright | 24 | 1329 | 4 | 4 | 7 |
| Kansas City | Kansas | Linn | 4 | 710 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2345 | 4 | 5 | 8 |
| Kansas City | Missouri | Bates | 16 | 1034 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Phelps | 107 | 2885 | 4 | 6 | 12 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2229 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2521 | 4 | 4 | 7 |
| Kansas City | Missouri | Clinton | 60 | 1474 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Macon | 10 | 1164 | 4 | 7 | 7 |
| Missouri non-MSA | Missouri | Pulaski | 34 | 2917 | 3 | 4 | 11 |
| Missouri non-MSA | Missouri | Pike | 17 | 1451 | 3 | 4 | 5 |
| St. Louis-Farmington | Illinois | Bond | 27 | 1808 | 3 | 5 | 8 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 12 | 1571 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Carroll | 18 | 790 | 3 | 4 | 4 |
| Columbia-Jefferson City | Missouri | Osage | 10 | 1359 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Miller | 45 | 2281 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | St. Clair | 6 | 560 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 21 | 1221 | 3 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1643 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Ripley | 10 | 789 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 33 | 842 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 41 | 1745 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Dent | 11 | 802 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Benton | 20 | 1387 | 2 | 3 | 6 |
| Missouri non-MSA | Missouri | Linn | 10 | 525 | 2 | 3 | 3 |
| Springfield | Missouri | Dallas | 20 | 790 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Barton | 9 | 918 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | McDonald | 24 | 1871 | 2 | 4 | 6 |
| Missouri non-MSA | Missouri | Perry | 22 | 1992 | 2 | 2 | 4 |
| St. Joseph | Missouri | DeKalb | 24 | 899 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Wayne | 9 | 789 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Madison | 13 | 1331 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Cedar | 9 | 644 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Randolph | 24 | 1788 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Daviess | 10 | 563 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Vernon | 32 | 1328 | 2 | 3 | 7 |
| St. Joseph | Missouri | Andrew | 17 | 1251 | 2 | 3 | 4 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1655 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Marion | 36 | 2584 | 2 | 5 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 24 | 1386 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Morgan | 36 | 1591 | 2 | 1 | 4 |
| Missouri non-MSA | Missouri | Texas | 21 | 1499 | 2 | 1 | 4 |
| Missouri non-MSA | Missouri | Gentry | 19 | 717 | 2 | 2 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1031 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 262 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 415 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ozark | 10 | 519 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Oregon | 3 | 659 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Clark | 6 | 442 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Monroe | 7 | 579 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Grundy | 30 | 799 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Douglas | 23 | 744 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Shelby | 5 | 347 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 694 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ralls | 10 | 737 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Iron | 1 | 461 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 459 | 1 | 0 | 1 |
| Kansas City | Missouri | Caldwell | 8 | 617 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Lewis | 3 | 621 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Maries | 7 | 519 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 240 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 3 | 403 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Dade | 12 | 410 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 10 | 459 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 162 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 359 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 740 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 2 | 172 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 5 | 453 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 550 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 256 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 137 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 288 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 8 | 409 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 217 | 0 | 0 | 0 |
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
