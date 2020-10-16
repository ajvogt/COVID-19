# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/16/2020  
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
| St. Louis-Farmington | 1773 | 73139 | 631 | 574 | 537 |
| Missouri non-MSA | 411 | 32927 | 561 | 535 | 440 |
| Kansas City | 725 | 52027 | 505 | 488 | 417 |
| Columbia-Jefferson City | 47 | 10162 | 186 | 149 | 111 |
| Springfield | 118 | 12069 | 175 | 191 | 171 |
| Joplin | 75 | 6449 | 77 | 79 | 67 |
| Cape Girardeau-Sikeston | 56 | 4043 | 73 | 64 | 54 |
| St. Joseph | 38 | 3332 | 52 | 56 | 45 |
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
| St. Louis-Farmington | Missouri | St. Louis | 854 | 27050 | 191 | 167 | 165 |
| Kansas City | Missouri | Jackson | 117 | 8977 | 143 | 99 | 78 |
| St. Louis-Farmington | Missouri | St. Charles | 130 | 9196 | 120 | 103 | 80 |
| Springfield | Missouri | Greene | 96 | 8026 | 110 | 116 | 105 |
| Kansas City | Kansas | Johnson | 171 | 12685 | 105 | 97 | 102 |
| Columbia-Jefferson City | Missouri | Boone | 14 | 5459 | 82 | 52 | 42 |
| Kansas City | Missouri | Kansas City | 158 | 13101 | 68 | 130 | 95 |
| St. Louis-Farmington | Illinois | Madison | 150 | 6565 | 53 | 48 | 51 |
| Joplin | Missouri | Newton | 16 | 1830 | 50 | 23 | 20 |
| St. Louis-Farmington | Missouri | Jefferson | 69 | 4988 | 49 | 50 | 48 |
| Columbia-Jefferson City | Missouri | Cole | 16 | 2258 | 49 | 48 | 34 |
| St. Louis-Farmington | Missouri | St. Louis City | 216 | 7750 | 48 | 39 | 36 |
| Kansas City | Missouri | Clay | 46 | 2210 | 44 | 27 | 18 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 35 | 2356 | 42 | 39 | 33 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1335 | 41 | 16 | 14 |
| St. Louis-Farmington | Illinois | St. Clair | 208 | 7382 | 41 | 41 | 44 |
| Kansas City | Kansas | Wyandotte | 145 | 7734 | 41 | 46 | 41 |
| St. Joseph | Missouri | Buchanan | 33 | 2614 | 39 | 42 | 33 |
| St. Louis-Farmington | Missouri | St. Francois | 19 | 2540 | 32 | 29 | 26 |
| Springfield | Missouri | Christian | 8 | 1972 | 30 | 35 | 30 |
| St. Louis-Farmington | Missouri | Franklin | 34 | 2202 | 29 | 31 | 27 |
| Missouri non-MSA | Missouri | Camden | 22 | 1386 | 27 | 25 | 22 |
| Missouri non-MSA | Missouri | Phelps | 19 | 715 | 27 | 16 | 12 |
| Kansas City | Missouri | Cass | 27 | 1814 | 26 | 20 | 17 |
| Joplin | Missouri | Jasper | 59 | 4619 | 26 | 56 | 47 |
| Columbia-Jefferson City | Missouri | Callaway | 4 | 950 | 25 | 19 | 13 |
| Missouri non-MSA | Missouri | Laclede | 13 | 1011 | 23 | 24 | 19 |
| Cape Girardeau-Sikeston | Missouri | Scott | 18 | 1164 | 23 | 19 | 13 |
| Missouri non-MSA | Missouri | Butler | 8 | 915 | 20 | 18 | 14 |
| Missouri non-MSA | Missouri | Howell | 4 | 959 | 20 | 23 | 17 |
| Missouri non-MSA | Missouri | Lawrence | 13 | 907 | 19 | 19 | 15 |
| St. Louis-Farmington | Illinois | Clinton | 23 | 1480 | 17 | 17 | 16 |
| Springfield | Missouri | Webster | 6 | 973 | 17 | 22 | 18 |
| Missouri non-MSA | Missouri | Pulaski | 8 | 857 | 16 | 12 | 12 |
| Kansas City | Missouri | Platte | 12 | 864 | 15 | 10 | 9 |
| Missouri non-MSA | Missouri | Texas | 3 | 506 | 14 | 12 | 10 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 324 | 14 | 11 | 6 |
| Kansas City | Missouri | Clinton | 4 | 385 | 13 | 10 | 6 |
| Kansas City | Kansas | Leavenworth | 17 | 2386 | 12 | 13 | 18 |
| Kansas City | Missouri | Lafayette | 19 | 709 | 12 | 12 | 11 |
| St. Louis-Farmington | Missouri | Lincoln | 4 | 1004 | 12 | 15 | 10 |
| Missouri non-MSA | Missouri | Miller | 3 | 681 | 12 | 12 | 10 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 962 | 12 | 11 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 708 | 12 | 13 | 11 |
| Missouri non-MSA | Missouri | Barton | 2 | 365 | 12 | 12 | 7 |
| Springfield | Missouri | Polk | 7 | 834 | 11 | 12 | 13 |
| Missouri non-MSA | Missouri | Barry | 7 | 632 | 11 | 9 | 7 |
| Missouri non-MSA | Missouri | Madison | 2 | 406 | 11 | 6 | 5 |
| Missouri non-MSA | Missouri | Pettis | 13 | 1321 | 11 | 11 | 13 |
| Missouri non-MSA | Missouri | Morgan | 5 | 535 | 11 | 11 | 10 |
| Columbia-Jefferson City | Missouri | Moniteau | 6 | 445 | 10 | 8 | 6 |
| Missouri non-MSA | Missouri | Wright | 0 | 530 | 10 | 12 | 12 |
| Missouri non-MSA | Missouri | Crawford | 6 | 511 | 9 | 7 | 7 |
| Missouri non-MSA | Missouri | Randolph | 3 | 452 | 9 | 13 | 8 |
| St. Louis-Farmington | Illinois | Macoupin | 8 | 685 | 9 | 7 | 8 |
| Missouri non-MSA | Missouri | Stone | 6 | 606 | 9 | 9 | 8 |
| Missouri non-MSA | Missouri | Taney | 34 | 1502 | 9 | 20 | 14 |
| Missouri non-MSA | Missouri | Dent | 2 | 217 | 8 | 4 | 4 |
| St. Louis-Farmington | Illinois | Monroe | 27 | 819 | 8 | 8 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 17 | 667 | 8 | 9 | 5 |
| Missouri non-MSA | Missouri | Livingston | 5 | 535 | 8 | 9 | 5 |
| Missouri non-MSA | Missouri | Marion | 14 | 789 | 7 | 8 | 5 |
| St. Louis-Farmington | Missouri | Warren | 1 | 557 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Washington | 11 | 561 | 7 | 9 | 8 |
| Missouri non-MSA | Missouri | Henry | 5 | 319 | 7 | 8 | 5 |
| Missouri non-MSA | Missouri | Adair | 0 | 436 | 7 | 6 | 4 |
| St. Joseph | Missouri | Andrew | 3 | 365 | 7 | 7 | 5 |
| St. Louis-Farmington | Illinois | Bond | 9 | 417 | 7 | 4 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 11 | 640 | 6 | 7 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 2 | 418 | 6 | 4 | 5 |
| Missouri non-MSA | Missouri | Audrain | 5 | 516 | 6 | 4 | 4 |
| Kansas City | Missouri | Bates | 3 | 213 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Ripley | 3 | 197 | 6 | 1 | 2 |
| Kansas City | Kansas | Miami | 2 | 474 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | McDonald | 12 | 1166 | 5 | 3 | 4 |
| Missouri non-MSA | Missouri | Perry | 7 | 726 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Cedar | 2 | 198 | 5 | 5 | 4 |
| St. Joseph | Missouri | DeKalb | 2 | 212 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Saline | 9 | 864 | 5 | 9 | 8 |
| Missouri non-MSA | Missouri | Dade | 0 | 123 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Daviess | 2 | 194 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 1 | 264 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 193 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Hickory | 3 | 168 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Vernon | 3 | 272 | 4 | 6 | 4 |
| Springfield | Missouri | Dallas | 1 | 264 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 265 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Carter | 3 | 143 | 4 | 2 | 3 |
| Missouri non-MSA | Missouri | Wayne | 1 | 274 | 4 | 3 | 4 |
| Kansas City | Missouri | Ray | 2 | 222 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 202 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Benton | 5 | 431 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Shannon | 2 | 181 | 3 | 5 | 3 |
| Missouri non-MSA | Missouri | Maries | 0 | 122 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 4 | 355 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Dunklin | 11 | 938 | 3 | 9 | 9 |
| Missouri non-MSA | Missouri | Pike | 4 | 288 | 3 | 3 | 2 |
| Kansas City | Kansas | Linn | 1 | 109 | 3 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 512 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Carroll | 2 | 162 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Douglas | 3 | 256 | 2 | 3 | 3 |
| Kansas City | Missouri | Caldwell | 1 | 144 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Gentry | 10 | 165 | 2 | 2 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 438 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 1 | 165 | 2 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 214 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 177 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 1 | 112 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 145 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 99 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 0 | 95 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Lewis | 2 | 153 | 2 | 4 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 82 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 187 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Harrison | 1 | 157 | 1 | 3 | 2 |
| Missouri non-MSA | Missouri | Putnam | 1 | 46 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 88 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 99 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 1 | 96 | 1 | 1 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 105 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 50 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 1 | 70 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Grundy | 8 | 230 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Scotland | 1 | 48 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 58 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 1 | 54 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 141 | 0 | 1 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 66 | 0 | 0 | 1 |
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
