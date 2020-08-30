# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/30/2020  
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
| St. Louis-Farmington | 1388 | 47328 | 578 | 590 | 613 |
| Kansas City | 440 | 33877 | 383 | 391 | 409 |
| Missouri non-MSA | 137 | 14198 | 248 | 237 | 221 |
| Springfield | 13 | 4184 | 119 | 104 | 82 |
| Columbia-Jefferson City | 16 | 4088 | 106 | 100 | 77 |
| Joplin | 48 | 3357 | 36 | 33 | 32 |
| Cape Girardeau-Sikeston | 22 | 1715 | 27 | 28 | 23 |
| St. Joseph | 12 | 1534 | 20 | 16 | 11 |
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
| St. Louis-Farmington | Missouri | St. Louis | 729 | 19071 | 192 | 190 | 217 |
| Kansas City | Kansas | Johnson | 116 | 8048 | 115 | 120 | 108 |
| Kansas City | Missouri | Kansas City | 69 | 9109 | 111 | 112 | 114 |
| Springfield | Missouri | Greene | 10 | 2947 | 90 | 79 | 60 |
| St. Louis-Farmington | Missouri | St. Charles | 99 | 5632 | 67 | 73 | 78 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 2358 | 66 | 58 | 41 |
| St. Louis-Farmington | Illinois | Madison | 97 | 3956 | 64 | 64 | 63 |
| St. Louis-Farmington | Illinois | St. Clair | 170 | 5227 | 59 | 61 | 60 |
| Kansas City | Missouri | Jackson | 77 | 5386 | 54 | 61 | 73 |
| St. Louis-Farmington | Missouri | Jefferson | 37 | 2584 | 50 | 49 | 45 |
| Kansas City | Kansas | Wyandotte | 113 | 5980 | 46 | 46 | 55 |
| St. Louis-Farmington | Missouri | St. Louis City | 188 | 6086 | 32 | 38 | 55 |
| St. Louis-Farmington | Missouri | St. Francois | 4 | 988 | 29 | 35 | 23 |
| Joplin | Missouri | Jasper | 35 | 2286 | 28 | 24 | 22 |
| St. Louis-Farmington | Missouri | Franklin | 20 | 1002 | 22 | 19 | 17 |
| Missouri non-MSA | Missouri | Nodaway | 1 | 390 | 18 | 12 | 8 |
| Missouri non-MSA | Missouri | Marion | 3 | 453 | 18 | 13 | 10 |
| Springfield | Missouri | Christian | 1 | 634 | 17 | 15 | 12 |
| Columbia-Jefferson City | Missouri | Cole | 4 | 820 | 16 | 20 | 18 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 691 | 16 | 15 | 12 |
| Kansas City | Missouri | Clay | 31 | 1355 | 15 | 15 | 16 |
| Kansas City | Missouri | Cass | 11 | 1053 | 15 | 14 | 15 |
| St. Joseph | Missouri | Buchanan | 10 | 1276 | 14 | 10 | 7 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 7 | 944 | 13 | 14 | 12 |
| Missouri non-MSA | Missouri | Perry | 4 | 369 | 12 | 8 | 5 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 316 | 10 | 9 | 7 |
| Kansas City | Kansas | Leavenworth | 9 | 1638 | 9 | 6 | 8 |
| Missouri non-MSA | Missouri | Camden | 8 | 510 | 9 | 8 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 551 | 9 | 8 | 9 |
| St. Louis-Farmington | Illinois | Jersey | 6 | 275 | 8 | 9 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 4 | 398 | 8 | 7 | 7 |
| Cape Girardeau-Sikeston | Missouri | Scott | 14 | 606 | 8 | 10 | 9 |
| Joplin | Missouri | Newton | 13 | 1071 | 8 | 9 | 9 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 345 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 383 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | Taney | 14 | 900 | 7 | 13 | 17 |
| Missouri non-MSA | Missouri | Phelps | 0 | 199 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Pettis | 8 | 789 | 7 | 10 | 13 |
| St. Louis-Farmington | Illinois | Monroe | 14 | 444 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Madison | 0 | 119 | 7 | 6 | 3 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 351 | 7 | 7 | 5 |
| Missouri non-MSA | Missouri | Johnson | 3 | 587 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Washington | 1 | 228 | 6 | 7 | 5 |
| Missouri non-MSA | Missouri | Howell | 3 | 242 | 6 | 4 | 3 |
| Springfield | Missouri | Webster | 1 | 214 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Crawford | 1 | 178 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Miller | 1 | 238 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Gasconade | 4 | 84 | 5 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 1 | 220 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 290 | 4 | 3 | 2 |
| St. Louis-Farmington | Missouri | Warren | 0 | 319 | 4 | 5 | 5 |
| St. Louis-Farmington | Illinois | Bond | 3 | 131 | 4 | 3 | 2 |
| Kansas City | Missouri | Platte | 10 | 472 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Barry | 4 | 352 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 473 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Stone | 2 | 267 | 4 | 7 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 323 | 4 | 4 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 110 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Butler | 2 | 373 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Ralls | 0 | 108 | 4 | 3 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 121 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Saline | 7 | 543 | 3 | 4 | 4 |
| Kansas City | Missouri | Lafayette | 2 | 233 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Barton | 0 | 102 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Laclede | 1 | 285 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Audrain | 1 | 260 | 3 | 2 | 2 |
| Springfield | Missouri | Polk | 0 | 281 | 3 | 3 | 3 |
| Kansas City | Kansas | Miami | 0 | 188 | 3 | 2 | 2 |
| Springfield | Missouri | Dallas | 1 | 108 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 224 | 2 | 3 | 3 |
| St. Joseph | Missouri | Andrew | 1 | 127 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 47 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 230 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Texas | 1 | 96 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Monroe | 0 | 68 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 105 | 2 | 2 | 2 |
| Kansas City | Missouri | Clinton | 0 | 128 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Benton | 1 | 155 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 173 | 2 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 63 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | McDonald | 10 | 987 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 2 | 109 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 186 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 0 | 63 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Vernon | 0 | 80 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 82 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 88 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 117 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 112 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Maries | 0 | 44 | 1 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 68 | 1 | 1 | 0 |
| Kansas City | Missouri | Bates | 1 | 70 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 1 | 140 | 1 | 0 | 2 |
| Missouri non-MSA | Missouri | Carter | 1 | 36 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 40 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 78 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 56 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 70 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 41 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 86 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 0 | 61 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 47 | 1 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 26 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 36 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Henry | 3 | 112 | 0 | 1 | 1 |
| Kansas City | Missouri | Ray | 0 | 124 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Lewis | 2 | 59 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Livingston | 1 | 73 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 51 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 92 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 75 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 46 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 48 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 110 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 17 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 52 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 11 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 38 | 0 | 0 | 0 |
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
