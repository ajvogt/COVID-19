# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/04/2020  
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
| St. Louis-Farmington | 1950 | 89908 | 1085 | 931 | 761 |
| Kansas City | 927 | 62548 | 717 | 594 | 509 |
| Missouri non-MSA | 606 | 43966 | 683 | 605 | 545 |
| Columbia-Jefferson City | 69 | 13951 | 260 | 215 | 191 |
| Springfield | 189 | 15170 | 200 | 171 | 163 |
| Joplin | 99 | 7817 | 78 | 76 | 70 |
| Cape Girardeau-Sikeston | 87 | 5257 | 75 | 67 | 62 |
| St. Joseph | 56 | 4231 | 42 | 42 | 47 |
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
| St. Louis-Farmington | Missouri | St. Louis | 894 | 32801 | 380 | 315 | 256 |
| Kansas City | Kansas | Johnson | 219 | 15414 | 196 | 161 | 126 |
| Kansas City | Missouri | Kansas City | 222 | 15738 | 186 | 139 | 111 |
| St. Louis-Farmington | Missouri | St. Charles | 157 | 11998 | 167 | 150 | 131 |
| Kansas City | Missouri | Jackson | 142 | 10893 | 122 | 113 | 104 |
| Springfield | Missouri | Greene | 142 | 9856 | 119 | 101 | 98 |
| St. Louis-Farmington | Illinois | Madison | 163 | 7980 | 102 | 82 | 66 |
| St. Louis-Farmington | Missouri | Jefferson | 90 | 6239 | 91 | 72 | 49 |
| Columbia-Jefferson City | Missouri | Cole | 26 | 3591 | 89 | 74 | 61 |
| St. Louis-Farmington | Missouri | St. Louis City | 225 | 8976 | 78 | 69 | 56 |
| Columbia-Jefferson City | Missouri | Boone | 15 | 6513 | 76 | 61 | 66 |
| St. Louis-Farmington | Illinois | St. Clair | 228 | 8552 | 72 | 66 | 54 |
| Joplin | Missouri | Jasper | 77 | 5625 | 55 | 55 | 45 |
| Kansas City | Kansas | Wyandotte | 165 | 8612 | 53 | 46 | 45 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 1563 | 49 | 38 | 27 |
| St. Louis-Farmington | Missouri | Franklin | 50 | 3022 | 46 | 45 | 36 |
| St. Louis-Farmington | Missouri | St. Francois | 29 | 3178 | 45 | 37 | 32 |
| Kansas City | Missouri | Clay | 49 | 2841 | 43 | 37 | 33 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 55 | 2934 | 34 | 32 | 32 |
| Missouri non-MSA | Missouri | Pettis | 24 | 1855 | 34 | 28 | 21 |
| Springfield | Missouri | Christian | 17 | 2534 | 33 | 30 | 29 |
| Missouri non-MSA | Missouri | Butler | 8 | 1423 | 33 | 27 | 23 |
| Kansas City | Missouri | Cass | 32 | 2285 | 32 | 26 | 23 |
| Missouri non-MSA | Missouri | Taney | 35 | 1928 | 29 | 24 | 18 |
| St. Joseph | Missouri | Buchanan | 44 | 3163 | 26 | 27 | 31 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1303 | 25 | 19 | 16 |
| Cape Girardeau-Sikeston | Missouri | Scott | 27 | 1600 | 24 | 21 | 21 |
| Joplin | Missouri | Newton | 22 | 2192 | 23 | 20 | 25 |
| St. Louis-Farmington | Illinois | Monroe | 34 | 1096 | 23 | 16 | 12 |
| Springfield | Missouri | Polk | 11 | 1100 | 22 | 15 | 12 |
| St. Louis-Farmington | Illinois | Clinton | 32 | 1966 | 22 | 23 | 22 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1349 | 20 | 20 | 15 |
| Missouri non-MSA | Missouri | Barry | 10 | 960 | 20 | 16 | 14 |
| Missouri non-MSA | Missouri | Marion | 14 | 1065 | 19 | 16 | 11 |
| Missouri non-MSA | Missouri | Lawrence | 24 | 1239 | 19 | 17 | 16 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1626 | 18 | 15 | 20 |
| Missouri non-MSA | Missouri | Howell | 14 | 1301 | 18 | 19 | 17 |
| Missouri non-MSA | Missouri | Miller | 15 | 1004 | 18 | 15 | 14 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 519 | 17 | 14 | 9 |
| Springfield | Missouri | Webster | 17 | 1266 | 17 | 15 | 16 |
| Missouri non-MSA | Missouri | Camden | 36 | 1717 | 16 | 17 | 19 |
| Missouri non-MSA | Missouri | Phelps | 30 | 953 | 16 | 13 | 14 |
| Kansas City | Kansas | Leavenworth | 20 | 2651 | 15 | 12 | 13 |
| Kansas City | Missouri | Lafayette | 26 | 953 | 15 | 14 | 11 |
| Columbia-Jefferson City | Missouri | Moniteau | 12 | 727 | 14 | 16 | 12 |
| Missouri non-MSA | Missouri | Morgan | 8 | 771 | 14 | 12 | 11 |
| Missouri non-MSA | Missouri | Saline | 11 | 1050 | 14 | 10 | 8 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 972 | 13 | 13 | 13 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 582 | 13 | 11 | 13 |
| Missouri non-MSA | Missouri | Audrain | 11 | 680 | 13 | 10 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1222 | 13 | 15 | 11 |
| Missouri non-MSA | Missouri | Pulaski | 11 | 1095 | 13 | 13 | 12 |
| Kansas City | Missouri | Platte | 13 | 1083 | 13 | 11 | 11 |
| Missouri non-MSA | Missouri | Henry | 8 | 469 | 13 | 8 | 7 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 3 | 567 | 13 | 9 | 6 |
| Missouri non-MSA | Missouri | Perry | 8 | 900 | 12 | 9 | 8 |
| Missouri non-MSA | Missouri | Laclede | 23 | 1284 | 12 | 14 | 16 |
| Missouri non-MSA | Missouri | Washington | 20 | 754 | 12 | 10 | 9 |
| Columbia-Jefferson City | Missouri | Cooper | 4 | 698 | 12 | 8 | 7 |
| Missouri non-MSA | Missouri | Stone | 11 | 779 | 11 | 9 | 8 |
| Missouri non-MSA | Missouri | Crawford | 9 | 722 | 11 | 11 | 9 |
| Missouri non-MSA | Missouri | Randolph | 3 | 698 | 11 | 13 | 13 |
| Missouri non-MSA | Missouri | Sullivan | 3 | 393 | 11 | 8 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 850 | 10 | 10 | 8 |
| Missouri non-MSA | Missouri | Adair | 0 | 592 | 10 | 8 | 7 |
| Kansas City | Missouri | Clinton | 25 | 574 | 10 | 10 | 10 |
| St. Louis-Farmington | Illinois | Macoupin | 11 | 893 | 9 | 10 | 9 |
| Kansas City | Missouri | Ray | 2 | 340 | 9 | 6 | 5 |
| Missouri non-MSA | Missouri | Texas | 3 | 656 | 9 | 8 | 9 |
| St. Louis-Farmington | Missouri | Warren | 2 | 689 | 8 | 8 | 6 |
| Missouri non-MSA | Missouri | Pike | 8 | 409 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | Hickory | 4 | 261 | 8 | 5 | 4 |
| Kansas City | Kansas | Miami | 2 | 564 | 7 | 6 | 5 |
| Springfield | Missouri | Dallas | 2 | 414 | 7 | 9 | 6 |
| Missouri non-MSA | Missouri | Madison | 3 | 553 | 7 | 7 | 8 |
| St. Louis-Farmington | Illinois | Bond | 9 | 566 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 14 | 781 | 7 | 7 | 6 |
| St. Joseph | Missouri | DeKalb | 3 | 352 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Vernon | 3 | 385 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | McDonald | 12 | 1266 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Macon | 1 | 258 | 6 | 4 | 3 |
| St. Joseph | Missouri | Andrew | 8 | 489 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 202 | 6 | 6 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 487 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Maries | 1 | 230 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Lewis | 2 | 244 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 303 | 6 | 5 | 4 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 517 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Wright | 8 | 627 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Wayne | 3 | 344 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Shannon | 5 | 277 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Monroe | 2 | 198 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Livingston | 9 | 591 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Carroll | 4 | 228 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Benton | 7 | 513 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Cedar | 4 | 262 | 4 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 277 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Grundy | 11 | 288 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Ripley | 4 | 300 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Gentry | 10 | 212 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Dent | 4 | 284 | 4 | 3 | 4 |
| Kansas City | Missouri | Caldwell | 1 | 197 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 13 | 312 | 3 | 2 | 2 |
| Kansas City | Missouri | Bates | 8 | 276 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Clark | 1 | 137 | 3 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 156 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Barton | 4 | 455 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Oregon | 0 | 254 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Iron | 0 | 123 | 2 | 2 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 86 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Carter | 3 | 195 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 1 | 230 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Linn | 7 | 179 | 2 | 1 | 1 |
| Kansas City | Kansas | Linn | 1 | 127 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 1 | 97 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 76 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 223 | 2 | 2 | 2 |
| St. Joseph | Kansas | Doniphan | 1 | 227 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Daviess | 4 | 237 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Holt | 1 | 131 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 1 | 155 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Atchison | 1 | 91 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 203 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 133 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 84 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 51 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 70 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 112 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 61 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 37 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
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
