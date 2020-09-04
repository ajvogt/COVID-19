# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/04/2020  
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
| St. Louis-Farmington | 1437 | 50050 | 580 | 577 | 602 |
| Kansas City | 453 | 35592 | 376 | 389 | 400 |
| Missouri non-MSA | 146 | 15554 | 290 | 259 | 236 |
| Columbia-Jefferson City | 18 | 4937 | 153 | 129 | 96 |
| Springfield | 13 | 4898 | 144 | 123 | 97 |
| Joplin | 48 | 3611 | 49 | 42 | 36 |
| Cape Girardeau-Sikeston | 24 | 1841 | 27 | 27 | 25 |
| St. Joseph | 13 | 1623 | 20 | 17 | 13 |
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
| St. Louis-Farmington | Missouri | St. Louis | 755 | 20039 | 218 | 196 | 208 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 2994 | 112 | 88 | 57 |
| Springfield | Missouri | Greene | 10 | 3471 | 107 | 92 | 72 |
| Kansas City | Kansas | Johnson | 118 | 8499 | 106 | 117 | 108 |
| Kansas City | Missouri | Kansas City | 72 | 9520 | 97 | 103 | 112 |
| Kansas City | Missouri | Jackson | 81 | 5773 | 74 | 67 | 71 |
| St. Louis-Farmington | Missouri | St. Charles | 105 | 5939 | 66 | 67 | 73 |
| St. Louis-Farmington | Illinois | Madison | 103 | 4219 | 57 | 60 | 65 |
| St. Louis-Farmington | Missouri | Jefferson | 40 | 2849 | 51 | 50 | 47 |
| St. Louis-Farmington | Illinois | St. Clair | 173 | 5450 | 49 | 56 | 58 |
| Joplin | Missouri | Jasper | 35 | 2494 | 41 | 33 | 27 |
| St. Louis-Farmington | Missouri | St. Louis City | 188 | 6304 | 38 | 37 | 52 |
| Kansas City | Kansas | Wyandotte | 117 | 6136 | 36 | 41 | 50 |
| Missouri non-MSA | Missouri | Nodaway | 6 | 590 | 35 | 24 | 14 |
| St. Louis-Farmington | Missouri | St. Francois | 5 | 1134 | 28 | 32 | 27 |
| Springfield | Missouri | Christian | 1 | 741 | 21 | 17 | 14 |
| St. Louis-Farmington | Missouri | Franklin | 22 | 1092 | 21 | 20 | 17 |
| Columbia-Jefferson City | Missouri | Cole | 4 | 916 | 20 | 18 | 19 |
| Kansas City | Missouri | Clay | 31 | 1443 | 17 | 17 | 16 |
| Missouri non-MSA | Missouri | Marion | 3 | 497 | 17 | 13 | 11 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 771 | 14 | 15 | 13 |
| St. Joseph | Missouri | Buchanan | 11 | 1336 | 14 | 12 | 9 |
| Kansas City | Missouri | Cass | 11 | 1108 | 14 | 14 | 14 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 8 | 1003 | 12 | 13 | 13 |
| Missouri non-MSA | Missouri | Madison | 0 | 176 | 11 | 9 | 5 |
| Missouri non-MSA | Missouri | Perry | 4 | 422 | 10 | 10 | 7 |
| Missouri non-MSA | Missouri | Camden | 8 | 563 | 10 | 9 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 14 | 655 | 10 | 9 | 9 |
| Missouri non-MSA | Missouri | Howell | 3 | 291 | 10 | 7 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 544 | 10 | 8 | 9 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 598 | 10 | 9 | 8 |
| Missouri non-MSA | Missouri | Pettis | 8 | 822 | 9 | 8 | 12 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 362 | 9 | 9 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 5 | 425 | 9 | 7 | 7 |
| Joplin | Missouri | Newton | 13 | 1117 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | Phelps | 0 | 240 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | Audrain | 1 | 308 | 8 | 5 | 3 |
| Springfield | Missouri | Webster | 1 | 257 | 8 | 6 | 4 |
| Kansas City | Kansas | Leavenworth | 9 | 1680 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Miller | 1 | 274 | 7 | 7 | 5 |
| Kansas City | Missouri | Platte | 10 | 508 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Taney | 14 | 933 | 6 | 8 | 15 |
| Missouri non-MSA | Missouri | Crawford | 1 | 209 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 355 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Johnson | 3 | 609 | 5 | 5 | 4 |
| Springfield | Missouri | Polk | 0 | 315 | 5 | 4 | 4 |
| St. Louis-Farmington | Illinois | Bond | 3 | 162 | 5 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 1 | 252 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Laclede | 1 | 311 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Pulaski | 2 | 402 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 3 | 98 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 370 | 5 | 5 | 5 |
| St. Louis-Farmington | Illinois | Monroe | 14 | 477 | 5 | 7 | 6 |
| Kansas City | Missouri | Lafayette | 2 | 257 | 4 | 3 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 340 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Stone | 2 | 294 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Grundy | 1 | 66 | 4 | 2 | 1 |
| St. Louis-Farmington | Illinois | Macoupin | 5 | 364 | 4 | 6 | 7 |
| Kansas City | Kansas | Miami | 0 | 218 | 4 | 3 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 138 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 248 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Randolph | 1 | 132 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Washington | 1 | 251 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Saline | 7 | 557 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Texas | 1 | 113 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 130 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Butler | 3 | 386 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Barry | 5 | 362 | 3 | 3 | 4 |
| St. Louis-Farmington | Illinois | Jersey | 6 | 285 | 3 | 6 | 7 |
| Missouri non-MSA | Missouri | Ralls | 0 | 116 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 303 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 118 | 2 | 2 | 2 |
| Kansas City | Missouri | Clinton | 0 | 142 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 132 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 239 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Barton | 0 | 110 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Douglas | 2 | 119 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 0 | 35 | 2 | 1 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 136 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 196 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 57 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 92 | 2 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 73 | 2 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 78 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 78 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 93 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Daviess | 0 | 33 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 87 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 2 | 146 | 1 | 0 | 2 |
| Missouri non-MSA | Missouri | Dent | 0 | 44 | 1 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 78 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 0 | 33 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 48 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 9 | 100 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 32 | 1 | 0 | 0 |
| Springfield | Missouri | Dallas | 1 | 114 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Holt | 0 | 67 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Cedar | 0 | 55 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 31 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | McDonald | 10 | 993 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 47 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 81 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 93 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 120 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 95 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 27 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 114 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 39 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 66 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 72 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Mercer | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 1 | 77 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 60 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 46 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 54 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 176 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Benton | 1 | 158 | 0 | 2 | 2 |
| Kansas City | Missouri | Ray | 0 | 128 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 57 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 19 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 56 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 39 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 27 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 27 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 45 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 42 | 0 | 0 | 0 |
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
