# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/21/2020  
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
| St. Louis-Farmington | 1333 | 41969 | 635 | 606 | 686 |
| Kansas City | 417 | 30142 | 399 | 408 | 459 |
| Missouri non-MSA | 109 | 11925 | 224 | 219 | 215 |
| Springfield | 13 | 3175 | 85 | 76 | 71 |
| Columbia-Jefferson City | 12 | 3127 | 80 | 70 | 65 |
| Joplin | 46 | 3010 | 30 | 32 | 34 |
| Cape Girardeau-Sikeston | 20 | 1456 | 29 | 25 | 21 |
| St. Joseph | 12 | 1372 | 11 | 9 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 710 | 17294 | 203 | 209 | 264 |
| Kansas City | Missouri | Kansas City | 66 | 8073 | 112 | 122 | 138 |
| Kansas City | Kansas | Johnson | 110 | 6860 | 104 | 101 | 99 |
| St. Louis-Farmington | Missouri | St. Charles | 96 | 5000 | 84 | 78 | 103 |
| St. Louis-Farmington | Illinois | Madison | 88 | 3366 | 73 | 68 | 60 |
| Kansas City | Missouri | Jackson | 70 | 4828 | 66 | 72 | 94 |
| Kansas City | Kansas | Wyandotte | 109 | 5552 | 66 | 58 | 60 |
| St. Louis-Farmington | Illinois | St. Clair | 166 | 4664 | 64 | 58 | 62 |
| Springfield | Missouri | Greene | 10 | 2174 | 62 | 55 | 50 |
| St. Louis-Farmington | Missouri | Jefferson | 30 | 2140 | 53 | 45 | 45 |
| St. Louis-Farmington | Missouri | St. Louis City | 181 | 5773 | 49 | 55 | 75 |
| Columbia-Jefferson City | Missouri | Boone | 5 | 1762 | 37 | 33 | 33 |
| St. Louis-Farmington | Missouri | St. Francois | 4 | 674 | 30 | 23 | 15 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 653 | 25 | 20 | 16 |
| Joplin | Missouri | Jasper | 35 | 2025 | 21 | 22 | 24 |
| Missouri non-MSA | Missouri | Taney | 3 | 816 | 19 | 21 | 21 |
| St. Louis-Farmington | Missouri | Franklin | 19 | 806 | 18 | 15 | 14 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 548 | 16 | 12 | 9 |
| Missouri non-MSA | Missouri | Pettis | 5 | 701 | 16 | 16 | 16 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 6 | 810 | 15 | 13 | 11 |
| Kansas City | Missouri | Cass | 9 | 912 | 14 | 15 | 19 |
| Kansas City | Missouri | Clay | 30 | 1194 | 13 | 15 | 18 |
| Springfield | Missouri | Christian | 1 | 498 | 13 | 12 | 12 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 430 | 13 | 10 | 9 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 519 | 12 | 10 | 8 |
| Missouri non-MSA | Missouri | Marion | 1 | 307 | 10 | 9 | 8 |
| Missouri non-MSA | Missouri | Stone | 1 | 223 | 9 | 8 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 274 | 9 | 8 | 5 |
| Joplin | Missouri | Newton | 11 | 985 | 9 | 10 | 10 |
| Missouri non-MSA | Missouri | Washington | 1 | 169 | 9 | 7 | 4 |
| St. Louis-Farmington | Missouri | Warren | 0 | 276 | 8 | 6 | 5 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 199 | 8 | 8 | 4 |
| Kansas City | Kansas | Leavenworth | 9 | 1560 | 8 | 8 | 9 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 223 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 247 | 7 | 5 | 6 |
| Missouri non-MSA | Missouri | Camden | 8 | 434 | 7 | 7 | 10 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 468 | 7 | 8 | 10 |
| St. Joseph | Missouri | Buchanan | 10 | 1163 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 304 | 7 | 7 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 293 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | New Madrid | 3 | 322 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Barry | 4 | 313 | 5 | 4 | 4 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 373 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 191 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 281 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Miller | 1 | 175 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Crawford | 0 | 126 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Laclede | 1 | 248 | 5 | 4 | 3 |
| Kansas City | Missouri | Platte | 10 | 424 | 4 | 6 | 7 |
| Springfield | Missouri | Polk | 0 | 252 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Saline | 7 | 502 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Butler | 2 | 327 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Phelps | 0 | 132 | 4 | 3 | 2 |
| St. Louis-Farmington | Illinois | Bond | 3 | 95 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 174 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Johnson | 3 | 527 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Perry | 4 | 274 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Audrain | 1 | 235 | 3 | 2 | 2 |
| Springfield | Missouri | Webster | 1 | 166 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 68 | 3 | 3 | 1 |
| Kansas City | Missouri | Clinton | 0 | 111 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Howell | 2 | 186 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Madison | 0 | 49 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 77 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 94 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 197 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Benton | 1 | 130 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Holt | 0 | 49 | 2 | 3 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 77 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | McDonald | 8 | 971 | 2 | 1 | 4 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 172 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 79 | 2 | 2 | 1 |
| Kansas City | Kansas | Miami | 0 | 165 | 2 | 2 | 2 |
| Kansas City | Missouri | Lafayette | 2 | 203 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 0 | 49 | 1 | 1 | 1 |
| Springfield | Missouri | Dallas | 1 | 85 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 250 | 1 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 66 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Vernon | 0 | 68 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 77 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 34 | 1 | 0 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 48 | 1 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 58 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 26 | 1 | 1 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 87 | 1 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 103 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 1 | 73 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 103 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 71 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 39 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Douglas | 2 | 97 | 1 | 0 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 19 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Henry | 3 | 99 | 1 | 1 | 1 |
| Kansas City | Kansas | Linn | 0 | 50 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 40 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 155 | 0 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 56 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 75 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 1 | 68 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 70 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 36 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 105 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 24 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 40 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 62 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 43 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Grundy | 1 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 87 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 45 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 17 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 52 | 0 | 1 | 1 |
| Kansas City | Missouri | Ray | 0 | 117 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Pike | 1 | 133 | -1 | 3 | 2 |
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
