# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/27/2021  
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
| St. Louis-Farmington | 4562 | 255846 | 370 | 384 | 557 |
| Kansas City | 2481 | 175778 | 242 | 345 | 418 |
| Missouri non-MSA | 2008 | 109865 | 99 | 99 | 158 |
| Springfield | 612 | 36209 | 41 | 37 | 62 |
| Columbia-Jefferson City | 310 | 34416 | 25 | 27 | 49 |
| Joplin | 282 | 16288 | 19 | 18 | 31 |
| Cape Girardeau-Sikeston | 221 | 12826 | 8 | 11 | 19 |
| St. Joseph | 201 | 10090 | 7 | 7 | 12 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1965 | 88203 | 146 | 143 | 204 |
| Kansas City | Kansas | Johnson | 744 | 54224 | 81 | 168 | 165 |
| St. Louis-Farmington | Illinois | Madison | 453 | 27896 | 47 | 50 | 73 |
| St. Louis-Farmington | Illinois | St. Clair | 466 | 25341 | 45 | 48 | 68 |
| Kansas City | Missouri | Jackson | 380 | 30082 | 42 | 49 | 73 |
| St. Louis-Farmington | Missouri | St. Charles | 413 | 32878 | 35 | 39 | 55 |
| Kansas City | Kansas | Wyandotte | 266 | 19161 | 32 | 36 | 37 |
| St. Louis-Farmington | Missouri | St. Louis City | 420 | 21349 | 31 | 31 | 44 |
| Springfield | Missouri | Greene | 427 | 23370 | 28 | 26 | 43 |
| Kansas City | Missouri | Kansas City | 515 | 36643 | 22 | 30 | 56 |
| St. Louis-Farmington | Missouri | Jefferson | 210 | 18967 | 19 | 19 | 33 |
| Joplin | Missouri | Jasper | 216 | 12212 | 16 | 14 | 25 |
| Kansas City | Missouri | Clay | 144 | 7884 | 15 | 12 | 17 |
| Columbia-Jefferson City | Missouri | Boone | 80 | 15885 | 14 | 14 | 24 |
| Kansas City | Kansas | Leavenworth | 77 | 6765 | 12 | 15 | 21 |
| Missouri non-MSA | Missouri | Butler | 34 | 3478 | 10 | 9 | 9 |
| St. Louis-Farmington | Missouri | Franklin | 154 | 8409 | 9 | 11 | 16 |
| Kansas City | Missouri | Cass | 89 | 7223 | 9 | 10 | 15 |
| Springfield | Missouri | Christian | 78 | 6864 | 7 | 7 | 11 |
| Kansas City | Missouri | Platte | 42 | 3111 | 7 | 5 | 8 |
| St. Louis-Farmington | Illinois | Monroe | 83 | 4058 | 6 | 6 | 10 |
| Missouri non-MSA | Missouri | Phelps | 121 | 3018 | 6 | 4 | 5 |
| Kansas City | Missouri | Ray | 24 | 1512 | 6 | 4 | 4 |
| Missouri non-MSA | Missouri | Taney | 88 | 4579 | 5 | 5 | 7 |
| St. Louis-Farmington | Missouri | St. Francois | 104 | 7582 | 5 | 6 | 9 |
| Missouri non-MSA | Missouri | Johnson | 45 | 3871 | 5 | 5 | 8 |
| St. Louis-Farmington | Illinois | Macoupin | 79 | 4344 | 5 | 6 | 9 |
| Kansas City | Kansas | Miami | 41 | 2629 | 5 | 5 | 5 |
| St. Joseph | Missouri | Buchanan | 135 | 6949 | 4 | 4 | 8 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 125 | 7510 | 4 | 5 | 11 |
| Kansas City | Missouri | Lafayette | 54 | 2553 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Pettis | 76 | 4783 | 4 | 3 | 6 |
| St. Louis-Farmington | Illinois | Clinton | 89 | 5566 | 4 | 3 | 10 |
| St. Louis-Farmington | Missouri | Lincoln | 36 | 4289 | 4 | 7 | 8 |
| Columbia-Jefferson City | Missouri | Callaway | 43 | 4478 | 4 | 5 | 8 |
| Missouri non-MSA | Missouri | Howell | 42 | 2816 | 3 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Cole | 114 | 8568 | 3 | 4 | 9 |
| Springfield | Missouri | Polk | 30 | 2156 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Adair | 16 | 2074 | 3 | 2 | 3 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1902 | 3 | 3 | 3 |
| Cape Girardeau-Sikeston | Missouri | Scott | 76 | 3816 | 3 | 5 | 5 |
| St. Louis-Farmington | Illinois | Jersey | 46 | 2492 | 3 | 3 | 5 |
| Joplin | Missouri | Newton | 66 | 4076 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Camden | 81 | 3718 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Pulaski | 44 | 2988 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Stone | 37 | 2028 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Henry | 36 | 1741 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Lawrence | 71 | 2755 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Crawford | 30 | 2048 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Barry | 44 | 2187 | 2 | 1 | 3 |
| St. Louis-Farmington | Missouri | Warren | 18 | 2092 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Saline | 35 | 2424 | 1 | 1 | 4 |
| Missouri non-MSA | Missouri | Barton | 12 | 963 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Laclede | 66 | 2919 | 1 | 1 | 4 |
| Missouri non-MSA | Missouri | McDonald | 26 | 1922 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Macon | 14 | 1211 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2306 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Perry | 26 | 2046 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 24 | 1266 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dunklin | 19 | 2412 | 1 | 1 | 2 |
| St. Joseph | Kansas | Doniphan | 22 | 939 | 1 | 1 | 1 |
| Kansas City | Missouri | Bates | 23 | 1078 | 1 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Osage | 13 | 1401 | 1 | 1 | 2 |
| Springfield | Missouri | Dallas | 24 | 826 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Livingston | 37 | 1330 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Vernon | 39 | 1391 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 15 | 1617 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Audrain | 58 | 2073 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Benton | 26 | 1450 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Monroe | 10 | 596 | 1 | 0 | 0 |
| Springfield | Missouri | Webster | 53 | 2993 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Marion | 41 | 2645 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Randolph | 29 | 1812 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 263 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Carter | 8 | 424 | 1 | 0 | 0 |
| Kansas City | Missouri | Clinton | 64 | 1525 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Chariton | 6 | 421 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Cooper | 26 | 1689 | 0 | 1 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 478 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 580 | 0 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 5 | 716 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Texas | 22 | 1541 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Washington | 46 | 2118 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Wayne | 10 | 819 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ripley | 14 | 854 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 3 | 268 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 447 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 39 | 876 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dent | 16 | 820 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Cedar | 17 | 671 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | New Madrid | 45 | 1768 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ralls | 12 | 758 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Nodaway | 24 | 2559 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Oregon | 3 | 676 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 8 | 747 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Pemiscot | 28 | 1412 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Miller | 49 | 2315 | 0 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 27 | 920 | 0 | 0 | 1 |
| Kansas City | Missouri | Caldwell | 10 | 641 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 7 | 353 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 179 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 34 | 828 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Douglas | 25 | 768 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 10 | 481 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 6 | 472 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 22 | 1485 | 0 | 0 | 1 |
| St. Joseph | Missouri | Andrew | 17 | 1282 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 13 | 550 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dade | 13 | 419 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 11 | 587 | 0 | 0 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1053 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 142 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 23 | 834 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Harrison | 14 | 828 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 567 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 29 | 1679 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 535 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Morgan | 40 | 1621 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 3 | 225 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 20 | 734 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 14 | 746 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 16 | 1343 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 12 | 541 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 7 | 629 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 5 | 464 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 13 | 467 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 260 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 177 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 366 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 29 | 1364 | 0 | 0 | 2 |
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
