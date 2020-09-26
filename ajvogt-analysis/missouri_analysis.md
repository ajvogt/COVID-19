# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/26/2020  
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
| St. Louis-Farmington | 1592 | 62439 | 531 | 567 | 568 |
| Missouri non-MSA | 281 | 24118 | 422 | 423 | 362 |
| Kansas City | 585 | 43255 | 367 | 364 | 358 |
| Springfield | 66 | 8660 | 169 | 177 | 164 |
| Columbia-Jefferson City | 31 | 7823 | 97 | 120 | 138 |
| Joplin | 65 | 5205 | 66 | 72 | 66 |
| Cape Girardeau-Sikeston | 31 | 2949 | 51 | 53 | 44 |
| St. Joseph | 20 | 2404 | 45 | 41 | 32 |
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
| St. Louis-Farmington | Missouri | St. Louis | 796 | 23688 | 161 | 167 | 178 |
| Kansas City | Kansas | Johnson | 146 | 10773 | 116 | 110 | 105 |
| Springfield | Missouri | Greene | 54 | 5934 | 105 | 109 | 111 |
| Kansas City | Missouri | Kansas City | 123 | 11034 | 94 | 72 | 78 |
| St. Louis-Farmington | Missouri | St. Charles | 115 | 7545 | 75 | 76 | 71 |
| St. Louis-Farmington | Missouri | Jefferson | 57 | 4133 | 56 | 60 | 57 |
| St. Louis-Farmington | Illinois | Madison | 136 | 5565 | 47 | 56 | 60 |
| Joplin | Missouri | Jasper | 51 | 3751 | 45 | 53 | 52 |
| St. Louis-Farmington | Illinois | St. Clair | 189 | 6487 | 43 | 40 | 47 |
| Columbia-Jefferson City | Missouri | Boone | 8 | 4628 | 42 | 60 | 84 |
| St. Joseph | Missouri | Buchanan | 16 | 1919 | 36 | 31 | 23 |
| St. Louis-Farmington | Missouri | St. Louis City | 196 | 7003 | 36 | 34 | 32 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 12 | 1678 | 35 | 34 | 26 |
| Kansas City | Kansas | Wyandotte | 134 | 6843 | 33 | 32 | 33 |
| St. Louis-Farmington | Missouri | Franklin | 29 | 1681 | 31 | 31 | 25 |
| Springfield | Missouri | Christian | 5 | 1372 | 27 | 32 | 26 |
| Columbia-Jefferson City | Missouri | Cole | 11 | 1509 | 25 | 27 | 25 |
| St. Louis-Farmington | Missouri | St. Francois | 8 | 2046 | 25 | 46 | 39 |
| Missouri non-MSA | Missouri | Camden | 11 | 939 | 24 | 20 | 15 |
| Kansas City | Kansas | Leavenworth | 11 | 2039 | 23 | 19 | 13 |
| Kansas City | Missouri | Jackson | 92 | 7064 | 21 | 53 | 62 |
| Joplin | Missouri | Newton | 14 | 1454 | 21 | 19 | 13 |
| Springfield | Missouri | Webster | 3 | 620 | 19 | 20 | 14 |
| Kansas City | Missouri | Cass | 22 | 1489 | 18 | 19 | 16 |
| Missouri non-MSA | Missouri | Pettis | 12 | 1100 | 18 | 16 | 11 |
| Kansas City | Missouri | Lafayette | 2 | 497 | 17 | 14 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 5 | 648 | 16 | 14 | 9 |
| Missouri non-MSA | Missouri | Howell | 3 | 602 | 16 | 16 | 12 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 611 | 16 | 13 | 9 |
| Missouri non-MSA | Missouri | Laclede | 4 | 604 | 16 | 16 | 11 |
| Missouri non-MSA | Missouri | Johnson | 4 | 1081 | 16 | 21 | 17 |
| Missouri non-MSA | Missouri | Butler | 6 | 640 | 15 | 13 | 9 |
| St. Louis-Farmington | Illinois | Clinton | 20 | 1129 | 15 | 14 | 16 |
| Kansas City | Missouri | Clay | 41 | 1799 | 14 | 17 | 16 |
| Springfield | Missouri | Polk | 3 | 544 | 14 | 12 | 9 |
| Missouri non-MSA | Missouri | Wright | 0 | 305 | 12 | 12 | 7 |
| Missouri non-MSA | Missouri | Taney | 31 | 1184 | 11 | 11 | 10 |
| Missouri non-MSA | Missouri | Phelps | 8 | 466 | 11 | 11 | 9 |
| Missouri non-MSA | Missouri | Benton | 3 | 304 | 11 | 9 | 5 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 638 | 10 | 11 | 12 |
| Missouri non-MSA | Missouri | Morgan | 1 | 332 | 10 | 10 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 7 | 779 | 10 | 11 | 10 |
| Kansas City | Missouri | Platte | 10 | 688 | 9 | 9 | 7 |
| Missouri non-MSA | Missouri | Miller | 1 | 488 | 9 | 10 | 9 |
| Missouri non-MSA | Missouri | Saline | 9 | 711 | 9 | 8 | 6 |
| Missouri non-MSA | Missouri | Washington | 10 | 384 | 9 | 6 | 5 |
| St. Louis-Farmington | Illinois | Macoupin | 7 | 535 | 9 | 8 | 7 |
| Missouri non-MSA | Missouri | Stone | 4 | 447 | 9 | 8 | 6 |
| Missouri non-MSA | Missouri | Perry | 7 | 616 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 512 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Stoddard | 12 | 490 | 8 | 10 | 7 |
| Cape Girardeau-Sikeston | Missouri | Scott | 17 | 851 | 7 | 9 | 9 |
| Missouri non-MSA | Missouri | Crawford | 4 | 391 | 7 | 11 | 7 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 419 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Texas | 2 | 312 | 7 | 9 | 7 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 344 | 7 | 7 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 748 | 6 | 7 | 7 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 652 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Wayne | 0 | 212 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Barry | 6 | 473 | 6 | 5 | 4 |
| Kansas City | Kansas | Miami | 1 | 357 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Randolph | 3 | 244 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 9 | 749 | 6 | 6 | 14 |
| St. Louis-Farmington | Missouri | Warren | 1 | 467 | 5 | 6 | 5 |
| St. Joseph | Missouri | Andrew | 2 | 244 | 5 | 5 | 4 |
| Kansas City | Missouri | Clinton | 0 | 231 | 5 | 4 | 3 |
| St. Louis-Farmington | Illinois | Bond | 5 | 313 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Daviess | 1 | 112 | 5 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 307 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Henry | 4 | 191 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Carter | 1 | 100 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Madison | 0 | 296 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Douglas | 3 | 188 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 16 | 524 | 4 | 3 | 5 |
| Columbia-Jefferson City | Missouri | Osage | 2 | 150 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 66 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Dent | 1 | 142 | 3 | 5 | 3 |
| Missouri non-MSA | Missouri | Marion | 14 | 651 | 3 | 5 | 9 |
| Missouri non-MSA | Missouri | Linn | 1 | 84 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1061 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ripley | 0 | 161 | 3 | 2 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 58 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 116 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 192 | 3 | 3 | 3 |
| Springfield | Missouri | Dallas | 1 | 190 | 3 | 3 | 3 |
| St. Joseph | Missouri | DeKalb | 2 | 131 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Audrain | 2 | 420 | 3 | 6 | 5 |
| Missouri non-MSA | Missouri | Cedar | 0 | 103 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Vernon | 1 | 169 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Livingston | 1 | 396 | 3 | 3 | 10 |
| Missouri non-MSA | Missouri | Pike | 4 | 239 | 2 | 4 | 3 |
| Kansas City | Missouri | Caldwell | 1 | 89 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 150 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Ozark | 0 | 124 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Grundy | 3 | 183 | 2 | 5 | 4 |
| Kansas City | Missouri | Bates | 2 | 113 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Shannon | 1 | 94 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 180 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Lewis | 2 | 87 | 2 | 1 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 15 | 389 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Dade | 0 | 61 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 331 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Maries | 0 | 81 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 294 | 1 | 2 | 2 |
| Kansas City | Missouri | Ray | 0 | 168 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 67 | 1 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 76 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 148 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 172 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 18 | 160 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Harrison | 1 | 107 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 83 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 55 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 38 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 51 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 190 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 2 | 90 | 0 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 110 | 0 | 1 | 1 |
| Kansas City | Kansas | Linn | 0 | 71 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 64 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 1 | 89 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 50 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 1 | 75 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 118 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 20 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 1 | 132 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 22 | 0 | 0 | 0 |
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
