# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/16/2020  
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
| St. Louis-Farmington | 1280 | 39066 | 676 | 618 | 666 |
| Kansas City | 408 | 28391 | 480 | 428 | 468 |
| Missouri non-MSA | 107 | 10874 | 256 | 208 | 203 |
| Springfield | 13 | 2718 | 78 | 63 | 65 |
| Columbia-Jefferson City | 10 | 2685 | 70 | 54 | 56 |
| Joplin | 38 | 2882 | 39 | 31 | 37 |
| Cape Girardeau-Sikeston | 19 | 1316 | 28 | 20 | 20 |
| St. Joseph | 12 | 1306 | 8 | 6 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 678 | 16409 | 249 | 231 | 261 |
| Kansas City | Missouri | Kansas City | 65 | 7535 | 151 | 119 | 138 |
| Kansas City | Kansas | Johnson | 108 | 6357 | 102 | 95 | 97 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 4610 | 93 | 78 | 102 |
| Kansas City | Missouri | Jackson | 66 | 4523 | 87 | 80 | 93 |
| St. Louis-Farmington | Illinois | Madison | 85 | 3051 | 74 | 65 | 56 |
| Kansas City | Kansas | Wyandotte | 107 | 5329 | 66 | 68 | 67 |
| St. Louis-Farmington | Illinois | St. Clair | 162 | 4370 | 59 | 57 | 62 |
| St. Louis-Farmington | Missouri | St. Louis City | 181 | 5553 | 59 | 69 | 78 |
| Springfield | Missouri | Greene | 10 | 1836 | 56 | 45 | 43 |
| St. Louis-Farmington | Missouri | Jefferson | 27 | 1887 | 49 | 39 | 41 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1534 | 29 | 23 | 28 |
| Joplin | Missouri | Jasper | 32 | 1938 | 28 | 20 | 27 |
| Missouri non-MSA | Missouri | Taney | 3 | 708 | 22 | 21 | 18 |
| Missouri non-MSA | Missouri | Pettis | 5 | 639 | 21 | 16 | 15 |
| Kansas City | Missouri | Cass | 9 | 857 | 21 | 16 | 20 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 527 | 21 | 15 | 13 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 498 | 21 | 14 | 10 |
| St. Louis-Farmington | Missouri | Franklin | 19 | 729 | 19 | 15 | 13 |
| Kansas City | Missouri | Clay | 30 | 1133 | 17 | 16 | 17 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 5 | 735 | 14 | 9 | 11 |
| Kansas City | Kansas | Leavenworth | 9 | 1549 | 12 | 11 | 10 |
| Springfield | Missouri | Christian | 1 | 424 | 12 | 10 | 11 |
| Missouri non-MSA | Missouri | Marion | 1 | 264 | 11 | 8 | 7 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 461 | 11 | 8 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 378 | 11 | 9 | 8 |
| Joplin | Missouri | Newton | 6 | 944 | 10 | 10 | 10 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 271 | 10 | 6 | 4 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 468 | 10 | 9 | 6 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 430 | 10 | 9 | 10 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 235 | 9 | 7 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 3 | 294 | 9 | 8 | 6 |
| Kansas City | Missouri | Platte | 10 | 404 | 8 | 6 | 7 |
| Missouri non-MSA | Missouri | Camden | 7 | 398 | 8 | 7 | 10 |
| Missouri non-MSA | Missouri | Saline | 7 | 481 | 8 | 5 | 5 |
| Missouri non-MSA | Missouri | Washington | 1 | 126 | 8 | 5 | 2 |
| St. Joseph | Missouri | Buchanan | 10 | 1123 | 6 | 4 | 5 |
| St. Louis-Farmington | Missouri | Warren | 0 | 238 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 221 | 6 | 4 | 6 |
| Missouri non-MSA | Missouri | Pike | 1 | 141 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Stone | 1 | 168 | 6 | 6 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 158 | 6 | 4 | 4 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 353 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 252 | 5 | 4 | 5 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 145 | 5 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 179 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 170 | 5 | 2 | 2 |
| Missouri non-MSA | Missouri | Butler | 2 | 311 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Barry | 4 | 283 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Phelps | 0 | 115 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Holt | 0 | 41 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Perry | 4 | 255 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Crawford | 0 | 102 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Miller | 1 | 145 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Benton | 2 | 117 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Laclede | 1 | 221 | 3 | 1 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 178 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 54 | 3 | 2 | 1 |
| Springfield | Missouri | Polk | 0 | 234 | 3 | 3 | 6 |
| Kansas City | Missouri | Lafayette | 2 | 198 | 3 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 161 | 3 | 2 | 3 |
| Springfield | Missouri | Webster | 1 | 149 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 255 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Johnson | 3 | 507 | 3 | 3 | 7 |
| Missouri non-MSA | Missouri | Audrain | 1 | 220 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Howell | 2 | 173 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Ripley | 0 | 72 | 3 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 68 | 2 | 1 | 2 |
| Kansas City | Kansas | Miami | 0 | 152 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 242 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Henry | 3 | 94 | 2 | 1 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 81 | 2 | 1 | 1 |
| St. Louis-Farmington | Illinois | Bond | 3 | 77 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 94 | 2 | 2 | 2 |
| Kansas City | Missouri | Clinton | 0 | 95 | 2 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 75 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 68 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 82 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Texas | 1 | 65 | 2 | 2 | 1 |
| Kansas City | Kansas | Linn | 0 | 50 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Lewis | 1 | 54 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 58 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 34 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 62 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 42 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 153 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 73 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 40 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 65 | 1 | 2 | 2 |
| Kansas City | Missouri | Bates | 1 | 54 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dent | 0 | 20 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 34 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 67 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 39 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 36 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 2 | 92 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 0 | 28 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | McDonald | 8 | 958 | 1 | 2 | 6 |
| Missouri non-MSA | Missouri | Knox | 0 | 35 | 1 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 96 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 21 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 27 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 44 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 87 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 64 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 16 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 24 | 0 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 119 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 102 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Dade | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 71 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 22 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 39 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 44 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 10 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 13 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 9 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 46 | 0 | 0 | 0 |
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
