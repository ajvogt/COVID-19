# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/11/2020  
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
| St. Louis-Farmington | 1483 | 53896 | 549 | 565 | 595 |
| Missouri non-MSA | 187 | 17808 | 322 | 306 | 268 |
| Kansas City | 506 | 37741 | 307 | 341 | 384 |
| Springfield | 25 | 6033 | 162 | 153 | 120 |
| Columbia-Jefferson City | 24 | 5993 | 150 | 152 | 119 |
| Joplin | 50 | 4093 | 68 | 59 | 47 |
| Cape Girardeau-Sikeston | 25 | 2094 | 36 | 31 | 30 |
| St. Joseph | 16 | 1785 | 23 | 21 | 17 |
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
| St. Louis-Farmington | Missouri | St. Louis | 763 | 21187 | 164 | 191 | 196 |
| Springfield | Missouri | Greene | 19 | 4304 | 119 | 113 | 89 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 3695 | 100 | 106 | 75 |
| Kansas City | Kansas | Johnson | 128 | 9118 | 88 | 97 | 108 |
| St. Louis-Farmington | Illinois | Madison | 115 | 4693 | 67 | 62 | 66 |
| Kansas City | Missouri | Jackson | 85 | 6232 | 65 | 69 | 69 |
| St. Louis-Farmington | Missouri | St. Charles | 105 | 6385 | 63 | 65 | 71 |
| Joplin | Missouri | Jasper | 37 | 2924 | 61 | 51 | 38 |
| Kansas City | Missouri | Kansas City | 96 | 9932 | 58 | 78 | 101 |
| St. Louis-Farmington | Illinois | St. Clair | 176 | 5852 | 57 | 53 | 58 |
| St. Louis-Farmington | Missouri | Jefferson | 47 | 3207 | 51 | 51 | 51 |
| Missouri non-MSA | Missouri | Livingston | 1 | 342 | 37 | 19 | 9 |
| St. Louis-Farmington | Missouri | St. Francois | 6 | 1372 | 34 | 31 | 32 |
| Kansas City | Kansas | Wyandotte | 119 | 6360 | 32 | 34 | 46 |
| St. Louis-Farmington | Missouri | St. Louis City | 192 | 6505 | 28 | 33 | 40 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1088 | 24 | 22 | 21 |
| Missouri non-MSA | Missouri | Johnson | 4 | 768 | 22 | 14 | 9 |
| Springfield | Missouri | Christian | 3 | 893 | 21 | 21 | 17 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 8 | 1153 | 21 | 17 | 16 |
| St. Louis-Farmington | Missouri | Franklin | 22 | 1223 | 18 | 20 | 19 |
| St. Louis-Farmington | Illinois | Clinton | 19 | 902 | 18 | 16 | 16 |
| St. Joseph | Missouri | Buchanan | 13 | 1455 | 17 | 15 | 12 |
| Kansas City | Missouri | Clay | 39 | 1541 | 14 | 15 | 15 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 458 | 13 | 11 | 9 |
| Kansas City | Missouri | Cass | 16 | 1203 | 13 | 13 | 14 |
| Missouri non-MSA | Missouri | Camden | 9 | 647 | 12 | 11 | 9 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 558 | 11 | 8 | 7 |
| Missouri non-MSA | Missouri | Howell | 3 | 370 | 11 | 10 | 7 |
| Missouri non-MSA | Missouri | Marion | 7 | 574 | 11 | 14 | 12 |
| Missouri non-MSA | Missouri | Taney | 22 | 1008 | 10 | 8 | 12 |
| Springfield | Missouri | Webster | 1 | 330 | 10 | 9 | 6 |
| Missouri non-MSA | Missouri | Nodaway | 7 | 655 | 9 | 22 | 15 |
| Kansas City | Kansas | Miami | 0 | 282 | 9 | 6 | 4 |
| Kansas City | Kansas | Leavenworth | 9 | 1743 | 9 | 8 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 15 | 713 | 8 | 9 | 10 |
| Missouri non-MSA | Missouri | Texas | 2 | 171 | 8 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 308 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 600 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | Butler | 4 | 442 | 8 | 5 | 5 |
| Missouri non-MSA | Missouri | Miller | 1 | 329 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Phelps | 1 | 294 | 7 | 8 | 6 |
| St. Louis-Farmington | Illinois | Bond | 4 | 216 | 7 | 6 | 5 |
| St. Louis-Farmington | Illinois | Macoupin | 6 | 418 | 7 | 6 | 7 |
| Springfield | Missouri | Polk | 1 | 369 | 7 | 6 | 5 |
| Joplin | Missouri | Newton | 13 | 1169 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 419 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Madison | 0 | 224 | 6 | 9 | 6 |
| St. Louis-Farmington | Illinois | Jersey | 11 | 333 | 6 | 4 | 7 |
| Missouri non-MSA | Missouri | Pettis | 8 | 867 | 6 | 7 | 10 |
| Missouri non-MSA | Missouri | Morgan | 1 | 176 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Perry | 4 | 466 | 6 | 8 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 399 | 6 | 6 | 5 |
| Kansas City | Missouri | Platte | 10 | 552 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Laclede | 1 | 353 | 6 | 5 | 5 |
| St. Louis-Farmington | Missouri | Lincoln | 2 | 637 | 5 | 8 | 7 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 176 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Saline | 9 | 595 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 10 | 462 | 5 | 7 | 6 |
| St. Louis-Farmington | Missouri | Warren | 0 | 375 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Adair | 0 | 283 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Ozark | 0 | 70 | 5 | 3 | 1 |
| Missouri non-MSA | Missouri | Grundy | 1 | 100 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Pulaski | 2 | 435 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Stone | 2 | 324 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Washington | 1 | 279 | 4 | 3 | 6 |
| Missouri non-MSA | Missouri | Ripley | 0 | 121 | 4 | 2 | 2 |
| Kansas City | Missouri | Lafayette | 2 | 285 | 4 | 4 | 3 |
| Kansas City | Missouri | Clinton | 0 | 170 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 331 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 6 | 126 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Barry | 5 | 389 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Audrain | 2 | 333 | 3 | 6 | 4 |
| Missouri non-MSA | Missouri | Randolph | 1 | 157 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Pike | 2 | 171 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Vernon | 0 | 117 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 141 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Wright | 0 | 118 | 3 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 137 | 3 | 2 | 2 |
| St. Joseph | Missouri | Andrew | 1 | 156 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Henry | 4 | 139 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Daviess | 0 | 52 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 214 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Dent | 0 | 61 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Crawford | 2 | 225 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 255 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Wayne | 0 | 108 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | McDonald | 10 | 1008 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 124 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 71 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 90 | 1 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 2 | 85 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 99 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 128 | 1 | 2 | 3 |
| St. Joseph | Kansas | Doniphan | 0 | 89 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 91 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 65 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Douglas | 3 | 128 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 55 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 55 | 1 | 1 | 1 |
| Kansas City | Missouri | Ray | 0 | 136 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 68 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 65 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 1 | 121 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 183 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Benton | 1 | 165 | 1 | 0 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 52 | 1 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 37 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 78 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 39 | 0 | 1 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 51 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 72 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Linn | 1 | 49 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 37 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 1 | 69 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 51 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Gentry | 9 | 103 | 0 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 80 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 29 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 22 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 131 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 20 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 56 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 41 | 0 | 0 | 0 |
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
