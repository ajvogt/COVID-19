# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/25/2020  
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
| St. Louis-Farmington | 1867 | 79904 | 746 | 683 | 608 |
| Missouri non-MSA | 526 | 37740 | 511 | 478 | 470 |
| Kansas City | 832 | 56162 | 426 | 439 | 449 |
| Columbia-Jefferson City | 58 | 11802 | 166 | 160 | 137 |
| Springfield | 159 | 13371 | 132 | 131 | 163 |
| Joplin | 91 | 7083 | 62 | 65 | 65 |
| Cape Girardeau-Sikeston | 71 | 4559 | 54 | 50 | 56 |
| St. Joseph | 49 | 3832 | 54 | 50 | 49 |
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
| St. Louis-Farmington | Missouri | St. Louis | 871 | 29396 | 256 | 233 | 198 |
| St. Louis-Farmington | Missouri | St. Charles | 147 | 10400 | 131 | 123 | 98 |
| Kansas City | Kansas | Johnson | 192 | 13646 | 102 | 104 | 103 |
| Kansas City | Missouri | Jackson | 122 | 9765 | 96 | 103 | 90 |
| Kansas City | Missouri | Kansas City | 195 | 14117 | 88 | 74 | 106 |
| Springfield | Missouri | Greene | 122 | 8788 | 79 | 75 | 99 |
| Columbia-Jefferson City | Missouri | Cole | 22 | 2849 | 61 | 53 | 45 |
| St. Louis-Farmington | Illinois | St. Clair | 218 | 7878 | 59 | 50 | 48 |
| St. Louis-Farmington | Illinois | Madison | 154 | 7084 | 57 | 57 | 52 |
| St. Louis-Farmington | Missouri | St. Louis City | 221 | 8231 | 53 | 50 | 42 |
| St. Louis-Farmington | Missouri | Jefferson | 84 | 5420 | 48 | 41 | 45 |
| Joplin | Missouri | Jasper | 70 | 5091 | 45 | 31 | 46 |
| Columbia-Jefferson City | Missouri | Boone | 14 | 5889 | 43 | 46 | 44 |
| St. Louis-Farmington | Missouri | Franklin | 44 | 2542 | 36 | 33 | 30 |
| St. Joseph | Missouri | Buchanan | 39 | 2916 | 34 | 32 | 34 |
| Kansas City | Kansas | Wyandotte | 164 | 8111 | 33 | 42 | 43 |
| Kansas City | Missouri | Clay | 49 | 2477 | 27 | 35 | 23 |
| St. Louis-Farmington | Illinois | Clinton | 26 | 1733 | 27 | 23 | 21 |
| St. Louis-Farmington | Missouri | St. Francois | 27 | 2776 | 27 | 22 | 26 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 49 | 2599 | 25 | 25 | 32 |
| Missouri non-MSA | Missouri | Pettis | 17 | 1563 | 25 | 18 | 16 |
| Columbia-Jefferson City | Missouri | Callaway | 5 | 1152 | 22 | 21 | 17 |
| Springfield | Missouri | Christian | 13 | 2215 | 22 | 26 | 29 |
| Cape Girardeau-Sikeston | Missouri | Scott | 19 | 1377 | 21 | 18 | 17 |
| Kansas City | Missouri | Cass | 30 | 1993 | 19 | 18 | 17 |
| Missouri non-MSA | Missouri | Taney | 33 | 1663 | 18 | 13 | 16 |
| Missouri non-MSA | Missouri | Butler | 8 | 1121 | 18 | 20 | 16 |
| Columbia-Jefferson City | Missouri | Moniteau | 9 | 601 | 18 | 14 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 12 | 1091 | 17 | 10 | 10 |
| Missouri non-MSA | Missouri | Lawrence | 20 | 1062 | 16 | 17 | 15 |
| Joplin | Missouri | Newton | 21 | 1992 | 16 | 33 | 18 |
| Missouri non-MSA | Missouri | Howell | 10 | 1102 | 16 | 15 | 17 |
| Missouri non-MSA | Missouri | Randolph | 3 | 595 | 16 | 12 | 12 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1101 | 16 | 14 | 12 |
| Missouri non-MSA | Missouri | Laclede | 22 | 1159 | 16 | 17 | 18 |
| Missouri non-MSA | Missouri | Camden | 33 | 1544 | 15 | 17 | 21 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 853 | 15 | 13 | 12 |
| Missouri non-MSA | Missouri | Miller | 9 | 834 | 14 | 14 | 11 |
| Kansas City | Kansas | Leavenworth | 18 | 2520 | 13 | 13 | 18 |
| Missouri non-MSA | Missouri | Barry | 8 | 786 | 13 | 14 | 10 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1128 | 13 | 12 | 13 |
| Missouri non-MSA | Missouri | Morgan | 7 | 649 | 12 | 10 | 10 |
| Springfield | Missouri | Webster | 13 | 1108 | 12 | 13 | 16 |
| Missouri non-MSA | Missouri | Marion | 14 | 890 | 12 | 8 | 8 |
| Missouri non-MSA | Missouri | Crawford | 8 | 609 | 11 | 9 | 7 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 361 | 11 | 8 | 5 |
| Kansas City | Missouri | Platte | 12 | 965 | 11 | 11 | 9 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 462 | 10 | 15 | 10 |
| St. Louis-Farmington | Illinois | Macoupin | 10 | 784 | 10 | 10 | 8 |
| Kansas City | Missouri | Clinton | 15 | 479 | 10 | 10 | 8 |
| Missouri non-MSA | Missouri | Phelps | 21 | 812 | 10 | 15 | 12 |
| Missouri non-MSA | Missouri | Pulaski | 9 | 944 | 9 | 8 | 10 |
| St. Louis-Farmington | Illinois | Monroe | 29 | 903 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1452 | 9 | 12 | 12 |
| Springfield | Missouri | Polk | 10 | 922 | 9 | 9 | 12 |
| Kansas City | Missouri | Lafayette | 24 | 797 | 9 | 8 | 10 |
| Missouri non-MSA | Missouri | New Madrid | 22 | 751 | 9 | 7 | 7 |
| Springfield | Missouri | Dallas | 1 | 338 | 9 | 6 | 5 |
| Missouri non-MSA | Missouri | Texas | 3 | 575 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 437 | 8 | 6 | 4 |
| Missouri non-MSA | Missouri | Washington | 18 | 638 | 8 | 6 | 8 |
| Missouri non-MSA | Missouri | Saline | 10 | 934 | 7 | 5 | 7 |
| Missouri non-MSA | Missouri | Madison | 3 | 478 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Pike | 8 | 343 | 7 | 4 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 12 | 713 | 7 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Cooper | 3 | 605 | 7 | 6 | 6 |
| St. Joseph | Missouri | DeKalb | 2 | 287 | 7 | 7 | 5 |
| St. Louis-Farmington | Illinois | Bond | 9 | 488 | 6 | 7 | 6 |
| St. Joseph | Kansas | Doniphan | 0 | 201 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 499 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Perry | 8 | 789 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Ripley | 4 | 254 | 6 | 6 | 3 |
| Missouri non-MSA | Missouri | Stone | 9 | 669 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Maries | 0 | 175 | 6 | 4 | 3 |
| St. Joseph | Missouri | Andrew | 8 | 428 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Shannon | 4 | 227 | 6 | 3 | 4 |
| Missouri non-MSA | Missouri | Audrain | 11 | 563 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Vernon | 3 | 321 | 5 | 4 | 5 |
| St. Louis-Farmington | Missouri | Warren | 1 | 604 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Wright | 5 | 582 | 5 | 6 | 9 |
| Missouri non-MSA | Missouri | Henry | 6 | 370 | 5 | 5 | 6 |
| Kansas City | Kansas | Miami | 2 | 509 | 5 | 5 | 5 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 2 | 463 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1207 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 244 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 138 | 4 | 3 | 1 |
| Kansas City | Missouri | Ray | 2 | 264 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Benton | 5 | 476 | 4 | 3 | 6 |
| Missouri non-MSA | Missouri | Ozark | 1 | 201 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Barton | 3 | 414 | 3 | 6 | 7 |
| Missouri non-MSA | Missouri | Lewis | 2 | 192 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Grundy | 9 | 256 | 3 | 1 | 2 |
| Missouri non-MSA | Missouri | Harrison | 1 | 187 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Daviess | 4 | 220 | 3 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 244 | 3 | 3 | 2 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 470 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Monroe | 2 | 146 | 3 | 3 | 1 |
| Kansas City | Missouri | Bates | 5 | 243 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Douglas | 11 | 280 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 1 | 293 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Livingston | 7 | 556 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Carter | 3 | 168 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 3 | 193 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Ralls | 0 | 200 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 223 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Dent | 3 | 241 | 2 | 3 | 3 |
| Kansas City | Missouri | Caldwell | 1 | 166 | 2 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 120 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 118 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 10 | 181 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Scotland | 1 | 71 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Cedar | 4 | 219 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Macon | 1 | 203 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carroll | 3 | 179 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 1 | 65 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Holt | 1 | 114 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 102 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 1 | 299 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Dade | 0 | 135 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 4 | 158 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 98 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 1 | 105 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 1 | 75 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 53 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 58 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 39 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 62 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 1 | 110 | 0 | 1 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 31 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 67 | 0 | 0 | 0 |
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
