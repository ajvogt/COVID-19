# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/11/2020  
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
| St. Louis-Farmington | 2022 | 103335 | 1918 | 1501 | 1087 |
| Kansas City | 984 | 71793 | 1011 | 897 | 689 |
| Missouri non-MSA | 696 | 50644 | 954 | 818 | 652 |
| Columbia-Jefferson City | 80 | 16698 | 392 | 326 | 237 |
| Springfield | 212 | 16739 | 224 | 212 | 173 |
| Joplin | 115 | 8645 | 118 | 98 | 82 |
| Cape Girardeau-Sikeston | 98 | 6061 | 114 | 95 | 73 |
| St. Joseph | 64 | 4747 | 72 | 58 | 53 |
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
| St. Louis-Farmington | Missouri | St. Louis | 900 | 37016 | 602 | 491 | 355 |
| St. Louis-Farmington | Missouri | St. Charles | 163 | 13873 | 267 | 217 | 173 |
| Kansas City | Missouri | Kansas City | 236 | 17564 | 260 | 223 | 149 |
| Kansas City | Kansas | Johnson | 236 | 18783 | 249 | 247 | 195 |
| St. Louis-Farmington | Illinois | Madison | 170 | 9601 | 231 | 166 | 108 |
| Kansas City | Missouri | Jackson | 150 | 12493 | 228 | 175 | 139 |
| Columbia-Jefferson City | Missouri | Boone | 15 | 7629 | 159 | 117 | 79 |
| St. Louis-Farmington | Missouri | Jefferson | 94 | 7349 | 158 | 125 | 83 |
| St. Louis-Farmington | Illinois | St. Clair | 242 | 9596 | 149 | 111 | 79 |
| Springfield | Missouri | Greene | 155 | 10839 | 140 | 130 | 103 |
| St. Louis-Farmington | Missouri | St. Louis City | 230 | 9917 | 134 | 106 | 78 |
| Columbia-Jefferson City | Missouri | Cole | 34 | 4333 | 106 | 97 | 74 |
| Joplin | Missouri | Jasper | 89 | 6267 | 91 | 73 | 54 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 58 | 3457 | 74 | 54 | 40 |
| St. Louis-Farmington | Missouri | St. Francois | 36 | 3664 | 69 | 57 | 39 |
| St. Louis-Farmington | Missouri | Franklin | 57 | 3481 | 65 | 56 | 46 |
| Kansas City | Missouri | Clay | 52 | 3297 | 65 | 54 | 43 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 1978 | 59 | 54 | 37 |
| Missouri non-MSA | Missouri | Pettis | 28 | 2256 | 57 | 45 | 31 |
| St. Joseph | Missouri | Buchanan | 46 | 3513 | 50 | 38 | 35 |
| Kansas City | Kansas | Wyandotte | 167 | 9282 | 48 | 56 | 52 |
| Springfield | Missouri | Christian | 20 | 2868 | 47 | 40 | 34 |
| St. Louis-Farmington | Illinois | Clinton | 37 | 2294 | 46 | 34 | 29 |
| Kansas City | Missouri | Cass | 35 | 2609 | 46 | 39 | 29 |
| St. Louis-Farmington | Illinois | Macoupin | 13 | 1205 | 44 | 27 | 18 |
| St. Louis-Farmington | Illinois | Jersey | 22 | 787 | 38 | 22 | 12 |
| Missouri non-MSA | Missouri | Johnson | 11 | 1877 | 35 | 27 | 20 |
| St. Louis-Farmington | Missouri | Lincoln | 7 | 1593 | 34 | 27 | 21 |
| St. Louis-Farmington | Illinois | Monroe | 40 | 1335 | 34 | 28 | 18 |
| Missouri non-MSA | Missouri | Taney | 36 | 2149 | 31 | 30 | 22 |
| Missouri non-MSA | Missouri | Washington | 20 | 969 | 30 | 21 | 14 |
| Cape Girardeau-Sikeston | Missouri | Scott | 33 | 1805 | 29 | 26 | 23 |
| Missouri non-MSA | Missouri | Lawrence | 32 | 1440 | 28 | 23 | 20 |
| Missouri non-MSA | Missouri | Perry | 8 | 1095 | 27 | 20 | 12 |
| Missouri non-MSA | Missouri | Camden | 40 | 1903 | 26 | 21 | 20 |
| Joplin | Missouri | Newton | 26 | 2378 | 26 | 24 | 28 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1488 | 26 | 25 | 19 |
| Missouri non-MSA | Missouri | Marion | 15 | 1243 | 25 | 22 | 15 |
| Missouri non-MSA | Missouri | Henry | 8 | 635 | 23 | 18 | 11 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 683 | 23 | 20 | 14 |
| Columbia-Jefferson City | Missouri | Moniteau | 13 | 889 | 23 | 19 | 16 |
| Kansas City | Missouri | Lafayette | 27 | 1113 | 22 | 19 | 14 |
| Columbia-Jefferson City | Missouri | Cooper | 6 | 856 | 22 | 17 | 11 |
| Missouri non-MSA | Missouri | Butler | 8 | 1578 | 22 | 27 | 24 |
| Missouri non-MSA | Missouri | Phelps | 33 | 1105 | 21 | 19 | 17 |
| St. Louis-Farmington | Illinois | Bond | 9 | 718 | 21 | 14 | 11 |
| Missouri non-MSA | Missouri | Laclede | 28 | 1432 | 21 | 16 | 17 |
| Missouri non-MSA | Missouri | Miller | 20 | 1146 | 20 | 19 | 17 |
| Missouri non-MSA | Missouri | Adair | 0 | 731 | 19 | 15 | 10 |
| Springfield | Missouri | Webster | 23 | 1405 | 19 | 18 | 16 |
| Missouri non-MSA | Missouri | Saline | 11 | 1189 | 19 | 16 | 11 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1359 | 19 | 16 | 13 |
| Kansas City | Kansas | Leavenworth | 21 | 2913 | 19 | 18 | 16 |
| Kansas City | Missouri | Platte | 13 | 1216 | 19 | 16 | 13 |
| Missouri non-MSA | Missouri | Barry | 19 | 1088 | 18 | 19 | 16 |
| Missouri non-MSA | Missouri | Pike | 8 | 536 | 18 | 13 | 8 |
| Missouri non-MSA | Missouri | Crawford | 10 | 846 | 17 | 14 | 12 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 973 | 17 | 14 | 10 |
| Missouri non-MSA | Missouri | Stoddard | 17 | 1094 | 17 | 15 | 14 |
| Missouri non-MSA | Missouri | Randolph | 4 | 818 | 17 | 14 | 13 |
| Kansas City | Missouri | Ray | 2 | 453 | 16 | 12 | 8 |
| Missouri non-MSA | Missouri | Pulaski | 13 | 1207 | 16 | 14 | 12 |
| Missouri non-MSA | Missouri | Texas | 6 | 765 | 15 | 12 | 10 |
| Missouri non-MSA | Missouri | Vernon | 3 | 491 | 15 | 11 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 685 | 14 | 14 | 14 |
| Missouri non-MSA | Missouri | Stone | 13 | 878 | 14 | 13 | 10 |
| Missouri non-MSA | Missouri | Macon | 1 | 349 | 13 | 9 | 5 |
| St. Louis-Farmington | Missouri | Warren | 2 | 779 | 12 | 10 | 8 |
| Missouri non-MSA | Missouri | Pemiscot | 15 | 866 | 12 | 9 | 8 |
| Missouri non-MSA | Missouri | Audrain | 11 | 763 | 11 | 12 | 9 |
| Missouri non-MSA | Missouri | Benton | 7 | 595 | 11 | 8 | 5 |
| Missouri non-MSA | Missouri | Morgan | 8 | 850 | 11 | 12 | 11 |
| Kansas City | Missouri | Clinton | 33 | 653 | 11 | 10 | 10 |
| Missouri non-MSA | Missouri | Howell | 19 | 1379 | 11 | 14 | 16 |
| Missouri non-MSA | Missouri | Madison | 7 | 628 | 10 | 9 | 8 |
| Missouri non-MSA | Missouri | Lewis | 2 | 312 | 9 | 7 | 5 |
| Springfield | Missouri | Polk | 11 | 1163 | 9 | 15 | 12 |
| St. Joseph | Missouri | Andrew | 8 | 552 | 9 | 7 | 7 |
| Missouri non-MSA | Missouri | Ripley | 5 | 361 | 8 | 6 | 6 |
| Missouri non-MSA | Missouri | Chariton | 0 | 137 | 8 | 5 | 2 |
| Kansas City | Kansas | Miami | 2 | 680 | 8 | 8 | 7 |
| St. Joseph | Missouri | DeKalb | 8 | 412 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Gentry | 11 | 271 | 8 | 6 | 4 |
| Missouri non-MSA | Missouri | Carroll | 4 | 282 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Monroe | 3 | 252 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Sullivan | 4 | 446 | 7 | 9 | 6 |
| Missouri non-MSA | Missouri | Ralls | 0 | 274 | 7 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 328 | 7 | 5 | 4 |
| Kansas City | Missouri | Bates | 8 | 327 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Cedar | 4 | 313 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Grundy | 12 | 338 | 7 | 5 | 3 |
| Springfield | Missouri | Dallas | 3 | 464 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Dade | 5 | 204 | 7 | 4 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 5 | 614 | 6 | 9 | 7 |
| Kansas City | Missouri | Caldwell | 1 | 244 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Barton | 4 | 502 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 180 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Clark | 2 | 183 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Dent | 4 | 325 | 5 | 4 | 4 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 127 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Linn | 10 | 219 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Holt | 2 | 171 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 294 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 527 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Harrison | 1 | 241 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 341 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Wayne | 3 | 381 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 88 | 5 | 3 | 1 |
| Missouri non-MSA | Missouri | Hickory | 4 | 297 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Montgomery | 5 | 237 | 5 | 5 | 4 |
| St. Joseph | Kansas | Doniphan | 2 | 270 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Wright | 11 | 661 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Livingston | 9 | 624 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Maries | 1 | 262 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Daviess | 5 | 267 | 4 | 3 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 185 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 151 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Douglas | 14 | 339 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | McDonald | 15 | 1291 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Scotland | 1 | 108 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Atchison | 1 | 114 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Shannon | 6 | 300 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Reynolds | 1 | 116 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 128 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 4 | 211 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Knox | 1 | 85 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 1 | 245 | 2 | 2 | 2 |
| Kansas City | Kansas | Linn | 1 | 166 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Mercer | 0 | 50 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 74 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 38 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
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
