# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/02/2020  
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
| St. Louis-Farmington | 1413 | 48955 | 591 | 581 | 606 |
| Kansas City | 445 | 34795 | 402 | 384 | 405 |
| Missouri non-MSA | 145 | 14912 | 285 | 248 | 228 |
| Columbia-Jefferson City | 17 | 4552 | 150 | 116 | 86 |
| Springfield | 13 | 4565 | 137 | 114 | 90 |
| Joplin | 48 | 3469 | 43 | 37 | 33 |
| Cape Girardeau-Sikeston | 23 | 1781 | 32 | 27 | 24 |
| St. Joseph | 12 | 1562 | 21 | 16 | 11 |
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
| St. Louis-Farmington | Missouri | St. Louis | 738 | 19665 | 207 | 192 | 213 |
| Kansas City | Kansas | Johnson | 117 | 8300 | 116 | 117 | 109 |
| Kansas City | Missouri | Kansas City | 71 | 9316 | 111 | 104 | 112 |
| Springfield | Missouri | Greene | 10 | 3248 | 104 | 88 | 67 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 2714 | 104 | 77 | 49 |
| Kansas City | Missouri | Jackson | 78 | 5606 | 70 | 63 | 71 |
| St. Louis-Farmington | Missouri | St. Charles | 105 | 5801 | 66 | 70 | 74 |
| St. Louis-Farmington | Illinois | Madison | 100 | 4102 | 62 | 61 | 63 |
| St. Louis-Farmington | Missouri | Jefferson | 40 | 2770 | 59 | 53 | 47 |
| St. Louis-Farmington | Illinois | St. Clair | 170 | 5347 | 48 | 56 | 57 |
| Kansas City | Kansas | Wyandotte | 114 | 6057 | 45 | 43 | 52 |
| St. Louis-Farmington | Missouri | St. Francois | 5 | 1099 | 37 | 34 | 26 |
| Missouri non-MSA | Missouri | Nodaway | 6 | 553 | 36 | 22 | 13 |
| St. Louis-Farmington | Missouri | St. Louis City | 188 | 6216 | 34 | 37 | 53 |
| Joplin | Missouri | Jasper | 35 | 2375 | 34 | 28 | 24 |
| St. Louis-Farmington | Missouri | Franklin | 22 | 1040 | 21 | 18 | 17 |
| Springfield | Missouri | Christian | 1 | 693 | 21 | 15 | 13 |
| Columbia-Jefferson City | Missouri | Cole | 4 | 863 | 19 | 17 | 18 |
| Missouri non-MSA | Missouri | Marion | 3 | 483 | 17 | 14 | 11 |
| Kansas City | Missouri | Clay | 31 | 1403 | 16 | 16 | 16 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 740 | 15 | 16 | 13 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 8 | 975 | 15 | 14 | 12 |
| Kansas City | Missouri | Cass | 11 | 1080 | 15 | 13 | 14 |
| St. Joseph | Missouri | Buchanan | 10 | 1302 | 15 | 11 | 8 |
| Missouri non-MSA | Missouri | Perry | 4 | 395 | 12 | 9 | 6 |
| Cape Girardeau-Sikeston | Missouri | Scott | 14 | 632 | 11 | 10 | 9 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 338 | 11 | 9 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 4 | 413 | 10 | 7 | 7 |
| Missouri non-MSA | Missouri | Madison | 0 | 147 | 10 | 7 | 4 |
| Missouri non-MSA | Missouri | Howell | 3 | 274 | 9 | 6 | 4 |
| Joplin | Missouri | Newton | 13 | 1094 | 9 | 9 | 9 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 517 | 9 | 8 | 9 |
| Missouri non-MSA | Missouri | Camden | 8 | 536 | 9 | 8 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 574 | 9 | 8 | 9 |
| Kansas City | Kansas | Leavenworth | 9 | 1669 | 9 | 8 | 9 |
| Missouri non-MSA | Missouri | Pettis | 8 | 802 | 8 | 9 | 13 |
| Missouri non-MSA | Missouri | Pulaski | 2 | 389 | 7 | 8 | 6 |
| Columbia-Jefferson City | Missouri | Cooper | 1 | 239 | 7 | 5 | 4 |
| St. Louis-Farmington | Illinois | Macoupin | 4 | 352 | 7 | 7 | 7 |
| St. Louis-Farmington | Illinois | Monroe | 14 | 461 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Phelps | 0 | 212 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Taney | 14 | 914 | 6 | 9 | 16 |
| Missouri non-MSA | Missouri | Johnson | 3 | 597 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Crawford | 1 | 193 | 6 | 5 | 4 |
| Kansas City | Missouri | Platte | 10 | 492 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 3 | 93 | 6 | 3 | 2 |
| Missouri non-MSA | Missouri | Miller | 1 | 252 | 5 | 6 | 5 |
| Springfield | Missouri | Webster | 1 | 224 | 5 | 4 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 6 | 278 | 5 | 7 | 6 |
| Missouri non-MSA | Missouri | Washington | 1 | 239 | 5 | 6 | 6 |
| St. Louis-Farmington | Illinois | Bond | 3 | 154 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 356 | 5 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 125 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Stone | 2 | 281 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Laclede | 1 | 301 | 4 | 4 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 130 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Barry | 5 | 358 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 340 | 4 | 4 | 4 |
| St. Louis-Farmington | Missouri | Warren | 0 | 330 | 4 | 4 | 5 |
| Kansas City | Missouri | Lafayette | 2 | 245 | 4 | 3 | 3 |
| Springfield | Missouri | Polk | 0 | 292 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Butler | 3 | 379 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Audrain | 1 | 268 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 115 | 3 | 3 | 3 |
| Kansas City | Kansas | Miami | 0 | 200 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 296 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Texas | 1 | 101 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 236 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 231 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Saline | 7 | 547 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Barton | 0 | 105 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Grundy | 1 | 52 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Randolph | 1 | 128 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 49 | 2 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 125 | 2 | 1 | 1 |
| Springfield | Missouri | Dallas | 1 | 108 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 112 | 2 | 2 | 2 |
| St. Joseph | Missouri | DeKalb | 1 | 67 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 3 | 191 | 2 | 1 | 2 |
| Kansas City | Missouri | Bates | 1 | 77 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 87 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 2 | 112 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 70 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Pike | 2 | 145 | 1 | 0 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 121 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Vernon | 0 | 83 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 91 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | McDonald | 10 | 992 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Harrison | 1 | 73 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 44 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 46 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 82 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 64 | 1 | 1 | 1 |
| Kansas City | Missouri | Clinton | 0 | 129 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Carter | 1 | 37 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 30 | 1 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 68 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 64 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 0 | 26 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Henry | 3 | 116 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 0 | 29 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 80 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 39 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 174 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 50 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Benton | 1 | 155 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Ripley | 0 | 91 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Daviess | 0 | 26 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 56 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 53 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 29 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 94 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 112 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 24 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 55 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 49 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 1 | 74 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 51 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 22 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 42 | 0 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 124 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 46 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 38 | 0 | 0 | 0 |
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
