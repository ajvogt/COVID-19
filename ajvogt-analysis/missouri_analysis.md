# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/19/2021  
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
| St. Louis-Farmington | 4413 | 252829 | 424 | 509 | 740 |
| Kansas City | 2395 | 172671 | 322 | 374 | 565 |
| Missouri non-MSA | 1958 | 109057 | 104 | 137 | 214 |
| Springfield | 589 | 35878 | 39 | 56 | 85 |
| Columbia-Jefferson City | 304 | 34213 | 34 | 43 | 66 |
| Joplin | 276 | 16138 | 20 | 25 | 41 |
| Cape Girardeau-Sikeston | 213 | 12747 | 13 | 21 | 24 |
| St. Joseph | 190 | 10023 | 7 | 9 | 18 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1881 | 86981 | 141 | 174 | 265 |
| Kansas City | Kansas | Johnson | 723 | 52582 | 139 | 156 | 219 |
| Kansas City | Missouri | Jackson | 369 | 29741 | 61 | 68 | 98 |
| St. Louis-Farmington | Illinois | Madison | 447 | 27507 | 54 | 67 | 103 |
| St. Louis-Farmington | Missouri | St. Charles | 405 | 32621 | 54 | 60 | 74 |
| St. Louis-Farmington | Illinois | St. Clair | 454 | 24954 | 52 | 65 | 87 |
| St. Louis-Farmington | Missouri | St. Louis City | 406 | 21131 | 41 | 42 | 52 |
| Kansas City | Missouri | Kansas City | 490 | 36436 | 34 | 39 | 85 |
| Springfield | Missouri | Greene | 414 | 23138 | 27 | 39 | 56 |
| Kansas City | Kansas | Wyandotte | 261 | 18792 | 26 | 34 | 45 |
| St. Louis-Farmington | Missouri | Jefferson | 204 | 18813 | 21 | 27 | 47 |
| Columbia-Jefferson City | Missouri | Boone | 77 | 15763 | 16 | 22 | 35 |
| Kansas City | Kansas | Leavenworth | 73 | 6632 | 16 | 23 | 28 |
| Joplin | Missouri | Jasper | 212 | 12085 | 14 | 19 | 32 |
| St. Louis-Farmington | Missouri | Franklin | 153 | 8322 | 11 | 15 | 21 |
| Kansas City | Missouri | Cass | 84 | 7144 | 11 | 14 | 22 |
| St. Louis-Farmington | Missouri | Lincoln | 31 | 4248 | 9 | 8 | 10 |
| Missouri non-MSA | Missouri | Butler | 33 | 3399 | 9 | 9 | 10 |
| Kansas City | Missouri | Clay | 140 | 7766 | 9 | 13 | 21 |
| St. Louis-Farmington | Missouri | St. Francois | 102 | 7539 | 8 | 8 | 12 |
| Columbia-Jefferson City | Missouri | Callaway | 43 | 4448 | 8 | 7 | 10 |
| St. Louis-Farmington | Illinois | Monroe | 80 | 4005 | 7 | 8 | 13 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 119 | 7473 | 6 | 12 | 14 |
| Springfield | Missouri | Christian | 75 | 6801 | 6 | 9 | 16 |
| Missouri non-MSA | Missouri | Johnson | 43 | 3832 | 6 | 8 | 9 |
| Columbia-Jefferson City | Missouri | Cole | 114 | 8543 | 6 | 9 | 12 |
| St. Louis-Farmington | Illinois | Macoupin | 76 | 4294 | 6 | 7 | 14 |
| Cape Girardeau-Sikeston | Missouri | Scott | 74 | 3783 | 6 | 6 | 6 |
| Kansas City | Kansas | Miami | 34 | 2581 | 5 | 5 | 12 |
| Joplin | Missouri | Newton | 64 | 4053 | 5 | 6 | 8 |
| Kansas City | Missouri | Platte | 42 | 3055 | 5 | 6 | 8 |
| Missouri non-MSA | Missouri | Taney | 82 | 4538 | 5 | 5 | 9 |
| Kansas City | Missouri | Lafayette | 53 | 2520 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Pettis | 75 | 4753 | 4 | 6 | 9 |
| St. Louis-Farmington | Illinois | Bond | 23 | 1876 | 4 | 3 | 4 |
| St. Louis-Farmington | Missouri | Warren | 17 | 2074 | 4 | 4 | 6 |
| St. Louis-Farmington | Illinois | Jersey | 44 | 2466 | 3 | 5 | 8 |
| Missouri non-MSA | Missouri | Lawrence | 71 | 2737 | 3 | 5 | 6 |
| St. Joseph | Missouri | Buchanan | 127 | 6904 | 3 | 5 | 11 |
| Missouri non-MSA | Missouri | Henry | 36 | 1719 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Phelps | 119 | 2966 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 24 | 2554 | 3 | 2 | 2 |
| St. Louis-Farmington | Illinois | Clinton | 88 | 5528 | 3 | 8 | 16 |
| Kansas City | Missouri | Ray | 23 | 1465 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Benton | 25 | 1440 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | McDonald | 25 | 1911 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Saline | 35 | 2409 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Perry | 24 | 2035 | 2 | 2 | 2 |
| Springfield | Missouri | Webster | 49 | 2987 | 2 | 2 | 6 |
| Missouri non-MSA | Missouri | Stone | 35 | 2004 | 2 | 3 | 5 |
| Springfield | Missouri | Polk | 29 | 2135 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2292 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Livingston | 36 | 1320 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Adair | 16 | 2050 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 43 | 2964 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Crawford | 29 | 2032 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Marion | 41 | 2636 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 13 | 1607 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Vernon | 36 | 1376 | 1 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 24 | 1682 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2400 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Camden | 80 | 3693 | 1 | 3 | 6 |
| Missouri non-MSA | Missouri | Barton | 12 | 950 | 1 | 1 | 2 |
| Kansas City | Missouri | Clinton | 63 | 1515 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Audrain | 57 | 2063 | 1 | 2 | 3 |
| St. Joseph | Missouri | Andrew | 17 | 1278 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Howell | 42 | 2787 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Scotland | 3 | 256 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 38 | 870 | 1 | 1 | 2 |
| Springfield | Missouri | Dallas | 22 | 817 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Miller | 49 | 2311 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Clark | 6 | 467 | 1 | 1 | 1 |
| Kansas City | Kansas | Linn | 8 | 740 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Texas | 22 | 1535 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Barry | 44 | 2167 | 1 | 2 | 4 |
| Kansas City | Missouri | Bates | 22 | 1068 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Washington | 45 | 2112 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Macon | 13 | 1196 | 1 | 1 | 4 |
| Missouri non-MSA | Missouri | Carroll | 22 | 832 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Laclede | 64 | 2905 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | Grundy | 34 | 824 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 24 | 1252 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 28 | 1408 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 12 | 1390 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ripley | 14 | 846 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Pike | 21 | 1480 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Randolph | 28 | 1805 | 0 | 0 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 440 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 565 | 0 | 1 | 0 |
| St. Joseph | Kansas | Doniphan | 20 | 926 | 0 | 1 | 2 |
| St. Joseph | Missouri | DeKalb | 26 | 915 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Douglas | 23 | 765 | 0 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 29 | 1677 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 39 | 1619 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Chariton | 6 | 414 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ralls | 12 | 754 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dent | 16 | 815 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Daviess | 11 | 585 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Harrison | 14 | 825 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Monroe | 10 | 588 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 12 | 547 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Wayne | 10 | 814 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 532 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 10 | 634 | 0 | 0 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1051 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 574 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Wright | 27 | 1363 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Linn | 11 | 540 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Oregon | 3 | 671 | 0 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 5 | 710 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 5 | 463 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 177 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 260 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 10 | 476 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 17 | 663 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 140 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 470 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Madison | 16 | 1342 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 745 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 365 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 13 | 416 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 5 | 626 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 223 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 20 | 732 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Hickory | 13 | 465 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 8 | 418 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 175 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 6 | 349 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 3 | 263 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | New Madrid | 45 | 1765 | 0 | 0 | 2 |
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
