# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/09/2021  
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
| St. Louis-Farmington | 4156 | 247996 | 681 | 769 | 999 |
| Kansas City | 2227 | 169212 | 435 | 557 | 758 |
| Missouri non-MSA | 1822 | 107853 | 207 | 226 | 313 |
| Springfield | 553 | 35366 | 81 | 93 | 120 |
| Columbia-Jefferson City | 277 | 33865 | 70 | 76 | 90 |
| Joplin | 270 | 15899 | 45 | 48 | 52 |
| Cape Girardeau-Sikeston | 207 | 12586 | 31 | 28 | 30 |
| St. Joseph | 186 | 9950 | 15 | 19 | 27 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1773 | 85265 | 231 | 284 | 350 |
| Kansas City | Kansas | Johnson | 690 | 51150 | 160 | 202 | 289 |
| St. Louis-Farmington | Illinois | Madison | 438 | 26907 | 93 | 105 | 137 |
| St. Louis-Farmington | Illinois | St. Clair | 439 | 24386 | 88 | 91 | 119 |
| Kansas City | Missouri | Jackson | 327 | 29056 | 83 | 101 | 129 |
| St. Louis-Farmington | Missouri | St. Louis City | 374 | 20735 | 67 | 56 | 69 |
| St. Louis-Farmington | Missouri | St. Charles | 378 | 31977 | 55 | 63 | 99 |
| Springfield | Missouri | Greene | 388 | 22783 | 54 | 61 | 78 |
| Kansas City | Missouri | Kansas City | 458 | 36076 | 53 | 90 | 121 |
| St. Louis-Farmington | Missouri | Jefferson | 183 | 18575 | 43 | 51 | 71 |
| Joplin | Missouri | Jasper | 208 | 11911 | 37 | 39 | 42 |
| Kansas City | Kansas | Wyandotte | 245 | 18472 | 36 | 43 | 63 |
| Columbia-Jefferson City | Missouri | Boone | 69 | 15593 | 34 | 39 | 47 |
| Kansas City | Kansas | Leavenworth | 71 | 6451 | 29 | 31 | 35 |
| Kansas City | Missouri | Clay | 131 | 7662 | 22 | 24 | 30 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 116 | 7391 | 20 | 18 | 19 |
| St. Louis-Farmington | Illinois | Clinton | 85 | 5462 | 19 | 19 | 22 |
| St. Louis-Farmington | Missouri | Franklin | 138 | 8181 | 18 | 22 | 32 |
| Springfield | Missouri | Christian | 71 | 6720 | 17 | 18 | 23 |
| Kansas City | Missouri | Cass | 72 | 7003 | 16 | 21 | 32 |
| Columbia-Jefferson City | Missouri | Cole | 107 | 8473 | 15 | 15 | 16 |
| St. Louis-Farmington | Illinois | Monroe | 75 | 3926 | 13 | 16 | 18 |
| Columbia-Jefferson City | Missouri | Callaway | 37 | 4380 | 12 | 12 | 12 |
| St. Louis-Farmington | Missouri | St. Francois | 92 | 7458 | 11 | 13 | 16 |
| St. Joseph | Missouri | Buchanan | 126 | 6860 | 11 | 12 | 17 |
| St. Louis-Farmington | Illinois | Macoupin | 73 | 4223 | 11 | 13 | 22 |
| Missouri non-MSA | Missouri | Johnson | 38 | 3751 | 10 | 9 | 11 |
| Kansas City | Missouri | Platte | 37 | 3001 | 9 | 11 | 12 |
| Missouri non-MSA | Missouri | Taney | 73 | 4486 | 9 | 11 | 15 |
| Missouri non-MSA | Missouri | Butler | 27 | 3296 | 9 | 8 | 10 |
| St. Louis-Farmington | Missouri | Lincoln | 27 | 4157 | 9 | 11 | 13 |
| Missouri non-MSA | Missouri | Laclede | 64 | 2891 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | Pettis | 71 | 4695 | 8 | 10 | 12 |
| Kansas City | Missouri | Lafayette | 48 | 2470 | 8 | 7 | 8 |
| Joplin | Missouri | Newton | 62 | 3988 | 8 | 8 | 10 |
| Cape Girardeau-Sikeston | Missouri | Scott | 71 | 3724 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Lawrence | 65 | 2697 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Camden | 75 | 3668 | 7 | 7 | 9 |
| St. Louis-Farmington | Illinois | Jersey | 44 | 2414 | 6 | 7 | 10 |
| Missouri non-MSA | Missouri | Phelps | 115 | 2933 | 6 | 5 | 9 |
| Missouri non-MSA | Missouri | Saline | 33 | 2386 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2270 | 5 | 4 | 5 |
| St. Louis-Farmington | Missouri | Warren | 13 | 2032 | 5 | 6 | 8 |
| Missouri non-MSA | Missouri | Ripley | 11 | 828 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Barry | 43 | 2146 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2381 | 4 | 4 | 6 |
| Springfield | Missouri | Webster | 46 | 2964 | 4 | 6 | 10 |
| Missouri non-MSA | Missouri | Stone | 33 | 1975 | 4 | 6 | 7 |
| Kansas City | Missouri | Ray | 22 | 1441 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Audrain | 51 | 2046 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Benton | 23 | 1419 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Marion | 39 | 2613 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Henry | 30 | 1684 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Adair | 11 | 2019 | 3 | 5 | 8 |
| Missouri non-MSA | Missouri | Vernon | 33 | 1357 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Pulaski | 37 | 2944 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Carroll | 21 | 820 | 3 | 3 | 3 |
| Springfield | Missouri | Polk | 26 | 2096 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Livingston | 32 | 1298 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Washington | 42 | 2096 | 3 | 3 | 6 |
| Missouri non-MSA | Missouri | Ozark | 11 | 541 | 3 | 2 | 4 |
| St. Louis-Farmington | Illinois | Bond | 22 | 1831 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Howell | 42 | 2760 | 3 | 4 | 8 |
| Missouri non-MSA | Missouri | Perry | 22 | 2014 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Texas | 21 | 1522 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Wright | 26 | 1351 | 2 | 3 | 5 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1669 | 2 | 3 | 4 |
| Kansas City | Missouri | Clinton | 60 | 1499 | 2 | 3 | 4 |
| Kansas City | Kansas | Miami | 30 | 2522 | 2 | 7 | 14 |
| Missouri non-MSA | Missouri | Pike | 21 | 1472 | 2 | 3 | 4 |
| Kansas City | Missouri | Bates | 19 | 1056 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Crawford | 28 | 2013 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 13 | 1590 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | McDonald | 25 | 1890 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 43 | 1762 | 2 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Osage | 12 | 1378 | 2 | 2 | 4 |
| St. Joseph | Kansas | Doniphan | 17 | 918 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Macon | 12 | 1183 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Miller | 48 | 2298 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Morgan | 37 | 1608 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Barton | 10 | 934 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Daviess | 11 | 581 | 2 | 2 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 467 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1669 | 1 | 2 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1045 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 36 | 856 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Mississippi | 22 | 1234 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Grundy | 32 | 814 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Harrison | 14 | 813 | 1 | 3 | 4 |
| Missouri non-MSA | Missouri | Cedar | 10 | 657 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shannon | 10 | 474 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 6 | 454 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 25 | 1400 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Wayne | 9 | 801 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 572 | 1 | 2 | 2 |
| St. Joseph | Missouri | Andrew | 17 | 1265 | 1 | 2 | 3 |
| Kansas City | Kansas | Linn | 7 | 726 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Randolph | 27 | 1800 | 1 | 1 | 3 |
| Springfield | Missouri | Dallas | 22 | 803 | 1 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 426 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Gentry | 19 | 727 | 1 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 703 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Madison | 15 | 1340 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Linn | 10 | 534 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Dent | 14 | 811 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Douglas | 23 | 755 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 2 | 171 | 1 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 10 | 627 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 556 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 13 | 415 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 527 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 8 | 414 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 26 | 907 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Nodaway | 23 | 2525 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Chariton | 3 | 408 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 244 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 8 | 584 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 10 | 364 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 11 | 463 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 3 | 663 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ralls | 12 | 742 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 6 | 349 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Lewis | 4 | 623 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 139 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 221 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 742 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 175 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 258 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 263 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 3 | 457 | 0 | 0 | 0 |
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
