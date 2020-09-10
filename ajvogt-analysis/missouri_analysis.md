# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/10/2020  
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
| St. Louis-Farmington | 1475 | 53415 | 550 | 574 | 604 |
| Missouri non-MSA | 181 | 17504 | 320 | 304 | 262 |
| Kansas City | 502 | 37415 | 310 | 350 | 384 |
| Columbia-Jefferson City | 24 | 5860 | 166 | 156 | 116 |
| Springfield | 24 | 5885 | 160 | 154 | 117 |
| Joplin | 50 | 3979 | 62 | 55 | 44 |
| Cape Girardeau-Sikeston | 25 | 2053 | 33 | 32 | 29 |
| St. Joseph | 16 | 1780 | 26 | 24 | 17 |
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
| St. Louis-Farmington | Missouri | St. Louis | 762 | 21001 | 164 | 190 | 202 |
| Springfield | Missouri | Greene | 19 | 4200 | 118 | 115 | 87 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 3627 | 115 | 109 | 74 |
| Kansas City | Kansas | Johnson | 126 | 9023 | 83 | 101 | 107 |
| St. Louis-Farmington | Missouri | St. Charles | 105 | 6343 | 68 | 67 | 74 |
| Kansas City | Missouri | Jackson | 84 | 6168 | 65 | 70 | 69 |
| St. Louis-Farmington | Illinois | Madison | 113 | 4631 | 64 | 62 | 66 |
| Kansas City | Missouri | Kansas City | 95 | 9852 | 61 | 83 | 102 |
| Joplin | Missouri | Jasper | 37 | 2824 | 54 | 47 | 35 |
| St. Louis-Farmington | Missouri | Jefferson | 47 | 3190 | 53 | 55 | 52 |
| St. Louis-Farmington | Illinois | St. Clair | 176 | 5779 | 52 | 51 | 58 |
| Missouri non-MSA | Missouri | Livingston | 1 | 341 | 37 | 19 | 9 |
| St. Louis-Farmington | Missouri | St. Francois | 6 | 1367 | 36 | 35 | 33 |
| Kansas City | Kansas | Wyandotte | 119 | 6317 | 32 | 33 | 46 |
| St. Louis-Farmington | Missouri | St. Louis City | 191 | 6486 | 30 | 33 | 41 |
| Missouri non-MSA | Missouri | Johnson | 4 | 767 | 24 | 14 | 9 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1048 | 23 | 20 | 20 |
| Springfield | Missouri | Christian | 3 | 878 | 22 | 21 | 17 |
| St. Louis-Farmington | Missouri | Franklin | 22 | 1203 | 21 | 20 | 19 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 8 | 1122 | 19 | 16 | 15 |
| St. Joseph | Missouri | Buchanan | 13 | 1450 | 18 | 16 | 11 |
| St. Louis-Farmington | Illinois | Clinton | 19 | 884 | 17 | 16 | 15 |
| Kansas City | Missouri | Clay | 39 | 1530 | 16 | 15 | 15 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 442 | 14 | 11 | 9 |
| Kansas City | Missouri | Cass | 16 | 1187 | 13 | 13 | 14 |
| Missouri non-MSA | Missouri | Marion | 7 | 571 | 11 | 14 | 12 |
| Missouri non-MSA | Missouri | Nodaway | 7 | 649 | 11 | 23 | 15 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 551 | 11 | 8 | 7 |
| Missouri non-MSA | Missouri | Camden | 9 | 630 | 10 | 10 | 9 |
| Springfield | Missouri | Webster | 1 | 318 | 9 | 8 | 6 |
| Missouri non-MSA | Missouri | Taney | 22 | 993 | 9 | 8 | 12 |
| Kansas City | Kansas | Miami | 0 | 282 | 9 | 6 | 4 |
| Kansas City | Kansas | Leavenworth | 9 | 1743 | 9 | 8 | 8 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 306 | 8 | 8 | 5 |
| Missouri non-MSA | Missouri | Audrain | 2 | 332 | 8 | 6 | 4 |
| Missouri non-MSA | Missouri | Texas | 1 | 165 | 8 | 5 | 3 |
| Cape Girardeau-Sikeston | Missouri | Scott | 15 | 708 | 8 | 10 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 586 | 7 | 8 | 8 |
| Missouri non-MSA | Missouri | Howell | 3 | 338 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | Madison | 0 | 222 | 7 | 9 | 6 |
| Missouri non-MSA | Missouri | Phelps | 1 | 276 | 7 | 7 | 6 |
| Joplin | Missouri | Newton | 13 | 1155 | 7 | 8 | 9 |
| St. Louis-Farmington | Illinois | Bond | 4 | 212 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Miller | 1 | 313 | 6 | 6 | 6 |
| Kansas City | Missouri | Platte | 10 | 543 | 6 | 6 | 5 |
| St. Louis-Farmington | Illinois | Macoupin | 6 | 410 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Butler | 4 | 430 | 6 | 5 | 4 |
| Springfield | Missouri | Polk | 0 | 356 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 392 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 408 | 6 | 6 | 5 |
| St. Louis-Farmington | Missouri | Lincoln | 2 | 630 | 6 | 8 | 8 |
| Missouri non-MSA | Missouri | Pettis | 9 | 860 | 6 | 7 | 10 |
| Missouri non-MSA | Missouri | Ozark | 0 | 70 | 6 | 3 | 1 |
| Missouri non-MSA | Missouri | Grundy | 1 | 100 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Saline | 9 | 593 | 6 | 4 | 5 |
| Missouri non-MSA | Missouri | Morgan | 1 | 169 | 5 | 4 | 2 |
| St. Louis-Farmington | Illinois | Jersey | 7 | 326 | 5 | 5 | 7 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 172 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 10 | 460 | 5 | 7 | 6 |
| Missouri non-MSA | Missouri | Laclede | 1 | 344 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Adair | 0 | 278 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Perry | 4 | 448 | 5 | 8 | 7 |
| Missouri non-MSA | Missouri | Pulaski | 2 | 435 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Stone | 2 | 321 | 5 | 4 | 6 |
| Kansas City | Missouri | Clinton | 0 | 168 | 4 | 3 | 2 |
| St. Louis-Farmington | Missouri | Warren | 0 | 369 | 4 | 4 | 5 |
| Kansas City | Missouri | Lafayette | 2 | 281 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Ripley | 0 | 121 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Barry | 5 | 388 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 328 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Washington | 1 | 273 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Vernon | 0 | 115 | 3 | 2 | 2 |
| St. Joseph | Missouri | Andrew | 1 | 157 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 138 | 3 | 2 | 2 |
| Springfield | Missouri | Dallas | 1 | 133 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Wright | 0 | 115 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 4 | 122 | 3 | 5 | 3 |
| Missouri non-MSA | Missouri | Crawford | 2 | 221 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Pike | 2 | 170 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 0 | 52 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 151 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 108 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Henry | 4 | 135 | 2 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 89 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 67 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Dent | 0 | 58 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 210 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Barton | 0 | 122 | 2 | 2 | 1 |
| St. Joseph | Missouri | DeKalb | 2 | 84 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 250 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Ralls | 0 | 126 | 1 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 96 | 1 | 1 | 1 |
| Kansas City | Missouri | Ray | 0 | 135 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 3 | 124 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 63 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Benton | 1 | 165 | 1 | 0 | 2 |
| Missouri non-MSA | Missouri | Shelby | 0 | 55 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 63 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 86 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 182 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 37 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 1 | 121 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 89 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Lewis | 2 | 67 | 1 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 51 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 45 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | McDonald | 10 | 1000 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 36 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 78 | 0 | 1 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 50 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 42 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 72 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Gentry | 9 | 104 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 50 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 37 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 1 | 68 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 51 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 26 | 0 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 80 | 0 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 131 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 28 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 56 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 49 | 0 | 0 | 0 |
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
