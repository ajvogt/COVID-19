# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/13/2021  
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
| St. Louis-Farmington | 3672 | 220451 | 1652 | 1595 | 1542 |
| Kansas City | 1777 | 149459 | 1304 | 1212 | 1136 |
| Missouri non-MSA | 1557 | 99825 | 672 | 662 | 624 |
| Springfield | 461 | 32301 | 265 | 264 | 238 |
| Columbia-Jefferson City | 237 | 31499 | 181 | 175 | 172 |
| Joplin | 234 | 14460 | 88 | 91 | 74 |
| Cape Girardeau-Sikeston | 192 | 11767 | 63 | 59 | 58 |
| St. Joseph | 151 | 9259 | 56 | 55 | 50 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1514 | 76107 | 600 | 562 | 534 |
| Kansas City | Kansas | Johnson | 517 | 43450 | 438 | 398 | 376 |
| Kansas City | Missouri | Kansas City | 375 | 32910 | 245 | 233 | 209 |
| Kansas City | Missouri | Jackson | 279 | 25848 | 228 | 202 | 181 |
| St. Louis-Farmington | Missouri | St. Charles | 315 | 29481 | 213 | 195 | 195 |
| St. Louis-Farmington | Illinois | Madison | 444 | 23239 | 202 | 191 | 182 |
| St. Louis-Farmington | Illinois | St. Clair | 398 | 21264 | 197 | 188 | 164 |
| Springfield | Missouri | Greene | 313 | 20784 | 169 | 168 | 152 |
| St. Louis-Farmington | Missouri | Jefferson | 153 | 16734 | 145 | 139 | 120 |
| Kansas City | Kansas | Wyandotte | 201 | 16794 | 109 | 113 | 121 |
| Columbia-Jefferson City | Missouri | Boone | 54 | 14316 | 90 | 84 | 84 |
| St. Louis-Farmington | Missouri | Franklin | 122 | 7339 | 68 | 66 | 56 |
| Joplin | Missouri | Jasper | 174 | 10761 | 67 | 69 | 56 |
| Kansas City | Missouri | Cass | 62 | 6180 | 61 | 52 | 50 |
| Kansas City | Missouri | Clay | 117 | 6895 | 60 | 53 | 48 |
| Springfield | Missouri | Christian | 60 | 6098 | 51 | 52 | 50 |
| Kansas City | Kansas | Leavenworth | 46 | 5512 | 47 | 40 | 38 |
| St. Louis-Farmington | Missouri | St. Francois | 79 | 7043 | 46 | 45 | 43 |
| Columbia-Jefferson City | Missouri | Cole | 101 | 8052 | 40 | 40 | 36 |
| St. Louis-Farmington | Illinois | Macoupin | 92 | 3657 | 39 | 32 | 29 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 106 | 6874 | 36 | 36 | 37 |
| St. Joseph | Missouri | Buchanan | 108 | 6421 | 34 | 33 | 30 |
| St. Louis-Farmington | Illinois | Clinton | 81 | 4831 | 33 | 32 | 30 |
| Missouri non-MSA | Missouri | Taney | 60 | 4113 | 31 | 29 | 23 |
| Missouri non-MSA | Missouri | Pettis | 68 | 4355 | 30 | 26 | 27 |
| Missouri non-MSA | Missouri | Pulaski | 32 | 2805 | 30 | 20 | 21 |
| Missouri non-MSA | Missouri | Camden | 66 | 3426 | 28 | 24 | 21 |
| St. Louis-Farmington | Illinois | Monroe | 63 | 3444 | 27 | 28 | 29 |
| Kansas City | Kansas | Miami | 15 | 2133 | 27 | 29 | 26 |
| Kansas City | Missouri | Platte | 26 | 2704 | 26 | 27 | 24 |
| St. Louis-Farmington | Missouri | Lincoln | 23 | 3817 | 25 | 24 | 27 |
| Springfield | Missouri | Webster | 44 | 2698 | 23 | 24 | 20 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3461 | 23 | 19 | 19 |
| Columbia-Jefferson City | Missouri | Callaway | 29 | 4048 | 23 | 25 | 25 |
| Joplin | Missouri | Newton | 60 | 3699 | 20 | 22 | 18 |
| Missouri non-MSA | Missouri | Howell | 39 | 2540 | 19 | 19 | 16 |
| Cape Girardeau-Sikeston | Missouri | Scott | 67 | 3521 | 18 | 16 | 15 |
| Missouri non-MSA | Missouri | Lawrence | 60 | 2532 | 17 | 19 | 14 |
| Missouri non-MSA | Missouri | Adair | 6 | 1799 | 16 | 16 | 17 |
| Missouri non-MSA | Missouri | Butler | 17 | 3011 | 16 | 17 | 15 |
| Springfield | Missouri | Polk | 25 | 1981 | 16 | 14 | 12 |
| Missouri non-MSA | Missouri | Saline | 26 | 2185 | 15 | 15 | 13 |
| St. Louis-Farmington | Illinois | Bond | 20 | 1695 | 15 | 11 | 11 |
| Missouri non-MSA | Missouri | Phelps | 93 | 2695 | 15 | 19 | 19 |
| Kansas City | Missouri | Lafayette | 44 | 2241 | 14 | 14 | 15 |
| St. Louis-Farmington | Missouri | Warren | 11 | 1807 | 14 | 14 | 14 |
| Missouri non-MSA | Missouri | Washington | 41 | 1934 | 14 | 13 | 10 |
| Missouri non-MSA | Missouri | Laclede | 51 | 2669 | 13 | 15 | 15 |
| Missouri non-MSA | Missouri | Livingston | 25 | 1147 | 13 | 10 | 9 |
| Kansas City | Missouri | Ray | 11 | 1268 | 13 | 12 | 13 |
| Missouri non-MSA | Missouri | Stone | 28 | 1785 | 13 | 14 | 12 |
| Missouri non-MSA | Missouri | Vernon | 29 | 1234 | 12 | 19 | 14 |
| Missouri non-MSA | Missouri | Crawford | 21 | 1865 | 12 | 14 | 15 |
| Missouri non-MSA | Missouri | Miller | 44 | 2169 | 12 | 12 | 13 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2214 | 12 | 11 | 12 |
| Kansas City | Missouri | Clinton | 60 | 1381 | 12 | 11 | 10 |
| Missouri non-MSA | Missouri | Wright | 24 | 1221 | 11 | 13 | 10 |
| Missouri non-MSA | Missouri | Audrain | 43 | 1916 | 11 | 20 | 18 |
| Missouri non-MSA | Missouri | Marion | 32 | 2482 | 11 | 12 | 12 |
| Missouri non-MSA | Missouri | Barry | 37 | 1935 | 11 | 12 | 10 |
| St. Louis-Farmington | Illinois | Jersey | 51 | 2122 | 10 | 12 | 16 |
| Missouri non-MSA | Missouri | Henry | 25 | 1540 | 10 | 9 | 9 |
| Missouri non-MSA | Missouri | McDonald | 23 | 1774 | 10 | 9 | 8 |
| Missouri non-MSA | Missouri | Macon | 10 | 1018 | 10 | 8 | 8 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17451 | 10 | 46 | 82 |
| Missouri non-MSA | Missouri | Benton | 19 | 1314 | 10 | 10 | 9 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2440 | 9 | 11 | 8 |
| Kansas City | Kansas | Linn | 3 | 617 | 9 | 9 | 7 |
| Missouri non-MSA | Missouri | Randolph | 20 | 1700 | 9 | 8 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2111 | 9 | 8 | 7 |
| Kansas City | Missouri | Bates | 14 | 940 | 9 | 10 | 9 |
| St. Joseph | Kansas | Doniphan | 7 | 810 | 9 | 8 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 9 | 1277 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Morgan | 31 | 1540 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Pike | 17 | 1357 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | Barton | 9 | 851 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 39 | 1691 | 8 | 6 | 7 |
| Missouri non-MSA | Missouri | Oregon | 3 | 616 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Texas | 20 | 1438 | 7 | 8 | 10 |
| Columbia-Jefferson City | Missouri | Moniteau | 19 | 1587 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Grundy | 27 | 747 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Gasconade | 30 | 758 | 7 | 7 | 6 |
| St. Joseph | Missouri | Andrew | 15 | 1192 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Perry | 20 | 1935 | 7 | 6 | 8 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1558 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Ozark | 5 | 444 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Linn | 11 | 463 | 6 | 3 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 11 | 1500 | 6 | 7 | 8 |
| St. Joseph | Missouri | DeKalb | 21 | 836 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Harrison | 10 | 695 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Madison | 11 | 1279 | 5 | 7 | 8 |
| Missouri non-MSA | Missouri | Wayne | 9 | 728 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Douglas | 20 | 688 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Carroll | 18 | 717 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Ripley | 9 | 729 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1336 | 5 | 5 | 4 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1002 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Cedar | 9 | 587 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Gentry | 16 | 659 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Daviess | 9 | 519 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 11 | 704 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Iron | 1 | 444 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Ralls | 8 | 710 | 4 | 4 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 661 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 503 | 3 | 4 | 3 |
| Springfield | Missouri | Dallas | 19 | 740 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Lewis | 3 | 583 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Atchison | 6 | 284 | 3 | 1 | 1 |
| Kansas City | Missouri | Caldwell | 7 | 586 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 437 | 3 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 370 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 19 | 1169 | 3 | 3 | 4 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 420 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Dent | 9 | 742 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Monroe | 7 | 555 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Chariton | 3 | 365 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 231 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 7 | 400 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 535 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Dade | 10 | 388 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 2 | 150 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 490 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 4 | 321 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 245 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 5 | 391 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 342 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 9 | 445 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 128 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 206 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 157 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 233 | 0 | 0 | 0 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
* 1/4/2021: small fix for including 2021 data
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
