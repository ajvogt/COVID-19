# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/28/2020  
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
| St. Louis-Farmington | 1889 | 82309 | 777 | 781 | 622 |
| Missouri non-MSA | 538 | 39184 | 527 | 580 | 470 |
| Kansas City | 841 | 57529 | 471 | 506 | 444 |
| Columbia-Jefferson City | 59 | 12127 | 170 | 183 | 137 |
| Springfield | 163 | 13765 | 141 | 159 | 150 |
| Joplin | 94 | 7266 | 74 | 78 | 65 |
| Cape Girardeau-Sikeston | 78 | 4727 | 58 | 62 | 54 |
| St. Joseph | 51 | 3931 | 42 | 57 | 47 |
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
| St. Louis-Farmington | Missouri | St. Louis | 885 | 30135 | 250 | 247 | 201 |
| St. Louis-Farmington | Missouri | St. Charles | 147 | 10827 | 134 | 153 | 104 |
| Kansas City | Kansas | Johnson | 196 | 14037 | 126 | 113 | 102 |
| Kansas City | Missouri | Jackson | 123 | 10033 | 103 | 122 | 84 |
| Kansas City | Missouri | Kansas City | 196 | 14435 | 91 | 97 | 109 |
| Springfield | Missouri | Greene | 126 | 9019 | 83 | 92 | 90 |
| St. Louis-Farmington | Illinois | Madison | 155 | 7264 | 61 | 59 | 52 |
| St. Louis-Farmington | Missouri | St. Louis City | 221 | 8428 | 60 | 55 | 45 |
| St. Louis-Farmington | Illinois | St. Clair | 221 | 8042 | 59 | 53 | 47 |
| Columbia-Jefferson City | Missouri | Cole | 22 | 2962 | 59 | 61 | 46 |
| Joplin | Missouri | Jasper | 73 | 5235 | 56 | 42 | 47 |
| St. Louis-Farmington | Missouri | Jefferson | 84 | 5597 | 53 | 53 | 45 |
| Columbia-Jefferson City | Missouri | Boone | 14 | 5978 | 47 | 52 | 43 |
| St. Louis-Farmington | Missouri | Franklin | 44 | 2694 | 45 | 44 | 31 |
| Kansas City | Kansas | Wyandotte | 164 | 8237 | 40 | 43 | 43 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 50 | 2690 | 31 | 32 | 30 |
| Kansas City | Missouri | Clay | 49 | 2536 | 30 | 39 | 24 |
| St. Louis-Farmington | Missouri | St. Francois | 27 | 2862 | 28 | 28 | 25 |
| Columbia-Jefferson City | Missouri | Callaway | 5 | 1216 | 27 | 25 | 18 |
| St. Joseph | Missouri | Buchanan | 40 | 2976 | 27 | 37 | 32 |
| Springfield | Missouri | Christian | 13 | 2299 | 27 | 32 | 28 |
| St. Louis-Farmington | Illinois | Clinton | 28 | 1811 | 25 | 26 | 21 |
| Missouri non-MSA | Missouri | Pettis | 17 | 1617 | 22 | 22 | 15 |
| Kansas City | Missouri | Cass | 30 | 2058 | 21 | 23 | 18 |
| Missouri non-MSA | Missouri | Butler | 8 | 1188 | 21 | 25 | 17 |
| Missouri non-MSA | Missouri | Taney | 33 | 1725 | 20 | 17 | 17 |
| Missouri non-MSA | Missouri | Howell | 10 | 1173 | 20 | 20 | 18 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1205 | 19 | 18 | 14 |
| Cape Girardeau-Sikeston | Missouri | Scott | 25 | 1429 | 19 | 22 | 18 |
| Joplin | Missouri | Newton | 21 | 2031 | 18 | 36 | 18 |
| Missouri non-MSA | Missouri | Camden | 34 | 1602 | 17 | 21 | 19 |
| Columbia-Jefferson City | Missouri | Moniteau | 10 | 623 | 17 | 16 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 12 | 1130 | 16 | 13 | 11 |
| Missouri non-MSA | Missouri | Lawrence | 21 | 1105 | 16 | 20 | 16 |
| Missouri non-MSA | Missouri | Laclede | 22 | 1197 | 15 | 19 | 18 |
| Missouri non-MSA | Missouri | Randolph | 3 | 616 | 15 | 14 | 11 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1128 | 14 | 15 | 12 |
| Missouri non-MSA | Missouri | Pulaski | 11 | 1003 | 14 | 13 | 11 |
| Kansas City | Missouri | Lafayette | 24 | 845 | 14 | 12 | 10 |
| Missouri non-MSA | Missouri | Miller | 9 | 878 | 13 | 17 | 12 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 876 | 13 | 15 | 12 |
| Springfield | Missouri | Webster | 13 | 1146 | 13 | 16 | 16 |
| Missouri non-MSA | Missouri | Marion | 14 | 929 | 13 | 11 | 8 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1494 | 13 | 15 | 12 |
| Missouri non-MSA | Missouri | Barry | 9 | 816 | 12 | 16 | 10 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 398 | 12 | 10 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 11 | 824 | 11 | 12 | 9 |
| Missouri non-MSA | Missouri | Crawford | 8 | 639 | 11 | 11 | 7 |
| Missouri non-MSA | Missouri | Morgan | 7 | 672 | 10 | 12 | 10 |
| St. Louis-Farmington | Illinois | Monroe | 30 | 935 | 10 | 9 | 8 |
| Kansas City | Missouri | Clinton | 17 | 502 | 10 | 12 | 8 |
| Springfield | Missouri | Dallas | 1 | 359 | 10 | 8 | 5 |
| Missouri non-MSA | Missouri | Phelps | 24 | 838 | 10 | 17 | 11 |
| Kansas City | Missouri | Platte | 13 | 991 | 10 | 13 | 9 |
| Kansas City | Kansas | Leavenworth | 18 | 2540 | 9 | 11 | 16 |
| Missouri non-MSA | Missouri | New Madrid | 22 | 774 | 9 | 8 | 8 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 488 | 9 | 17 | 11 |
| Missouri non-MSA | Missouri | Washington | 18 | 667 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Texas | 3 | 590 | 8 | 9 | 8 |
| Missouri non-MSA | Missouri | Stone | 9 | 696 | 8 | 9 | 7 |
| Missouri non-MSA | Missouri | Madison | 3 | 499 | 8 | 9 | 6 |
| Springfield | Missouri | Polk | 10 | 942 | 7 | 10 | 9 |
| Missouri non-MSA | Missouri | Adair | 0 | 519 | 7 | 8 | 5 |
| St. Louis-Farmington | Missouri | Warren | 1 | 629 | 7 | 7 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 12 | 730 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | Audrain | 11 | 586 | 7 | 7 | 5 |
| Missouri non-MSA | Missouri | Perry | 8 | 812 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 157 | 6 | 4 | 2 |
| St. Joseph | Missouri | DeKalb | 2 | 301 | 6 | 8 | 5 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 443 | 6 | 7 | 4 |
| Missouri non-MSA | Missouri | Saline | 10 | 952 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Pike | 8 | 351 | 6 | 5 | 3 |
| St. Louis-Farmington | Illinois | Bond | 9 | 513 | 6 | 8 | 6 |
| Missouri non-MSA | Missouri | Ripley | 4 | 271 | 6 | 7 | 3 |
| Missouri non-MSA | Missouri | Vernon | 3 | 336 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Maries | 0 | 187 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Shannon | 4 | 243 | 5 | 4 | 4 |
| St. Joseph | Missouri | Andrew | 8 | 443 | 5 | 7 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 2 | 476 | 5 | 6 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 3 | 613 | 5 | 7 | 6 |
| Missouri non-MSA | Missouri | Sullivan | 1 | 315 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 260 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Barton | 3 | 432 | 4 | 8 | 8 |
| Kansas City | Kansas | Miami | 2 | 509 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Henry | 7 | 378 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Ozark | 1 | 211 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Monroe | 2 | 165 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Lewis | 2 | 201 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1217 | 3 | 5 | 3 |
| Kansas City | Missouri | Bates | 5 | 252 | 3 | 4 | 4 |
| Kansas City | Missouri | Ray | 2 | 274 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Wright | 5 | 589 | 3 | 7 | 7 |
| Missouri non-MSA | Missouri | Dent | 3 | 256 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Carroll | 3 | 195 | 3 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 132 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Hickory | 3 | 203 | 3 | 3 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 477 | 3 | 3 | 2 |
| St. Joseph | Kansas | Doniphan | 1 | 211 | 3 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 247 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Carter | 3 | 176 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 4 | 232 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Benton | 5 | 482 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Reynolds | 1 | 80 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 232 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Daviess | 3 | 222 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Grundy | 11 | 259 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 12 | 288 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Macon | 1 | 212 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Wayne | 1 | 307 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 207 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Livingston | 8 | 558 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Dade | 0 | 140 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 121 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 189 | 1 | 3 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 103 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 107 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 10 | 183 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Scotland | 1 | 73 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Clark | 1 | 113 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 57 | 1 | 1 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 170 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 4 | 161 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 34 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 64 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 1 | 116 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 1 | 77 | 0 | 0 | 0 |
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
