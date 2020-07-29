# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 07/29/2020  
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
| St. Louis-Farmington | 1200 | 26756 | 767 | 616 | 429 |
| Kansas City | 333 | 20223 | 553 | 473 | 365 |
| Missouri non-MSA | 79 | 6943 | 210 | 177 | 132 |
| Springfield | 13 | 1497 | 68 | 59 | 37 |
| Columbia-Jefferson City | 8 | 1604 | 63 | 48 | 36 |
| Joplin | 27 | 2343 | 53 | 50 | 51 |
| Cape Girardeau-Sikeston | 16 | 959 | 22 | 23 | 20 |
| St. Joseph | 12 | 1178 | 8 | 8 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 643 | 11595 | 319 | 246 | 174 |
| Kansas City | Missouri | Kansas City | 46 | 5263 | 191 | 146 | 99 |
| St. Louis-Farmington | Missouri | St. Charles | 84 | 2912 | 143 | 105 | 63 |
| Kansas City | Missouri | Jackson | 55 | 2795 | 115 | 82 | 54 |
| Kansas City | Kansas | Johnson | 96 | 4586 | 100 | 102 | 99 |
| St. Louis-Farmington | Missouri | St. Louis City | 167 | 4125 | 86 | 77 | 57 |
| St. Louis-Farmington | Illinois | St. Clair | 154 | 3264 | 67 | 62 | 48 |
| Kansas City | Kansas | Wyandotte | 92 | 4197 | 64 | 77 | 66 |
| St. Louis-Farmington | Illinois | Madison | 71 | 1942 | 57 | 46 | 34 |
| Springfield | Missouri | Greene | 10 | 972 | 43 | 34 | 23 |
| St. Louis-Farmington | Missouri | Jefferson | 24 | 1065 | 43 | 32 | 20 |
| Joplin | Missouri | Jasper | 23 | 1572 | 40 | 36 | 37 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1023 | 37 | 28 | 23 |
| Kansas City | Missouri | Cass | 8 | 517 | 29 | 21 | 12 |
| Kansas City | Missouri | Clay | 19 | 784 | 19 | 14 | 12 |
| Missouri non-MSA | Missouri | Camden | 3 | 241 | 18 | 10 | 6 |
| Missouri non-MSA | Missouri | Pettis | 3 | 322 | 16 | 11 | 6 |
| Missouri non-MSA | Missouri | Taney | 3 | 284 | 14 | 10 | 7 |
| Joplin | Missouri | Newton | 4 | 771 | 13 | 13 | 14 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 469 | 12 | 11 | 8 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 3 | 560 | 12 | 14 | 13 |
| Springfield | Missouri | Christian | 1 | 210 | 12 | 9 | 5 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 242 | 11 | 8 | 4 |
| Columbia-Jefferson City | Missouri | Cole | 2 | 248 | 11 | 9 | 5 |
| Kansas City | Kansas | Leavenworth | 7 | 1361 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | McDonald | 7 | 896 | 10 | 10 | 13 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 109 | 9 | 5 | 3 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 311 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Butler | 2 | 210 | 8 | 6 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 3 | 218 | 8 | 5 | 4 |
| Kansas City | Missouri | Platte | 6 | 270 | 8 | 7 | 5 |
| Springfield | Missouri | Polk | 0 | 170 | 8 | 10 | 5 |
| Missouri non-MSA | Missouri | Marion | 1 | 102 | 7 | 4 | 2 |
| Missouri non-MSA | Missouri | Howell | 0 | 112 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Johnson | 1 | 427 | 6 | 11 | 10 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 152 | 6 | 6 | 4 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 250 | 6 | 5 | 3 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 311 | 5 | 4 | 2 |
| St. Joseph | Missouri | Buchanan | 10 | 1028 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Barry | 0 | 207 | 5 | 7 | 5 |
| Missouri non-MSA | Missouri | Miller | 0 | 78 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 142 | 4 | 6 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 128 | 4 | 4 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 65 | 4 | 2 | 1 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 230 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Carroll | 0 | 79 | 4 | 2 | 2 |
| Kansas City | Missouri | Ray | 0 | 67 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Laclede | 1 | 177 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Stone | 1 | 70 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Saline | 6 | 378 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Benton | 1 | 61 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 202 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Randolph | 1 | 47 | 3 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 96 | 3 | 2 | 1 |
| Kansas City | Kansas | Miami | 0 | 103 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 126 | 3 | 1 | 1 |
| Springfield | Missouri | Webster | 1 | 102 | 3 | 3 | 2 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 117 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Douglas | 2 | 53 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Pemiscot | 6 | 186 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 55 | 3 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 100 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Audrain | 1 | 180 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 174 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 58 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 40 | 2 | 2 | 1 |
| Kansas City | Missouri | Clinton | 0 | 57 | 2 | 1 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 135 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Lewis | 1 | 27 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Pike | 1 | 64 | 2 | 1 | 0 |
| St. Louis-Farmington | Illinois | Bond | 2 | 41 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 43 | 1 | 1 | 0 |
| Springfield | Missouri | Dallas | 1 | 43 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 14 | 1 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 32 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 62 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Livingston | 0 | 40 | 1 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 78 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 80 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 15 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Adair | 0 | 123 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Perry | 3 | 192 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ripley | 0 | 38 | 1 | 1 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 29 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Washington | 1 | 49 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 11 | 1 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 43 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 43 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 53 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 0 | 23 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 31 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 44 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Phelps | 0 | 65 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 0 | 41 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Madison | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 9 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 29 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 11 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 15 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 59 | 0 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 0 | 32 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 129 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 45 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Crawford | 0 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 54 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 32 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 14 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 2 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 5 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 9 | 0 | 0 | 0 |
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
