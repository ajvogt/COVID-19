# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/11/2020  
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
| St. Louis-Farmington | 1742 | 70337 | 554 | 514 | 548 |
| Missouri non-MSA | 402 | 31046 | 548 | 456 | 441 |
| Kansas City | 707 | 50008 | 466 | 435 | 408 |
| Springfield | 118 | 11530 | 202 | 185 | 183 |
| Columbia-Jefferson City | 47 | 9561 | 171 | 118 | 118 |
| Joplin | 73 | 6167 | 78 | 64 | 69 |
| Cape Girardeau-Sikeston | 47 | 3847 | 76 | 58 | 58 |
| St. Joseph | 37 | 3130 | 53 | 47 | 44 |
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
| St. Louis-Farmington | Missouri | St. Louis | 839 | 26134 | 162 | 158 | 164 |
| Springfield | Missouri | Greene | 96 | 7728 | 130 | 115 | 114 |
| Kansas City | Missouri | Kansas City | 168 | 13077 | 117 | 142 | 104 |
| Kansas City | Missouri | Jackson | 116 | 8319 | 102 | 60 | 69 |
| St. Louis-Farmington | Missouri | St. Charles | 127 | 8676 | 98 | 76 | 76 |
| Kansas City | Kansas | Johnson | 163 | 12186 | 91 | 93 | 102 |
| Columbia-Jefferson City | Missouri | Boone | 14 | 5244 | 71 | 42 | 51 |
| Joplin | Missouri | Jasper | 59 | 4646 | 64 | 60 | 57 |
| Columbia-Jefferson City | Missouri | Cole | 16 | 2095 | 53 | 40 | 33 |
| St. Louis-Farmington | Missouri | Jefferson | 69 | 4846 | 50 | 46 | 54 |
| Kansas City | Kansas | Wyandotte | 134 | 7520 | 48 | 45 | 38 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 27 | 2241 | 46 | 36 | 36 |
| St. Louis-Farmington | Illinois | Madison | 148 | 6281 | 44 | 43 | 52 |
| St. Louis-Farmington | Illinois | St. Clair | 202 | 7168 | 41 | 42 | 43 |
| St. Louis-Farmington | Missouri | St. Louis City | 217 | 7528 | 39 | 35 | 34 |
| St. Joseph | Missouri | Buchanan | 32 | 2458 | 38 | 34 | 33 |
| St. Louis-Farmington | Missouri | St. Francois | 18 | 2467 | 37 | 28 | 36 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1272 | 37 | 12 | 16 |
| Springfield | Missouri | Christian | 8 | 1848 | 32 | 30 | 31 |
| Missouri non-MSA | Missouri | Camden | 21 | 1302 | 29 | 22 | 21 |
| St. Louis-Farmington | Missouri | Franklin | 33 | 2073 | 24 | 25 | 28 |
| Springfield | Missouri | Webster | 6 | 920 | 23 | 20 | 19 |
| Kansas City | Missouri | Cass | 29 | 1733 | 23 | 16 | 17 |
| Missouri non-MSA | Missouri | Laclede | 12 | 920 | 22 | 21 | 18 |
| Cape Girardeau-Sikeston | Missouri | Scott | 17 | 1114 | 22 | 17 | 13 |
| Kansas City | Missouri | Clay | 44 | 1985 | 21 | 12 | 14 |
| Columbia-Jefferson City | Missouri | Callaway | 4 | 858 | 20 | 14 | 13 |
| Missouri non-MSA | Missouri | Howell | 4 | 881 | 18 | 19 | 17 |
| St. Louis-Farmington | Illinois | Clinton | 23 | 1400 | 17 | 17 | 16 |
| Missouri non-MSA | Missouri | Randolph | 2 | 414 | 16 | 11 | 8 |
| Missouri non-MSA | Missouri | Butler | 8 | 834 | 16 | 13 | 13 |
| Missouri non-MSA | Missouri | Lawrence | 13 | 823 | 15 | 14 | 13 |
| Missouri non-MSA | Missouri | Taney | 38 | 1480 | 14 | 20 | 15 |
| Joplin | Missouri | Newton | 14 | 1521 | 14 | 3 | 11 |
| Missouri non-MSA | Missouri | Pettis | 13 | 1301 | 14 | 12 | 14 |
| Missouri non-MSA | Missouri | Pulaski | 8 | 819 | 14 | 11 | 12 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 665 | 14 | 12 | 11 |
| Kansas City | Kansas | Leavenworth | 15 | 2334 | 14 | 21 | 19 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 948 | 12 | 13 | 10 |
| Missouri non-MSA | Missouri | Livingston | 5 | 518 | 12 | 8 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 895 | 12 | 10 | 8 |
| Missouri non-MSA | Missouri | Morgan | 5 | 497 | 12 | 10 | 10 |
| Missouri non-MSA | Missouri | Phelps | 15 | 589 | 11 | 8 | 9 |
| Missouri non-MSA | Missouri | Texas | 2 | 458 | 11 | 9 | 9 |
| Missouri non-MSA | Missouri | Barton | 2 | 318 | 11 | 9 | 6 |
| Missouri non-MSA | Missouri | Dunklin | 11 | 948 | 11 | 11 | 11 |
| Kansas City | Missouri | Lafayette | 19 | 673 | 11 | 11 | 12 |
| Missouri non-MSA | Missouri | Miller | 3 | 633 | 11 | 9 | 10 |
| Springfield | Missouri | Polk | 7 | 792 | 10 | 15 | 14 |
| Missouri non-MSA | Missouri | Washington | 12 | 544 | 10 | 9 | 8 |
| Kansas City | Missouri | Platte | 12 | 802 | 10 | 7 | 8 |
| Kansas City | Missouri | Clinton | 0 | 333 | 10 | 6 | 5 |
| Missouri non-MSA | Missouri | Wright | 0 | 486 | 9 | 10 | 12 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 250 | 9 | 6 | 5 |
| Missouri non-MSA | Missouri | Saline | 9 | 852 | 9 | 9 | 8 |
| Missouri non-MSA | Missouri | New Madrid | 17 | 653 | 9 | 8 | 6 |
| Missouri non-MSA | Missouri | Madison | 1 | 367 | 8 | 4 | 4 |
| Missouri non-MSA | Missouri | Stone | 6 | 570 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Crawford | 7 | 481 | 8 | 6 | 8 |
| Missouri non-MSA | Missouri | Marion | 14 | 765 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Barry | 8 | 584 | 8 | 7 | 6 |
| Columbia-Jefferson City | Missouri | Moniteau | 5 | 399 | 8 | 6 | 6 |
| St. Joseph | Missouri | Andrew | 3 | 342 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Dent | 2 | 197 | 7 | 3 | 4 |
| St. Louis-Farmington | Illinois | Monroe | 26 | 786 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Perry | 8 | 707 | 7 | 6 | 8 |
| Missouri non-MSA | Missouri | Pemiscot | 11 | 616 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Henry | 5 | 289 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Benton | 5 | 421 | 6 | 7 | 8 |
| Columbia-Jefferson City | Missouri | Cooper | 3 | 515 | 6 | 6 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 8 | 636 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Shannon | 2 | 174 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Cedar | 2 | 180 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Vernon | 2 | 255 | 5 | 5 | 4 |
| Springfield | Missouri | Dallas | 1 | 242 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 406 | 4 | 4 | 4 |
| Kansas City | Missouri | Bates | 3 | 186 | 4 | 5 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 2 | 392 | 4 | 3 | 7 |
| St. Louis-Farmington | Missouri | Warren | 1 | 524 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Hickory | 3 | 150 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 249 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Oregon | 0 | 173 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Audrain | 5 | 483 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Lewis | 2 | 150 | 4 | 4 | 2 |
| St. Joseph | Missouri | DeKalb | 2 | 189 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Carter | 3 | 137 | 4 | 2 | 3 |
| Missouri non-MSA | Missouri | McDonald | 12 | 1138 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Wayne | 1 | 260 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Daviess | 1 | 172 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Dade | 0 | 107 | 3 | 3 | 2 |
| Kansas City | Kansas | Miami | 1 | 433 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 247 | 3 | 3 | 2 |
| Kansas City | Missouri | Ray | 2 | 208 | 3 | 3 | 2 |
| St. Louis-Farmington | Illinois | Bond | 8 | 382 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Pike | 4 | 275 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Grundy | 7 | 230 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Mississippi | 4 | 344 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Linn | 1 | 144 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Ripley | 1 | 161 | 3 | 0 | 1 |
| Missouri non-MSA | Missouri | Ozark | 1 | 158 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 186 | 3 | 1 | 2 |
| Missouri non-MSA | Missouri | Carroll | 2 | 155 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 109 | 2 | 1 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 20 | 422 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 3 | 248 | 2 | 3 | 4 |
| Kansas City | Missouri | Caldwell | 1 | 130 | 2 | 2 | 2 |
| St. Joseph | Kansas | Doniphan | 0 | 141 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 91 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Macon | 0 | 182 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Gentry | 10 | 148 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 145 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 200 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 86 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 168 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 73 | 2 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 100 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 85 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 1 | 95 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 41 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 1 | 100 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 68 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 45 | 1 | 1 | 0 |
| Kansas City | Kansas | Linn | 0 | 89 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 90 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 1 | 54 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 55 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 66 | 0 | 0 | 1 |
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
