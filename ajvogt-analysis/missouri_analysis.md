# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/17/2020  
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
| St. Louis-Farmington | 1777 | 74104 | 671 | 582 | 552 |
| Missouri non-MSA | 416 | 33506 | 558 | 489 | 447 |
| Kansas City | 731 | 52645 | 521 | 450 | 429 |
| Columbia-Jefferson City | 47 | 10377 | 188 | 152 | 115 |
| Springfield | 125 | 12257 | 175 | 168 | 172 |
| Joplin | 75 | 6500 | 74 | 66 | 66 |
| Cape Girardeau-Sikeston | 56 | 4116 | 72 | 61 | 55 |
| St. Joseph | 39 | 3387 | 53 | 49 | 46 |
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
| St. Louis-Farmington | Missouri | St. Louis | 854 | 27472 | 219 | 184 | 174 |
| Kansas City | Missouri | Jackson | 117 | 9062 | 141 | 104 | 78 |
| St. Louis-Farmington | Missouri | St. Charles | 130 | 9353 | 127 | 102 | 82 |
| Springfield | Missouri | Greene | 103 | 8131 | 111 | 102 | 105 |
| Kansas City | Kansas | Johnson | 173 | 12818 | 107 | 99 | 104 |
| Columbia-Jefferson City | Missouri | Boone | 14 | 5508 | 80 | 58 | 42 |
| Kansas City | Missouri | Kansas City | 159 | 13263 | 74 | 82 | 101 |
| St. Louis-Farmington | Illinois | Madison | 152 | 6650 | 58 | 51 | 52 |
| Joplin | Missouri | Newton | 16 | 1841 | 51 | 30 | 19 |
| Kansas City | Missouri | Clay | 46 | 2257 | 49 | 32 | 20 |
| St. Louis-Farmington | Missouri | St. Louis City | 216 | 7803 | 49 | 43 | 37 |
| Columbia-Jefferson City | Missouri | Cole | 16 | 2327 | 46 | 45 | 35 |
| St. Louis-Farmington | Missouri | Jefferson | 69 | 5032 | 46 | 40 | 48 |
| Kansas City | Kansas | Wyandotte | 145 | 7814 | 45 | 47 | 42 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 35 | 2402 | 43 | 37 | 34 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1344 | 41 | 25 | 14 |
| St. Louis-Farmington | Illinois | St. Clair | 210 | 7430 | 41 | 42 | 44 |
| St. Joseph | Missouri | Buchanan | 33 | 2641 | 38 | 35 | 35 |
| Springfield | Missouri | Christian | 8 | 2018 | 33 | 31 | 30 |
| St. Louis-Farmington | Missouri | Franklin | 34 | 2240 | 31 | 26 | 28 |
| St. Louis-Farmington | Missouri | St. Francois | 19 | 2551 | 27 | 26 | 25 |
| Kansas City | Missouri | Cass | 27 | 1831 | 26 | 20 | 17 |
| Missouri non-MSA | Missouri | Camden | 23 | 1406 | 25 | 24 | 22 |
| Missouri non-MSA | Missouri | Phelps | 19 | 727 | 25 | 16 | 12 |
| Missouri non-MSA | Missouri | Butler | 8 | 951 | 23 | 17 | 14 |
| Joplin | Missouri | Jasper | 59 | 4659 | 23 | 35 | 46 |
| Columbia-Jefferson City | Missouri | Callaway | 4 | 974 | 23 | 19 | 14 |
| Cape Girardeau-Sikeston | Missouri | Scott | 18 | 1186 | 22 | 17 | 14 |
| Missouri non-MSA | Missouri | Laclede | 15 | 1026 | 21 | 20 | 19 |
| Missouri non-MSA | Missouri | Howell | 4 | 976 | 20 | 17 | 17 |
| St. Louis-Farmington | Illinois | Clinton | 23 | 1515 | 19 | 18 | 17 |
| Missouri non-MSA | Missouri | Lawrence | 13 | 928 | 19 | 16 | 15 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 351 | 17 | 12 | 7 |
| Missouri non-MSA | Missouri | Miller | 5 | 723 | 16 | 12 | 11 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 976 | 14 | 12 | 9 |
| Springfield | Missouri | Webster | 6 | 990 | 14 | 19 | 18 |
| Missouri non-MSA | Missouri | Pulaski | 8 | 865 | 14 | 10 | 12 |
| Kansas City | Missouri | Platte | 12 | 876 | 14 | 11 | 9 |
| Kansas City | Missouri | Clinton | 7 | 402 | 14 | 10 | 7 |
| Missouri non-MSA | Missouri | Pettis | 13 | 1351 | 13 | 11 | 14 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 723 | 13 | 12 | 10 |
| Missouri non-MSA | Missouri | Texas | 3 | 510 | 13 | 10 | 10 |
| Kansas City | Kansas | Leavenworth | 17 | 2424 | 12 | 13 | 19 |
| Kansas City | Missouri | Lafayette | 19 | 718 | 12 | 10 | 11 |
| Columbia-Jefferson City | Missouri | Moniteau | 6 | 459 | 12 | 8 | 6 |
| Missouri non-MSA | Missouri | Madison | 2 | 415 | 12 | 8 | 5 |
| Missouri non-MSA | Missouri | Barry | 7 | 651 | 12 | 9 | 7 |
| Springfield | Missouri | Polk | 7 | 849 | 11 | 10 | 14 |
| Missouri non-MSA | Missouri | Barton | 2 | 373 | 11 | 11 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 4 | 1017 | 11 | 13 | 11 |
| Missouri non-MSA | Missouri | Morgan | 5 | 551 | 11 | 10 | 10 |
| Missouri non-MSA | Missouri | Randolph | 3 | 463 | 10 | 12 | 9 |
| Missouri non-MSA | Missouri | Wright | 0 | 542 | 10 | 10 | 12 |
| St. Louis-Farmington | Illinois | Macoupin | 8 | 703 | 10 | 8 | 8 |
| Missouri non-MSA | Missouri | Taney | 33 | 1520 | 10 | 11 | 14 |
| Missouri non-MSA | Missouri | Crawford | 6 | 518 | 9 | 7 | 7 |
| St. Louis-Farmington | Illinois | Bond | 9 | 432 | 8 | 5 | 5 |
| Missouri non-MSA | Missouri | Dent | 2 | 221 | 8 | 5 | 4 |
| Missouri non-MSA | Missouri | Marion | 14 | 801 | 8 | 6 | 6 |
| Missouri non-MSA | Missouri | Henry | 5 | 328 | 8 | 6 | 5 |
| St. Louis-Farmington | Missouri | Warren | 1 | 564 | 8 | 5 | 4 |
| Missouri non-MSA | Missouri | Stone | 6 | 615 | 7 | 8 | 8 |
| St. Louis-Farmington | Illinois | Monroe | 27 | 829 | 7 | 9 | 7 |
| St. Joseph | Missouri | Andrew | 4 | 372 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Adair | 0 | 444 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Washington | 11 | 573 | 7 | 8 | 8 |
| Kansas City | Missouri | Bates | 3 | 221 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 17 | 673 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 12 | 650 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Audrain | 5 | 520 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1169 | 6 | 4 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 541 | 6 | 5 | 6 |
| St. Joseph | Missouri | DeKalb | 2 | 221 | 6 | 4 | 3 |
| Kansas City | Kansas | Miami | 2 | 474 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Livingston | 5 | 530 | 5 | 7 | 5 |
| Missouri non-MSA | Missouri | Oregon | 0 | 202 | 5 | 4 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 2 | 423 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Cedar | 2 | 205 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Wayne | 1 | 286 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Perry | 7 | 731 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Ripley | 3 | 199 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 5 | 372 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Dade | 0 | 126 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Vernon | 3 | 279 | 5 | 4 | 4 |
| Springfield | Missouri | Dallas | 1 | 269 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 268 | 4 | 3 | 3 |
| Kansas City | Missouri | Ray | 2 | 226 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 1 | 267 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Saline | 9 | 873 | 4 | 7 | 8 |
| Missouri non-MSA | Missouri | Carter | 3 | 144 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Hickory | 3 | 171 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Daviess | 2 | 194 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 206 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Dunklin | 11 | 951 | 4 | 6 | 9 |
| Missouri non-MSA | Missouri | Shannon | 2 | 183 | 4 | 3 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 446 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Pike | 4 | 291 | 3 | 3 | 2 |
| Kansas City | Missouri | Caldwell | 1 | 150 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 1 | 169 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 217 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Benton | 5 | 432 | 3 | 4 | 8 |
| Missouri non-MSA | Missouri | Maries | 0 | 126 | 2 | 2 | 2 |
| Kansas City | Kansas | Linn | 1 | 109 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Lewis | 2 | 161 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Iron | 0 | 87 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Carroll | 2 | 162 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 3 | 259 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Monroe | 1 | 113 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 100 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Gentry | 10 | 167 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 95 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 54 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 160 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Putnam | 1 | 47 | 1 | 1 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 153 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 54 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 90 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 179 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 150 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Holt | 1 | 98 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 188 | 1 | 1 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 105 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 100 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 8 | 231 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Atchison | 1 | 70 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 58 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 67 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 1 | 54 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 30 | 0 | 0 | 0 |
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
