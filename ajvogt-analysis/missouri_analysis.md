# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/23/2020  
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
| St. Louis-Farmington | 1342 | 43280 | 602 | 639 | 680 |
| Kansas City | 419 | 31191 | 400 | 440 | 452 |
| Missouri non-MSA | 111 | 12458 | 226 | 241 | 217 |
| Columbia-Jefferson City | 13 | 3346 | 94 | 82 | 68 |
| Springfield | 13 | 3348 | 90 | 84 | 74 |
| Joplin | 46 | 3099 | 31 | 35 | 34 |
| Cape Girardeau-Sikeston | 20 | 1525 | 29 | 29 | 22 |
| St. Joseph | 12 | 1390 | 12 | 10 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 713 | 17721 | 187 | 218 | 259 |
| Kansas City | Kansas | Johnson | 110 | 7241 | 126 | 114 | 102 |
| Kansas City | Missouri | Kansas City | 65 | 8331 | 113 | 132 | 132 |
| St. Louis-Farmington | Missouri | St. Charles | 96 | 5159 | 78 | 86 | 100 |
| Kansas City | Missouri | Jackson | 71 | 5005 | 68 | 78 | 92 |
| Springfield | Missouri | Greene | 10 | 2314 | 68 | 62 | 53 |
| St. Louis-Farmington | Illinois | Madison | 91 | 3503 | 64 | 69 | 61 |
| St. Louis-Farmington | Illinois | St. Clair | 166 | 4814 | 63 | 61 | 62 |
| Columbia-Jefferson City | Missouri | Boone | 5 | 1890 | 50 | 40 | 35 |
| St. Louis-Farmington | Missouri | Jefferson | 30 | 2233 | 49 | 49 | 46 |
| Kansas City | Kansas | Wyandotte | 111 | 5653 | 46 | 56 | 58 |
| St. Louis-Farmington | Missouri | St. Louis City | 184 | 5861 | 44 | 51 | 70 |
| St. Louis-Farmington | Missouri | St. Francois | 4 | 783 | 40 | 30 | 18 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 702 | 25 | 23 | 16 |
| Joplin | Missouri | Jasper | 35 | 2089 | 21 | 25 | 24 |
| Missouri non-MSA | Missouri | Taney | 3 | 846 | 19 | 21 | 21 |
| St. Louis-Farmington | Missouri | Franklin | 19 | 844 | 16 | 18 | 14 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 6 | 847 | 16 | 15 | 11 |
| Kansas City | Missouri | Clay | 30 | 1245 | 16 | 16 | 18 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 574 | 15 | 12 | 9 |
| Missouri non-MSA | Missouri | Pettis | 5 | 735 | 13 | 17 | 16 |
| Springfield | Missouri | Christian | 1 | 515 | 13 | 12 | 12 |
| Kansas City | Missouri | Cass | 9 | 948 | 13 | 17 | 19 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 544 | 11 | 11 | 9 |
| Missouri non-MSA | Missouri | Stone | 1 | 237 | 9 | 8 | 6 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 213 | 9 | 7 | 5 |
| Joplin | Missouri | Newton | 11 | 1010 | 9 | 10 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 443 | 9 | 10 | 8 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 244 | 9 | 7 | 5 |
| Missouri non-MSA | Missouri | Marion | 1 | 325 | 8 | 10 | 8 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 488 | 8 | 9 | 10 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 329 | 8 | 9 | 5 |
| Missouri non-MSA | Missouri | Washington | 1 | 184 | 8 | 8 | 4 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 290 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | Miller | 1 | 198 | 7 | 6 | 4 |
| St. Joseph | Missouri | Buchanan | 10 | 1175 | 7 | 7 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 301 | 7 | 6 | 5 |
| St. Louis-Farmington | Missouri | Warren | 0 | 287 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Camden | 8 | 446 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 212 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 3 | 336 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Laclede | 1 | 262 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Nodaway | 1 | 261 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Barry | 4 | 322 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 294 | 5 | 4 | 4 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 391 | 5 | 5 | 6 |
| Kansas City | Missouri | Platte | 10 | 441 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Saline | 7 | 517 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Johnson | 3 | 542 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Crawford | 1 | 137 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Butler | 2 | 345 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Madison | 0 | 67 | 4 | 3 | 1 |
| Missouri non-MSA | Missouri | Phelps | 0 | 145 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Perry | 4 | 284 | 4 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 184 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Ralls | 0 | 80 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 204 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Howell | 2 | 199 | 3 | 3 | 4 |
| Springfield | Missouri | Polk | 0 | 259 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Benton | 1 | 141 | 3 | 3 | 3 |
| St. Louis-Farmington | Illinois | Bond | 3 | 100 | 3 | 2 | 2 |
| Springfield | Missouri | Webster | 1 | 172 | 3 | 3 | 2 |
| Kansas City | Kansas | Leavenworth | 9 | 1572 | 3 | 8 | 8 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 90 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 102 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Audrain | 1 | 238 | 2 | 2 | 2 |
| Kansas City | Missouri | Clinton | 0 | 113 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | McDonald | 8 | 975 | 2 | 1 | 4 |
| Missouri non-MSA | Missouri | Iron | 0 | 40 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 257 | 2 | 2 | 2 |
| Kansas City | Kansas | Miami | 0 | 167 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Monroe | 0 | 51 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 82 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 174 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Holt | 0 | 54 | 1 | 3 | 1 |
| Missouri non-MSA | Missouri | Texas | 1 | 78 | 1 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 94 | 1 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 88 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 106 | 1 | 2 | 2 |
| St. Joseph | Kansas | Doniphan | 0 | 58 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Henry | 3 | 106 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 46 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 70 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 51 | 1 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 107 | 1 | 1 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 208 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Dent | 0 | 30 | 1 | 1 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 50 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 79 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 28 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 78 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 34 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 69 | 1 | 1 | 0 |
| Kansas City | Missouri | Bates | 1 | 60 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 159 | 0 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 71 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Carroll | 0 | 107 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 33 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 2 | 97 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Wright | 0 | 77 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 43 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 48 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 71 | 0 | 1 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 39 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 38 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Livingston | 1 | 67 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 62 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 46 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 43 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 10 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 40 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 50 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 87 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 19 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 53 | 0 | 0 | 1 |
| Kansas City | Missouri | Ray | 0 | 118 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Pike | 1 | 130 | -1 | 2 | 2 |
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
