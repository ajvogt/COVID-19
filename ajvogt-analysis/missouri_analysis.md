# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/20/2020  
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
| St. Louis-Farmington | 3028 | 185254 | 1866 | 1864 | 2023 |
| Kansas City | 1412 | 123138 | 1173 | 1251 | 1276 |
| Missouri non-MSA | 1183 | 85363 | 676 | 780 | 827 |
| Springfield | 338 | 26766 | 256 | 268 | 254 |
| Columbia-Jefferson City | 171 | 27556 | 198 | 202 | 238 |
| Cape Girardeau-Sikeston | 159 | 10445 | 69 | 75 | 96 |
| Joplin | 184 | 12648 | 65 | 68 | 82 |
| St. Joseph | 121 | 8072 | 53 | 68 | 84 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1260 | 63872 | 628 | 613 | 655 |
| Kansas City | Kansas | Johnson | 385 | 35086 | 417 | 415 | 408 |
| St. Louis-Farmington | Missouri | St. Charles | 259 | 25096 | 250 | 244 | 271 |
| St. Louis-Farmington | Illinois | Madison | 354 | 19129 | 235 | 230 | 236 |
| Kansas City | Missouri | Kansas City | 327 | 27850 | 197 | 220 | 250 |
| St. Louis-Farmington | Illinois | St. Clair | 323 | 17387 | 177 | 193 | 206 |
| Kansas City | Missouri | Jackson | 206 | 21404 | 159 | 196 | 215 |
| Springfield | Missouri | Greene | 238 | 17209 | 158 | 169 | 161 |
| St. Louis-Farmington | Missouri | St. Louis City | 282 | 15783 | 140 | 140 | 154 |
| Kansas City | Kansas | Wyandotte | 190 | 14105 | 135 | 143 | 129 |
| St. Louis-Farmington | Missouri | Jefferson | 121 | 13871 | 132 | 133 | 157 |
| Columbia-Jefferson City | Missouri | Boone | 36 | 12402 | 102 | 104 | 106 |
| Springfield | Missouri | Christian | 35 | 4968 | 60 | 61 | 54 |
| Kansas City | Missouri | Cass | 46 | 5008 | 58 | 61 | 59 |
| St. Louis-Farmington | Missouri | Franklin | 106 | 5970 | 55 | 57 | 60 |
| St. Louis-Farmington | Missouri | St. Francois | 58 | 6048 | 53 | 49 | 54 |
| Joplin | Missouri | Jasper | 144 | 9393 | 50 | 54 | 65 |
| Kansas City | Kansas | Leavenworth | 36 | 4698 | 50 | 49 | 46 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 91 | 6040 | 46 | 46 | 57 |
| Kansas City | Missouri | Clay | 87 | 5719 | 45 | 53 | 56 |
| Missouri non-MSA | Missouri | Pettis | 50 | 3790 | 39 | 59 | 42 |
| St. Louis-Farmington | Missouri | Lincoln | 17 | 3225 | 37 | 37 | 40 |
| Columbia-Jefferson City | Missouri | Cole | 77 | 7174 | 37 | 40 | 61 |
| St. Louis-Farmington | Illinois | Clinton | 77 | 4133 | 36 | 39 | 44 |
| St. Joseph | Missouri | Buchanan | 86 | 5718 | 34 | 47 | 56 |
| St. Louis-Farmington | Illinois | Macoupin | 57 | 2984 | 32 | 34 | 40 |
| St. Louis-Farmington | Illinois | Monroe | 56 | 2758 | 30 | 32 | 35 |
| Columbia-Jefferson City | Missouri | Callaway | 17 | 3473 | 27 | 28 | 33 |
| Kansas City | Kansas | Miami | 7 | 1514 | 25 | 26 | 23 |
| Missouri non-MSA | Missouri | Johnson | 25 | 3021 | 23 | 24 | 26 |
| Missouri non-MSA | Missouri | Taney | 47 | 3538 | 22 | 30 | 35 |
| Kansas City | Missouri | Platte | 19 | 2128 | 22 | 21 | 23 |
| Springfield | Missouri | Webster | 35 | 2216 | 20 | 20 | 20 |
| Missouri non-MSA | Missouri | Miller | 42 | 1892 | 20 | 18 | 17 |
| St. Louis-Farmington | Illinois | Jersey | 34 | 1753 | 20 | 23 | 24 |
| Missouri non-MSA | Missouri | Adair | 4 | 1419 | 19 | 18 | 15 |
| Missouri non-MSA | Missouri | Audrain | 23 | 1474 | 19 | 19 | 19 |
| Missouri non-MSA | Missouri | Camden | 58 | 2898 | 19 | 20 | 22 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1975 | 19 | 15 | 14 |
| Missouri non-MSA | Missouri | Phelps | 76 | 2232 | 18 | 20 | 28 |
| Missouri non-MSA | Missouri | Laclede | 38 | 2318 | 17 | 23 | 23 |
| St. Louis-Farmington | Illinois | Bond | 15 | 1410 | 16 | 16 | 17 |
| Missouri non-MSA | Missouri | Texas | 13 | 1245 | 16 | 15 | 12 |
| Kansas City | Missouri | Lafayette | 36 | 1866 | 16 | 16 | 18 |
| Cape Girardeau-Sikeston | Missouri | Scott | 52 | 3157 | 16 | 20 | 29 |
| Kansas City | Missouri | Ray | 7 | 970 | 15 | 13 | 12 |
| Missouri non-MSA | Missouri | Stone | 23 | 1492 | 15 | 14 | 15 |
| St. Louis-Farmington | Missouri | Warren | 8 | 1484 | 15 | 12 | 15 |
| Missouri non-MSA | Missouri | Butler | 12 | 2636 | 15 | 22 | 26 |
| Joplin | Missouri | Newton | 40 | 3255 | 14 | 13 | 17 |
| Missouri non-MSA | Missouri | Marion | 23 | 2185 | 13 | 18 | 21 |
| Missouri non-MSA | Missouri | Saline | 16 | 1855 | 13 | 14 | 14 |
| Missouri non-MSA | Missouri | Benton | 15 | 1132 | 13 | 17 | 14 |
| Missouri non-MSA | Missouri | Pulaski | 26 | 2231 | 13 | 24 | 28 |
| Springfield | Missouri | Polk | 16 | 1704 | 13 | 14 | 14 |
| Missouri non-MSA | Missouri | Crawford | 15 | 1478 | 13 | 14 | 14 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2183 | 12 | 12 | 15 |
| Missouri non-MSA | Missouri | Perry | 15 | 1768 | 12 | 10 | 13 |
| Columbia-Jefferson City | Missouri | Cooper | 17 | 1399 | 12 | 11 | 11 |
| Missouri non-MSA | Missouri | Henry | 18 | 1347 | 12 | 11 | 13 |
| Missouri non-MSA | Missouri | Morgan | 16 | 1364 | 12 | 14 | 13 |
| Missouri non-MSA | Missouri | Howell | 35 | 2124 | 11 | 33 | 21 |
| Missouri non-MSA | Missouri | Stoddard | 31 | 1945 | 11 | 13 | 18 |
| Missouri non-MSA | Missouri | Barry | 35 | 1687 | 11 | 11 | 13 |
| Missouri non-MSA | Missouri | Vernon | 13 | 876 | 11 | 9 | 9 |
| Missouri non-MSA | Missouri | Macon | 5 | 844 | 11 | 8 | 11 |
| Kansas City | Missouri | Clinton | 50 | 1145 | 10 | 12 | 11 |
| Missouri non-MSA | Missouri | Randolph | 15 | 1498 | 10 | 13 | 14 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1303 | 10 | 10 | 13 |
| Missouri non-MSA | Missouri | Livingston | 19 | 942 | 10 | 9 | 8 |
| Missouri non-MSA | Missouri | Madison | 10 | 1090 | 9 | 9 | 12 |
| Missouri non-MSA | Missouri | Pike | 11 | 1171 | 9 | 10 | 14 |
| Missouri non-MSA | Missouri | Wright | 19 | 950 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2224 | 8 | 9 | 14 |
| Missouri non-MSA | Missouri | Mississippi | 10 | 1086 | 8 | 9 | 13 |
| Kansas City | Missouri | Bates | 10 | 716 | 8 | 8 | 9 |
| St. Joseph | Missouri | Andrew | 13 | 1004 | 7 | 8 | 11 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1101 | 7 | 6 | 9 |
| Columbia-Jefferson City | Missouri | Moniteau | 16 | 1417 | 7 | 7 | 10 |
| Missouri non-MSA | Missouri | Washington | 34 | 1661 | 7 | 9 | 14 |
| Missouri non-MSA | Missouri | New Madrid | 26 | 1521 | 7 | 8 | 11 |
| Missouri non-MSA | Missouri | Carroll | 9 | 592 | 7 | 8 | 8 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1553 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Harrison | 7 | 570 | 7 | 9 | 7 |
| Missouri non-MSA | Missouri | Douglas | 19 | 555 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Gentry | 15 | 559 | 6 | 6 | 7 |
| Kansas City | Kansas | Linn | 3 | 438 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 29 | 611 | 6 | 6 | 7 |
| St. Joseph | Kansas | Doniphan | 5 | 632 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 443 | 6 | 5 | 5 |
| St. Joseph | Missouri | DeKalb | 17 | 718 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Dent | 6 | 644 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Iron | 1 | 325 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Grundy | 19 | 624 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Wayne | 4 | 611 | 5 | 6 | 6 |
| Kansas City | Missouri | Caldwell | 3 | 491 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Barton | 7 | 723 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Ripley | 8 | 627 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 20 | 1224 | 4 | 5 | 7 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 590 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Ralls | 4 | 590 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Monroe | 5 | 470 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | St. Clair | 4 | 418 | 3 | 3 | 4 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 11 | 925 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 618 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Oregon | 3 | 493 | 3 | 6 | 5 |
| Springfield | Missouri | Dallas | 14 | 669 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 176 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 9 | 425 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Lewis | 2 | 501 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Maries | 6 | 432 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Linn | 11 | 392 | 2 | 3 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 5 | 323 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Dade | 8 | 338 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 8 | 483 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Chariton | 2 | 294 | 2 | 2 | 3 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 351 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Shelby | 1 | 275 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Shannon | 9 | 392 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 116 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 4 | 348 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 214 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Putnam | 1 | 187 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Scotland | 3 | 217 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 6 | 410 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Holt | 7 | 316 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Carter | 6 | 353 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Clark | 4 | 344 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Atchison | 4 | 255 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Knox | 1 | 144 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 106 | 0 | 1 | 1 |
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
