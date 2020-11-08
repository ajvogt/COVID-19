# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/08/2020  
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
| St. Louis-Farmington | 1983 | 97503 | 1566 | 1257 | 959 |
| Kansas City | 962 | 66753 | 883 | 756 | 608 |
| Missouri non-MSA | 636 | 47815 | 822 | 719 | 627 |
| Columbia-Jefferson City | 70 | 15776 | 354 | 283 | 230 |
| Springfield | 206 | 16065 | 192 | 192 | 174 |
| Joplin | 107 | 8364 | 98 | 91 | 81 |
| Cape Girardeau-Sikeston | 92 | 5709 | 95 | 82 | 72 |
| St. Joseph | 59 | 4450 | 54 | 44 | 49 |
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
| St. Louis-Farmington | Missouri | St. Louis | 897 | 35219 | 519 | 415 | 317 |
| Kansas City | Kansas | Johnson | 233 | 16717 | 260 | 219 | 158 |
| St. Louis-Farmington | Missouri | St. Charles | 157 | 13071 | 224 | 190 | 157 |
| Kansas City | Missouri | Kansas City | 227 | 16633 | 198 | 179 | 133 |
| St. Louis-Farmington | Illinois | Madison | 168 | 8976 | 190 | 135 | 92 |
| Kansas City | Missouri | Jackson | 145 | 11748 | 181 | 141 | 125 |
| Columbia-Jefferson City | Missouri | Boone | 15 | 7291 | 132 | 100 | 80 |
| St. Louis-Farmington | Missouri | Jefferson | 90 | 6825 | 127 | 100 | 72 |
| Springfield | Missouri | Greene | 153 | 10423 | 121 | 116 | 105 |
| St. Louis-Farmington | Illinois | St. Clair | 240 | 9099 | 108 | 87 | 66 |
| Columbia-Jefferson City | Missouri | Cole | 26 | 4066 | 108 | 86 | 71 |
| St. Louis-Farmington | Missouri | St. Louis City | 225 | 9472 | 103 | 88 | 68 |
| Joplin | Missouri | Jasper | 85 | 6039 | 73 | 67 | 53 |
| St. Louis-Farmington | Missouri | St. Francois | 30 | 3436 | 59 | 47 | 37 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 55 | 3219 | 56 | 44 | 38 |
| St. Louis-Farmington | Missouri | Franklin | 50 | 3270 | 55 | 52 | 42 |
| Kansas City | Missouri | Clay | 51 | 3097 | 54 | 44 | 39 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 1831 | 53 | 48 | 35 |
| Kansas City | Kansas | Wyandotte | 166 | 8876 | 53 | 54 | 47 |
| Missouri non-MSA | Missouri | Pettis | 24 | 2111 | 50 | 39 | 29 |
| Springfield | Missouri | Christian | 17 | 2730 | 42 | 36 | 32 |
| St. Louis-Farmington | Illinois | Clinton | 36 | 2142 | 34 | 29 | 26 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1805 | 34 | 25 | 25 |
| Kansas City | Missouri | Cass | 33 | 2425 | 33 | 30 | 26 |
| St. Louis-Farmington | Illinois | Jersey | 22 | 724 | 33 | 18 | 10 |
| St. Joseph | Missouri | Buchanan | 45 | 3302 | 32 | 27 | 32 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1450 | 30 | 24 | 19 |
| Cape Girardeau-Sikeston | Missouri | Scott | 31 | 1722 | 29 | 24 | 24 |
| Missouri non-MSA | Missouri | Butler | 8 | 1500 | 28 | 27 | 24 |
| Missouri non-MSA | Missouri | Taney | 36 | 2057 | 28 | 28 | 20 |
| St. Louis-Farmington | Illinois | Monroe | 40 | 1241 | 27 | 24 | 16 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1475 | 26 | 24 | 18 |
| St. Louis-Farmington | Illinois | Macoupin | 12 | 1054 | 26 | 19 | 14 |
| Missouri non-MSA | Missouri | Lawrence | 26 | 1351 | 24 | 20 | 19 |
| Joplin | Missouri | Newton | 22 | 2325 | 24 | 23 | 28 |
| Missouri non-MSA | Missouri | Washington | 20 | 889 | 23 | 17 | 12 |
| Columbia-Jefferson City | Missouri | Cooper | 4 | 816 | 22 | 15 | 10 |
| Missouri non-MSA | Missouri | Marion | 14 | 1145 | 22 | 18 | 13 |
| Missouri non-MSA | Missouri | Perry | 8 | 1016 | 21 | 16 | 11 |
| Kansas City | Missouri | Lafayette | 26 | 1052 | 21 | 18 | 14 |
| Kansas City | Kansas | Leavenworth | 21 | 2749 | 20 | 16 | 15 |
| Missouri non-MSA | Missouri | Miller | 18 | 1100 | 20 | 19 | 16 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 613 | 20 | 18 | 12 |
| Missouri non-MSA | Missouri | Camden | 37 | 1817 | 20 | 19 | 20 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1316 | 18 | 16 | 13 |
| Missouri non-MSA | Missouri | Henry | 8 | 561 | 17 | 13 | 9 |
| Missouri non-MSA | Missouri | Randolph | 3 | 795 | 17 | 14 | 13 |
| Missouri non-MSA | Missouri | Barry | 18 | 1019 | 17 | 16 | 15 |
| Kansas City | Missouri | Platte | 13 | 1168 | 17 | 14 | 13 |
| Missouri non-MSA | Missouri | Laclede | 25 | 1372 | 17 | 15 | 17 |
| Missouri non-MSA | Missouri | Saline | 11 | 1119 | 16 | 13 | 9 |
| Columbia-Jefferson City | Missouri | Moniteau | 13 | 806 | 16 | 14 | 14 |
| Missouri non-MSA | Missouri | Phelps | 30 | 1028 | 16 | 15 | 16 |
| Missouri non-MSA | Missouri | Pike | 8 | 492 | 16 | 10 | 7 |
| Missouri non-MSA | Missouri | Crawford | 9 | 795 | 15 | 13 | 11 |
| Springfield | Missouri | Webster | 23 | 1340 | 15 | 16 | 16 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 919 | 15 | 12 | 10 |
| St. Louis-Farmington | Illinois | Bond | 9 | 644 | 15 | 11 | 9 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 650 | 14 | 13 | 14 |
| Missouri non-MSA | Missouri | Pulaski | 11 | 1154 | 13 | 15 | 13 |
| Missouri non-MSA | Missouri | Stone | 13 | 841 | 13 | 12 | 10 |
| Missouri non-MSA | Missouri | Texas | 4 | 721 | 13 | 10 | 10 |
| Missouri non-MSA | Missouri | Adair | 0 | 663 | 13 | 11 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 1027 | 12 | 12 | 13 |
| Missouri non-MSA | Missouri | Morgan | 8 | 819 | 12 | 12 | 12 |
| St. Joseph | Missouri | DeKalb | 5 | 403 | 12 | 8 | 7 |
| Missouri non-MSA | Missouri | Howell | 16 | 1339 | 12 | 16 | 17 |
| Kansas City | Missouri | Clinton | 33 | 623 | 11 | 10 | 11 |
| Kansas City | Missouri | Ray | 2 | 391 | 11 | 9 | 6 |
| Missouri non-MSA | Missouri | Audrain | 10 | 718 | 11 | 11 | 8 |
| Missouri non-MSA | Missouri | Vernon | 3 | 441 | 11 | 8 | 6 |
| St. Louis-Farmington | Missouri | Warren | 2 | 738 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Macon | 1 | 319 | 10 | 8 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 14 | 825 | 9 | 8 | 7 |
| Missouri non-MSA | Missouri | Benton | 7 | 560 | 8 | 6 | 5 |
| Springfield | Missouri | Polk | 11 | 1135 | 7 | 15 | 12 |
| Missouri non-MSA | Missouri | Sullivan | 3 | 426 | 7 | 9 | 6 |
| Missouri non-MSA | Missouri | Lewis | 2 | 274 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 511 | 7 | 5 | 6 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 316 | 7 | 5 | 4 |
| St. Joseph | Missouri | Andrew | 8 | 518 | 7 | 6 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 4 | 590 | 7 | 9 | 7 |
| Missouri non-MSA | Missouri | Ripley | 5 | 331 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 325 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Carroll | 4 | 257 | 6 | 5 | 3 |
| Kansas City | Kansas | Miami | 2 | 605 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Chariton | 0 | 113 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Clark | 2 | 167 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Grundy | 11 | 321 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 2 | 226 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Gentry | 10 | 233 | 5 | 3 | 2 |
| Springfield | Missouri | Dallas | 2 | 437 | 5 | 7 | 6 |
| Missouri non-MSA | Missouri | Wayne | 3 | 358 | 5 | 4 | 3 |
| Kansas City | Missouri | Caldwell | 1 | 228 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Oregon | 0 | 280 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Madison | 3 | 578 | 5 | 7 | 8 |
| Missouri non-MSA | Missouri | Monroe | 2 | 225 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 162 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Dent | 4 | 307 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Barton | 4 | 483 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 79 | 4 | 2 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 117 | 4 | 3 | 1 |
| Missouri non-MSA | Missouri | Wright | 9 | 644 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Dade | 3 | 181 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Ralls | 0 | 251 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Maries | 1 | 248 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Harrison | 1 | 227 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 7 | 203 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Livingston | 9 | 610 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Holt | 1 | 154 | 4 | 2 | 2 |
| Kansas City | Missouri | Bates | 8 | 296 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Hickory | 4 | 282 | 4 | 6 | 4 |
| Missouri non-MSA | Missouri | Shannon | 6 | 290 | 4 | 4 | 4 |
| Kansas City | Kansas | Linn | 1 | 145 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 4 | 281 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Douglas | 13 | 327 | 3 | 3 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 178 | 3 | 4 | 2 |
| Missouri non-MSA | Missouri | Daviess | 4 | 252 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Iron | 0 | 133 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | McDonald | 14 | 1278 | 2 | 5 | 5 |
| Missouri non-MSA | Missouri | Atchison | 1 | 102 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 3 | 206 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Scotland | 1 | 97 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 81 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 1 | 107 | 1 | 3 | 2 |
| Missouri non-MSA | Missouri | Ozark | 1 | 238 | 1 | 2 | 3 |
| St. Joseph | Kansas | Doniphan | 1 | 227 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 121 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 0 | 43 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 67 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 39 | 0 | 0 | 0 |
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
