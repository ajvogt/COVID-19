# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/14/2020  
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
| St. Louis-Farmington | 1264 | 37520 | 577 | 613 | 646 |
| Kansas City | 399 | 27344 | 417 | 411 | 458 |
| Missouri non-MSA | 104 | 10355 | 214 | 200 | 196 |
| Springfield | 13 | 2575 | 66 | 61 | 63 |
| Columbia-Jefferson City | 10 | 2563 | 61 | 57 | 54 |
| Joplin | 37 | 2794 | 34 | 28 | 38 |
| Cape Girardeau-Sikeston | 19 | 1248 | 22 | 17 | 20 |
| St. Joseph | 12 | 1292 | 6 | 6 | 7 |
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
| St. Louis-Farmington | Missouri | St. Louis | 673 | 15872 | 215 | 237 | 257 |
| Kansas City | Missouri | Kansas City | 65 | 7285 | 131 | 115 | 135 |
| Kansas City | Kansas | Johnson | 106 | 6127 | 98 | 96 | 98 |
| Kansas City | Missouri | Jackson | 66 | 4363 | 79 | 83 | 90 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 4408 | 73 | 80 | 99 |
| St. Louis-Farmington | Illinois | Madison | 79 | 2855 | 63 | 57 | 52 |
| St. Louis-Farmington | Missouri | St. Louis City | 178 | 5430 | 61 | 72 | 79 |
| St. Louis-Farmington | Illinois | St. Clair | 162 | 4215 | 52 | 56 | 60 |
| Kansas City | Kansas | Wyandotte | 108 | 5087 | 49 | 54 | 65 |
| Springfield | Missouri | Greene | 10 | 1737 | 48 | 43 | 41 |
| St. Louis-Farmington | Missouri | Jefferson | 26 | 1769 | 37 | 38 | 38 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1500 | 29 | 26 | 29 |
| Joplin | Missouri | Jasper | 31 | 1874 | 24 | 19 | 27 |
| Missouri non-MSA | Missouri | Taney | 3 | 678 | 22 | 21 | 18 |
| Kansas City | Missouri | Cass | 9 | 811 | 17 | 15 | 19 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 462 | 16 | 13 | 9 |
| Missouri non-MSA | Missouri | Pettis | 4 | 589 | 16 | 14 | 14 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 477 | 16 | 14 | 12 |
| Kansas City | Missouri | Clay | 22 | 1098 | 16 | 17 | 17 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 680 | 13 | 13 | 12 |
| Springfield | Missouri | Christian | 1 | 403 | 11 | 11 | 10 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 5 | 705 | 11 | 9 | 11 |
| Joplin | Missouri | Newton | 6 | 920 | 10 | 9 | 11 |
| Missouri non-MSA | Missouri | Marion | 1 | 236 | 9 | 7 | 6 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 416 | 9 | 10 | 9 |
| Missouri non-MSA | Missouri | New Madrid | 3 | 279 | 9 | 8 | 7 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 429 | 8 | 7 | 7 |
| Kansas City | Kansas | Leavenworth | 9 | 1503 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 254 | 8 | 5 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 141 | 8 | 5 | 3 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 209 | 7 | 6 | 4 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 433 | 7 | 8 | 6 |
| Kansas City | Missouri | Platte | 10 | 393 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Pike | 1 | 140 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Saline | 7 | 472 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 339 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Camden | 7 | 382 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Stone | 1 | 156 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 246 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Washington | 1 | 105 | 5 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 148 | 5 | 5 | 3 |
| St. Joseph | Missouri | Buchanan | 10 | 1112 | 5 | 4 | 5 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 334 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Butler | 2 | 297 | 4 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 168 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Perry | 4 | 249 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Barry | 4 | 273 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Adair | 0 | 178 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Miller | 1 | 138 | 3 | 4 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 216 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Holt | 0 | 31 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | Johnson | 3 | 501 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | Benton | 1 | 112 | 3 | 3 | 2 |
| Springfield | Missouri | Polk | 0 | 221 | 3 | 2 | 6 |
| Missouri non-MSA | Missouri | Laclede | 1 | 212 | 3 | 1 | 3 |
| Missouri non-MSA | Missouri | Crawford | 0 | 90 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 45 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Phelps | 0 | 104 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 153 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Howell | 2 | 164 | 2 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 156 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 94 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 192 | 2 | 3 | 5 |
| Kansas City | Missouri | Lafayette | 2 | 189 | 2 | 3 | 2 |
| Kansas City | Kansas | Miami | 0 | 150 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 244 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 237 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Texas | 0 | 64 | 2 | 2 | 1 |
| Kansas City | Missouri | Clinton | 0 | 88 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 92 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Lewis | 1 | 52 | 2 | 1 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 77 | 2 | 1 | 1 |
| Springfield | Missouri | Webster | 1 | 142 | 2 | 2 | 2 |
| Springfield | Missouri | Dallas | 1 | 72 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 60 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 63 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Audrain | 1 | 210 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Randolph | 1 | 75 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 0 | 42 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 31 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 36 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 63 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 58 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 66 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Livingston | 0 | 64 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 54 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Vernon | 0 | 58 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 149 | 1 | 1 | 1 |
| St. Louis-Farmington | Illinois | Bond | 3 | 68 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | McDonald | 8 | 955 | 1 | 2 | 7 |
| Kansas City | Missouri | Bates | 1 | 52 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 38 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 16 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 67 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 33 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 27 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 33 | 1 | 1 | 1 |
| Kansas City | Kansas | Linn | 0 | 43 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 16 | 0 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 94 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 24 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 71 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Douglas | 2 | 89 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Atchison | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 29 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 86 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 102 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Dade | 0 | 17 | 0 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 119 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Scotland | 1 | 16 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 38 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 43 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 21 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 48 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 24 | 0 | 1 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 36 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 9 | 0 | 0 | 0 |
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
