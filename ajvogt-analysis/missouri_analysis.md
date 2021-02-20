# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/20/2021  
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
| Kansas City | 2425 | 174079 | 449 | 408 | 552 |
| St. Louis-Farmington | 4457 | 253254 | 399 | 480 | 709 |
| Missouri non-MSA | 1962 | 109168 | 99 | 124 | 208 |
| Springfield | 591 | 35921 | 34 | 55 | 82 |
| Columbia-Jefferson City | 304 | 34239 | 30 | 39 | 63 |
| Joplin | 278 | 16151 | 18 | 23 | 39 |
| Cape Girardeau-Sikeston | 207 | 12766 | 14 | 19 | 24 |
| St. Joseph | 192 | 10040 | 8 | 9 | 17 |
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
| Kansas City | Kansas | Johnson | 733 | 53652 | 254 | 195 | 220 |
| St. Louis-Farmington | Missouri | St. Louis | 1915 | 87177 | 140 | 165 | 255 |
| Kansas City | Missouri | Jackson | 369 | 29783 | 56 | 64 | 94 |
| St. Louis-Farmington | Illinois | Madison | 448 | 27562 | 52 | 64 | 98 |
| St. Louis-Farmington | Illinois | St. Clair | 459 | 25021 | 52 | 62 | 84 |
| St. Louis-Farmington | Missouri | St. Charles | 405 | 32633 | 43 | 56 | 70 |
| Kansas City | Kansas | Wyandotte | 264 | 18935 | 40 | 37 | 45 |
| Kansas City | Missouri | Kansas City | 497 | 36486 | 39 | 40 | 82 |
| St. Louis-Farmington | Missouri | St. Louis City | 406 | 21131 | 31 | 38 | 48 |
| Springfield | Missouri | Greene | 415 | 23171 | 24 | 38 | 55 |
| St. Louis-Farmington | Missouri | Jefferson | 204 | 18831 | 19 | 24 | 45 |
| Kansas City | Kansas | Leavenworth | 76 | 6680 | 17 | 21 | 27 |
| Columbia-Jefferson City | Missouri | Boone | 77 | 15784 | 14 | 19 | 33 |
| Joplin | Missouri | Jasper | 214 | 12096 | 13 | 17 | 31 |
| St. Louis-Farmington | Missouri | Franklin | 153 | 8341 | 12 | 13 | 21 |
| Kansas City | Missouri | Cass | 84 | 7157 | 10 | 13 | 22 |
| St. Louis-Farmington | Missouri | Lincoln | 32 | 4260 | 10 | 8 | 11 |
| Kansas City | Missouri | Clay | 141 | 7775 | 8 | 12 | 20 |
| Missouri non-MSA | Missouri | Butler | 33 | 3403 | 8 | 8 | 9 |
| St. Louis-Farmington | Missouri | St. Francois | 102 | 7544 | 8 | 8 | 11 |
| Columbia-Jefferson City | Missouri | Callaway | 43 | 4450 | 7 | 7 | 9 |
| Cape Girardeau-Sikeston | Missouri | Scott | 73 | 3794 | 7 | 6 | 6 |
| Springfield | Missouri | Christian | 75 | 6814 | 6 | 9 | 16 |
| St. Louis-Farmington | Illinois | Macoupin | 78 | 4306 | 6 | 8 | 14 |
| St. Louis-Farmington | Illinois | Monroe | 80 | 4011 | 6 | 8 | 13 |
| Missouri non-MSA | Missouri | Johnson | 43 | 3833 | 6 | 8 | 9 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 114 | 7479 | 6 | 11 | 14 |
| Kansas City | Kansas | Miami | 39 | 2592 | 5 | 5 | 8 |
| Columbia-Jefferson City | Missouri | Cole | 114 | 8543 | 5 | 7 | 12 |
| St. Joseph | Missouri | Buchanan | 129 | 6916 | 5 | 5 | 11 |
| Joplin | Missouri | Newton | 64 | 4055 | 5 | 5 | 8 |
| Missouri non-MSA | Missouri | Taney | 82 | 4539 | 4 | 5 | 9 |
| St. Louis-Farmington | Illinois | Jersey | 44 | 2470 | 4 | 5 | 7 |
| Kansas City | Missouri | Platte | 42 | 3062 | 3 | 5 | 8 |
| Kansas City | Missouri | Lafayette | 53 | 2522 | 3 | 4 | 6 |
| St. Louis-Farmington | Missouri | Warren | 17 | 2078 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Pettis | 75 | 4753 | 3 | 5 | 9 |
| Missouri non-MSA | Missouri | Henry | 36 | 1725 | 3 | 3 | 4 |
| St. Louis-Farmington | Illinois | Bond | 23 | 1880 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 24 | 2555 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Phelps | 119 | 2972 | 3 | 4 | 5 |
| St. Louis-Farmington | Illinois | Clinton | 89 | 5537 | 3 | 7 | 15 |
| Missouri non-MSA | Missouri | Lawrence | 71 | 2740 | 2 | 4 | 5 |
| Kansas City | Missouri | Ray | 23 | 1469 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Benton | 25 | 1443 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Pulaski | 43 | 2971 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Vernon | 38 | 1382 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Stone | 36 | 2012 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Perry | 24 | 2036 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2295 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Saline | 35 | 2411 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 14 | 1609 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Barry | 44 | 2172 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Livingston | 36 | 1321 | 1 | 1 | 4 |
| Missouri non-MSA | Missouri | Marion | 41 | 2638 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Crawford | 29 | 2033 | 1 | 1 | 3 |
| Springfield | Missouri | Webster | 49 | 2986 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | McDonald | 25 | 1911 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Howell | 42 | 2789 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Camden | 80 | 3697 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | Mississippi | 24 | 1256 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 6 | 469 | 1 | 1 | 1 |
| Kansas City | Missouri | Clinton | 64 | 1518 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Adair | 16 | 2051 | 1 | 2 | 5 |
| St. Joseph | Missouri | Andrew | 17 | 1279 | 1 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 24 | 1683 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Texas | 22 | 1536 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Miller | 49 | 2311 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Audrain | 57 | 2065 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2402 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Laclede | 64 | 2907 | 1 | 1 | 5 |
| Missouri non-MSA | Missouri | Barton | 12 | 951 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 28 | 1408 | 1 | 0 | 1 |
| Kansas City | Missouri | Bates | 22 | 1068 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Macon | 13 | 1200 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Washington | 45 | 2113 | 1 | 2 | 3 |
| Kansas City | Kansas | Linn | 8 | 743 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Scotland | 3 | 256 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 12 | 1392 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ripley | 14 | 849 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Pike | 21 | 1482 | 1 | 1 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 442 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carroll | 22 | 832 | 1 | 1 | 3 |
| St. Joseph | Missouri | DeKalb | 26 | 916 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Grundy | 34 | 825 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 38 | 871 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Morgan | 39 | 1619 | 0 | 1 | 1 |
| Springfield | Missouri | Polk | 30 | 2133 | 0 | 3 | 3 |
| St. Joseph | Kansas | Doniphan | 20 | 929 | 0 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 29 | 1677 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 28 | 1805 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 565 | 0 | 1 | 0 |
| Springfield | Missouri | Dallas | 22 | 817 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Chariton | 6 | 415 | 0 | 0 | 1 |
| Kansas City | Missouri | Caldwell | 10 | 637 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 533 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 12 | 547 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Daviess | 11 | 585 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dent | 16 | 815 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Douglas | 23 | 765 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Monroe | 10 | 589 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 17 | 666 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 472 | 0 | 0 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1051 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Wayne | 10 | 814 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 478 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 177 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 27 | 1364 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Harrison | 14 | 826 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Lewis | 5 | 628 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 260 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 12 | 754 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Oregon | 3 | 672 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Linn | 11 | 540 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 574 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Holt | 10 | 366 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 5 | 710 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 13 | 417 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 5 | 463 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 745 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 140 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 20 | 733 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Hickory | 13 | 466 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 223 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 3 | 263 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 6 | 349 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 16 | 1342 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 175 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 8 | 417 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | New Madrid | 45 | 1764 | 0 | 0 | 1 |
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
