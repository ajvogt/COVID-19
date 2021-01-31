# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/31/2021  
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
| St. Louis-Farmington | 4131 | 242124 | 903 | 1032 | 1325 |
| Kansas City | 2102 | 165183 | 764 | 830 | 995 |
| Missouri non-MSA | 1708 | 106034 | 273 | 296 | 461 |
| Springfield | 534 | 34665 | 113 | 118 | 185 |
| Columbia-Jefferson City | 261 | 33217 | 79 | 82 | 123 |
| Joplin | 255 | 15529 | 53 | 53 | 68 |
| Cape Girardeau-Sikeston | 201 | 12341 | 27 | 26 | 42 |
| St. Joseph | 175 | 9786 | 24 | 26 | 39 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1686 | 83346 | 367 | 380 | 462 |
| Kansas City | Kansas | Johnson | 655 | 49641 | 249 | 333 | 359 |
| Kansas City | Missouri | Kansas City | 440 | 35521 | 159 | 140 | 182 |
| Kansas City | Missouri | Jackson | 308 | 28363 | 149 | 132 | 164 |
| St. Louis-Farmington | Illinois | Madison | 500 | 26033 | 119 | 145 | 165 |
| St. Louis-Farmington | Illinois | St. Clair | 472 | 23617 | 101 | 119 | 152 |
| St. Louis-Farmington | Missouri | St. Charles | 344 | 31463 | 78 | 97 | 144 |
| Springfield | Missouri | Greene | 380 | 22314 | 73 | 77 | 119 |
| St. Louis-Farmington | Missouri | Jefferson | 170 | 18178 | 61 | 71 | 102 |
| Kansas City | Kansas | Wyandotte | 230 | 18114 | 51 | 64 | 84 |
| Columbia-Jefferson City | Missouri | Boone | 61 | 15278 | 44 | 48 | 64 |
| St. Louis-Farmington | Missouri | St. Louis City | 350 | 20219 | 43 | 62 | 91 |
| Joplin | Missouri | Jasper | 195 | 11601 | 42 | 43 | 53 |
| Kansas City | Missouri | Cass | 69 | 6862 | 37 | 32 | 43 |
| Kansas City | Kansas | Leavenworth | 59 | 6186 | 31 | 37 | 38 |
| Kansas City | Missouri | Clay | 124 | 7469 | 29 | 28 | 39 |
| St. Louis-Farmington | Missouri | Franklin | 131 | 8018 | 27 | 32 | 48 |
| Springfield | Missouri | Christian | 63 | 6569 | 21 | 23 | 37 |
| St. Louis-Farmington | Illinois | Clinton | 91 | 5305 | 20 | 23 | 27 |
| St. Louis-Farmington | Illinois | Monroe | 72 | 3803 | 19 | 19 | 22 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 110 | 7226 | 18 | 16 | 25 |
| St. Louis-Farmington | Illinois | Macoupin | 101 | 4127 | 17 | 23 | 28 |
| St. Joseph | Missouri | Buchanan | 122 | 6752 | 15 | 16 | 24 |
| Columbia-Jefferson City | Missouri | Cole | 104 | 8342 | 14 | 14 | 24 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 4078 | 14 | 14 | 18 |
| Missouri non-MSA | Missouri | Taney | 68 | 4403 | 14 | 15 | 21 |
| Kansas City | Kansas | Miami | 28 | 2482 | 14 | 19 | 22 |
| St. Louis-Farmington | Missouri | St. Francois | 83 | 7342 | 12 | 14 | 26 |
| Kansas City | Missouri | Platte | 36 | 2912 | 12 | 10 | 16 |
| Missouri non-MSA | Missouri | Pettis | 69 | 4617 | 10 | 11 | 18 |
| Joplin | Missouri | Newton | 60 | 3928 | 10 | 10 | 15 |
| Springfield | Missouri | Webster | 46 | 2926 | 10 | 10 | 16 |
| Columbia-Jefferson City | Missouri | Callaway | 34 | 4258 | 9 | 9 | 16 |
| Missouri non-MSA | Missouri | Johnson | 35 | 3667 | 9 | 10 | 15 |
| Missouri non-MSA | Missouri | Butler | 24 | 3223 | 9 | 10 | 13 |
| Missouri non-MSA | Missouri | Camden | 74 | 3608 | 8 | 8 | 15 |
| Missouri non-MSA | Missouri | Laclede | 58 | 2826 | 8 | 7 | 11 |
| Kansas City | Missouri | Lafayette | 46 | 2401 | 8 | 9 | 11 |
| St. Louis-Farmington | Illinois | Jersey | 63 | 2351 | 8 | 11 | 12 |
| Missouri non-MSA | Missouri | Stone | 32 | 1925 | 8 | 6 | 10 |
| St. Louis-Farmington | Missouri | Warren | 12 | 1983 | 7 | 9 | 11 |
| Kansas City | Missouri | Ray | 19 | 1407 | 7 | 7 | 9 |
| Missouri non-MSA | Missouri | Adair | 7 | 1983 | 7 | 8 | 12 |
| Missouri non-MSA | Missouri | Lawrence | 61 | 2639 | 7 | 7 | 11 |
| Missouri non-MSA | Missouri | Howell | 41 | 2736 | 7 | 7 | 14 |
| Missouri non-MSA | Missouri | Henry | 28 | 1650 | 6 | 5 | 7 |
| Missouri non-MSA | Missouri | Saline | 30 | 2331 | 6 | 7 | 11 |
| Cape Girardeau-Sikeston | Missouri | Scott | 71 | 3672 | 6 | 6 | 11 |
| Missouri non-MSA | Missouri | Washington | 41 | 2066 | 6 | 6 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2228 | 6 | 5 | 7 |
| Missouri non-MSA | Missouri | Audrain | 50 | 2014 | 6 | 5 | 7 |
| Missouri non-MSA | Missouri | Harrison | 12 | 792 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Barry | 41 | 2103 | 5 | 5 | 10 |
| Missouri non-MSA | Missouri | Phelps | 107 | 2882 | 5 | 7 | 13 |
| Missouri non-MSA | Missouri | Macon | 10 | 1161 | 5 | 7 | 8 |
| Missouri non-MSA | Missouri | Livingston | 32 | 1267 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Crawford | 24 | 1983 | 5 | 5 | 9 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2344 | 5 | 6 | 8 |
| St. Joseph | Kansas | Doniphan | 12 | 894 | 5 | 4 | 5 |
| Kansas City | Missouri | Bates | 16 | 1030 | 5 | 4 | 6 |
| Springfield | Missouri | Polk | 25 | 2067 | 5 | 3 | 9 |
| Missouri non-MSA | Missouri | Wright | 24 | 1326 | 4 | 5 | 8 |
| Kansas City | Kansas | Linn | 4 | 710 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Carroll | 18 | 786 | 4 | 4 | 4 |
| Kansas City | Missouri | Clinton | 60 | 1468 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2521 | 4 | 4 | 7 |
| St. Louis-Farmington | Illinois | Bond | 27 | 1808 | 4 | 5 | 8 |
| Missouri non-MSA | Missouri | Miller | 45 | 2278 | 4 | 4 | 8 |
| Columbia-Jefferson City | Missouri | Osage | 10 | 1355 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 12 | 1567 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | McDonald | 24 | 1869 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | Mississippi | 21 | 1220 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Pulaski | 34 | 2906 | 3 | 4 | 12 |
| Missouri non-MSA | Missouri | Barton | 9 | 918 | 3 | 2 | 5 |
| Missouri non-MSA | Missouri | Benton | 20 | 1387 | 3 | 3 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 33 | 841 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Pike | 17 | 1445 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | St. Clair | 6 | 555 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 10 | 563 | 3 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1640 | 3 | 2 | 4 |
| Springfield | Missouri | Dallas | 20 | 789 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Ripley | 10 | 784 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Vernon | 32 | 1327 | 2 | 3 | 8 |
| Missouri non-MSA | Missouri | Linn | 10 | 523 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Cedar | 9 | 642 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Dent | 11 | 799 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 41 | 1741 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Wayne | 9 | 787 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Marion | 36 | 2580 | 2 | 5 | 8 |
| Missouri non-MSA | Missouri | Perry | 22 | 1992 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Madison | 13 | 1329 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Gentry | 19 | 714 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 24 | 1383 | 2 | 2 | 3 |
| St. Joseph | Missouri | Andrew | 17 | 1247 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Ozark | 10 | 518 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Morgan | 36 | 1589 | 2 | 1 | 4 |
| Missouri non-MSA | Missouri | Oregon | 3 | 659 | 2 | 2 | 4 |
| St. Joseph | Missouri | DeKalb | 24 | 893 | 2 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1652 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Randolph | 24 | 1785 | 2 | 2 | 6 |
| Missouri non-MSA | Missouri | Texas | 21 | 1498 | 1 | 2 | 5 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1030 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shelby | 5 | 347 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 23 | 744 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Monroe | 7 | 579 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 6 | 438 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 260 | 1 | 1 | 2 |
| Kansas City | Missouri | Caldwell | 8 | 617 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Dade | 12 | 410 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 413 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Ralls | 10 | 737 | 1 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 692 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Maries | 7 | 519 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Grundy | 30 | 793 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 740 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Iron | 1 | 461 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 458 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Lewis | 3 | 621 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Chariton | 3 | 403 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 2 | 161 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Hickory | 10 | 459 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 5 | 453 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Holt | 10 | 357 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 172 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 217 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 8 | 410 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 238 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 137 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 288 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 256 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 549 | 0 | 0 | 1 |
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
