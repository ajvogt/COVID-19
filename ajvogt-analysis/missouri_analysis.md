# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/11/2021  
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
| St. Louis-Farmington | 3577 | 218133 | 1665 | 1621 | 1614 |
| Kansas City | 1743 | 147103 | 1209 | 1227 | 1115 |
| Missouri non-MSA | 1511 | 99069 | 675 | 669 | 688 |
| Springfield | 448 | 31943 | 283 | 260 | 255 |
| Columbia-Jefferson City | 218 | 31347 | 182 | 181 | 186 |
| Joplin | 232 | 14386 | 93 | 93 | 77 |
| Cape Girardeau-Sikeston | 188 | 11709 | 67 | 60 | 63 |
| St. Joseph | 142 | 9168 | 53 | 55 | 53 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1475 | 75200 | 600 | 577 | 542 |
| Kansas City | Kansas | Johnson | 517 | 42456 | 394 | 409 | 343 |
| Kansas City | Missouri | Kansas City | 369 | 32740 | 264 | 244 | 225 |
| St. Louis-Farmington | Missouri | St. Charles | 300 | 29212 | 212 | 195 | 213 |
| St. Louis-Farmington | Illinois | Madison | 433 | 22953 | 199 | 187 | 189 |
| Kansas City | Missouri | Jackson | 264 | 25384 | 198 | 189 | 182 |
| St. Louis-Farmington | Illinois | St. Clair | 392 | 20972 | 197 | 182 | 166 |
| Springfield | Missouri | Greene | 306 | 20542 | 182 | 166 | 163 |
| St. Louis-Farmington | Missouri | Jefferson | 149 | 16551 | 150 | 138 | 129 |
| Kansas City | Kansas | Wyandotte | 201 | 16576 | 97 | 122 | 114 |
| Columbia-Jefferson City | Missouri | Boone | 50 | 14253 | 93 | 86 | 93 |
| Joplin | Missouri | Jasper | 172 | 10702 | 71 | 71 | 59 |
| St. Louis-Farmington | Missouri | Franklin | 116 | 7267 | 66 | 66 | 60 |
| Springfield | Missouri | Christian | 55 | 6046 | 57 | 52 | 55 |
| Kansas City | Missouri | Cass | 58 | 6095 | 55 | 51 | 54 |
| Kansas City | Missouri | Clay | 113 | 6779 | 50 | 50 | 50 |
| St. Louis-Farmington | Missouri | St. Francois | 76 | 7000 | 47 | 48 | 48 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 103 | 6841 | 39 | 38 | 40 |
| Columbia-Jefferson City | Missouri | Cole | 93 | 8015 | 39 | 41 | 39 |
| Kansas City | Kansas | Leavenworth | 46 | 5395 | 39 | 40 | 34 |
| St. Louis-Farmington | Illinois | Clinton | 81 | 4790 | 34 | 32 | 31 |
| St. Louis-Farmington | Illinois | Macoupin | 91 | 3574 | 34 | 30 | 28 |
| St. Joseph | Missouri | Buchanan | 99 | 6370 | 33 | 32 | 33 |
| Missouri non-MSA | Missouri | Pettis | 67 | 4328 | 31 | 31 | 35 |
| Missouri non-MSA | Missouri | Taney | 57 | 4052 | 29 | 26 | 25 |
| Missouri non-MSA | Missouri | Pulaski | 29 | 2791 | 29 | 21 | 24 |
| Kansas City | Kansas | Miami | 15 | 2083 | 29 | 31 | 24 |
| St. Louis-Farmington | Illinois | Monroe | 62 | 3407 | 29 | 29 | 31 |
| Missouri non-MSA | Missouri | Camden | 65 | 3407 | 28 | 24 | 22 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3791 | 27 | 24 | 31 |
| Springfield | Missouri | Webster | 44 | 2669 | 26 | 23 | 21 |
| Columbia-Jefferson City | Missouri | Callaway | 25 | 4030 | 24 | 27 | 26 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3439 | 22 | 19 | 21 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17446 | 21 | 65 | 94 |
| Joplin | Missouri | Newton | 60 | 3684 | 21 | 22 | 18 |
| Missouri non-MSA | Missouri | Lawrence | 57 | 2515 | 21 | 18 | 14 |
| Kansas City | Missouri | Platte | 25 | 2646 | 21 | 25 | 23 |
| Missouri non-MSA | Missouri | Howell | 39 | 2529 | 19 | 20 | 27 |
| Cape Girardeau-Sikeston | Missouri | Scott | 66 | 3504 | 19 | 16 | 16 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2422 | 19 | 9 | 8 |
| Missouri non-MSA | Missouri | Adair | 5 | 1778 | 17 | 15 | 17 |
| Missouri non-MSA | Missouri | Butler | 16 | 2997 | 17 | 18 | 17 |
| Missouri non-MSA | Missouri | Laclede | 51 | 2660 | 16 | 15 | 18 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1793 | 15 | 14 | 14 |
| Missouri non-MSA | Missouri | Stone | 27 | 1758 | 14 | 13 | 13 |
| Missouri non-MSA | Missouri | Saline | 26 | 2166 | 14 | 14 | 14 |
| Missouri non-MSA | Missouri | Barry | 37 | 1927 | 14 | 11 | 11 |
| Missouri non-MSA | Missouri | Miller | 43 | 2167 | 14 | 13 | 15 |
| Missouri non-MSA | Missouri | Crawford | 20 | 1855 | 14 | 15 | 16 |
| Springfield | Missouri | Polk | 24 | 1954 | 13 | 13 | 12 |
| St. Louis-Farmington | Illinois | Bond | 20 | 1661 | 13 | 12 | 12 |
| Missouri non-MSA | Missouri | Washington | 41 | 1917 | 13 | 13 | 11 |
| Kansas City | Missouri | Lafayette | 43 | 2213 | 13 | 15 | 16 |
| Kansas City | Missouri | Ray | 10 | 1253 | 13 | 13 | 13 |
| Missouri non-MSA | Missouri | Phelps | 93 | 2666 | 12 | 18 | 20 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2202 | 12 | 11 | 12 |
| Missouri non-MSA | Missouri | Benton | 18 | 1304 | 12 | 10 | 10 |
| Missouri non-MSA | Missouri | Vernon | 24 | 1223 | 12 | 19 | 14 |
| Missouri non-MSA | Missouri | Livingston | 24 | 1136 | 11 | 10 | 9 |
| Missouri non-MSA | Missouri | Wright | 24 | 1196 | 11 | 13 | 11 |
| St. Louis-Farmington | Illinois | Jersey | 47 | 2100 | 11 | 13 | 16 |
| Kansas City | Missouri | Clinton | 59 | 1366 | 10 | 10 | 10 |
| Missouri non-MSA | Missouri | Marion | 30 | 2464 | 10 | 13 | 13 |
| Kansas City | Kansas | Linn | 3 | 607 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Macon | 10 | 1014 | 10 | 9 | 8 |
| Missouri non-MSA | Missouri | Audrain | 41 | 1901 | 9 | 22 | 20 |
| Missouri non-MSA | Missouri | Henry | 24 | 1529 | 9 | 9 | 9 |
| Missouri non-MSA | Missouri | Randolph | 19 | 1694 | 9 | 8 | 10 |
| Kansas City | Missouri | Bates | 13 | 929 | 8 | 10 | 9 |
| Missouri non-MSA | Missouri | Morgan | 30 | 1532 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2101 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Barton | 8 | 836 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | McDonald | 22 | 1753 | 8 | 9 | 8 |
| Missouri non-MSA | Missouri | Texas | 19 | 1433 | 7 | 9 | 11 |
| Missouri non-MSA | Missouri | Oregon | 3 | 608 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | New Madrid | 38 | 1685 | 7 | 8 | 7 |
| St. Joseph | Kansas | Doniphan | 7 | 792 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | Perry | 19 | 1928 | 7 | 7 | 8 |
| St. Joseph | Missouri | Andrew | 15 | 1178 | 7 | 8 | 8 |
| Columbia-Jefferson City | Missouri | Moniteau | 19 | 1579 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 30 | 747 | 7 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1264 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Pike | 17 | 1344 | 7 | 6 | 8 |
| Missouri non-MSA | Missouri | Grundy | 26 | 741 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 11 | 1496 | 6 | 8 | 9 |
| Missouri non-MSA | Missouri | Madison | 11 | 1276 | 6 | 9 | 9 |
| Missouri non-MSA | Missouri | Linn | 10 | 458 | 6 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 19 | 1549 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | Douglas | 20 | 679 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 22 | 1331 | 5 | 5 | 4 |
| St. Joseph | Missouri | DeKalb | 21 | 828 | 5 | 5 | 5 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 999 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Ozark | 5 | 427 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Wayne | 8 | 718 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Carroll | 18 | 709 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Daviess | 9 | 514 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 10 | 699 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Ripley | 9 | 718 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Gentry | 16 | 653 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Harrison | 10 | 680 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Cedar | 9 | 579 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Ralls | 7 | 708 | 4 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 657 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Iron | 1 | 437 | 3 | 3 | 5 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 416 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Lewis | 3 | 580 | 3 | 4 | 3 |
| Springfield | Missouri | Dallas | 19 | 732 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Atchison | 5 | 283 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 6 | 553 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 498 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 532 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 230 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 18 | 1166 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Shannon | 9 | 434 | 3 | 1 | 2 |
| Missouri non-MSA | Missouri | Dent | 9 | 737 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Chariton | 3 | 359 | 2 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 365 | 2 | 2 | 2 |
| Kansas City | Missouri | Caldwell | 7 | 581 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Shelby | 4 | 319 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 6 | 396 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Dade | 10 | 382 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Maries | 7 | 487 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 243 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 342 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 1 | 147 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 5 | 389 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 9 | 445 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 127 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 204 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 233 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 156 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
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
