# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/11/2020  
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
| St. Louis-Farmington | 2722 | 168200 | 1959 | 1905 | 2162 |
| Kansas City | 1298 | 111969 | 1394 | 1245 | 1339 |
| Missouri non-MSA | 1023 | 78413 | 918 | 793 | 925 |
| Springfield | 313 | 24283 | 278 | 245 | 251 |
| Columbia-Jefferson City | 139 | 25741 | 241 | 226 | 301 |
| Cape Girardeau-Sikeston | 148 | 9805 | 95 | 94 | 124 |
| St. Joseph | 104 | 7553 | 90 | 89 | 93 |
| Joplin | 169 | 12055 | 75 | 73 | 113 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1143 | 58197 | 644 | 616 | 706 |
| Kansas City | Kansas | Johnson | 327 | 31155 | 439 | 373 | 412 |
| Kansas City | Missouri | Kansas City | 313 | 25983 | 266 | 254 | 280 |
| St. Louis-Farmington | Missouri | St. Charles | 229 | 22809 | 248 | 253 | 297 |
| Kansas City | Missouri | Jackson | 196 | 19784 | 243 | 227 | 243 |
| St. Louis-Farmington | Illinois | Madison | 313 | 17020 | 236 | 225 | 247 |
| St. Louis-Farmington | Illinois | St. Clair | 297 | 15741 | 225 | 212 | 204 |
| Springfield | Missouri | Greene | 228 | 15647 | 171 | 155 | 160 |
| St. Louis-Farmington | Missouri | Jefferson | 113 | 12667 | 142 | 148 | 177 |
| Kansas City | Kansas | Wyandotte | 184 | 12778 | 142 | 114 | 116 |
| St. Louis-Farmington | Missouri | St. Louis City | 267 | 14472 | 140 | 138 | 151 |
| Columbia-Jefferson City | Missouri | Boone | 28 | 11450 | 108 | 96 | 127 |
| Missouri non-MSA | Missouri | Pettis | 38 | 3275 | 81 | 44 | 33 |
| Kansas City | Missouri | Cass | 41 | 4460 | 67 | 59 | 61 |
| St. Joseph | Missouri | Buchanan | 70 | 5374 | 66 | 61 | 62 |
| Joplin | Missouri | Jasper | 130 | 8929 | 61 | 60 | 88 |
| St. Louis-Farmington | Missouri | Franklin | 95 | 5458 | 59 | 55 | 65 |
| Kansas City | Missouri | Clay | 80 | 5254 | 59 | 58 | 65 |
| Columbia-Jefferson City | Missouri | Cole | 65 | 6833 | 59 | 58 | 83 |
| Springfield | Missouri | Christian | 28 | 4388 | 57 | 53 | 50 |
| Kansas City | Kansas | Leavenworth | 34 | 4269 | 53 | 46 | 45 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 89 | 5620 | 52 | 54 | 72 |
| Missouri non-MSA | Missouri | Pulaski | 24 | 2048 | 48 | 34 | 28 |
| Missouri non-MSA | Missouri | Taney | 46 | 3284 | 44 | 37 | 37 |
| St. Louis-Farmington | Illinois | Clinton | 66 | 3796 | 43 | 40 | 50 |
| St. Louis-Farmington | Missouri | St. Francois | 51 | 5533 | 40 | 42 | 62 |
| St. Louis-Farmington | Missouri | Lincoln | 13 | 2860 | 39 | 35 | 42 |
| Columbia-Jefferson City | Missouri | Callaway | 13 | 3229 | 38 | 35 | 41 |
| St. Louis-Farmington | Illinois | Macoupin | 37 | 2679 | 37 | 40 | 49 |
| St. Louis-Farmington | Illinois | Monroe | 53 | 2444 | 36 | 31 | 36 |
| Cape Girardeau-Sikeston | Missouri | Scott | 44 | 3004 | 32 | 31 | 39 |
| Missouri non-MSA | Missouri | Butler | 10 | 2468 | 31 | 26 | 29 |
| Missouri non-MSA | Missouri | Marion | 20 | 2063 | 31 | 24 | 27 |
| Kansas City | Kansas | Miami | 7 | 1296 | 29 | 23 | 20 |
| Missouri non-MSA | Missouri | Laclede | 37 | 2104 | 28 | 25 | 22 |
| St. Louis-Farmington | Illinois | Jersey | 27 | 1581 | 28 | 26 | 26 |
| Missouri non-MSA | Missouri | Benton | 11 | 987 | 28 | 16 | 13 |
| Missouri non-MSA | Missouri | Johnson | 21 | 2806 | 27 | 25 | 30 |
| Missouri non-MSA | Missouri | Camden | 51 | 2730 | 26 | 23 | 27 |
| Missouri non-MSA | Missouri | Phelps | 54 | 2062 | 25 | 27 | 31 |
| Springfield | Missouri | Webster | 29 | 2027 | 24 | 17 | 20 |
| Kansas City | Missouri | Platte | 17 | 1931 | 22 | 23 | 23 |
| Springfield | Missouri | Polk | 15 | 1586 | 22 | 16 | 14 |
| Missouri non-MSA | Missouri | Audrain | 16 | 1300 | 22 | 18 | 17 |
| Missouri non-MSA | Missouri | Morgan | 13 | 1242 | 19 | 14 | 13 |
| Missouri non-MSA | Missouri | Miller | 28 | 1711 | 19 | 17 | 18 |
| Missouri non-MSA | Missouri | Stoddard | 25 | 1830 | 19 | 17 | 24 |
| St. Louis-Farmington | Illinois | Bond | 14 | 1272 | 18 | 18 | 18 |
| Kansas City | Missouri | Lafayette | 31 | 1723 | 17 | 17 | 20 |
| Missouri non-MSA | Missouri | Adair | 3 | 1242 | 17 | 13 | 17 |
| Missouri non-MSA | Missouri | Randolph | 10 | 1376 | 17 | 14 | 18 |
| Missouri non-MSA | Missouri | Stone | 20 | 1358 | 17 | 14 | 16 |
| Missouri non-MSA | Missouri | Crawford | 14 | 1348 | 15 | 13 | 16 |
| Missouri non-MSA | Missouri | Saline | 14 | 1726 | 15 | 12 | 17 |
| Kansas City | Missouri | Clinton | 48 | 1037 | 14 | 13 | 12 |
| Missouri non-MSA | Missouri | Pike | 11 | 1078 | 14 | 14 | 18 |
| Kansas City | Missouri | Ray | 6 | 837 | 14 | 12 | 12 |
| Joplin | Missouri | Newton | 39 | 3126 | 14 | 12 | 24 |
| Missouri non-MSA | Missouri | Texas | 10 | 1086 | 13 | 10 | 10 |
| Missouri non-MSA | Missouri | Henry | 16 | 1230 | 13 | 12 | 19 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2069 | 13 | 15 | 20 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1827 | 12 | 11 | 15 |
| Missouri non-MSA | Missouri | Barry | 32 | 1588 | 12 | 11 | 16 |
| Missouri non-MSA | Missouri | Mississippi | 7 | 1001 | 12 | 11 | 15 |
| Missouri non-MSA | Missouri | Howell | 33 | 1702 | 12 | 9 | 10 |
| Missouri non-MSA | Missouri | Nodaway | 17 | 2161 | 12 | 16 | 22 |
| Kansas City | Missouri | Bates | 9 | 646 | 11 | 8 | 10 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1207 | 11 | 12 | 17 |
| Missouri non-MSA | Missouri | Vernon | 13 | 786 | 11 | 9 | 9 |
| Missouri non-MSA | Missouri | Harrison | 7 | 495 | 11 | 7 | 8 |
| Columbia-Jefferson City | Missouri | Cooper | 10 | 1288 | 11 | 10 | 14 |
| St. Louis-Farmington | Missouri | Warren | 3 | 1350 | 11 | 12 | 19 |
| Missouri non-MSA | Missouri | Madison | 10 | 1004 | 11 | 11 | 12 |
| St. Joseph | Missouri | Andrew | 13 | 926 | 10 | 10 | 12 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1344 | 10 | 10 | 15 |
| Missouri non-MSA | Missouri | Washington | 27 | 1587 | 10 | 13 | 20 |
| Missouri non-MSA | Missouri | Carroll | 8 | 518 | 9 | 7 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1039 | 9 | 9 | 11 |
| Missouri non-MSA | Missouri | Perry | 15 | 1661 | 9 | 10 | 18 |
| Missouri non-MSA | Missouri | New Madrid | 25 | 1450 | 8 | 9 | 15 |
| Missouri non-MSA | Missouri | McDonald | 16 | 1486 | 8 | 6 | 6 |
| Missouri non-MSA | Missouri | Wright | 16 | 853 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Macon | 4 | 759 | 8 | 7 | 13 |
| Missouri non-MSA | Missouri | Pemiscot | 19 | 1183 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | Dent | 5 | 596 | 8 | 7 | 9 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 10 | 890 | 8 | 7 | 9 |
| Missouri non-MSA | Missouri | Gentry | 14 | 495 | 7 | 6 | 7 |
| St. Joseph | Kansas | Doniphan | 5 | 587 | 7 | 9 | 10 |
| Missouri non-MSA | Missouri | Livingston | 17 | 857 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 27 | 553 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Ralls | 2 | 557 | 7 | 7 | 9 |
| Missouri non-MSA | Missouri | Wayne | 3 | 562 | 7 | 5 | 6 |
| Kansas City | Kansas | Linn | 2 | 371 | 6 | 7 | 6 |
| St. Joseph | Missouri | DeKalb | 16 | 666 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Grundy | 14 | 577 | 6 | 5 | 7 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 321 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Lewis | 2 | 475 | 5 | 3 | 5 |
| Kansas City | Missouri | Caldwell | 3 | 445 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Barton | 6 | 679 | 5 | 4 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 558 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 391 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Daviess | 8 | 385 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Shelby | 1 | 256 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Carter | 6 | 334 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Douglas | 17 | 482 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Linn | 11 | 364 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Maries | 4 | 408 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Monroe | 5 | 436 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | St. Clair | 3 | 386 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Ripley | 8 | 586 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Clark | 4 | 335 | 3 | 2 | 5 |
| Missouri non-MSA | Missouri | Shannon | 9 | 366 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Atchison | 4 | 245 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Iron | 1 | 271 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Oregon | 2 | 418 | 3 | 3 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 5 | 291 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Holt | 5 | 299 | 3 | 2 | 4 |
| Springfield | Missouri | Dallas | 13 | 635 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Dade | 8 | 317 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Worth | 0 | 97 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 273 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Ozark | 4 | 320 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 6 | 395 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 8 | 585 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Scotland | 1 | 205 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 196 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Cedar | 8 | 460 | 1 | 1 | 4 |
| Missouri non-MSA | Missouri | Putnam | 1 | 177 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Mercer | 1 | 98 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 145 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 141 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
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
