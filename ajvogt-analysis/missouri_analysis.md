# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/27/2020  
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
| St. Louis-Farmington | 3209 | 194539 | 1326 | 1596 | 1767 |
| Kansas City | 1517 | 129614 | 925 | 1049 | 1169 |
| Missouri non-MSA | 1313 | 89403 | 577 | 626 | 736 |
| Springfield | 373 | 28119 | 193 | 225 | 242 |
| Columbia-Jefferson City | 193 | 28747 | 170 | 184 | 205 |
| Joplin | 197 | 13058 | 58 | 62 | 67 |
| Cape Girardeau-Sikeston | 172 | 10814 | 52 | 60 | 77 |
| St. Joseph | 127 | 8353 | 40 | 46 | 68 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1342 | 66843 | 424 | 526 | 575 |
| Kansas City | Kansas | Johnson | 413 | 36727 | 234 | 326 | 359 |
| Kansas City | Missouri | Kansas City | 349 | 29167 | 188 | 192 | 224 |
| St. Louis-Farmington | Missouri | St. Charles | 281 | 26393 | 185 | 218 | 237 |
| Kansas City | Missouri | Jackson | 230 | 22654 | 178 | 168 | 201 |
| St. Louis-Farmington | Illinois | Madison | 373 | 20238 | 158 | 196 | 212 |
| Springfield | Missouri | Greene | 251 | 18097 | 126 | 142 | 154 |
| St. Louis-Farmington | Illinois | St. Clair | 331 | 18259 | 124 | 151 | 183 |
| Kansas City | Kansas | Wyandotte | 193 | 14857 | 107 | 121 | 122 |
| St. Louis-Farmington | Missouri | Jefferson | 126 | 14556 | 97 | 115 | 132 |
| St. Louis-Farmington | Missouri | St. Louis City | 292 | 16463 | 97 | 119 | 130 |
| Columbia-Jefferson City | Missouri | Boone | 42 | 13022 | 88 | 95 | 97 |
| Kansas City | Missouri | Cass | 52 | 5354 | 49 | 53 | 57 |
| St. Louis-Farmington | Missouri | Franklin | 109 | 6308 | 48 | 51 | 54 |
| Kansas City | Missouri | Clay | 93 | 6057 | 48 | 46 | 53 |
| Joplin | Missouri | Jasper | 154 | 9690 | 42 | 46 | 53 |
| Springfield | Missouri | Christian | 45 | 5263 | 42 | 51 | 54 |
| Missouri non-MSA | Missouri | Pulaski | 27 | 2494 | 37 | 25 | 31 |
| St. Louis-Farmington | Missouri | St. Francois | 68 | 6308 | 37 | 45 | 45 |
| Columbia-Jefferson City | Missouri | Cole | 85 | 7418 | 34 | 36 | 46 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 95 | 6278 | 34 | 40 | 47 |
| St. Louis-Farmington | Illinois | Monroe | 56 | 2977 | 31 | 30 | 32 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3438 | 30 | 34 | 35 |
| St. Louis-Farmington | Illinois | Clinton | 80 | 4328 | 27 | 32 | 36 |
| St. Joseph | Missouri | Buchanan | 91 | 5887 | 24 | 29 | 45 |
| Columbia-Jefferson City | Missouri | Callaway | 19 | 3635 | 23 | 25 | 29 |
| Missouri non-MSA | Missouri | Phelps | 82 | 2391 | 22 | 20 | 23 |
| Missouri non-MSA | Missouri | Crawford | 19 | 1629 | 21 | 17 | 15 |
| Kansas City | Missouri | Platte | 20 | 2279 | 21 | 21 | 22 |
| Missouri non-MSA | Missouri | Camden | 60 | 3048 | 21 | 20 | 21 |
| St. Louis-Farmington | Illinois | Macoupin | 67 | 3130 | 20 | 26 | 34 |
| Missouri non-MSA | Missouri | Johnson | 28 | 3167 | 20 | 22 | 23 |
| Kansas City | Kansas | Miami | 10 | 1648 | 19 | 22 | 22 |
| Kansas City | Missouri | Lafayette | 38 | 1997 | 18 | 17 | 17 |
| Missouri non-MSA | Missouri | Adair | 4 | 1547 | 18 | 19 | 16 |
| Kansas City | Kansas | Leavenworth | 38 | 4823 | 17 | 34 | 40 |
| Missouri non-MSA | Missouri | Taney | 51 | 3660 | 17 | 20 | 30 |
| St. Louis-Farmington | Illinois | Jersey | 36 | 1870 | 16 | 18 | 22 |
| Missouri non-MSA | Missouri | Laclede | 44 | 2434 | 16 | 17 | 22 |
| Joplin | Missouri | Newton | 43 | 3368 | 16 | 15 | 14 |
| Missouri non-MSA | Missouri | Audrain | 31 | 1584 | 15 | 17 | 18 |
| Missouri non-MSA | Missouri | Howell | 36 | 2233 | 15 | 13 | 22 |
| Missouri non-MSA | Missouri | Butler | 14 | 2743 | 15 | 15 | 21 |
| Springfield | Missouri | Webster | 38 | 2322 | 15 | 18 | 18 |
| Cape Girardeau-Sikeston | Missouri | Scott | 59 | 3261 | 14 | 15 | 23 |
| Missouri non-MSA | Missouri | Saline | 21 | 1957 | 14 | 14 | 13 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1586 | 14 | 15 | 13 |
| Kansas City | Missouri | Ray | 8 | 1065 | 13 | 14 | 13 |
| Missouri non-MSA | Missouri | Pettis | 60 | 3879 | 12 | 26 | 41 |
| Missouri non-MSA | Missouri | Miller | 42 | 1976 | 12 | 16 | 17 |
| Missouri non-MSA | Missouri | Marion | 24 | 2264 | 11 | 12 | 18 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 3 | 1380 | 11 | 10 | 11 |
| St. Louis-Farmington | Illinois | Bond | 16 | 1486 | 10 | 13 | 15 |
| Missouri non-MSA | Missouri | Randolph | 15 | 1569 | 10 | 10 | 13 |
| Missouri non-MSA | Missouri | Lawrence | 47 | 2251 | 9 | 11 | 13 |
| Missouri non-MSA | Missouri | Pike | 14 | 1239 | 9 | 9 | 12 |
| Missouri non-MSA | Missouri | Stone | 24 | 1558 | 9 | 12 | 13 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1617 | 9 | 8 | 7 |
| Missouri non-MSA | Missouri | Barry | 35 | 1751 | 9 | 10 | 11 |
| Missouri non-MSA | Missouri | Washington | 39 | 1724 | 9 | 8 | 10 |
| Kansas City | Missouri | Clinton | 56 | 1208 | 9 | 9 | 11 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2286 | 8 | 8 | 11 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1460 | 8 | 10 | 10 |
| Missouri non-MSA | Missouri | Vernon | 16 | 937 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | Wright | 23 | 1008 | 8 | 8 | 8 |
| Kansas City | Missouri | Bates | 10 | 774 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Iron | 1 | 382 | 8 | 6 | 5 |
| Springfield | Missouri | Polk | 21 | 1759 | 7 | 10 | 13 |
| Missouri non-MSA | Missouri | Madison | 10 | 1145 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | Dunklin | 15 | 2029 | 7 | 13 | 12 |
| Missouri non-MSA | Missouri | Livingston | 21 | 993 | 7 | 8 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1149 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Henry | 21 | 1395 | 6 | 9 | 11 |
| Missouri non-MSA | Missouri | Perry | 19 | 1815 | 6 | 9 | 10 |
| St. Joseph | Missouri | Andrew | 13 | 1050 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | New Madrid | 29 | 1567 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | Carroll | 14 | 636 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Morgan | 21 | 1408 | 6 | 9 | 12 |
| Missouri non-MSA | Missouri | Gasconade | 29 | 654 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Macon | 8 | 887 | 6 | 8 | 7 |
| Missouri non-MSA | Missouri | Texas | 16 | 1288 | 6 | 11 | 11 |
| Missouri non-MSA | Missouri | Douglas | 19 | 597 | 6 | 6 | 6 |
| St. Joseph | Kansas | Doniphan | 5 | 673 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Ralls | 6 | 631 | 5 | 4 | 6 |
| Columbia-Jefferson City | Missouri | Moniteau | 17 | 1455 | 5 | 6 | 8 |
| Kansas City | Missouri | Caldwell | 4 | 529 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Stoddard | 32 | 1982 | 5 | 8 | 13 |
| Kansas City | Kansas | Linn | 3 | 475 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Dent | 7 | 680 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Wayne | 6 | 645 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Harrison | 7 | 602 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 20 | 1256 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Montgomery | 8 | 475 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Grundy | 22 | 656 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Daviess | 9 | 454 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Gentry | 16 | 588 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 646 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Monroe | 5 | 497 | 3 | 3 | 4 |
| St. Joseph | Missouri | DeKalb | 18 | 743 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Chariton | 2 | 319 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ripley | 8 | 651 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Oregon | 3 | 517 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Benton | 16 | 1156 | 3 | 8 | 13 |
| Missouri non-MSA | Missouri | Barton | 9 | 747 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Lewis | 3 | 523 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Dade | 8 | 360 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 11 | 1107 | 3 | 5 | 9 |
| Missouri non-MSA | Missouri | Clark | 4 | 364 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Maries | 6 | 451 | 2 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 608 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 4 | 435 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Ozark | 4 | 364 | 2 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 11 | 941 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 191 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shannon | 9 | 406 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 6 | 366 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Cedar | 8 | 495 | 1 | 2 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 334 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 11 | 403 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Shelby | 3 | 285 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 9 | 420 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Worth | 1 | 115 | 1 | 0 | 1 |
| Springfield | Missouri | Dallas | 18 | 678 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Scotland | 3 | 225 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 195 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 1 | 124 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 221 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 323 | 1 | 1 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 3 | 356 | 0 | 1 | 4 |
| Missouri non-MSA | Missouri | Atchison | 5 | 259 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 147 | 0 | 0 | 0 |
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
