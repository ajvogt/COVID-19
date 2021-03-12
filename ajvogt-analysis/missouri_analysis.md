# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 03/11/2021  
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
| St. Louis-Farmington | 4756 | 259563 | 314 | 325 | 385 |
| Kansas City | 2568 | 177824 | 176 | 184 | 287 |
| Missouri non-MSA | 2088 | 110709 | 77 | 78 | 95 |
| Springfield | 635 | 36570 | 29 | 32 | 40 |
| Columbia-Jefferson City | 327 | 34670 | 23 | 21 | 26 |
| Joplin | 295 | 16403 | 11 | 11 | 16 |
| St. Joseph | 203 | 10150 | 6 | 5 | 6 |
| Cape Girardeau-Sikeston | 231 | 12893 | 3 | 6 | 10 |
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
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 82076 | 236 | 245 | 292 |
| St. Louis-Farmington | Missouri | St. Louis | 2044 | 89767 | 141 | 131 | 150 |
| Kansas City | Kansas | Johnson | 756 | 55084 | 78 | 77 | 131 |
| St. Louis-Farmington | Illinois | St. Clair | 477 | 25874 | 43 | 46 | 49 |
| St. Louis-Farmington | Illinois | Madison | 467 | 28360 | 36 | 41 | 48 |
| St. Louis-Farmington | Missouri | St. Louis City | 436 | 21744 | 28 | 32 | 33 |
| Kansas City | Missouri | Kansas City | 544 | 36890 | 23 | 20 | 27 |
| St. Louis-Farmington | Missouri | St. Charles | 436 | 33156 | 22 | 26 | 39 |
| Kansas City | Missouri | Jackson | 392 | 30343 | 21 | 23 | 42 |
| Springfield | Missouri | Greene | 443 | 23603 | 17 | 21 | 27 |
| Kansas City | Kansas | Wyandotte | 273 | 19375 | 13 | 18 | 30 |
| Columbia-Jefferson City | Missouri | Boone | 84 | 16003 | 13 | 10 | 13 |
| Kansas City | Kansas | Leavenworth | 83 | 6895 | 12 | 11 | 14 |
| St. Louis-Farmington | Missouri | Jefferson | 229 | 19109 | 11 | 13 | 17 |
| Joplin | Missouri | Jasper | 226 | 12298 | 8 | 8 | 12 |
| Missouri non-MSA | Missouri | Butler | 37 | 3573 | 8 | 8 | 9 |
| Kansas City | Missouri | Cass | 92 | 7322 | 7 | 8 | 10 |
| Kansas City | Missouri | Clay | 153 | 7973 | 7 | 8 | 10 |
| St. Louis-Farmington | Missouri | Franklin | 168 | 8480 | 6 | 6 | 9 |
| St. Louis-Farmington | Illinois | Macoupin | 80 | 4407 | 6 | 5 | 6 |
| Springfield | Missouri | Polk | 31 | 2210 | 5 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Callaway | 46 | 4535 | 4 | 4 | 5 |
| Springfield | Missouri | Christian | 84 | 6923 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Pettis | 77 | 4823 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Phelps | 123 | 3055 | 4 | 4 | 4 |
| St. Louis-Farmington | Missouri | Lincoln | 39 | 4334 | 4 | 4 | 5 |
| St. Louis-Farmington | Missouri | St. Francois | 109 | 7620 | 4 | 3 | 5 |
| St. Louis-Farmington | Illinois | Monroe | 89 | 4099 | 4 | 4 | 5 |
| Kansas City | Missouri | Platte | 44 | 3148 | 3 | 4 | 4 |
| St. Joseph | Missouri | Buchanan | 136 | 6984 | 3 | 3 | 4 |
| Kansas City | Missouri | Lafayette | 57 | 2597 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Johnson | 47 | 3894 | 3 | 2 | 4 |
| Columbia-Jefferson City | Missouri | Cole | 120 | 8615 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Taney | 91 | 4613 | 3 | 3 | 4 |
| Joplin | Missouri | Newton | 69 | 4105 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Nodaway | 25 | 2600 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 8 | 608 | 2 | 2 | 1 |
| St. Louis-Farmington | Illinois | Clinton | 89 | 5596 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Benton | 27 | 1469 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Crawford | 34 | 2072 | 2 | 1 | 1 |
| Cape Girardeau-Sikeston | Missouri | Scott | 79 | 3855 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Stoddard | 37 | 2327 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Marion | 42 | 2659 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Howell | 42 | 2837 | 1 | 1 | 2 |
| St. Joseph | Kansas | Doniphan | 22 | 954 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 30 | 1826 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Laclede | 66 | 2936 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Lawrence | 77 | 2773 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Vernon | 40 | 1405 | 1 | 1 | 1 |
| St. Louis-Farmington | Missouri | Warren | 20 | 2109 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Pulaski | 49 | 3000 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Stone | 39 | 2039 | 1 | 1 | 2 |
| Kansas City | Missouri | Ray | 25 | 1526 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 42 | 888 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | McDonald | 26 | 1935 | 1 | 1 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 47 | 2505 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Barry | 45 | 2204 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 131 | 7532 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Camden | 82 | 3740 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 15 | 1627 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 5 | 283 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | New Madrid | 45 | 1777 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Perry | 27 | 2057 | 1 | 1 | 1 |
| Springfield | Missouri | Webster | 53 | 3003 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Adair | 18 | 2088 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Miller | 51 | 2326 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 14 | 1411 | 1 | 0 | 1 |
| Kansas City | Kansas | Linn | 8 | 759 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 23 | 1494 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Saline | 39 | 2436 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 42 | 1632 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 29 | 1371 | 0 | 0 | 0 |
| Kansas City | Missouri | Clinton | 65 | 1530 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 541 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mississippi | 25 | 1277 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 38 | 1754 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Audrain | 57 | 2082 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 573 | 0 | 0 | 0 |
| Kansas City | Missouri | Bates | 24 | 1091 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 12 | 974 | 0 | 0 | 1 |
| Springfield | Missouri | Dallas | 24 | 831 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Cooper | 27 | 1698 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 27 | 925 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dunklin | 19 | 2416 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Cedar | 19 | 707 | 0 | 2 | 1 |
| Missouri non-MSA | Missouri | Carter | 9 | 428 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 23 | 839 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 14 | 859 | 0 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 7 | 726 | 0 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 18 | 1287 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 181 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 16 | 553 | 0 | 0 | 0 |
| Kansas City | Kansas | Miami | 41 | 2648 | 0 | 2 | 4 |
| Missouri non-MSA | Missouri | Washington | 48 | 2124 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 27 | 774 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 16 | 1349 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 15 | 1216 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Texas | 22 | 1546 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 11 | 643 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 6 | 425 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 7 | 357 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 484 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 10 | 633 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 9 | 453 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 369 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 12 | 547 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 17 | 823 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1919 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Monroe | 11 | 599 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 12 | 759 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 37 | 1332 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Wayne | 11 | 822 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 29 | 1682 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 14 | 748 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 3 | 678 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 261 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 11 | 588 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 34 | 830 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 21 | 735 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 12 | 483 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Pemiscot | 29 | 1413 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 5 | 465 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 143 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 179 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 263 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 6 | 472 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 14 | 467 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1053 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 14 | 420 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 14 | 823 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 4 | 225 | 0 | 0 | 0 |
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
