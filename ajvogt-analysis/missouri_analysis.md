# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/31/2020  
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
| St. Louis-Farmington | 1393 | 47877 | 583 | 585 | 603 |
| Kansas City | 440 | 34167 | 385 | 400 | 402 |
| Missouri non-MSA | 138 | 14426 | 258 | 234 | 221 |
| Springfield | 13 | 4299 | 126 | 106 | 83 |
| Columbia-Jefferson City | 16 | 4273 | 124 | 102 | 81 |
| Joplin | 48 | 3405 | 39 | 36 | 32 |
| Cape Girardeau-Sikeston | 22 | 1748 | 31 | 29 | 24 |
| St. Joseph | 12 | 1558 | 22 | 17 | 11 |
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
| St. Louis-Farmington | Missouri | St. Louis | 729 | 19278 | 200 | 190 | 213 |
| Kansas City | Kansas | Johnson | 116 | 8124 | 116 | 126 | 108 |
| Kansas City | Missouri | Kansas City | 69 | 9183 | 108 | 109 | 112 |
| Springfield | Missouri | Greene | 10 | 3039 | 96 | 81 | 61 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 2514 | 85 | 65 | 45 |
| St. Louis-Farmington | Missouri | St. Charles | 101 | 5693 | 67 | 74 | 75 |
| Kansas City | Missouri | Jackson | 77 | 5462 | 60 | 64 | 71 |
| St. Louis-Farmington | Illinois | Madison | 98 | 3982 | 60 | 62 | 62 |
| St. Louis-Farmington | Missouri | Jefferson | 38 | 2665 | 56 | 51 | 45 |
| St. Louis-Farmington | Illinois | St. Clair | 170 | 5244 | 51 | 58 | 57 |
| Kansas City | Kansas | Wyandotte | 113 | 6010 | 44 | 48 | 54 |
| St. Louis-Farmington | Missouri | St. Louis City | 188 | 6147 | 34 | 38 | 55 |
| St. Louis-Farmington | Missouri | St. Francois | 4 | 1041 | 33 | 33 | 25 |
| Joplin | Missouri | Jasper | 35 | 2328 | 30 | 27 | 23 |
| St. Louis-Farmington | Missouri | Franklin | 21 | 1018 | 22 | 19 | 16 |
| Missouri non-MSA | Missouri | Marion | 3 | 463 | 18 | 13 | 10 |
| Springfield | Missouri | Christian | 1 | 654 | 17 | 15 | 12 |
| Missouri non-MSA | Missouri | Nodaway | 1 | 392 | 17 | 11 | 8 |
| St. Joseph | Missouri | Buchanan | 10 | 1298 | 16 | 12 | 8 |
| Columbia-Jefferson City | Missouri | Cole | 4 | 831 | 16 | 17 | 18 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 7 | 960 | 16 | 15 | 12 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 692 | 15 | 14 | 12 |
| Kansas City | Missouri | Cass | 11 | 1065 | 14 | 14 | 14 |
| Kansas City | Missouri | Clay | 31 | 1363 | 14 | 15 | 16 |
| Missouri non-MSA | Missouri | Perry | 4 | 388 | 13 | 9 | 6 |
| Cape Girardeau-Sikeston | Missouri | Scott | 14 | 619 | 10 | 10 | 9 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 325 | 10 | 9 | 6 |
| Missouri non-MSA | Missouri | New Madrid | 4 | 407 | 9 | 7 | 7 |
| Missouri non-MSA | Missouri | Camden | 8 | 519 | 9 | 7 | 7 |
| Kansas City | Kansas | Leavenworth | 9 | 1638 | 9 | 6 | 8 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 559 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Madison | 0 | 131 | 8 | 6 | 3 |
| Joplin | Missouri | Newton | 13 | 1077 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | Howell | 3 | 255 | 8 | 5 | 4 |
| Missouri non-MSA | Missouri | Phelps | 0 | 208 | 8 | 6 | 4 |
| Missouri non-MSA | Missouri | Pulaski | 2 | 385 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | Pettis | 8 | 790 | 7 | 9 | 12 |
| St. Louis-Farmington | Illinois | Jersey | 6 | 275 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Taney | 14 | 906 | 7 | 11 | 17 |
| St. Louis-Farmington | Illinois | Monroe | 14 | 448 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Johnson | 3 | 592 | 7 | 5 | 4 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 345 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 4 | 94 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Washington | 1 | 237 | 6 | 7 | 6 |
| Springfield | Missouri | Webster | 1 | 217 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Miller | 1 | 245 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 352 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 487 | 6 | 7 | 8 |
| St. Louis-Farmington | Illinois | Bond | 3 | 143 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Crawford | 1 | 179 | 5 | 4 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 1 | 223 | 5 | 4 | 4 |
| Kansas City | Missouri | Platte | 10 | 478 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Stone | 2 | 274 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 294 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Barry | 4 | 353 | 4 | 4 | 4 |
| St. Louis-Farmington | Missouri | Warren | 0 | 321 | 4 | 5 | 5 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 125 | 4 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 114 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 328 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Laclede | 1 | 290 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Ralls | 0 | 109 | 3 | 3 | 2 |
| Kansas City | Missouri | Lafayette | 2 | 234 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Audrain | 1 | 264 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Barton | 0 | 102 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Butler | 2 | 373 | 3 | 4 | 4 |
| Kansas City | Kansas | Miami | 0 | 188 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Saline | 7 | 543 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Adair | 0 | 228 | 3 | 3 | 3 |
| Springfield | Missouri | Polk | 0 | 281 | 2 | 3 | 3 |
| St. Joseph | Missouri | Andrew | 1 | 127 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 50 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 234 | 2 | 4 | 3 |
| Springfield | Missouri | Dallas | 1 | 108 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Texas | 1 | 98 | 2 | 2 | 2 |
| Kansas City | Missouri | Clinton | 0 | 132 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 109 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Monroe | 0 | 68 | 2 | 2 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 65 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 188 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 173 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 2 | 110 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 1 | 143 | 1 | 0 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 84 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Vernon | 0 | 82 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 63 | 1 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 72 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Benton | 1 | 156 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Wright | 0 | 89 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Grundy | 1 | 43 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | McDonald | 10 | 987 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Maries | 0 | 46 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 118 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 118 | 1 | 2 | 2 |
| St. Joseph | Kansas | Doniphan | 0 | 68 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 36 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 42 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 71 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 78 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 56 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Henry | 3 | 114 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 87 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 48 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 0 | 62 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 0 | 25 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 38 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 51 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 59 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Atchison | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 1 | 74 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 76 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 52 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 93 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 26 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 22 | 0 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 125 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 110 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 46 | 0 | 0 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 41 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 52 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 38 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 18 | 0 | 0 | 0 |
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
