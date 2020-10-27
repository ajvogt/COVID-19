# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/27/2020  
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
| St. Louis-Farmington | 1870 | 81648 | 772 | 756 | 617 |
| Missouri non-MSA | 530 | 38771 | 520 | 550 | 470 |
| Kansas City | 835 | 56979 | 447 | 477 | 435 |
| Columbia-Jefferson City | 58 | 12056 | 169 | 178 | 138 |
| Springfield | 159 | 13635 | 140 | 150 | 156 |
| Joplin | 92 | 7189 | 69 | 73 | 64 |
| Cape Girardeau-Sikeston | 72 | 4647 | 55 | 57 | 54 |
| St. Joseph | 49 | 3917 | 50 | 56 | 48 |
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
| St. Louis-Farmington | Missouri | St. Louis | 870 | 29962 | 246 | 246 | 201 |
| St. Louis-Farmington | Missouri | St. Charles | 147 | 10684 | 135 | 143 | 102 |
| Kansas City | Missouri | Jackson | 123 | 9944 | 106 | 116 | 82 |
| Kansas City | Kansas | Johnson | 192 | 13813 | 106 | 106 | 98 |
| Springfield | Missouri | Greene | 122 | 8944 | 84 | 86 | 94 |
| Kansas City | Missouri | Kansas City | 195 | 14313 | 82 | 88 | 107 |
| St. Louis-Farmington | Illinois | St. Clair | 220 | 7993 | 62 | 52 | 47 |
| St. Louis-Farmington | Illinois | Madison | 154 | 7221 | 60 | 59 | 51 |
| Columbia-Jefferson City | Missouri | Cole | 22 | 2935 | 59 | 60 | 46 |
| St. Louis-Farmington | Missouri | St. Louis City | 221 | 8368 | 58 | 54 | 44 |
| Joplin | Missouri | Jasper | 71 | 5170 | 51 | 37 | 45 |
| St. Louis-Farmington | Missouri | Jefferson | 84 | 5531 | 51 | 48 | 44 |
| Columbia-Jefferson City | Missouri | Boone | 14 | 5961 | 48 | 51 | 43 |
| Kansas City | Kansas | Wyandotte | 164 | 8229 | 44 | 43 | 44 |
| St. Louis-Farmington | Missouri | Franklin | 44 | 2659 | 44 | 41 | 31 |
| St. Joseph | Missouri | Buchanan | 39 | 2965 | 30 | 36 | 33 |
| Kansas City | Missouri | Clay | 49 | 2504 | 29 | 37 | 22 |
| St. Louis-Farmington | Missouri | St. Francois | 27 | 2839 | 29 | 26 | 25 |
| St. Louis-Farmington | Illinois | Clinton | 26 | 1789 | 28 | 25 | 21 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 49 | 2645 | 28 | 28 | 30 |
| Columbia-Jefferson City | Missouri | Callaway | 5 | 1204 | 26 | 24 | 18 |
| Missouri non-MSA | Missouri | Pettis | 17 | 1607 | 25 | 21 | 16 |
| Springfield | Missouri | Christian | 13 | 2263 | 24 | 29 | 28 |
| Missouri non-MSA | Missouri | Taney | 33 | 1714 | 21 | 16 | 17 |
| Cape Girardeau-Sikeston | Missouri | Scott | 20 | 1407 | 20 | 20 | 17 |
| Missouri non-MSA | Missouri | Butler | 8 | 1177 | 20 | 24 | 17 |
| Kansas City | Missouri | Cass | 30 | 2020 | 19 | 20 | 17 |
| Missouri non-MSA | Missouri | Camden | 33 | 1584 | 19 | 20 | 19 |
| Joplin | Missouri | Newton | 21 | 2019 | 18 | 35 | 18 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1191 | 18 | 17 | 14 |
| Columbia-Jefferson City | Missouri | Moniteau | 9 | 618 | 18 | 15 | 10 |
| Missouri non-MSA | Missouri | Howell | 10 | 1140 | 17 | 18 | 17 |
| Missouri non-MSA | Missouri | Lawrence | 20 | 1096 | 17 | 19 | 15 |
| Missouri non-MSA | Missouri | Dunklin | 12 | 1118 | 17 | 12 | 11 |
| Missouri non-MSA | Missouri | Laclede | 22 | 1188 | 15 | 19 | 18 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1128 | 15 | 15 | 12 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 870 | 15 | 14 | 12 |
| Missouri non-MSA | Missouri | Randolph | 3 | 606 | 14 | 13 | 11 |
| Springfield | Missouri | Webster | 13 | 1142 | 13 | 15 | 16 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 396 | 13 | 10 | 6 |
| Kansas City | Missouri | Lafayette | 24 | 831 | 13 | 11 | 10 |
| Missouri non-MSA | Missouri | Miller | 9 | 865 | 12 | 16 | 12 |
| St. Louis-Farmington | Illinois | Macoupin | 11 | 816 | 12 | 12 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 9 | 979 | 12 | 11 | 10 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1487 | 12 | 15 | 12 |
| Missouri non-MSA | Missouri | Barry | 9 | 808 | 12 | 16 | 11 |
| Missouri non-MSA | Missouri | Marion | 14 | 906 | 12 | 10 | 8 |
| Missouri non-MSA | Missouri | Morgan | 7 | 665 | 11 | 12 | 10 |
| St. Louis-Farmington | Illinois | Monroe | 30 | 925 | 10 | 9 | 8 |
| Missouri non-MSA | Missouri | Crawford | 8 | 629 | 10 | 10 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 484 | 10 | 16 | 11 |
| Kansas City | Kansas | Leavenworth | 18 | 2540 | 9 | 11 | 16 |
| Kansas City | Missouri | Platte | 12 | 977 | 9 | 12 | 9 |
| Kansas City | Missouri | Clinton | 17 | 495 | 9 | 11 | 8 |
| Missouri non-MSA | Missouri | New Madrid | 22 | 770 | 9 | 8 | 8 |
| Springfield | Missouri | Dallas | 1 | 349 | 9 | 7 | 5 |
| Missouri non-MSA | Missouri | Phelps | 22 | 830 | 9 | 17 | 11 |
| Springfield | Missouri | Polk | 10 | 937 | 8 | 10 | 12 |
| Missouri non-MSA | Missouri | Washington | 18 | 662 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Madison | 3 | 494 | 8 | 9 | 6 |
| Missouri non-MSA | Missouri | Texas | 3 | 587 | 8 | 9 | 8 |
| Missouri non-MSA | Missouri | Saline | 10 | 951 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Perry | 8 | 809 | 7 | 7 | 6 |
| St. Joseph | Kansas | Doniphan | 0 | 211 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Stone | 9 | 689 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 439 | 7 | 6 | 4 |
| St. Joseph | Missouri | DeKalb | 2 | 300 | 6 | 7 | 5 |
| St. Louis-Farmington | Missouri | Warren | 1 | 622 | 6 | 7 | 4 |
| Missouri non-MSA | Missouri | Adair | 0 | 510 | 6 | 7 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 12 | 720 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Pike | 8 | 351 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Maries | 0 | 185 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Audrain | 11 | 577 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Ripley | 4 | 266 | 6 | 7 | 3 |
| St. Joseph | Missouri | Andrew | 8 | 441 | 6 | 7 | 6 |
| St. Louis-Farmington | Illinois | Bond | 9 | 507 | 5 | 8 | 6 |
| Missouri non-MSA | Missouri | Vernon | 3 | 331 | 5 | 5 | 5 |
| Kansas City | Missouri | Ray | 2 | 273 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 257 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Shannon | 4 | 236 | 5 | 4 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 3 | 609 | 5 | 6 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 2 | 471 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Ozark | 1 | 209 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 144 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Henry | 7 | 377 | 4 | 6 | 6 |
| Kansas City | Kansas | Miami | 2 | 509 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Barton | 3 | 426 | 4 | 7 | 8 |
| Missouri non-MSA | Missouri | Monroe | 2 | 161 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 1 | 305 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Benton | 5 | 481 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Lewis | 2 | 198 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Wright | 5 | 586 | 3 | 7 | 8 |
| Kansas City | Missouri | Bates | 5 | 250 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1215 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | Dent | 3 | 251 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 4 | 223 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Carter | 3 | 174 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 3 | 198 | 2 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 245 | 2 | 3 | 2 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 475 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Carroll | 3 | 190 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Cedar | 4 | 228 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Grundy | 10 | 259 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 228 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Wayne | 1 | 307 | 2 | 3 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 124 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Livingston | 7 | 557 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Harrison | 1 | 189 | 2 | 3 | 2 |
| Kansas City | Missouri | Caldwell | 1 | 171 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Dade | 0 | 140 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 120 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Douglas | 11 | 285 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Ralls | 0 | 202 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Gentry | 10 | 183 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 108 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 1 | 71 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 1 | 207 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 72 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 1 | 113 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 34 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 4 | 160 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 99 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 56 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Atchison | 1 | 77 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 64 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 1 | 115 | 0 | 1 | 1 |
| Kansas City | Kansas | Linn | 1 | 110 | 0 | 1 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 31 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 66 | 0 | 0 | 0 |
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
