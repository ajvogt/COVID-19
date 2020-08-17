# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/17/2020  
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
| St. Louis-Farmington | 1284 | 39682 | 688 | 637 | 670 |
| Kansas City | 409 | 28563 | 439 | 422 | 458 |
| Missouri non-MSA | 107 | 11144 | 249 | 219 | 207 |
| Springfield | 13 | 2811 | 76 | 68 | 67 |
| Columbia-Jefferson City | 10 | 2834 | 74 | 62 | 59 |
| Joplin | 38 | 2893 | 37 | 31 | 35 |
| Cape Girardeau-Sikeston | 19 | 1339 | 26 | 21 | 21 |
| St. Joseph | 12 | 1314 | 8 | 7 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 678 | 16614 | 261 | 238 | 262 |
| Kansas City | Missouri | Kansas City | 66 | 7649 | 143 | 122 | 139 |
| Kansas City | Kansas | Johnson | 108 | 6357 | 93 | 95 | 93 |
| St. Louis-Farmington | Missouri | St. Charles | 91 | 4649 | 85 | 78 | 102 |
| Kansas City | Missouri | Jackson | 66 | 4560 | 78 | 79 | 93 |
| St. Louis-Farmington | Illinois | Madison | 85 | 3111 | 74 | 66 | 56 |
| Kansas City | Kansas | Wyandotte | 107 | 5329 | 61 | 59 | 63 |
| St. Louis-Farmington | Illinois | St. Clair | 162 | 4425 | 59 | 58 | 62 |
| St. Louis-Farmington | Missouri | St. Louis City | 181 | 5614 | 59 | 70 | 78 |
| Springfield | Missouri | Greene | 10 | 1902 | 55 | 48 | 44 |
| St. Louis-Farmington | Missouri | Jefferson | 27 | 1944 | 50 | 42 | 42 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1594 | 31 | 26 | 29 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 571 | 29 | 19 | 12 |
| Joplin | Missouri | Jasper | 32 | 1947 | 26 | 21 | 25 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 589 | 25 | 19 | 14 |
| Missouri non-MSA | Missouri | Taney | 3 | 739 | 21 | 22 | 19 |
| Missouri non-MSA | Missouri | Pettis | 5 | 651 | 20 | 17 | 15 |
| St. Louis-Farmington | Missouri | Franklin | 19 | 742 | 17 | 15 | 13 |
| Kansas City | Missouri | Cass | 9 | 863 | 17 | 16 | 20 |
| Kansas City | Missouri | Clay | 30 | 1143 | 15 | 17 | 17 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 5 | 742 | 13 | 10 | 11 |
| Springfield | Missouri | Christian | 1 | 441 | 12 | 11 | 11 |
| Kansas City | Kansas | Leavenworth | 9 | 1549 | 12 | 11 | 9 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 476 | 11 | 9 | 7 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 485 | 11 | 10 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 388 | 11 | 10 | 8 |
| Joplin | Missouri | Newton | 6 | 946 | 11 | 10 | 10 |
| Missouri non-MSA | Missouri | Marion | 1 | 269 | 10 | 8 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 439 | 9 | 9 | 10 |
| Missouri non-MSA | Missouri | Stone | 1 | 191 | 8 | 7 | 5 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 241 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | Camden | 7 | 408 | 8 | 7 | 10 |
| Missouri non-MSA | Missouri | Washington | 1 | 133 | 8 | 5 | 3 |
| Missouri non-MSA | Missouri | Saline | 7 | 483 | 7 | 5 | 5 |
| St. Louis-Farmington | Missouri | Warren | 0 | 248 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 3 | 299 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 273 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 226 | 6 | 4 | 6 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 151 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Pike | 1 | 144 | 6 | 5 | 3 |
| St. Joseph | Missouri | Buchanan | 10 | 1129 | 6 | 5 | 5 |
| Kansas City | Missouri | Platte | 10 | 407 | 6 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 198 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Barry | 4 | 293 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Crawford | 0 | 111 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Holt | 0 | 46 | 5 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 172 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Butler | 2 | 317 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 264 | 5 | 5 | 5 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 354 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Laclede | 1 | 235 | 5 | 2 | 3 |
| Missouri non-MSA | Missouri | Phelps | 0 | 123 | 5 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 159 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Perry | 4 | 256 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Miller | 1 | 157 | 4 | 4 | 4 |
| Springfield | Missouri | Polk | 0 | 238 | 4 | 3 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 263 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Audrain | 1 | 227 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Johnson | 3 | 513 | 3 | 3 | 6 |
| Missouri non-MSA | Missouri | Ralls | 0 | 57 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 183 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Benton | 2 | 117 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Howell | 2 | 176 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Ripley | 0 | 75 | 3 | 2 | 1 |
| St. Louis-Farmington | Illinois | Bond | 3 | 80 | 2 | 1 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 198 | 2 | 3 | 3 |
| Kansas City | Kansas | Miami | 0 | 152 | 2 | 2 | 2 |
| Springfield | Missouri | Webster | 1 | 154 | 2 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 163 | 2 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 69 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 95 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Texas | 1 | 67 | 2 | 2 | 1 |
| Kansas City | Kansas | Linn | 0 | 50 | 2 | 1 | 1 |
| Kansas City | Missouri | Clinton | 0 | 97 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 95 | 2 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 62 | 2 | 1 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 81 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 69 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 82 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 37 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 74 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 23 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Douglas | 2 | 94 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Macon | 0 | 69 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 66 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 242 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 155 | 1 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 98 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Madison | 0 | 35 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 63 | 1 | 1 | 0 |
| Springfield | Missouri | Dallas | 1 | 76 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 0 | 36 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | McDonald | 8 | 959 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | Hickory | 0 | 40 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 29 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 41 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 54 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 37 | 1 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 54 | 1 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 21 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 28 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 42 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 72 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Mercer | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 87 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 104 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 64 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 25 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 40 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 23 | 0 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 119 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Dade | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 62 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 13 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 44 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
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
