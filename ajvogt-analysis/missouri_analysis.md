# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/21/2020  
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


## Missouri New Daily Deaths by Metropolitan Statistcal Areas
![](images/mo_daily_deaths.png)

## Missouri New Daily Confirmed Cases by Metropolitan Statistcal Areas
![](images/mo_daily_cases.png)

## Missouri Metropolitan Statistical Area Totals
<!-- msa_table start -->
| MSA | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|
| St. Louis-Farmington | 1825 | 76866 | 785 | 657 | 570 |
| Missouri non-MSA | 461 | 35495 | 633 | 516 | 451 |
| Kansas City | 772 | 54231 | 541 | 464 | 426 |
| Columbia-Jefferson City | 52 | 10936 | 196 | 164 | 121 |
| Springfield | 136 | 12774 | 177 | 162 | 166 |
| Joplin | 85 | 6748 | 83 | 71 | 62 |
| St. Joseph | 41 | 3632 | 71 | 54 | 48 |
| Cape Girardeau-Sikeston | 67 | 4315 | 66 | 62 | 53 |
<!-- msa_table end -->

## STL-Farmington MSA New Daily Deaths by County
![](images/stl_daily_deaths.png)

## STL-Farmington MSA New Daily Confirmed Cases by County
![](images/stl_daily_cases.png)

