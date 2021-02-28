# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/28/2021  
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
| St. Louis-Farmington | 4568 | 256162 | 352 | 371 | 525 |
| Kansas City | 2482 | 175841 | 225 | 339 | 409 |
| Missouri non-MSA | 2011 | 109983 | 104 | 102 | 150 |
| Springfield | 612 | 36246 | 41 | 37 | 59 |
| Columbia-Jefferson City | 310 | 34449 | 24 | 27 | 46 |
| Joplin | 285 | 16296 | 18 | 17 | 29 |
| Cape Girardeau-Sikeston | 221 | 12844 | 10 | 11 | 18 |
| St. Joseph | 201 | 10095 | 6 | 7 | 11 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1969 | 88294 | 135 | 137 | 182 |
| Kansas City | Kansas | Johnson | 744 | 54224 | 81 | 168 | 165 |
| St. Louis-Farmington | Illinois | Madison | 454 | 27949 | 47 | 48 | 70 |
| St. Louis-Farmington | Illinois | St. Clair | 466 | 25391 | 46 | 47 | 66 |
| Kansas City | Missouri | Jackson | 381 | 30116 | 38 | 47 | 70 |
| St. Louis-Farmington | Missouri | St. Charles | 413 | 32909 | 34 | 37 | 54 |
| Kansas City | Kansas | Wyandotte | 266 | 19161 | 32 | 36 | 37 |
| Springfield | Missouri | Greene | 427 | 23392 | 27 | 26 | 40 |
| St. Louis-Farmington | Missouri | St. Louis City | 421 | 21389 | 25 | 31 | 46 |
| St. Louis-Farmington | Missouri | Jefferson | 210 | 18984 | 19 | 19 | 31 |
| Kansas City | Missouri | Kansas City | 515 | 36639 | 16 | 27 | 52 |
| Joplin | Missouri | Jasper | 219 | 12219 | 15 | 13 | 23 |
| Kansas City | Kansas | Leavenworth | 77 | 6765 | 12 | 15 | 21 |
| Kansas City | Missouri | Clay | 144 | 7891 | 12 | 12 | 16 |
| Columbia-Jefferson City | Missouri | Boone | 80 | 15890 | 11 | 13 | 23 |
| Missouri non-MSA | Missouri | Butler | 34 | 3497 | 11 | 10 | 9 |
| Kansas City | Missouri | Cass | 89 | 7238 | 10 | 10 | 15 |
| St. Louis-Farmington | Missouri | Franklin | 154 | 8415 | 9 | 10 | 14 |
| Springfield | Missouri | Christian | 78 | 6873 | 7 | 7 | 11 |
| Kansas City | Missouri | Platte | 42 | 3115 | 6 | 5 | 7 |
| Missouri non-MSA | Missouri | Taney | 88 | 4584 | 6 | 5 | 6 |
| St. Louis-Farmington | Illinois | Monroe | 83 | 4063 | 5 | 6 | 10 |
| Columbia-Jefferson City | Missouri | Callaway | 43 | 4492 | 5 | 6 | 8 |
| Kansas City | Kansas | Miami | 41 | 2629 | 5 | 5 | 5 |
| Cape Girardeau-Sikeston | Missouri | Scott | 76 | 3830 | 5 | 5 | 5 |
| St. Louis-Farmington | Missouri | St. Francois | 104 | 7585 | 5 | 6 | 8 |
| Missouri non-MSA | Missouri | Johnson | 45 | 3876 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Cedar | 18 | 702 | 5 | 2 | 2 |
| Missouri non-MSA | Missouri | Phelps | 121 | 3018 | 5 | 4 | 4 |
| St. Louis-Farmington | Illinois | Macoupin | 79 | 4347 | 5 | 5 | 8 |
| Missouri non-MSA | Missouri | Pettis | 76 | 4786 | 4 | 3 | 6 |
| St. Louis-Farmington | Illinois | Clinton | 89 | 5571 | 4 | 3 | 10 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 125 | 7515 | 4 | 5 | 10 |
| St. Joseph | Missouri | Buchanan | 135 | 6953 | 4 | 4 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 36 | 4293 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Howell | 42 | 2817 | 3 | 2 | 3 |
| Kansas City | Missouri | Lafayette | 54 | 2553 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Camden | 81 | 3723 | 3 | 2 | 4 |
| Springfield | Missouri | Polk | 30 | 2161 | 3 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Cole | 114 | 8572 | 3 | 4 | 9 |
| Missouri non-MSA | Missouri | Adair | 16 | 2076 | 3 | 2 | 3 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1907 | 3 | 3 | 3 |
| Joplin | Missouri | Newton | 66 | 4077 | 2 | 3 | 5 |
| St. Louis-Farmington | Illinois | Jersey | 46 | 2493 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 72 | 2760 | 2 | 2 | 4 |
| Kansas City | Missouri | Ray | 24 | 1516 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Pulaski | 44 | 2990 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Henry | 36 | 1742 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Stone | 37 | 2029 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Barry | 44 | 2190 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Crawford | 30 | 2049 | 2 | 1 | 2 |
| St. Louis-Farmington | Missouri | Warren | 18 | 2094 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2309 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 24 | 1268 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Perry | 26 | 2049 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Laclede | 66 | 2920 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Vernon | 40 | 1395 | 1 | 1 | 2 |
| Kansas City | Missouri | Bates | 23 | 1081 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Macon | 14 | 1211 | 1 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 5 | 722 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Saline | 35 | 2424 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | McDonald | 26 | 1921 | 1 | 1 | 2 |
| St. Joseph | Kansas | Doniphan | 22 | 939 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dunklin | 19 | 2413 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 583 | 1 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Cooper | 26 | 1693 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Livingston | 37 | 1331 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Barton | 12 | 963 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 10 | 597 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 13 | 1401 | 1 | 1 | 1 |
| Springfield | Missouri | Webster | 53 | 2995 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Audrain | 58 | 2074 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Carter | 8 | 424 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Randolph | 29 | 1813 | 1 | 0 | 1 |
| Springfield | Missouri | Dallas | 24 | 825 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Benton | 26 | 1450 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Chariton | 6 | 422 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Texas | 22 | 1541 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Marion | 41 | 2646 | 1 | 1 | 2 |
| Kansas City | Missouri | Clinton | 64 | 1525 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Wayne | 10 | 819 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Washington | 46 | 2122 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Scotland | 3 | 263 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 15 | 1617 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 7 | 354 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 3 | 268 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | New Madrid | 45 | 1769 | 0 | 0 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 447 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 39 | 877 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 478 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 12 | 758 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 8 | 747 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dent | 16 | 820 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Nodaway | 24 | 2559 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Ripley | 14 | 854 | 0 | 0 | 2 |
| St. Joseph | Missouri | Andrew | 17 | 1283 | 0 | 0 | 1 |
| St. Joseph | Missouri | DeKalb | 27 | 920 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Oregon | 3 | 676 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Pemiscot | 28 | 1412 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Miller | 49 | 2315 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 13 | 550 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 536 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 16 | 1345 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 25 | 768 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 179 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 10 | 481 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 23 | 835 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dade | 13 | 419 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 6 | 471 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Morgan | 40 | 1622 | 0 | 0 | 1 |
| Kansas City | Missouri | Caldwell | 10 | 641 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Pike | 22 | 1485 | 0 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 29 | 1679 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Lewis | 7 | 630 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 11 | 587 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 3 | 225 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 12 | 542 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 142 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1052 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 13 | 467 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 20 | 734 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 34 | 828 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Harrison | 14 | 827 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 14 | 746 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 366 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 5 | 464 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 260 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 177 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 567 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 29 | 1364 | 0 | 0 | 1 |
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
