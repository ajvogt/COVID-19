# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/07/2020  
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
| Kansas City | 645 | 48166 | 475 | 443 | 383 |
| St. Louis-Farmington | 1694 | 67666 | 451 | 499 | 518 |
| Missouri non-MSA | 339 | 28265 | 407 | 400 | 380 |
| Springfield | 86 | 10500 | 157 | 169 | 167 |
| Columbia-Jefferson City | 38 | 8635 | 79 | 87 | 100 |
| Joplin | 68 | 5754 | 59 | 56 | 64 |
| St. Joseph | 35 | 2867 | 48 | 43 | 38 |
| Cape Girardeau-Sikeston | 37 | 3443 | 43 | 48 | 49 |
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
| Kansas City | Missouri | Kansas City | 146 | 12488 | 173 | 127 | 92 |
| St. Louis-Farmington | Missouri | St. Louis | 825 | 25416 | 141 | 162 | 161 |
| Kansas City | Kansas | Johnson | 158 | 12071 | 135 | 125 | 107 |
| Springfield | Missouri | Greene | 69 | 7040 | 91 | 103 | 104 |
| Joplin | Missouri | Jasper | 55 | 4305 | 67 | 51 | 54 |
| St. Louis-Farmington | Missouri | St. Charles | 115 | 8213 | 66 | 63 | 69 |
| Kansas City | Kansas | Wyandotte | 134 | 7353 | 51 | 44 | 36 |
| St. Louis-Farmington | Missouri | Jefferson | 66 | 4587 | 43 | 45 | 50 |
| Kansas City | Missouri | Jackson | 104 | 7850 | 37 | 56 | 61 |
| Columbia-Jefferson City | Missouri | Cole | 14 | 1844 | 37 | 31 | 27 |
| St. Joseph | Missouri | Buchanan | 30 | 2277 | 35 | 33 | 28 |
| St. Louis-Farmington | Illinois | St. Clair | 197 | 6962 | 33 | 44 | 42 |
| St. Louis-Farmington | Illinois | Madison | 147 | 6032 | 32 | 44 | 51 |
| St. Louis-Farmington | Missouri | St. Louis City | 213 | 7355 | 32 | 33 | 31 |
| Springfield | Missouri | Christian | 6 | 1688 | 30 | 29 | 29 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 18 | 2007 | 28 | 32 | 31 |
| St. Louis-Farmington | Missouri | Franklin | 32 | 1954 | 28 | 27 | 26 |
| Missouri non-MSA | Missouri | Taney | 36 | 1414 | 27 | 19 | 15 |
| Missouri non-MSA | Missouri | Howell | 3 | 795 | 23 | 18 | 15 |
| Missouri non-MSA | Missouri | Laclede | 9 | 816 | 21 | 17 | 16 |
| Kansas City | Kansas | Leavenworth | 14 | 2324 | 20 | 28 | 20 |
| Springfield | Missouri | Webster | 5 | 808 | 20 | 16 | 17 |
| Missouri non-MSA | Missouri | Camden | 16 | 1160 | 19 | 21 | 18 |
| St. Louis-Farmington | Missouri | St. Francois | 14 | 2259 | 18 | 22 | 32 |
| St. Louis-Farmington | Illinois | Clinton | 22 | 1319 | 16 | 16 | 15 |
| Missouri non-MSA | Missouri | Randolph | 2 | 379 | 16 | 11 | 7 |
| Missouri non-MSA | Missouri | Lawrence | 4 | 747 | 16 | 13 | 11 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 893 | 15 | 12 | 9 |
| Missouri non-MSA | Missouri | Butler | 7 | 752 | 13 | 12 | 11 |
| Missouri non-MSA | Missouri | Dunklin | 8 | 892 | 13 | 10 | 10 |
| Cape Girardeau-Sikeston | Missouri | Scott | 17 | 977 | 12 | 10 | 9 |
| Missouri non-MSA | Missouri | Saline | 9 | 809 | 11 | 9 | 7 |
| Missouri non-MSA | Missouri | Wright | 0 | 440 | 11 | 12 | 11 |
| Columbia-Jefferson City | Missouri | Callaway | 3 | 751 | 11 | 11 | 10 |
| Kansas City | Missouri | Cass | 26 | 1605 | 11 | 13 | 15 |
| Missouri non-MSA | Missouri | Stoddard | 14 | 597 | 11 | 9 | 9 |
| Missouri non-MSA | Missouri | Miller | 2 | 584 | 10 | 9 | 9 |
| Missouri non-MSA | Missouri | Morgan | 2 | 447 | 10 | 10 | 9 |
| Columbia-Jefferson City | Missouri | Boone | 11 | 4801 | 10 | 23 | 44 |
| Springfield | Missouri | Polk | 5 | 739 | 10 | 17 | 13 |
| Missouri non-MSA | Missouri | Barton | 1 | 265 | 10 | 6 | 5 |
| Kansas City | Missouri | Lafayette | 6 | 606 | 10 | 9 | 11 |
| Missouri non-MSA | Missouri | Washington | 11 | 501 | 10 | 11 | 7 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 845 | 9 | 8 | 6 |
| Missouri non-MSA | Missouri | Texas | 2 | 392 | 9 | 8 | 7 |
| Missouri non-MSA | Missouri | Pettis | 12 | 1221 | 8 | 12 | 12 |
| Missouri non-MSA | Missouri | Benton | 5 | 395 | 8 | 10 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 16 | 596 | 8 | 6 | 5 |
| Kansas City | Kansas | Miami | 1 | 428 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Pulaski | 7 | 732 | 8 | 10 | 10 |
| Missouri non-MSA | Missouri | Stone | 6 | 525 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Marion | 14 | 723 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Livingston | 3 | 459 | 7 | 5 | 4 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 210 | 7 | 5 | 3 |
| St. Louis-Farmington | Illinois | Monroe | 24 | 736 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Henry | 5 | 252 | 6 | 6 | 4 |
| St. Louis-Farmington | Illinois | Macoupin | 8 | 603 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Barry | 6 | 540 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Vernon | 1 | 233 | 6 | 5 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 480 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 10 | 579 | 6 | 6 | 6 |
| St. Joseph | Missouri | Andrew | 3 | 301 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Lewis | 2 | 132 | 5 | 3 | 2 |
| Kansas City | Missouri | Platte | 10 | 750 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Linn | 1 | 123 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Shannon | 1 | 147 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Perry | 7 | 671 | 5 | 4 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 5 | 361 | 5 | 5 | 5 |
| Kansas City | Missouri | Clay | 42 | 1863 | 5 | 8 | 12 |
| Kansas City | Missouri | Bates | 3 | 160 | 4 | 4 | 2 |
| St. Joseph | Missouri | DeKalb | 2 | 169 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Cedar | 0 | 154 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Daviess | 1 | 154 | 4 | 4 | 3 |
| St. Louis-Farmington | Illinois | Bond | 8 | 365 | 4 | 5 | 5 |
| Springfield | Missouri | Dallas | 1 | 225 | 4 | 3 | 3 |
| Kansas City | Missouri | Clinton | 0 | 274 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 379 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 327 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 152 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Crawford | 5 | 432 | 3 | 5 | 7 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 228 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Douglas | 3 | 232 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Hickory | 3 | 132 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Phelps | 12 | 513 | 3 | 6 | 8 |
| Missouri non-MSA | Missouri | Harrison | 1 | 135 | 2 | 2 | 1 |
| Kansas City | Missouri | Ray | 0 | 187 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Grundy | 4 | 215 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Audrain | 5 | 466 | 2 | 3 | 5 |
| Kansas City | Missouri | Caldwell | 1 | 119 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 228 | 2 | 3 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 168 | 2 | 1 | 2 |
| St. Louis-Farmington | Missouri | Warren | 1 | 498 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Pike | 4 | 255 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Gentry | 9 | 139 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 83 | 1 | 2 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 19 | 408 | 1 | 1 | 2 |
| Kansas City | Kansas | Linn | 0 | 88 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 188 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 1 | 139 | 1 | 1 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 365 | 1 | 3 | 6 |
| Missouri non-MSA | Missouri | Scotland | 1 | 41 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 236 | 1 | 3 | 4 |
| St. Joseph | Kansas | Doniphan | 0 | 120 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 94 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 94 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 74 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 2 | 139 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 63 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 1 | 86 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 61 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 157 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 74 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 53 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 3 | 112 | 0 | 2 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 66 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 55 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 1 | 317 | 0 | 2 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 80 | 0 | 2 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 89 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 1 | 92 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 2 | 151 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 23 | 166 | 0 | 0 | 2 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 39 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1117 | 0 | 4 | 3 |
| Missouri non-MSA | Missouri | Ripley | 1 | 145 | -3 | 0 | 1 |
| Joplin | Missouri | Newton | 13 | 1449 | -8 | 5 | 10 |
| Missouri non-MSA | Missouri | Johnson | 5 | 1018 | -13 | 0 | 10 |
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
