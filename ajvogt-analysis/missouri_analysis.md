# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/24/2020  
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
| St. Louis-Farmington | 1846 | 78865 | 680 | 675 | 587 |
| Missouri non-MSA | 484 | 36977 | 495 | 527 | 459 |
| Kansas City | 807 | 55647 | 428 | 475 | 443 |
| Columbia-Jefferson City | 53 | 11543 | 166 | 177 | 133 |
| Springfield | 149 | 13185 | 132 | 154 | 163 |
| Joplin | 85 | 7007 | 72 | 73 | 65 |
| Cape Girardeau-Sikeston | 68 | 4492 | 53 | 63 | 55 |
| St. Joseph | 44 | 3750 | 51 | 52 | 48 |
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
| St. Louis-Farmington | Missouri | St. Louis | 867 | 29143 | 238 | 229 | 194 |
| St. Louis-Farmington | Missouri | St. Charles | 144 | 10150 | 113 | 120 | 91 |
| Kansas City | Missouri | Kansas City | 184 | 13989 | 103 | 89 | 105 |
| Kansas City | Kansas | Johnson | 190 | 13494 | 96 | 102 | 102 |
| Kansas City | Missouri | Jackson | 118 | 9662 | 85 | 113 | 86 |
| Springfield | Missouri | Greene | 118 | 8667 | 76 | 94 | 98 |
| Columbia-Jefferson City | Missouri | Cole | 18 | 2756 | 61 | 54 | 44 |
| St. Louis-Farmington | Illinois | St. Clair | 217 | 7814 | 54 | 48 | 47 |
| St. Louis-Farmington | Illinois | Madison | 154 | 7021 | 53 | 55 | 51 |
| Joplin | Missouri | Jasper | 68 | 5028 | 52 | 38 | 46 |
| St. Louis-Farmington | Missouri | St. Louis City | 218 | 8157 | 50 | 49 | 40 |
| Columbia-Jefferson City | Missouri | Boone | 14 | 5819 | 44 | 62 | 43 |
| Kansas City | Kansas | Wyandotte | 162 | 8088 | 39 | 42 | 44 |
| St. Louis-Farmington | Missouri | Jefferson | 79 | 5305 | 39 | 42 | 42 |
| St. Louis-Farmington | Missouri | Franklin | 43 | 2464 | 32 | 31 | 28 |
| St. Joseph | Missouri | Buchanan | 38 | 2858 | 31 | 34 | 34 |
| St. Louis-Farmington | Illinois | Clinton | 26 | 1709 | 27 | 23 | 20 |
| Kansas City | Missouri | Clay | 46 | 2449 | 27 | 38 | 22 |
| Missouri non-MSA | Missouri | Pettis | 15 | 1524 | 24 | 18 | 15 |
| Cape Girardeau-Sikeston | Missouri | Scott | 19 | 1356 | 24 | 23 | 17 |
| St. Louis-Farmington | Missouri | St. Francois | 24 | 2720 | 24 | 26 | 25 |
| Springfield | Missouri | Christian | 11 | 2183 | 23 | 28 | 28 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 46 | 2564 | 23 | 33 | 32 |
| Missouri non-MSA | Missouri | Butler | 8 | 1106 | 22 | 22 | 16 |
| Joplin | Missouri | Newton | 17 | 1979 | 19 | 35 | 19 |
| Kansas City | Missouri | Cass | 28 | 1967 | 19 | 22 | 17 |
| Columbia-Jefferson City | Missouri | Callaway | 5 | 1105 | 18 | 20 | 16 |
| Columbia-Jefferson City | Missouri | Moniteau | 9 | 583 | 17 | 15 | 9 |
| Missouri non-MSA | Missouri | Taney | 33 | 1641 | 17 | 13 | 16 |
| Missouri non-MSA | Missouri | Dunklin | 12 | 1071 | 17 | 10 | 10 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 841 | 16 | 14 | 12 |
| Missouri non-MSA | Missouri | Camden | 28 | 1519 | 16 | 20 | 21 |
| Missouri non-MSA | Missouri | Barry | 8 | 764 | 16 | 14 | 10 |
| Missouri non-MSA | Missouri | Randolph | 3 | 575 | 16 | 13 | 11 |
| Missouri non-MSA | Missouri | Howell | 7 | 1083 | 15 | 17 | 17 |
| Missouri non-MSA | Missouri | Lawrence | 14 | 1034 | 15 | 17 | 15 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 1079 | 14 | 14 | 11 |
| Springfield | Missouri | Webster | 11 | 1091 | 14 | 14 | 16 |
| Missouri non-MSA | Missouri | Laclede | 21 | 1126 | 14 | 17 | 18 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 449 | 14 | 15 | 10 |
| Kansas City | Kansas | Leavenworth | 18 | 2520 | 13 | 13 | 18 |
| Missouri non-MSA | Missouri | Miller | 7 | 812 | 12 | 14 | 11 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1102 | 12 | 11 | 12 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1428 | 12 | 26 | 12 |
| Kansas City | Missouri | Platte | 12 | 956 | 11 | 12 | 10 |
| Missouri non-MSA | Missouri | Morgan | 6 | 629 | 11 | 11 | 10 |
| Missouri non-MSA | Missouri | Crawford | 7 | 593 | 10 | 10 | 7 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 341 | 10 | 7 | 5 |
| St. Louis-Farmington | Illinois | Monroe | 28 | 901 | 10 | 8 | 8 |
| Missouri non-MSA | Missouri | Marion | 14 | 871 | 10 | 9 | 7 |
| St. Louis-Farmington | Illinois | Macoupin | 10 | 771 | 9 | 10 | 8 |
| Missouri non-MSA | Missouri | Phelps | 21 | 794 | 9 | 17 | 11 |
| Springfield | Missouri | Polk | 8 | 913 | 9 | 10 | 13 |
| Kansas City | Missouri | Lafayette | 24 | 782 | 9 | 10 | 9 |
| Missouri non-MSA | Missouri | New Madrid | 20 | 736 | 9 | 8 | 7 |
| Springfield | Missouri | Dallas | 1 | 331 | 8 | 6 | 4 |
| Missouri non-MSA | Missouri | Pulaski | 9 | 927 | 8 | 11 | 10 |
| Kansas City | Missouri | Clinton | 14 | 463 | 8 | 11 | 8 |
| Missouri non-MSA | Missouri | Saline | 10 | 926 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 12 | 703 | 7 | 7 | 6 |
| St. Louis-Farmington | Illinois | Bond | 9 | 484 | 7 | 8 | 6 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 592 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Washington | 17 | 623 | 7 | 7 | 8 |
| St. Joseph | Missouri | DeKalb | 2 | 271 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Madison | 3 | 465 | 7 | 9 | 6 |
| Missouri non-MSA | Missouri | Adair | 0 | 493 | 7 | 7 | 5 |
| St. Joseph | Missouri | Andrew | 4 | 420 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Ripley | 4 | 247 | 6 | 6 | 3 |
| Missouri non-MSA | Missouri | Perry | 8 | 779 | 6 | 6 | 5 |
| St. Joseph | Kansas | Doniphan | 0 | 201 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 5 | 417 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Texas | 3 | 553 | 6 | 9 | 8 |
| Missouri non-MSA | Missouri | Stone | 9 | 657 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Benton | 5 | 473 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Audrain | 7 | 560 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Barton | 3 | 413 | 5 | 8 | 7 |
| Missouri non-MSA | Missouri | Pike | 8 | 328 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Henry | 6 | 363 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Maries | 0 | 161 | 5 | 3 | 2 |
| Kansas City | Kansas | Miami | 2 | 509 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Shannon | 3 | 217 | 4 | 4 | 4 |
| Kansas City | Missouri | Ray | 2 | 260 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Vernon | 3 | 312 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Wright | 3 | 574 | 4 | 7 | 9 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 2 | 455 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Monroe | 1 | 144 | 4 | 3 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 237 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1196 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 126 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Ozark | 1 | 195 | 3 | 3 | 2 |
| St. Louis-Farmington | Missouri | Warren | 1 | 590 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | Lewis | 2 | 186 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Grundy | 9 | 255 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Livingston | 6 | 553 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Carter | 3 | 166 | 3 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 239 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Harrison | 1 | 182 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 223 | 3 | 4 | 4 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 467 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 198 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 1 | 285 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Douglas | 9 | 277 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dent | 3 | 239 | 2 | 5 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 117 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 3 | 188 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 4 | 211 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Holt | 1 | 113 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Carroll | 3 | 177 | 2 | 2 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 164 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Scotland | 1 | 68 | 2 | 1 | 1 |
| Kansas City | Missouri | Bates | 5 | 234 | 1 | 4 | 4 |
| Missouri non-MSA | Missouri | Cedar | 2 | 217 | 1 | 3 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 117 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 1 | 200 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 1 | 297 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Reynolds | 1 | 65 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Gentry | 10 | 177 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 99 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 104 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 96 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 2 | 156 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Atchison | 1 | 75 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 52 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 131 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Chariton | 0 | 57 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 29 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 61 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 1 | 110 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 0 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 36 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 67 | 0 | 0 | 0 |
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