<a name="msa-counties"></a>
## Metropolitan Statistical Area (MSA) Counties
<!-- county_table start -->
| MSA | State | County | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|---|---|
| St. Louis-Farmington | Missouri | St. Louis | 860 | 28380 | 243 | 211 | 184 |
| St. Louis-Farmington | Missouri | St. Charles | 144 | 9886 | 172 | 119 | 91 |
| Kansas City | Missouri | Jackson | 116 | 9310 | 141 | 104 | 74 |
| Kansas City | Missouri | Kansas City | 172 | 13792 | 102 | 93 | 108 |
| Springfield | Missouri | Greene | 106 | 8436 | 101 | 99 | 101 |
| Kansas City | Kansas | Johnson | 178 | 13154 | 100 | 101 | 99 |
| Columbia-Jefferson City | Missouri | Cole | 18 | 2543 | 64 | 49 | 38 |
| St. Louis-Farmington | Illinois | Madison | 152 | 6832 | 58 | 57 | 49 |
| Columbia-Jefferson City | Missouri | Boone | 14 | 5646 | 57 | 60 | 41 |
| Joplin | Missouri | Newton | 17 | 1905 | 54 | 32 | 18 |
| St. Louis-Farmington | Missouri | Jefferson | 78 | 5226 | 54 | 45 | 46 |
| St. Louis-Farmington | Missouri | St. Louis City | 218 | 8008 | 51 | 46 | 39 |
| Kansas City | Missouri | Clay | 45 | 2323 | 48 | 32 | 19 |
| St. Louis-Farmington | Illinois | St. Clair | 213 | 7623 | 47 | 47 | 44 |
| Kansas City | Kansas | Wyandotte | 158 | 7956 | 46 | 44 | 42 |
| St. Joseph | Missouri | Buchanan | 35 | 2783 | 46 | 36 | 34 |
| St. Louis-Farmington | Missouri | Franklin | 40 | 2379 | 43 | 30 | 28 |
| Springfield | Missouri | Christian | 10 | 2107 | 37 | 29 | 29 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 45 | 2473 | 33 | 33 | 32 |
| Missouri non-MSA | Missouri | Butler | 8 | 1040 | 29 | 20 | 16 |
| Joplin | Missouri | Jasper | 68 | 4843 | 28 | 38 | 44 |
| St. Louis-Farmington | Missouri | St. Francois | 22 | 2660 | 27 | 28 | 24 |
| St. Louis-Farmington | Illinois | Clinton | 24 | 1631 | 27 | 22 | 18 |
| Cape Girardeau-Sikeston | Missouri | Scott | 19 | 1295 | 25 | 22 | 16 |
| Missouri non-MSA | Missouri | Phelps | 19 | 767 | 25 | 18 | 11 |
| Kansas City | Missouri | Cass | 28 | 1909 | 25 | 21 | 17 |
| Missouri non-MSA | Missouri | Camden | 28 | 1478 | 25 | 22 | 22 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 424 | 24 | 15 | 9 |
| Missouri non-MSA | Missouri | Lawrence | 14 | 992 | 24 | 17 | 15 |
| Missouri non-MSA | Missouri | Laclede | 18 | 1086 | 23 | 19 | 19 |
| Columbia-Jefferson City | Missouri | Callaway | 5 | 1021 | 23 | 19 | 14 |
| Missouri non-MSA | Missouri | Pettis | 14 | 1457 | 22 | 16 | 15 |
| Missouri non-MSA | Missouri | Miller | 5 | 783 | 21 | 14 | 11 |
| Missouri non-MSA | Missouri | Howell | 6 | 1030 | 21 | 16 | 17 |
| Missouri non-MSA | Missouri | Barry | 8 | 731 | 21 | 13 | 9 |
| Springfield | Missouri | Webster | 11 | 1053 | 19 | 17 | 17 |
| Missouri non-MSA | Missouri | Johnson | 11 | 1403 | 18 | 27 | 13 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1068 | 17 | 12 | 11 |
| Kansas City | Missouri | Platte | 12 | 921 | 17 | 12 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 782 | 16 | 13 | 11 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 1024 | 16 | 12 | 10 |
| Columbia-Jefferson City | Missouri | Moniteau | 8 | 501 | 14 | 10 | 7 |
| Missouri non-MSA | Missouri | Morgan | 6 | 596 | 14 | 10 | 9 |
| Missouri non-MSA | Missouri | Taney | 33 | 1579 | 14 | 11 | 15 |
| Springfield | Missouri | Polk | 8 | 890 | 14 | 10 | 14 |
| Kansas City | Missouri | Clinton | 11 | 431 | 14 | 11 | 7 |
| Kansas City | Kansas | Leavenworth | 17 | 2471 | 13 | 14 | 19 |
| Missouri non-MSA | Missouri | Randolph | 3 | 508 | 13 | 9 | 9 |
| St. Louis-Farmington | Illinois | Macoupin | 10 | 741 | 12 | 9 | 8 |
| Missouri non-MSA | Missouri | Pulaski | 9 | 900 | 11 | 12 | 11 |
| Missouri non-MSA | Missouri | Barton | 2 | 399 | 11 | 9 | 7 |
| Missouri non-MSA | Missouri | Crawford | 7 | 561 | 11 | 9 | 7 |
| St. Louis-Farmington | Illinois | Bond | 9 | 471 | 11 | 7 | 6 |
| Missouri non-MSA | Missouri | Wright | 1 | 563 | 11 | 8 | 10 |
| Missouri non-MSA | Missouri | Madison | 2 | 443 | 10 | 9 | 5 |
| Missouri non-MSA | Missouri | Texas | 3 | 533 | 10 | 10 | 8 |
| Missouri non-MSA | Missouri | Marion | 14 | 838 | 10 | 8 | 7 |
| Kansas City | Missouri | Lafayette | 24 | 745 | 10 | 9 | 10 |
| Missouri non-MSA | Missouri | Stone | 7 | 640 | 10 | 8 | 8 |
| Missouri non-MSA | Missouri | Ripley | 4 | 229 | 9 | 6 | 3 |
| St. Joseph | Missouri | DeKalb | 2 | 256 | 9 | 6 | 4 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 314 | 9 | 6 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 12 | 1012 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Pemiscot | 12 | 678 | 8 | 7 | 7 |
| St. Joseph | Missouri | Andrew | 4 | 403 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Adair | 0 | 467 | 8 | 6 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 575 | 8 | 6 | 6 |
| Missouri non-MSA | Missouri | Washington | 16 | 603 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | Henry | 5 | 346 | 8 | 6 | 6 |
| Missouri non-MSA | Missouri | Saline | 9 | 907 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Perry | 7 | 761 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Mississippi | 5 | 398 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 20 | 707 | 7 | 7 | 6 |
| St. Louis-Farmington | Missouri | Warren | 1 | 577 | 7 | 5 | 4 |
| St. Louis-Farmington | Illinois | Monroe | 28 | 861 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Audrain | 7 | 535 | 7 | 4 | 4 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1190 | 7 | 5 | 4 |
| St. Joseph | Kansas | Doniphan | 0 | 190 | 7 | 4 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 2 | 438 | 6 | 5 | 4 |
| Springfield | Missouri | Dallas | 1 | 288 | 6 | 4 | 4 |
| Missouri non-MSA | Missouri | Benton | 5 | 462 | 5 | 4 | 7 |
| Missouri non-MSA | Missouri | Oregon | 0 | 213 | 5 | 4 | 3 |
| Kansas City | Missouri | Bates | 5 | 225 | 5 | 4 | 4 |
| Kansas City | Missouri | Ray | 2 | 247 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Vernon | 3 | 294 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 225 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Maries | 0 | 145 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Dent | 3 | 233 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Monroe | 1 | 135 | 5 | 3 | 1 |
| Kansas City | Kansas | Miami | 2 | 477 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Daviess | 3 | 205 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Wayne | 1 | 293 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Harrison | 1 | 177 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Pike | 8 | 307 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Cedar | 2 | 211 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Hickory | 3 | 181 | 4 | 3 | 3 |
| Kansas City | Missouri | Caldwell | 1 | 161 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 1 | 278 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Shannon | 3 | 202 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Livingston | 6 | 544 | 3 | 6 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 226 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 193 | 3 | 2 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 456 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Gentry | 10 | 173 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Douglas | 6 | 273 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Lewis | 2 | 173 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 111 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 1 | 179 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Dade | 0 | 127 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 92 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 104 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 63 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 3 | 155 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Carroll | 2 | 172 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 108 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Holt | 1 | 111 | 2 | 1 | 1 |
| Kansas City | Kansas | Linn | 1 | 109 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 60 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Macon | 1 | 197 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Grundy | 9 | 244 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 96 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 2 | 152 | 1 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 109 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 48 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Atchison | 1 | 73 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 59 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 1 | 55 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 67 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 31 | 0 | 0 | 0 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
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

### To-Do (updated 7/20/2020)

#### Analysis Page
- [ ] Update description to accurately reflect CSA vs. MSA
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
