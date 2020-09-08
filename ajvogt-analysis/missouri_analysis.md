# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/08/2020  
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
| St. Louis-Farmington | 1459 | 52582 | 610 | 593 | 608 |
| Kansas City | 494 | 36979 | 350 | 372 | 398 |
| Missouri non-MSA | 179 | 16998 | 325 | 301 | 263 |
| Columbia-Jefferson City | 24 | 5700 | 183 | 160 | 116 |
| Springfield | 23 | 5585 | 162 | 148 | 113 |
| Joplin | 50 | 3817 | 54 | 48 | 40 |
| Cape Girardeau-Sikeston | 24 | 1982 | 30 | 31 | 28 |
| St. Joseph | 14 | 1728 | 24 | 22 | 16 |
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
| St. Louis-Farmington | Missouri | St. Louis | 760 | 20735 | 186 | 197 | 202 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 3524 | 129 | 112 | 73 |
| Springfield | Missouri | Greene | 19 | 3999 | 120 | 111 | 85 |
| Kansas City | Kansas | Johnson | 121 | 8924 | 101 | 109 | 109 |
| Kansas City | Missouri | Jackson | 83 | 6038 | 73 | 69 | 70 |
| Kansas City | Missouri | Kansas City | 94 | 9808 | 73 | 92 | 111 |
| St. Louis-Farmington | Missouri | St. Charles | 105 | 6229 | 71 | 67 | 75 |
| St. Louis-Farmington | Illinois | Madison | 108 | 4536 | 70 | 66 | 66 |
| St. Louis-Farmington | Illinois | St. Clair | 175 | 5710 | 63 | 53 | 58 |
| St. Louis-Farmington | Missouri | Jefferson | 46 | 3109 | 57 | 56 | 52 |
| Joplin | Missouri | Jasper | 37 | 2685 | 47 | 40 | 31 |
| St. Louis-Farmington | Missouri | St. Louis City | 189 | 6439 | 37 | 34 | 43 |
| Missouri non-MSA | Missouri | Livingston | 1 | 338 | 37 | 19 | 9 |
| Kansas City | Kansas | Wyandotte | 118 | 6271 | 34 | 39 | 46 |
| St. Louis-Farmington | Missouri | St. Francois | 5 | 1322 | 33 | 35 | 32 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1016 | 24 | 21 | 21 |
| Springfield | Missouri | Christian | 2 | 829 | 22 | 20 | 16 |
| St. Louis-Farmington | Missouri | Franklin | 22 | 1170 | 20 | 20 | 19 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 857 | 20 | 17 | 15 |
| Missouri non-MSA | Missouri | Nodaway | 7 | 639 | 18 | 24 | 15 |
| Kansas City | Missouri | Clay | 39 | 1506 | 17 | 16 | 16 |
| Missouri non-MSA | Missouri | Johnson | 4 | 717 | 17 | 11 | 7 |
| St. Joseph | Missouri | Buchanan | 12 | 1421 | 17 | 16 | 11 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 8 | 1080 | 16 | 15 | 14 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 432 | 14 | 12 | 9 |
| Missouri non-MSA | Missouri | Marion | 7 | 558 | 12 | 14 | 12 |
| Missouri non-MSA | Missouri | Camden | 9 | 606 | 11 | 10 | 8 |
| Kansas City | Missouri | Cass | 16 | 1151 | 10 | 12 | 14 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 529 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 566 | 10 | 8 | 8 |
| Springfield | Missouri | Webster | 1 | 291 | 10 | 7 | 5 |
| Missouri non-MSA | Missouri | Howell | 3 | 333 | 9 | 9 | 6 |
| St. Louis-Farmington | Illinois | Bond | 4 | 209 | 9 | 7 | 4 |
| Cape Girardeau-Sikeston | Missouri | Scott | 14 | 690 | 9 | 10 | 10 |
| Kansas City | Kansas | Miami | 0 | 264 | 9 | 6 | 4 |
| Kansas City | Kansas | Leavenworth | 9 | 1731 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Madison | 0 | 204 | 8 | 9 | 6 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 625 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Pettis | 8 | 858 | 8 | 8 | 12 |
| Missouri non-MSA | Missouri | Phelps | 1 | 270 | 8 | 8 | 6 |
| Missouri non-MSA | Missouri | Texas | 1 | 157 | 8 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 289 | 8 | 7 | 5 |
| Kansas City | Missouri | Platte | 10 | 533 | 8 | 6 | 6 |
| Springfield | Missouri | Polk | 0 | 343 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Perry | 4 | 446 | 7 | 10 | 7 |
| Missouri non-MSA | Missouri | Taney | 22 | 964 | 7 | 7 | 13 |
| Missouri non-MSA | Missouri | Butler | 4 | 425 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Audrain | 2 | 316 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 381 | 6 | 5 | 4 |
| St. Louis-Farmington | Illinois | Macoupin | 6 | 396 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Miller | 1 | 298 | 6 | 6 | 6 |
| Joplin | Missouri | Newton | 13 | 1132 | 6 | 8 | 8 |
| St. Louis-Farmington | Illinois | Jersey | 6 | 321 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Saline | 9 | 589 | 6 | 4 | 5 |
| Missouri non-MSA | Missouri | Grundy | 1 | 91 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 270 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 9 | 450 | 5 | 7 | 7 |
| St. Louis-Farmington | Missouri | Warren | 0 | 362 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Ozark | 0 | 65 | 5 | 3 | 1 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 393 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Laclede | 1 | 329 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Morgan | 1 | 156 | 5 | 3 | 2 |
| Kansas City | Missouri | Lafayette | 2 | 274 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Stone | 2 | 314 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Crawford | 2 | 220 | 4 | 5 | 4 |
| Kansas City | Missouri | Clinton | 0 | 161 | 4 | 3 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 162 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Washington | 1 | 267 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 137 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 322 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Vernon | 0 | 109 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ripley | 0 | 112 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Barry | 5 | 379 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Pulaski | 2 | 415 | 3 | 6 | 7 |
| St. Joseph | Missouri | Andrew | 1 | 149 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Randolph | 1 | 149 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 139 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 0 | 47 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 106 | 3 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 207 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Wright | 0 | 108 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Dent | 0 | 55 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 4 | 130 | 2 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 80 | 2 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 123 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 64 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 116 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 86 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 93 | 1 | 1 | 1 |
| Kansas City | Missouri | Ray | 0 | 135 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 245 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Cedar | 0 | 62 | 1 | 1 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 78 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 122 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | McDonald | 10 | 998 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 2 | 155 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Atchison | 0 | 37 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 102 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 36 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 70 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 181 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 1 | 60 | 1 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 49 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 50 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 3 | 119 | 1 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 33 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 76 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carroll | 1 | 118 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Benton | 1 | 162 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Dade | 0 | 36 | 0 | 1 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 50 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 85 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 43 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 51 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 65 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 42 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 50 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 1 | 66 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 4 | 97 | 0 | 3 | 2 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 58 | 0 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 78 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 48 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 56 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 42 | -1 | 0 | 0 |
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
