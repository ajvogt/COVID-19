# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/09/2020  
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
| St. Louis-Farmington | 1985 | 99238 | 1668 | 1321 | 994 |
| Kansas City | 962 | 67731 | 944 | 797 | 624 |
| Missouri non-MSA | 639 | 48794 | 879 | 747 | 639 |
| Columbia-Jefferson City | 70 | 16172 | 371 | 301 | 237 |
| Springfield | 206 | 16279 | 202 | 196 | 175 |
| Joplin | 106 | 8512 | 108 | 96 | 84 |
| Cape Girardeau-Sikeston | 93 | 5856 | 103 | 90 | 74 |
| St. Joseph | 59 | 4557 | 65 | 48 | 51 |
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
| St. Louis-Farmington | Missouri | St. Louis | 897 | 35624 | 518 | 431 | 322 |
| Kansas City | Kansas | Johnson | 233 | 16947 | 271 | 228 | 162 |
| St. Louis-Farmington | Missouri | St. Charles | 157 | 13401 | 245 | 202 | 164 |
| Kansas City | Missouri | Kansas City | 227 | 16915 | 220 | 191 | 139 |
| St. Louis-Farmington | Illinois | Madison | 169 | 9154 | 200 | 143 | 97 |
| Kansas City | Missouri | Jackson | 145 | 11979 | 199 | 151 | 130 |
| Columbia-Jefferson City | Missouri | Boone | 15 | 7446 | 143 | 107 | 83 |
| St. Louis-Farmington | Missouri | Jefferson | 90 | 7007 | 140 | 109 | 76 |
| Springfield | Missouri | Greene | 153 | 10550 | 126 | 120 | 106 |
| St. Louis-Farmington | Missouri | St. Louis City | 225 | 9612 | 123 | 92 | 71 |
| St. Louis-Farmington | Illinois | St. Clair | 241 | 9258 | 121 | 95 | 70 |
| Columbia-Jefferson City | Missouri | Cole | 26 | 4175 | 106 | 91 | 72 |
| Joplin | Missouri | Jasper | 84 | 6159 | 83 | 71 | 55 |
| St. Louis-Farmington | Missouri | St. Francois | 30 | 3514 | 66 | 50 | 38 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 56 | 3322 | 64 | 50 | 40 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 1911 | 61 | 52 | 36 |
| St. Louis-Farmington | Missouri | Franklin | 50 | 3344 | 57 | 52 | 44 |
| Kansas City | Kansas | Wyandotte | 166 | 8948 | 54 | 57 | 48 |
| Missouri non-MSA | Missouri | Pettis | 24 | 2165 | 52 | 41 | 30 |
| Kansas City | Missouri | Clay | 51 | 3130 | 52 | 45 | 40 |
| Springfield | Missouri | Christian | 17 | 2772 | 44 | 38 | 32 |
| St. Joseph | Missouri | Buchanan | 45 | 3400 | 43 | 32 | 34 |
| Kansas City | Missouri | Cass | 33 | 2480 | 39 | 33 | 27 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1836 | 37 | 25 | 26 |
| St. Louis-Farmington | Illinois | Jersey | 22 | 747 | 36 | 19 | 10 |
| St. Louis-Farmington | Illinois | Clinton | 36 | 2164 | 35 | 29 | 26 |
| St. Louis-Farmington | Illinois | Macoupin | 12 | 1101 | 32 | 21 | 15 |
| Missouri non-MSA | Missouri | Butler | 8 | 1525 | 30 | 27 | 24 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1520 | 29 | 24 | 19 |
| Missouri non-MSA | Missouri | Taney | 36 | 2085 | 29 | 28 | 21 |
| Cape Girardeau-Sikeston | Missouri | Scott | 31 | 1755 | 29 | 26 | 24 |
| St. Louis-Farmington | Illinois | Monroe | 40 | 1265 | 28 | 24 | 16 |
| Missouri non-MSA | Missouri | Lawrence | 26 | 1381 | 26 | 20 | 19 |
| Missouri non-MSA | Missouri | Washington | 20 | 915 | 26 | 18 | 13 |
| Missouri non-MSA | Missouri | Marion | 14 | 1186 | 25 | 20 | 14 |
| Joplin | Missouri | Newton | 22 | 2353 | 24 | 24 | 28 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1450 | 24 | 23 | 19 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 646 | 23 | 19 | 13 |
| Missouri non-MSA | Missouri | Perry | 8 | 1036 | 22 | 17 | 11 |
| Kansas City | Missouri | Lafayette | 26 | 1072 | 22 | 18 | 14 |
| Columbia-Jefferson City | Missouri | Cooper | 4 | 833 | 22 | 16 | 11 |
| Missouri non-MSA | Missouri | Camden | 37 | 1836 | 21 | 19 | 20 |
| Kansas City | Kansas | Leavenworth | 21 | 2749 | 20 | 16 | 13 |
| Missouri non-MSA | Missouri | Henry | 8 | 589 | 20 | 15 | 10 |
| Missouri non-MSA | Missouri | Miller | 18 | 1119 | 20 | 18 | 17 |
| Missouri non-MSA | Missouri | Barry | 19 | 1050 | 19 | 17 | 16 |
| Missouri non-MSA | Missouri | Saline | 11 | 1148 | 19 | 14 | 10 |
| Missouri non-MSA | Missouri | Phelps | 31 | 1067 | 19 | 17 | 17 |
| Missouri non-MSA | Missouri | Laclede | 25 | 1397 | 18 | 15 | 17 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1328 | 18 | 15 | 13 |
| Missouri non-MSA | Missouri | Crawford | 9 | 824 | 18 | 14 | 12 |
| Springfield | Missouri | Webster | 23 | 1365 | 18 | 16 | 15 |
| Missouri non-MSA | Missouri | Randolph | 3 | 806 | 18 | 14 | 13 |
| Kansas City | Missouri | Platte | 13 | 1178 | 17 | 14 | 13 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 946 | 17 | 13 | 10 |
| Columbia-Jefferson City | Missouri | Moniteau | 13 | 821 | 16 | 14 | 14 |
| Missouri non-MSA | Missouri | Pike | 8 | 500 | 16 | 10 | 7 |
| St. Louis-Farmington | Illinois | Bond | 9 | 657 | 16 | 11 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 11 | 1182 | 15 | 15 | 13 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 666 | 15 | 13 | 14 |
| Missouri non-MSA | Missouri | Texas | 5 | 739 | 15 | 11 | 10 |
| Missouri non-MSA | Missouri | Stone | 13 | 857 | 14 | 12 | 9 |
| Missouri non-MSA | Missouri | Adair | 0 | 681 | 14 | 12 | 9 |
| Kansas City | Missouri | Ray | 2 | 416 | 14 | 10 | 7 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 1044 | 13 | 12 | 13 |
| St. Joseph | Missouri | DeKalb | 5 | 404 | 12 | 7 | 7 |
| Missouri non-MSA | Missouri | Macon | 1 | 336 | 12 | 9 | 5 |
| Missouri non-MSA | Missouri | Morgan | 8 | 828 | 11 | 11 | 11 |
| Missouri non-MSA | Missouri | Vernon | 3 | 454 | 11 | 9 | 7 |
| Missouri non-MSA | Missouri | Audrain | 10 | 734 | 11 | 11 | 8 |
| Missouri non-MSA | Missouri | Howell | 16 | 1351 | 11 | 16 | 17 |
| St. Louis-Farmington | Missouri | Warren | 2 | 749 | 11 | 9 | 8 |
| Missouri non-MSA | Missouri | Pemiscot | 14 | 833 | 10 | 8 | 7 |
| Missouri non-MSA | Missouri | Benton | 7 | 575 | 10 | 7 | 5 |
| Kansas City | Missouri | Clinton | 33 | 628 | 10 | 10 | 10 |
| Missouri non-MSA | Missouri | Lewis | 2 | 290 | 9 | 6 | 4 |
| Springfield | Missouri | Polk | 11 | 1145 | 8 | 15 | 12 |
| Missouri non-MSA | Missouri | Ripley | 5 | 344 | 7 | 5 | 6 |
| St. Joseph | Missouri | Andrew | 8 | 526 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Carroll | 4 | 266 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 3 | 430 | 7 | 9 | 6 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 513 | 7 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 320 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Gentry | 10 | 247 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Madison | 3 | 590 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Chariton | 0 | 119 | 6 | 4 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 4 | 597 | 6 | 9 | 7 |
| Missouri non-MSA | Missouri | Grundy | 11 | 326 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Monroe | 2 | 234 | 6 | 5 | 4 |
| Kansas City | Kansas | Miami | 2 | 605 | 6 | 6 | 5 |
| Springfield | Missouri | Dallas | 2 | 447 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 329 | 5 | 5 | 5 |
| Kansas City | Missouri | Caldwell | 1 | 233 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Ralls | 0 | 260 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 2 | 230 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Oregon | 0 | 285 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Barton | 4 | 491 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Clark | 2 | 168 | 5 | 4 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 121 | 5 | 3 | 1 |
| Missouri non-MSA | Missouri | Linn | 7 | 210 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Dent | 4 | 312 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Holt | 1 | 163 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 83 | 5 | 3 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 165 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Dade | 3 | 187 | 5 | 3 | 3 |
| Kansas City | Missouri | Bates | 8 | 306 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Harrison | 1 | 232 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Cedar | 4 | 288 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Wayne | 3 | 364 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Hickory | 4 | 288 | 4 | 6 | 4 |
| Missouri non-MSA | Missouri | Maries | 1 | 253 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Livingston | 9 | 615 | 4 | 4 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 182 | 4 | 4 | 2 |
| Kansas City | Kansas | Linn | 1 | 145 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Wright | 9 | 646 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Douglas | 13 | 331 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | McDonald | 14 | 1284 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Shannon | 6 | 295 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Iron | 0 | 138 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 4 | 254 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Atchison | 1 | 106 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Ozark | 1 | 241 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Carter | 3 | 206 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Scotland | 1 | 96 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 82 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 1 | 108 | 1 | 2 | 2 |
| St. Joseph | Kansas | Doniphan | 1 | 227 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 124 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 0 | 47 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 67 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 38 | 0 | 0 | 0 |
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
