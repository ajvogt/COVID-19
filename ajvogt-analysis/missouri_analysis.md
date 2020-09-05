# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/05/2020  
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
| St. Louis-Farmington | 1444 | 50886 | 610 | 592 | 606 |
| Kansas City | 459 | 35941 | 360 | 386 | 398 |
| Missouri non-MSA | 156 | 16013 | 303 | 273 | 245 |
| Columbia-Jefferson City | 21 | 5163 | 172 | 137 | 101 |
| Springfield | 13 | 5098 | 157 | 131 | 102 |
| Joplin | 49 | 3713 | 57 | 46 | 39 |
| Cape Girardeau-Sikeston | 24 | 1879 | 29 | 26 | 27 |
| St. Joseph | 13 | 1654 | 22 | 19 | 13 |
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
| St. Louis-Farmington | Missouri | St. Louis | 757 | 20174 | 200 | 189 | 203 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 3169 | 126 | 96 | 62 |
| Springfield | Missouri | Greene | 10 | 3633 | 118 | 98 | 76 |
| Kansas City | Kansas | Johnson | 120 | 8614 | 106 | 115 | 109 |
| Kansas City | Missouri | Kansas City | 74 | 9579 | 83 | 97 | 110 |
| St. Louis-Farmington | Illinois | Madison | 105 | 4380 | 73 | 67 | 68 |
| Kansas City | Missouri | Jackson | 82 | 5819 | 70 | 67 | 70 |
| St. Louis-Farmington | Missouri | St. Charles | 105 | 6002 | 63 | 65 | 72 |
| St. Louis-Farmington | Illinois | St. Clair | 173 | 5580 | 60 | 61 | 60 |
| St. Louis-Farmington | Missouri | Jefferson | 40 | 2913 | 53 | 52 | 47 |
| Joplin | Missouri | Jasper | 35 | 2586 | 47 | 37 | 29 |
| St. Louis-Farmington | Missouri | St. Louis City | 189 | 6335 | 39 | 37 | 49 |
| Kansas City | Kansas | Wyandotte | 117 | 6184 | 36 | 45 | 50 |
| St. Louis-Farmington | Missouri | St. Francois | 5 | 1207 | 35 | 34 | 29 |
| Missouri non-MSA | Missouri | Nodaway | 6 | 603 | 32 | 25 | 14 |
| Missouri non-MSA | Missouri | Livingston | 1 | 276 | 29 | 14 | 7 |
| Springfield | Missouri | Christian | 1 | 753 | 21 | 17 | 14 |
| Columbia-Jefferson City | Missouri | Cole | 6 | 931 | 20 | 17 | 19 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 809 | 19 | 18 | 14 |
| St. Louis-Farmington | Missouri | Franklin | 22 | 1110 | 18 | 20 | 18 |
| St. Joseph | Missouri | Buchanan | 11 | 1359 | 16 | 13 | 9 |
| Kansas City | Missouri | Clay | 31 | 1455 | 15 | 17 | 16 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 8 | 1028 | 14 | 13 | 13 |
| Kansas City | Missouri | Cass | 12 | 1122 | 13 | 14 | 14 |
| Cape Girardeau-Sikeston | Missouri | Scott | 14 | 662 | 11 | 9 | 10 |
| Missouri non-MSA | Missouri | Marion | 4 | 505 | 11 | 13 | 11 |
| Missouri non-MSA | Missouri | Camden | 8 | 577 | 11 | 9 | 8 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 382 | 10 | 10 | 8 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 545 | 10 | 7 | 8 |
| Missouri non-MSA | Missouri | Madison | 0 | 182 | 10 | 9 | 5 |
| Kansas City | Kansas | Leavenworth | 9 | 1704 | 9 | 9 | 8 |
| St. Louis-Farmington | Illinois | Bond | 4 | 191 | 9 | 6 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 9 | 430 | 9 | 6 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 602 | 9 | 9 | 8 |
| Joplin | Missouri | Newton | 14 | 1127 | 9 | 9 | 9 |
| Missouri non-MSA | Missouri | Perry | 4 | 423 | 9 | 10 | 6 |
| Springfield | Missouri | Webster | 1 | 266 | 8 | 6 | 4 |
| St. Louis-Farmington | Illinois | Monroe | 14 | 499 | 8 | 8 | 6 |
| Missouri non-MSA | Missouri | Howell | 3 | 293 | 8 | 6 | 5 |
| Kansas City | Kansas | Miami | 0 | 242 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Phelps | 0 | 244 | 7 | 7 | 5 |
| Springfield | Missouri | Polk | 0 | 328 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Miller | 1 | 280 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Pettis | 8 | 824 | 7 | 7 | 12 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 265 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Audrain | 2 | 304 | 7 | 4 | 3 |
| St. Louis-Farmington | Illinois | Macoupin | 6 | 388 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Taney | 15 | 939 | 6 | 7 | 14 |
| Kansas City | Missouri | Platte | 10 | 510 | 6 | 5 | 5 |
| St. Louis-Farmington | Illinois | Jersey | 6 | 315 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 362 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Stone | 2 | 304 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Johnson | 4 | 622 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Crawford | 1 | 215 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 2 | 411 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Grundy | 1 | 74 | 5 | 3 | 1 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 378 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Saline | 8 | 569 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Laclede | 1 | 314 | 4 | 4 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 349 | 4 | 4 | 5 |
| Kansas City | Missouri | Lafayette | 2 | 259 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 254 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Butler | 3 | 398 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Texas | 1 | 121 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Randolph | 1 | 135 | 4 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 142 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Washington | 1 | 253 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 308 | 3 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 131 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 122 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 138 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 0 | 41 | 2 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 142 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 3 | 100 | 2 | 4 | 2 |
| Kansas City | Missouri | Clinton | 0 | 146 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 241 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Barry | 5 | 367 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Barton | 0 | 111 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 197 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 95 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Daviess | 0 | 37 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 100 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Vernon | 0 | 95 | 2 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 75 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 88 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dent | 0 | 46 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 81 | 1 | 1 | 0 |
| Springfield | Missouri | Dallas | 1 | 118 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Chariton | 0 | 35 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 59 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 59 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Douglas | 2 | 117 | 1 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 78 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 0 | 69 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 116 | 1 | 3 | 3 |
| Kansas City | Missouri | Bates | 1 | 76 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | McDonald | 10 | 995 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 121 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 0 | 34 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 101 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 74 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 32 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 48 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 178 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 96 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 2 | 145 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Carroll | 0 | 115 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 82 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 48 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 39 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 28 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 56 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 61 | 0 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 128 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Benton | 1 | 158 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 1 | 66 | 0 | 1 | 1 |
| Kansas City | Kansas | Linn | 0 | 56 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 49 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 49 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 21 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 40 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 56 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 43 | 0 | 0 | 0 |
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
