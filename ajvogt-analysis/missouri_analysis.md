# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/14/2020  
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
| St. Louis-Farmington | 2787 | 174179 | 1872 | 1961 | 2132 |
| Kansas City | 1320 | 115374 | 1267 | 1271 | 1289 |
| Missouri non-MSA | 1049 | 81097 | 830 | 859 | 911 |
| Springfield | 315 | 25145 | 262 | 269 | 252 |
| Columbia-Jefferson City | 140 | 26331 | 198 | 229 | 278 |
| St. Joseph | 106 | 7746 | 77 | 86 | 91 |
| Joplin | 174 | 12235 | 70 | 74 | 100 |
| Cape Girardeau-Sikeston | 149 | 10005 | 68 | 90 | 112 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1153 | 60065 | 597 | 624 | 683 |
| Kansas City | Kansas | Johnson | 339 | 32163 | 413 | 388 | 373 |
| St. Louis-Farmington | Missouri | St. Charles | 234 | 23619 | 239 | 261 | 292 |
| St. Louis-Farmington | Illinois | Madison | 329 | 17766 | 228 | 241 | 242 |
| Kansas City | Missouri | Kansas City | 316 | 26637 | 216 | 244 | 275 |
| Kansas City | Missouri | Jackson | 197 | 20408 | 209 | 233 | 242 |
| St. Louis-Farmington | Illinois | St. Clair | 309 | 16341 | 207 | 209 | 206 |
| Springfield | Missouri | Greene | 229 | 16211 | 166 | 170 | 161 |
| Kansas City | Kansas | Wyandotte | 184 | 13156 | 151 | 124 | 115 |
| St. Louis-Farmington | Missouri | St. Louis City | 270 | 14974 | 144 | 143 | 161 |
| St. Louis-Farmington | Missouri | Jefferson | 113 | 13119 | 135 | 153 | 175 |
| Columbia-Jefferson City | Missouri | Boone | 29 | 11776 | 104 | 104 | 118 |
| Missouri non-MSA | Missouri | Pettis | 38 | 3528 | 79 | 60 | 37 |
| Kansas City | Missouri | Cass | 41 | 4653 | 62 | 63 | 62 |
| St. Louis-Farmington | Missouri | Franklin | 96 | 5633 | 58 | 59 | 65 |
| Springfield | Missouri | Christian | 29 | 4584 | 58 | 59 | 51 |
| Kansas City | Missouri | Clay | 81 | 5453 | 58 | 62 | 65 |
| Joplin | Missouri | Jasper | 135 | 9078 | 57 | 61 | 78 |
| Missouri non-MSA | Missouri | Howell | 34 | 2060 | 57 | 34 | 21 |
| St. Joseph | Missouri | Buchanan | 72 | 5514 | 55 | 62 | 61 |
| St. Louis-Farmington | Missouri | St. Francois | 51 | 5733 | 50 | 47 | 61 |
| Kansas City | Kansas | Leavenworth | 35 | 4347 | 49 | 44 | 41 |
| St. Louis-Farmington | Illinois | Clinton | 72 | 3908 | 41 | 42 | 48 |
| St. Louis-Farmington | Missouri | Lincoln | 13 | 3005 | 40 | 40 | 42 |
| Columbia-Jefferson City | Missouri | Cole | 65 | 6948 | 39 | 56 | 76 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 89 | 5738 | 39 | 50 | 64 |
| St. Louis-Farmington | Illinois | Macoupin | 46 | 2779 | 37 | 39 | 45 |
| Missouri non-MSA | Missouri | Taney | 46 | 3402 | 36 | 39 | 38 |
| St. Louis-Farmington | Illinois | Monroe | 54 | 2555 | 31 | 34 | 37 |
| Missouri non-MSA | Missouri | Pulaski | 24 | 2150 | 29 | 38 | 30 |
| Missouri non-MSA | Missouri | Laclede | 38 | 2210 | 28 | 29 | 23 |
| Kansas City | Kansas | Miami | 7 | 1339 | 28 | 23 | 19 |
| Columbia-Jefferson City | Missouri | Callaway | 13 | 3294 | 26 | 33 | 39 |
| Missouri non-MSA | Missouri | Butler | 10 | 2539 | 25 | 28 | 30 |
| Missouri non-MSA | Missouri | Johnson | 22 | 2873 | 25 | 24 | 28 |
| Missouri non-MSA | Missouri | Benton | 11 | 1043 | 22 | 19 | 13 |
| Missouri non-MSA | Missouri | Camden | 51 | 2781 | 22 | 23 | 25 |
| St. Louis-Farmington | Illinois | Jersey | 28 | 1623 | 21 | 25 | 24 |
| Missouri non-MSA | Missouri | Marion | 20 | 2104 | 21 | 23 | 25 |
| St. Louis-Farmington | Illinois | Bond | 15 | 1336 | 20 | 20 | 18 |
| Cape Girardeau-Sikeston | Missouri | Scott | 45 | 3058 | 20 | 29 | 36 |
| Missouri non-MSA | Missouri | Phelps | 60 | 2121 | 19 | 25 | 30 |
| Springfield | Missouri | Webster | 29 | 2087 | 19 | 19 | 21 |
| Missouri non-MSA | Missouri | Audrain | 16 | 1348 | 18 | 18 | 17 |
| Kansas City | Missouri | Platte | 17 | 1980 | 17 | 23 | 23 |
| Missouri non-MSA | Missouri | Adair | 3 | 1289 | 17 | 15 | 15 |
| Missouri non-MSA | Missouri | Morgan | 14 | 1291 | 16 | 15 | 13 |
| Kansas City | Missouri | Lafayette | 35 | 1770 | 16 | 17 | 19 |
| Missouri non-MSA | Missouri | Miller | 31 | 1759 | 15 | 19 | 18 |
| Missouri non-MSA | Missouri | Crawford | 14 | 1399 | 15 | 14 | 16 |
| Springfield | Missouri | Polk | 15 | 1617 | 14 | 17 | 13 |
| Missouri non-MSA | Missouri | Saline | 14 | 1766 | 14 | 13 | 16 |
| Missouri non-MSA | Missouri | Stone | 20 | 1396 | 14 | 15 | 15 |
| Kansas City | Missouri | Clinton | 48 | 1081 | 13 | 14 | 12 |
| Missouri non-MSA | Missouri | Randolph | 11 | 1430 | 13 | 16 | 17 |
| Missouri non-MSA | Missouri | Texas | 10 | 1137 | 12 | 12 | 11 |
| Missouri non-MSA | Missouri | Stoddard | 25 | 1872 | 12 | 17 | 23 |
| Joplin | Missouri | Newton | 39 | 3157 | 12 | 13 | 21 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2105 | 12 | 14 | 19 |
| Missouri non-MSA | Missouri | Barry | 33 | 1623 | 12 | 13 | 15 |
| Kansas City | Missouri | Ray | 6 | 870 | 11 | 12 | 12 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1250 | 11 | 13 | 16 |
| Missouri non-MSA | Missouri | Pike | 11 | 1107 | 11 | 13 | 17 |
| Columbia-Jefferson City | Missouri | Cooper | 10 | 1325 | 11 | 11 | 13 |
| Missouri non-MSA | Missouri | Henry | 16 | 1264 | 11 | 12 | 17 |
| St. Louis-Farmington | Missouri | Warren | 3 | 1386 | 11 | 12 | 17 |
| Missouri non-MSA | Missouri | Harrison | 7 | 528 | 10 | 9 | 8 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1851 | 10 | 11 | 14 |
| Missouri non-MSA | Missouri | Washington | 28 | 1613 | 10 | 14 | 19 |
| Missouri non-MSA | Missouri | Oregon | 2 | 474 | 10 | 7 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 17 | 2176 | 9 | 13 | 19 |
| St. Joseph | Missouri | Andrew | 13 | 956 | 9 | 11 | 12 |
| Missouri non-MSA | Missouri | Madison | 10 | 1027 | 9 | 10 | 12 |
| Missouri non-MSA | Missouri | Wright | 17 | 893 | 9 | 9 | 7 |
| Missouri non-MSA | Missouri | Mississippi | 8 | 1039 | 9 | 12 | 16 |
| Kansas City | Missouri | Bates | 9 | 664 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | Carroll | 8 | 547 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | New Madrid | 26 | 1473 | 8 | 8 | 14 |
| Kansas City | Kansas | Linn | 2 | 391 | 7 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1370 | 7 | 10 | 13 |
| Missouri non-MSA | Missouri | Perry | 15 | 1685 | 7 | 10 | 18 |
| Missouri non-MSA | Missouri | McDonald | 17 | 1505 | 7 | 7 | 6 |
| St. Joseph | Missouri | DeKalb | 16 | 689 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Vernon | 13 | 805 | 6 | 9 | 9 |
| Missouri non-MSA | Missouri | Grundy | 17 | 595 | 6 | 6 | 7 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 337 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Douglas | 18 | 511 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Gentry | 14 | 515 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Livingston | 18 | 875 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 19 | 1194 | 6 | 8 | 9 |
| Missouri non-MSA | Missouri | Wayne | 3 | 577 | 6 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1054 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Gasconade | 27 | 568 | 6 | 6 | 6 |
| St. Joseph | Kansas | Doniphan | 5 | 587 | 5 | 6 | 8 |
| Missouri non-MSA | Missouri | Ralls | 2 | 565 | 5 | 6 | 8 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 408 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Macon | 4 | 772 | 5 | 6 | 12 |
| Missouri non-MSA | Missouri | Barton | 6 | 694 | 5 | 4 | 5 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 10 | 903 | 4 | 7 | 7 |
| Missouri non-MSA | Missouri | Linn | 11 | 377 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Monroe | 5 | 445 | 4 | 4 | 5 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 5 | 306 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Dent | 5 | 606 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Iron | 1 | 288 | 4 | 3 | 4 |
| Kansas City | Missouri | Caldwell | 3 | 462 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Ozark | 4 | 340 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 8 | 402 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Ripley | 8 | 599 | 4 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 564 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Shannon | 9 | 376 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Atchison | 4 | 249 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Carter | 6 | 342 | 3 | 3 | 4 |
| Springfield | Missouri | Dallas | 13 | 646 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Hickory | 6 | 403 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 3 | 392 | 2 | 4 | 6 |
| Missouri non-MSA | Missouri | Dade | 8 | 323 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Holt | 5 | 306 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Lewis | 2 | 481 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Maries | 4 | 412 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Worth | 0 | 103 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 278 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Shelby | 1 | 260 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 8 | 592 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Mercer | 1 | 105 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 4 | 336 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Cedar | 8 | 466 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 152 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 204 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Scotland | 2 | 206 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 1 | 140 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 177 | 0 | 1 | 2 |
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
