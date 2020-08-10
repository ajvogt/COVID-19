# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/10/2020  
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
| St. Louis-Farmington | 1248 | 34861 | 587 | 670 | 604 |
| Kansas City | 382 | 25488 | 406 | 466 | 431 |
| Missouri non-MSA | 98 | 9396 | 189 | 211 | 177 |
| Springfield | 13 | 2276 | 59 | 68 | 56 |
| Columbia-Jefferson City | 10 | 2313 | 50 | 60 | 50 |
| Joplin | 37 | 2630 | 25 | 27 | 37 |
| Cape Girardeau-Sikeston | 19 | 1151 | 16 | 18 | 19 |
| St. Joseph | 12 | 1254 | 5 | 6 | 7 |
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
| St. Louis-Farmington | Missouri | St. Louis | 667 | 14785 | 216 | 255 | 239 |
| Kansas City | Missouri | Kansas City | 63 | 6648 | 102 | 133 | 120 |
| Kansas City | Kansas | Johnson | 103 | 5703 | 98 | 89 | 99 |
| St. Louis-Farmington | Missouri | St. Louis City | 174 | 5200 | 82 | 92 | 77 |
| Kansas City | Missouri | Jackson | 64 | 4014 | 80 | 107 | 82 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 4052 | 71 | 99 | 92 |
| St. Louis-Farmington | Illinois | Madison | 76 | 2591 | 57 | 53 | 48 |
| Kansas City | Kansas | Wyandotte | 99 | 4896 | 57 | 59 | 67 |
| St. Louis-Farmington | Illinois | St. Clair | 161 | 4006 | 56 | 61 | 60 |
| Springfield | Missouri | Greene | 10 | 1515 | 42 | 46 | 36 |
| St. Louis-Farmington | Missouri | Jefferson | 24 | 1593 | 34 | 45 | 34 |
| Missouri non-MSA | Missouri | Taney | 3 | 589 | 23 | 24 | 15 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1375 | 22 | 31 | 28 |
| Kansas City | Missouri | Clay | 20 | 1037 | 19 | 22 | 16 |
| Joplin | Missouri | Jasper | 31 | 1761 | 15 | 18 | 26 |
| Kansas City | Missouri | Cass | 9 | 742 | 15 | 21 | 18 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 618 | 14 | 12 | 11 |
| Missouri non-MSA | Missouri | Pettis | 4 | 505 | 13 | 16 | 12 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 410 | 13 | 13 | 10 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 374 | 10 | 10 | 8 |
| Springfield | Missouri | Christian | 1 | 351 | 10 | 12 | 9 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 368 | 9 | 9 | 6 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 407 | 9 | 7 | 5 |
| Joplin | Missouri | Newton | 6 | 869 | 9 | 9 | 10 |
| Kansas City | Kansas | Leavenworth | 8 | 1459 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 250 | 9 | 8 | 6 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 310 | 9 | 8 | 6 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 5 | 651 | 7 | 9 | 11 |
| Kansas City | Missouri | Platte | 10 | 363 | 7 | 7 | 7 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 395 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Camden | 5 | 350 | 7 | 10 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 224 | 6 | 3 | 2 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 179 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Stone | 1 | 129 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Marion | 1 | 193 | 6 | 7 | 5 |
| Missouri non-MSA | Missouri | Butler | 2 | 281 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 228 | 6 | 6 | 5 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 318 | 5 | 6 | 5 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 105 | 5 | 3 | 2 |
| St. Louis-Farmington | Missouri | Warren | 0 | 196 | 5 | 5 | 4 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 157 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Miller | 1 | 127 | 4 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 125 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Pike | 1 | 99 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 234 | 4 | 3 | 3 |
| St. Joseph | Missouri | Buchanan | 10 | 1084 | 4 | 4 | 4 |
| Kansas City | Missouri | Lafayette | 2 | 178 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Barry | 4 | 254 | 3 | 4 | 5 |
| Kansas City | Missouri | Ray | 2 | 116 | 3 | 4 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 159 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | McDonald | 7 | 950 | 3 | 4 | 8 |
| Missouri non-MSA | Missouri | Benton | 1 | 94 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Johnson | 2 | 487 | 3 | 5 | 8 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 146 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 179 | 3 | 6 | 5 |
| Missouri non-MSA | Missouri | Washington | 1 | 77 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 231 | 3 | 3 | 2 |
| Kansas City | Missouri | Clinton | 0 | 82 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 55 | 2 | 3 | 1 |
| Springfield | Missouri | Webster | 1 | 135 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Perry | 4 | 225 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Saline | 7 | 428 | 2 | 4 | 4 |
| Springfield | Missouri | Dallas | 1 | 67 | 2 | 1 | 1 |
| Springfield | Missouri | Polk | 0 | 208 | 2 | 4 | 6 |
| Missouri non-MSA | Missouri | Crawford | 0 | 73 | 2 | 2 | 1 |
| Kansas City | Kansas | Miami | 0 | 133 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Texas | 0 | 52 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Howell | 2 | 153 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Morgan | 0 | 81 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 31 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 69 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Lewis | 1 | 46 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Phelps | 0 | 88 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 29 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 52 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 56 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 0 | 27 | 1 | 1 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 68 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 32 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 38 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 79 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 23 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 2 | 82 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 144 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 48 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Livingston | 0 | 61 | 1 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 47 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Vernon | 0 | 53 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 25 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Audrain | 1 | 200 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 40 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 20 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 22 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Bond | 3 | 60 | 0 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 52 | 0 | 1 | 1 |
| Kansas City | Kansas | Linn | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 58 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 135 | 0 | 0 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 41 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 24 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 48 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 62 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 83 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 68 | 0 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 87 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Laclede | 1 | 200 | 0 | 2 | 3 |
| Missouri non-MSA | Missouri | Grundy | 1 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 101 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Chariton | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 13 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 11 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 9 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 43 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 60 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Daviess | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 20 | 0 | 0 | 0 |
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
