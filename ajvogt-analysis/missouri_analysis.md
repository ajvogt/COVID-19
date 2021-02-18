# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/18/2021  
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
| St. Louis-Farmington | 4362 | 252397 | 464 | 538 | 758 |
| Kansas City | 2354 | 172447 | 311 | 382 | 566 |
| Missouri non-MSA | 1900 | 108924 | 116 | 152 | 216 |
| Springfield | 572 | 35834 | 45 | 62 | 87 |
| Columbia-Jefferson City | 289 | 34177 | 36 | 45 | 66 |
| Joplin | 275 | 16104 | 20 | 27 | 41 |
| Cape Girardeau-Sikeston | 210 | 12718 | 14 | 22 | 23 |
| St. Joseph | 190 | 10016 | 7 | 10 | 18 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1873 | 86846 | 158 | 185 | 268 |
| Kansas City | Kansas | Johnson | 723 | 52582 | 139 | 156 | 219 |
| St. Louis-Farmington | Missouri | St. Charles | 396 | 32574 | 62 | 62 | 76 |
| St. Louis-Farmington | Illinois | Madison | 443 | 27452 | 59 | 70 | 106 |
| Kansas City | Missouri | Jackson | 357 | 29614 | 55 | 68 | 96 |
| St. Louis-Farmington | Illinois | St. Clair | 452 | 24889 | 53 | 67 | 89 |
| St. Louis-Farmington | Missouri | St. Louis City | 403 | 21090 | 46 | 45 | 53 |
| Springfield | Missouri | Greene | 403 | 23108 | 31 | 42 | 58 |
| Kansas City | Missouri | Kansas City | 480 | 36393 | 30 | 42 | 87 |
| Kansas City | Kansas | Wyandotte | 261 | 18792 | 26 | 34 | 45 |
| St. Louis-Farmington | Missouri | Jefferson | 196 | 18792 | 23 | 29 | 49 |
| Columbia-Jefferson City | Missouri | Boone | 71 | 15745 | 17 | 22 | 35 |
| Kansas City | Kansas | Leavenworth | 73 | 6632 | 16 | 23 | 28 |
| Joplin | Missouri | Jasper | 212 | 12063 | 15 | 20 | 32 |
| St. Louis-Farmington | Missouri | Franklin | 149 | 8305 | 13 | 15 | 22 |
| Kansas City | Missouri | Cass | 78 | 7130 | 12 | 15 | 23 |
| Missouri non-MSA | Missouri | Butler | 30 | 3392 | 11 | 9 | 10 |
| St. Louis-Farmington | Missouri | Lincoln | 30 | 4238 | 10 | 8 | 11 |
| St. Louis-Farmington | Missouri | St. Francois | 96 | 7536 | 9 | 9 | 12 |
| Kansas City | Missouri | Clay | 137 | 7749 | 9 | 14 | 21 |
| Columbia-Jefferson City | Missouri | Callaway | 39 | 4445 | 8 | 7 | 10 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 116 | 7463 | 8 | 13 | 14 |
| Missouri non-MSA | Missouri | Johnson | 40 | 3817 | 7 | 8 | 9 |
| St. Louis-Farmington | Illinois | Macoupin | 74 | 4288 | 6 | 7 | 15 |
| St. Louis-Farmington | Illinois | Monroe | 80 | 3994 | 6 | 9 | 14 |
| Springfield | Missouri | Christian | 71 | 6791 | 6 | 11 | 17 |
| Columbia-Jefferson City | Missouri | Cole | 111 | 8529 | 6 | 9 | 12 |
| Missouri non-MSA | Missouri | Taney | 77 | 4536 | 5 | 7 | 10 |
| Kansas City | Kansas | Miami | 34 | 2581 | 5 | 5 | 12 |
| Kansas City | Missouri | Platte | 38 | 3050 | 5 | 6 | 8 |
| Missouri non-MSA | Missouri | Lawrence | 68 | 2736 | 4 | 5 | 6 |
| Kansas City | Missouri | Lafayette | 52 | 2514 | 4 | 6 | 7 |
| Cape Girardeau-Sikeston | Missouri | Scott | 74 | 3766 | 4 | 6 | 6 |
| Joplin | Missouri | Newton | 63 | 4041 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Henry | 34 | 1718 | 4 | 3 | 4 |
| St. Louis-Farmington | Illinois | Jersey | 44 | 2459 | 4 | 5 | 8 |
| St. Louis-Farmington | Missouri | Warren | 13 | 2072 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Pettis | 75 | 4745 | 4 | 6 | 9 |
| St. Joseph | Missouri | Buchanan | 127 | 6900 | 4 | 7 | 11 |
| St. Louis-Farmington | Illinois | Bond | 23 | 1865 | 4 | 3 | 4 |
| St. Louis-Farmington | Illinois | Clinton | 88 | 5527 | 3 | 11 | 17 |
| Missouri non-MSA | Missouri | Phelps | 117 | 2959 | 3 | 3 | 5 |
| Springfield | Missouri | Polk | 28 | 2132 | 3 | 3 | 3 |
| Springfield | Missouri | Webster | 48 | 2986 | 3 | 3 | 6 |
| Missouri non-MSA | Missouri | Saline | 34 | 2407 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Adair | 13 | 2048 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Marion | 39 | 2635 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | McDonald | 25 | 1909 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2400 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 24 | 2549 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Pulaski | 40 | 2962 | 2 | 2 | 3 |
| Kansas City | Missouri | Ray | 22 | 1459 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Audrain | 54 | 2064 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Howell | 42 | 2786 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Livingston | 34 | 1319 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Benton | 23 | 1435 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Crawford | 29 | 2032 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Perry | 23 | 2030 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Stone | 35 | 2000 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Camden | 79 | 3692 | 2 | 3 | 6 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2287 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Washington | 45 | 2111 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 13 | 1605 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Vernon | 34 | 1373 | 1 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 23 | 1682 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Barton | 11 | 947 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 36 | 870 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Texas | 21 | 1534 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ripley | 13 | 845 | 1 | 3 | 3 |
| Springfield | Missouri | Dallas | 22 | 817 | 1 | 1 | 2 |
| St. Joseph | Missouri | Andrew | 17 | 1276 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Carroll | 21 | 831 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Morgan | 39 | 1619 | 1 | 1 | 1 |
| Kansas City | Missouri | Clinton | 61 | 1512 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Laclede | 64 | 2904 | 1 | 4 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 26 | 1409 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 12 | 1196 | 1 | 1 | 4 |
| Kansas City | Kansas | Linn | 8 | 740 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 24 | 1247 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Scotland | 3 | 253 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 12 | 1389 | 1 | 1 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 439 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Miller | 48 | 2307 | 1 | 1 | 3 |
| St. Joseph | Missouri | DeKalb | 26 | 914 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Barry | 43 | 2162 | 1 | 3 | 4 |
| Kansas City | Missouri | Bates | 20 | 1065 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Wright | 26 | 1363 | 1 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Moniteau | 28 | 1677 | 0 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 20 | 926 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Grundy | 34 | 821 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 27 | 1805 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 564 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 14 | 824 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Wayne | 10 | 813 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 23 | 764 | 0 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 5 | 710 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 574 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Clark | 6 | 463 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 21 | 1477 | 0 | 1 | 2 |
| Kansas City | Missouri | Caldwell | 10 | 634 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Oregon | 3 | 670 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 5 | 413 | 0 | 0 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1050 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ralls | 12 | 753 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Daviess | 11 | 584 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 745 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 176 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 7 | 531 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 20 | 732 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Monroe | 10 | 587 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 4 | 463 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 12 | 546 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Linn | 11 | 540 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Cedar | 17 | 663 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 260 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 8 | 418 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 12 | 465 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 10 | 476 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 470 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 140 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 15 | 812 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dade | 13 | 416 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 223 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 16 | 1342 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 6 | 349 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 3 | 263 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 364 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 175 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 4 | 624 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | New Madrid | 43 | 1765 | 0 | 1 | 2 |
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
