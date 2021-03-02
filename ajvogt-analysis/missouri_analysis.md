# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 03/02/2021  
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
| St. Louis-Farmington | 4574 | 256731 | 350 | 362 | 486 |
| Kansas City | 2481 | 176168 | 226 | 319 | 366 |
| Missouri non-MSA | 2009 | 110060 | 95 | 94 | 134 |
| Springfield | 613 | 36289 | 37 | 37 | 54 |
| Columbia-Jefferson City | 310 | 34476 | 23 | 27 | 41 |
| Joplin | 285 | 16304 | 16 | 15 | 25 |
| Cape Girardeau-Sikeston | 221 | 12852 | 10 | 11 | 17 |
| St. Joseph | 201 | 10103 | 5 | 7 | 10 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1970 | 88485 | 132 | 136 | 171 |
| Kansas City | Kansas | Johnson | 744 | 54370 | 94 | 155 | 157 |
| St. Louis-Farmington | Illinois | St. Clair | 467 | 25497 | 51 | 49 | 62 |
| St. Louis-Farmington | Illinois | Madison | 455 | 28026 | 48 | 45 | 66 |
| Kansas City | Missouri | Jackson | 381 | 30137 | 35 | 45 | 59 |
| St. Louis-Farmington | Missouri | St. Charles | 413 | 32961 | 32 | 33 | 49 |
| St. Louis-Farmington | Missouri | St. Louis City | 424 | 21479 | 30 | 34 | 42 |
| Kansas City | Kansas | Wyandotte | 266 | 19219 | 25 | 35 | 36 |
| Springfield | Missouri | Greene | 427 | 23428 | 25 | 26 | 37 |
| Kansas City | Missouri | Kansas City | 514 | 36687 | 16 | 26 | 38 |
| St. Louis-Farmington | Missouri | Jefferson | 210 | 19006 | 15 | 18 | 27 |
| Joplin | Missouri | Jasper | 219 | 12224 | 13 | 12 | 20 |
| Kansas City | Missouri | Clay | 144 | 7898 | 11 | 11 | 14 |
| Kansas City | Missouri | Cass | 89 | 7246 | 10 | 10 | 12 |
| Kansas City | Kansas | Leavenworth | 77 | 6783 | 10 | 13 | 19 |
| Missouri non-MSA | Missouri | Butler | 34 | 3504 | 10 | 9 | 9 |
| Columbia-Jefferson City | Missouri | Boone | 80 | 15903 | 10 | 13 | 20 |
| Springfield | Missouri | Christian | 78 | 6877 | 7 | 6 | 10 |
| Kansas City | Missouri | Platte | 42 | 3119 | 6 | 5 | 6 |
| St. Louis-Farmington | Missouri | Franklin | 154 | 8423 | 6 | 9 | 13 |
| Columbia-Jefferson City | Missouri | Callaway | 43 | 4494 | 5 | 6 | 7 |
| St. Louis-Farmington | Illinois | Monroe | 83 | 4066 | 5 | 5 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 76 | 3833 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Cedar | 18 | 704 | 5 | 2 | 2 |
| Kansas City | Kansas | Miami | 41 | 2637 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Taney | 88 | 4590 | 5 | 4 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 79 | 4352 | 4 | 5 | 7 |
| St. Louis-Farmington | Missouri | St. Francois | 104 | 7587 | 4 | 5 | 8 |
| Missouri non-MSA | Missouri | Phelps | 121 | 3020 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Howell | 42 | 2821 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Pettis | 76 | 4787 | 4 | 3 | 5 |
| Columbia-Jefferson City | Missouri | Cole | 114 | 8580 | 4 | 4 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 36 | 4299 | 3 | 5 | 7 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 125 | 7518 | 3 | 4 | 9 |
| Missouri non-MSA | Missouri | Camden | 81 | 3725 | 3 | 2 | 3 |
| Kansas City | Missouri | Lafayette | 54 | 2557 | 3 | 3 | 5 |
| St. Louis-Farmington | Illinois | Clinton | 89 | 5571 | 3 | 3 | 8 |
| St. Joseph | Missouri | Buchanan | 135 | 6956 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Nodaway | 24 | 2577 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Johnson | 45 | 3865 | 3 | 4 | 6 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1910 | 3 | 3 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 46 | 2496 | 3 | 3 | 4 |
| Springfield | Missouri | Polk | 31 | 2162 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Adair | 16 | 2076 | 2 | 2 | 3 |
| Joplin | Missouri | Newton | 66 | 4080 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 72 | 2763 | 2 | 2 | 4 |
| Kansas City | Missouri | Ray | 24 | 1517 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Stone | 37 | 2030 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 24 | 1270 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 44 | 2990 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Barry | 44 | 2193 | 2 | 2 | 3 |
| St. Louis-Farmington | Missouri | Warren | 18 | 2095 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2310 | 2 | 1 | 2 |
| Kansas City | Missouri | Bates | 23 | 1083 | 1 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 22 | 942 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Perry | 26 | 2051 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Crawford | 30 | 2052 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | McDonald | 26 | 1922 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 3 | 274 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Henry | 36 | 1743 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Macon | 14 | 1211 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dunklin | 19 | 2413 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Saline | 35 | 2427 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Barton | 12 | 967 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 13 | 1403 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Cooper | 26 | 1694 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Benton | 26 | 1453 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Audrain | 58 | 2075 | 1 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 5 | 721 | 1 | 0 | 0 |
| Springfield | Missouri | Webster | 53 | 2996 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Livingston | 37 | 1331 | 1 | 1 | 2 |
| Springfield | Missouri | Dallas | 24 | 826 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Randolph | 29 | 1813 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 583 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 10 | 597 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Texas | 22 | 1541 | 0 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 448 | 0 | 0 | 1 |
| Kansas City | Missouri | Clinton | 64 | 1525 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Laclede | 66 | 2923 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Carter | 8 | 424 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 478 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Washington | 47 | 2122 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 263 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 8 | 749 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Vernon | 37 | 1391 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Shelby | 7 | 354 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 39 | 878 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Marion | 41 | 2646 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Oregon | 3 | 676 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 15 | 1617 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 22 | 1488 | 0 | 0 | 1 |
| St. Joseph | Missouri | Andrew | 17 | 1284 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Linn | 12 | 544 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 10 | 819 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Douglas | 25 | 769 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 12 | 758 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 7 | 536 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 23 | 835 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dent | 16 | 820 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 13 | 550 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 179 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Pemiscot | 28 | 1412 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 7 | 631 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 29 | 1681 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Miller | 49 | 2316 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 6 | 422 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1053 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 10 | 641 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Morgan | 40 | 1622 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 482 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 13 | 420 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 27 | 921 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 14 | 854 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Madison | 16 | 1345 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 3 | 225 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 178 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 6 | 471 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 142 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 13 | 467 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 14 | 827 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 568 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 34 | 828 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 14 | 746 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 20 | 734 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 11 | 587 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 260 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 366 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | New Madrid | 45 | 1768 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 29 | 1365 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Iron | 5 | 464 | 0 | 0 | 0 |
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
