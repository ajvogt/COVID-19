# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/08/2021  
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
| St. Louis-Farmington | 4153 | 247626 | 696 | 787 | 1059 |
| Kansas City | 2213 | 168752 | 477 | 579 | 773 |
| Missouri non-MSA | 1822 | 107754 | 217 | 235 | 338 |
| Springfield | 553 | 35323 | 85 | 95 | 127 |
| Columbia-Jefferson City | 277 | 33837 | 76 | 76 | 95 |
| Joplin | 270 | 15881 | 45 | 49 | 55 |
| Cape Girardeau-Sikeston | 207 | 12578 | 31 | 28 | 33 |
| St. Joseph | 185 | 9936 | 18 | 20 | 29 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1773 | 85160 | 236 | 286 | 377 |
| Kansas City | Kansas | Johnson | 682 | 50922 | 183 | 216 | 282 |
| St. Louis-Farmington | Illinois | Madison | 438 | 26839 | 95 | 110 | 142 |
| St. Louis-Farmington | Illinois | St. Clair | 439 | 24336 | 94 | 97 | 123 |
| Kansas City | Missouri | Jackson | 327 | 29025 | 86 | 102 | 136 |
| St. Louis-Farmington | Missouri | St. Louis City | 371 | 20701 | 63 | 55 | 71 |
| Kansas City | Missouri | Kansas City | 458 | 36037 | 59 | 92 | 132 |
| St. Louis-Farmington | Missouri | St. Charles | 378 | 31941 | 56 | 65 | 106 |
| Springfield | Missouri | Greene | 388 | 22746 | 56 | 62 | 82 |
| St. Louis-Farmington | Missouri | Jefferson | 183 | 18553 | 46 | 53 | 76 |
| Kansas City | Kansas | Wyandotte | 245 | 18414 | 42 | 47 | 61 |
| Joplin | Missouri | Jasper | 208 | 11895 | 37 | 39 | 44 |
| Columbia-Jefferson City | Missouri | Boone | 69 | 15585 | 36 | 39 | 51 |
| Kansas City | Kansas | Leavenworth | 66 | 6378 | 27 | 29 | 32 |
| Kansas City | Missouri | Clay | 131 | 7656 | 23 | 24 | 33 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 116 | 7385 | 20 | 19 | 20 |
| St. Louis-Farmington | Illinois | Clinton | 85 | 5456 | 19 | 20 | 23 |
| St. Louis-Farmington | Missouri | Franklin | 138 | 8170 | 19 | 22 | 35 |
| Springfield | Missouri | Christian | 71 | 6718 | 19 | 19 | 25 |
| Kansas City | Missouri | Cass | 72 | 6997 | 17 | 21 | 35 |
| Columbia-Jefferson City | Missouri | Cole | 107 | 8464 | 15 | 15 | 17 |
| Columbia-Jefferson City | Missouri | Callaway | 37 | 4373 | 15 | 12 | 12 |
| St. Louis-Farmington | Illinois | Monroe | 75 | 3917 | 15 | 17 | 18 |
| St. Louis-Farmington | Missouri | St. Francois | 92 | 7454 | 12 | 13 | 18 |
| St. Joseph | Missouri | Buchanan | 126 | 6851 | 12 | 12 | 18 |
| St. Louis-Farmington | Illinois | Macoupin | 73 | 4213 | 11 | 14 | 24 |
| Kansas City | Missouri | Platte | 37 | 3001 | 10 | 11 | 12 |
| Missouri non-MSA | Missouri | Johnson | 38 | 3746 | 10 | 9 | 12 |
| Missouri non-MSA | Missouri | Pettis | 71 | 4690 | 9 | 10 | 13 |
| Missouri non-MSA | Missouri | Taney | 73 | 4478 | 9 | 11 | 16 |
| Missouri non-MSA | Missouri | Butler | 27 | 3294 | 9 | 9 | 11 |
| St. Louis-Farmington | Missouri | Lincoln | 27 | 4151 | 9 | 11 | 13 |
| Missouri non-MSA | Missouri | Laclede | 64 | 2891 | 8 | 7 | 8 |
| Kansas City | Missouri | Lafayette | 48 | 2467 | 8 | 7 | 9 |
| Joplin | Missouri | Newton | 62 | 3986 | 7 | 9 | 10 |
| Missouri non-MSA | Missouri | Camden | 75 | 3668 | 7 | 7 | 11 |
| Cape Girardeau-Sikeston | Missouri | Scott | 71 | 3723 | 7 | 6 | 8 |
| St. Louis-Farmington | Illinois | Jersey | 44 | 2408 | 7 | 7 | 10 |
| Missouri non-MSA | Missouri | Saline | 33 | 2384 | 7 | 6 | 8 |
| Missouri non-MSA | Missouri | Lawrence | 65 | 2689 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Phelps | 115 | 2928 | 6 | 5 | 9 |
| Missouri non-MSA | Missouri | Stone | 33 | 1973 | 6 | 7 | 8 |
| St. Louis-Farmington | Missouri | Warren | 13 | 2029 | 5 | 6 | 8 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2268 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Ripley | 11 | 826 | 5 | 4 | 4 |
| Kansas City | Kansas | Miami | 30 | 2517 | 5 | 9 | 14 |
| Springfield | Missouri | Webster | 46 | 2963 | 4 | 6 | 11 |
| Missouri non-MSA | Missouri | Barry | 43 | 2143 | 4 | 5 | 8 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2378 | 4 | 4 | 7 |
| Kansas City | Missouri | Ray | 22 | 1440 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Henry | 30 | 1683 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Benton | 23 | 1417 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Vernon | 33 | 1356 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Marion | 39 | 2612 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Carroll | 21 | 818 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Audrain | 51 | 2044 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Adair | 11 | 2017 | 3 | 5 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 37 | 2941 | 3 | 3 | 6 |
| Missouri non-MSA | Missouri | Livingston | 32 | 1295 | 3 | 4 | 6 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1667 | 3 | 3 | 4 |
| Springfield | Missouri | Polk | 26 | 2094 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Howell | 42 | 2760 | 3 | 4 | 8 |
| Kansas City | Missouri | Clinton | 60 | 1497 | 3 | 3 | 4 |
| St. Louis-Farmington | Illinois | Bond | 22 | 1831 | 3 | 3 | 6 |
| Missouri non-MSA | Missouri | Texas | 21 | 1521 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Washington | 42 | 2091 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Ozark | 11 | 540 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Wright | 26 | 1350 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Crawford | 28 | 2011 | 3 | 4 | 6 |
| Kansas City | Missouri | Bates | 19 | 1054 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Perry | 22 | 2012 | 2 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Osage | 12 | 1378 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Macon | 12 | 1183 | 2 | 3 | 6 |
| St. Joseph | Kansas | Doniphan | 16 | 913 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Daviess | 11 | 581 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Pike | 21 | 1469 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Morgan | 37 | 1608 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 13 | 1588 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | McDonald | 25 | 1888 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Miller | 48 | 2298 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 43 | 1762 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Barton | 10 | 934 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Harrison | 14 | 813 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Grundy | 32 | 814 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Shannon | 10 | 474 | 2 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 467 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1669 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 25 | 1400 | 2 | 2 | 2 |
| St. Joseph | Missouri | Andrew | 17 | 1265 | 2 | 2 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1044 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 22 | 1234 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Clark | 6 | 454 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 36 | 854 | 1 | 2 | 4 |
| Springfield | Missouri | Dallas | 22 | 802 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 10 | 656 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 571 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 23 | 755 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Randolph | 27 | 1799 | 1 | 2 | 4 |
| Kansas City | Kansas | Linn | 6 | 721 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Wayne | 9 | 800 | 1 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 426 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Gentry | 19 | 727 | 1 | 1 | 2 |
| Kansas City | Missouri | Caldwell | 10 | 626 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Madison | 15 | 1340 | 1 | 1 | 2 |
| St. Joseph | Missouri | DeKalb | 26 | 907 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Linn | 10 | 533 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Maries | 7 | 527 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 2 | 170 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 14 | 810 | 1 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 701 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 12 | 742 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 3 | 408 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 8 | 414 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 555 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 13 | 415 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Oregon | 3 | 663 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Nodaway | 23 | 2525 | 0 | 2 | 3 |
| Missouri non-MSA | Missouri | Monroe | 8 | 583 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Holt | 10 | 363 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 221 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 11 | 463 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 175 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 4 | 623 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 6 | 349 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 742 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 242 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 258 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 138 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 263 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 3 | 456 | 0 | 0 | 0 |
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
